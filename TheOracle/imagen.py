import os
import json
import requests
import asyncio
import aiofiles
import aiohttp
import discord
from discord.ext import commands
from datetime import time, datetime, timezone
from lumaai import LumaAI
from openai import AsyncOpenAI

################################################################################

class AsyncSingleton:
  def __init__(self, loader_func):
    """
    Initializes the AsyncSingleton.
    :param loader_func: An async function that loads the value.
    """
    self._loader_func = loader_func
    self._value = None
    self._lock = asyncio.Lock()

  async def get(self):
    """
    Accesses the variable. If it's not loaded yet, it will load it asynchronously.
    """
    if self._value is None:
      async with self._lock:  # Ensure only one coroutine initializes the value
        if self._value is None:  # Double-checked locking
          print(f"Calling on-demand loader: {self._loader_func.__name__}")
          self._value = await self._loader_func()
    return self._value

async def a_load_json(file_path: str) -> dict:
  """
  Loads a JSON file asynchronously.
  """
  print(f"Loading JSON: {file_path}.")
  async with aiofiles.open(file_path, "r") as file:
    data = await file.read()
  return json.loads(data)

CONFIG = AsyncSingleton(lambda: a_load_json("config.json"))
TTSLINES = AsyncSingleton(lambda: a_load_json("text.json"))
TEMPLATES = AsyncSingleton(lambda: a_load_json("templates.json"))
LUMACUTS = AsyncSingleton(lambda: a_load_json("lumacuts.json"))

################################################################################

async def a_get_openai_token() -> str:
  """
  Gets the OpenAI bearer token from the environment or config.json.
  """
  print("Fetching OpenAI token.")
  secret = os.getenv('OPENAI_SECRET')
  if secret:
    return secret
  else:
    config = await CONFIG.get()
    return config["tokens"]["openai"]
  
async def a_init_openai():
  """
  Creates and initializes the OpenAI client.
  """
  print("Initializing OpenAI client.")
  token = await a_get_openai_token()
  return AsyncOpenAI(api_key=token)

async def a_get_lumaai_token() -> str:
  """
  Gets the LumaAI API bearer token from the environment or config.json.
  """
  print("Fetching LumaAI token.")
  secret = os.getenv('LUMAAI_SECRET')
  if secret:
    return secret
  else:
    config = await CONFIG.get()
    return config["tokens"]["lumaai"]

async def a_init_lumaai():
  """
  Creates and initializes the LumaAI client.
  """
  print("Initializing LumaAI client.")
  token = await a_get_lumaai_token()
  return LumaAI(auth_token=token)

async def a_get_discord_token() -> str:
  """
  Gets the Discord bot token from the environment or config.json.
  """
  print("Fetching Discord token.")
  secret = os.getenv('DISCORD_SECRET')
  if secret:
    return secret
  else:
    config = await CONFIG.get()
    return config["tokens"]["discord"]

async def a_init_discord():
  """
  Creates and initializes the Discord bot.
  """
  print("Initializing Discord bot.")
  intents = discord.Intents.default()
  intents.messages = True
  intents.message_content = True
  bot = commands.Bot(command_prefix='!', intents=intents)
  return bot

OPENAI = AsyncSingleton(a_init_openai)
LUMAAI = AsyncSingleton(a_init_lumaai)
DISCORD = AsyncSingleton(a_init_discord)

################################################################################

# Keys: fades
async def a_get_lumacuts(key: str) -> list:
  """
  Loads a particular set of cut templates from lumacuts.json.
  """
  cuts_data = await LUMACUTS.get()
  if key not in cuts_data:
    raise ValueError(f"Key '{key}' not found in JSON file.")
  cuts = cuts_data[key]
  for cut in cuts:
    print(f"{cut["name"]}")
  return cuts

# Keys: gothfembust
async def a_get_template(key: str) -> str:
  """
  Loads a particular image template from template.json.
  """
  print("Getting prompt template.")
  template_data = await TEMPLATES.get()
  if key not in template_data:
    raise ValueError(f"Key '{key}' not found in JSON file.")
  return template_data[key]

async def a_format_template(template: str, arguments: dict) -> str:
  print("Formatting template.")
  return template.format(**arguments)

async def a_generate_filename(identifier: str) -> str:
  timestamp = datetime.now(timezone.utc).strftime("%Y%M%D%H%M%S")
  filename = f"{timestamp}_{identifier}"
  print(f"Generated filename: {filename}.")
  return filename

async def a_generate_text(prompt: str) -> str:
  """
  Generates text using OpenAI ChatGPT.
  """
  print("Sending text prompt to OpenAI.")
  client = await OPENAI.get()
  #client = AsyncOpenAI()
  completion = await client.chat.completions.create(
    model="chatgpt-4o-latest",
    max_completion_tokens=250,
    messages=[
      {"role":"system","content":"You are a helpful assistant."},
      {"role":"user","content":prompt}
    ]
  )
  return completion.choices[0].message.content

async def a_generate_image(prompt: str) -> str:
  """
  Generates images using OpenAI DALL-E-3
  """
  print("Sending image prompt to DALL-E-3")
  client = await OPENAI.get()
  completion = await client.images.generate(
    model="dall-e-3",
    prompt=prompt,
    size="1792x1024",
    quality="hd", # "standard"
    n=1
  )
  return completion.data[0].url

async def a_download_image(image_url, filename, channel):
  """
  Downloads an image from the given URL and posts it to the specified Discord channel.
  """
  print(f"Downloading: {filename}.png")
  async with aiohttp.ClientSession() as session:
    async with session.get(image_url) as response:
      if response.status == 200:
        file_path = f"{filename}.png"
        async with aiofiles.open(file_path, "wb") as file:
          await file.write(await response.read())
        print(f"{file_path} downloaded successfully.")
        if channel:
          await channel.send(file=discord.File(file_path))
          print(f"Image {file_path} posted to Discord channel.")
      else:
        print(f"Failed to download image. Status code: {response.status}")

async def co_produce_image(template_key, arguments, channel):
  print("Producing prompt.")
  template = await a_get_template(template_key)
  prompt = await a_format_template(template, arguments)
  print("Creating identifier.")
  identifier = f"{arguments['primary_color']}_{arguments['secondary_color']}"
  filename = await a_generate_filename(identifier)
  yield prompt, filename, channel

async def co_consume_image(producer_coroutine):
  print("Consuming prompt.")
  async for prompt, filename, channel in producer_coroutine:
    image_url = await a_generate_image(prompt)
    await a_download_image(image_url, filename, channel)

async def co_run_images(template_key, arguments, channel):
  producer_coroutine = co_produce_image(template_key, arguments, channel)
  await co_consume_image(producer_coroutine)

async def a_generate_audio(session, voice, text, channel):
  client = await OPENAI.get()
  file_path = f"{session}_{voice}_{text}.mp3"
  async with client.audio.speech.with_streaming_response.create(
    model='tts-1',
    voice=voice,
    input=text,
  ) as response:
    async with aiofiles.open(file_path, "wb") as file:
      async for chunk in response.iter_bytes():
        await file.write(chunk)
    print(f"Output: {file_path}")
  await channel.send(file=discord.File(file_path))

################################################################################

async def generate_video(start_asset, end_asset):
  # Simulate polling for video generation
  for i in range(5):
    print(f"Dreaming... {i+1}")
    await asyncio.sleep(1)  # Simulate polling interval
    if i == 4:  # Simulate success on 5th attempt
      print(f"Video generated successfully: {start_asset} -> {end_asset}")
      break

################################################################################

async def a_handle_audio_generate(args: str, channel: str):
  if len(args) < 2:
    raise ValueError("Audio generate requires at least 3 arguments.")
  session = args[0]
  voice = args[1]
  text = " ".join(args[2:])
  print(f"Starting TTS generation for text: {text}")
  return await a_generate_audio(session, voice, text, channel)

async def a_handle_text_generate(args: str, channel: str):
  if len(args) < 1:
    raise ValueError("Text generate requires a prompt.")
  prompt = " ".join(args)
  print(f"Starting text generation for prompt: {prompt}")
  return await a_generate_text(prompt)

async def a_handle_image_generate(args: str, channel: str):
  if len(args) != 3:
    raise ValueError("Image generate requires 3 arguments.")
  template, primary, secondary = args
  arguments = {
    "primary_color": primary,
    "secondary_color": secondary
  }
  print(f"Starting image generation for template '{template}' with colors {primary} and {secondary}.")
  await co_run_images(template, arguments, channel)

async def handle_video_generate(args):
  if len(args) < 1:
    raise ValueError("Video generate requires at least 1 argument.")
  if len(args) > 2:
    raise ValueError("Video generation requires no more than 2 arguments.")
  if len(args) == 1:
    start_asset = args
    asyncio.create_task(generate_video(start_asset))
  if len(args) == 2:
    start_asset, end_asset = args
    asyncio.create_task(generate_video(start_asset, end_asset))

################################################################################

DISPATCHER = {
  "text": {
    "generate": lambda args, channel: a_handle_text_generate(args, channel)
  },
  "image": {
    "generate": lambda args, channel: a_handle_image_generate(args, channel)
    # ,"list": lambda args: handle_image_list(args)
    # ,"delete": lambda args: handle_image_delete(args)
  },
  "audio": {
    "generate": lambda args, channel: a_handle_audio_generate(args, channel)
    # ,"list": lambda args: handle_audio_list(args)
    # ,"delete": lambda args: handle_audio_delete(args)

  }
#  ,"video": {
#    "generate": lambda args: handle_video_generate(args)
    # ,"append": lambda args: handle_video_append(args)
    # ,"list": lambda args: handle_video_list(args)
    # ,"delete": lambda args: handle_video_delete(args)
#  }
}

async def a_parse_and_dispatch(command: str, channel: str):
  print("Parsing message.")
  words = command.split()
  if len(words) < 2: # Basic input validation
    raise ValueError("Invalid command format. Must include <result> <action>.")
  result, action = words[0], words[1]
  args = words[2:]
  if result not in DISPATCHER or action not in DISPATCHER[result]: # Dispatch map validation
    raise ValueError(f"Unknown command: {result} {action}")
  response = await DISPATCHER[result][action](args, channel)
  return response

################################################################################

def s_run_luma():
  client = LUMAAI.get()

  generation = client.generations.create(
    aspect_ratio="16:9",
    loop="false",
    prompt="Blur and fade out",
    keyframes={
      "frame0":{
        "type":"generation",
        "id":"adc2e2c2-417c-4b33-bd35-5b3a20b9aae1"
      },
      "frame1":{
        "type":"image",
        "url":"https://theoraclesa.blob.core.windows.net/lumaai/key_black.jpg"
      }
    }
  )

  completed = False
  while not completed:
    generation = client.generations.get(id=generation.id)
    if generation.state == "completed":
      completed = True
    elif generation.state == "failed":
      raise RuntimeError(f"Generation failed: {generation.failure_reason}")
    print("Dreaming...")
    time.sleep(3)

  video_url = generation.assets.video

  response = requests.get(video_url, stream=True)
  with open(f'{generation.id}.mp4', 'wb') as file:
    file.write(response.content)
  print(f"File downloaded as {generation.id}.mp4")

################################################################################
## Entry Point
################################################################################

async def main():
  """
  Entry point to run the Discord bot.
  """
  print("Starting the Discord bot.")
  bot = await DISCORD.get()
  token = await a_get_discord_token()

  @bot.event
  async def on_ready():
    print(f"Logged in as {bot.user}")
    channel = bot.get_channel(1306414351598747709)
    if channel:
      await channel.send("Online.")

  @bot.command(name="imagen")
  async def imagen(ctx, *args):
    """
    Dispatch command that takes arguments and processes them using DISPATCHER.
    Example usage in Discord: !imagen text generate How hot is the sun?
    """
    # Join the arguments to form a single command string
    command_str = " ".join(args)
    try:
      channel = ctx.channel
      response = await a_parse_and_dispatch(command_str, channel)
      if response:
        await ctx.send(response)
      else:
        await ctx.send("Command executed successfully.")
    except ValueError as e:
      await ctx.send(f"Error: {str(e)}")
    except Exception as e:
      await ctx.send(f"An unexpected error occurred: {str(e)}")

  await bot.start(token)

if __name__ == "__main__":
  try:
    asyncio.run(main())
  except KeyboardInterrupt:
    print("Bot terminated by user.")
  except Exception as e:
    print(f"ERROR: {str(e)}")
