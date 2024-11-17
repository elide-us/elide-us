import json
import requests
import asyncio
import aiofiles
import aiohttp
from datetime import time, datetime, timezone
from lumaai import LumaAI
from openai import OpenAI, AsyncOpenAI

################################################################################

def run_luma():
  config = load_config()

  print("Initializing LumaAI")
  client = LumaAI(auth_token=config["lumaai_key"])

# generation = luma.generation.create(
#   prompt="Sweep left, fade to black"
#   aspect_ratio="16:9"
#   loop="true/false"
#   keyframes={
#     "frame0": {
#       "type": "image",
#       "url": "..."
#     },
#     "frame1": {
#       "type": "generation",
#       "id": "..."
#     }
#   }
# )

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

def run_tts():
  config = load_config()

  print("Initializing OpenAI")
  client = OpenAI(api_key=config["openai_key"])

  print("Parsing tts.json")
  with open("tts.json", "r") as json_file:
    lines = json.load(json_file)

  for line in lines["lines"]:
    filename = line["filename"]
    text = line["text"]
    print(f"Processing {filename}, '{text}'")

    with client.audio.speech.with_streaming_response.create(
      model='tts-1',
      voice='onyx',
      input=text,
    ) as response:
      with open(f"{filename}.mp3", "wb") as file:
        for chunk in response.iter_bytes():
          file.write(chunk)
        print(f"Output: {filename}.mp3")

################################################################################

def s_load_json(file_path):
  with open(file_path, "r") as file:
    data = json.load(file)
  return data

def s_get_template(key):
  print("Getting prompt template")
  template_data = s_load_json("prompts.json")
  if key not in template_data:
    raise ValueError(f"Key '{key}' not found in JSON file.")
  template = template_data[key]
  return template

def s_get_arguments_list(key):
  print("Getting template key map")
  argument_data = s_load_json("args.json")
  if key not in argument_data:
    raise ValueError(f"Key '{key}' not found in JSON file.")
  arguments = argument_data[key]
  return arguments

def s_generate_filename(arguments):
  timestamp = datetime.now(timezone.utc).strftime("%Y%m%d%H%M%S")
  filename = f"{timestamp}_{arguments['arg0']}_{arguments['arg1']}"
  print(f"Generated filename: {filename}.png")
  return filename

def s_merge_prompt(template, arg_set):
  print(f"Merging prompt with arguments: {arg_set}")
  return template.format(**arg_set)

def s_init_openai():
  print("Initializing OpenAI")
  config = s_load_json("config.json")
  return OpenAI(api_key=config["openai_key"])

def s_generate_image(client, prompt):
  print("Sending prompt to DALL-E-3")
  response = client.images.generate(
    model="dall-e-3",
    prompt=prompt,
    size="1792x1024",
    quality="standard",
    n=1
  )
  image_url = response.data[0].url
  return image_url

def s_download_image(image_url, filename):
  print(f"Downloading {filename}.png")
  response = requests.get(image_url, stream=True)
  with open(f"{filename}.png", "wb") as file:
    file.write(response.content)

async def co_produce_prompts(template_key, arguments_key):
  template = s_get_template(template_key)
  arguments_list = s_get_arguments_list(arguments_key)
  for arg_set in arguments_list:
    prompt = s_merge_prompt(template, arg_set)
    filename = s_generate_filename(arg_set)
    yield prompt, filename

async def co_consume_prompts(producer_coroutine):
  client = s_init_openai()
  async for prompt, filename in producer_coroutine:
    s_download_image(s_generate_image(client, prompt), filename)

async def co_run_images(template_key, arguments_key):
  producer_coroutine = co_produce_prompts(template_key, arguments_key)
  await co_consume_prompts(producer_coroutine)

def run_image(template_key, arguments_key):
  client = s_init_openai()
  template = s_get_template(template_key)

  arguments = s_get_arguments_list(arguments_key)
  for arg_set in arguments: # from a logic standpoint, this is the producer, or emitter of events
    prompt = s_merge_prompt(template, arg_set) # and these functions are the consumer
    filename = s_generate_filename(arg_set)
    s_download_image(s_generate_image(client, prompt), filename)

################################################################################

#run_image("gothfembust")
#run_image("dreamfembust", "sevenschools")
asyncio.run(co_run_images("dreamfembust", "sevenschools"))
#run_tts()

#run_luma()

################################################################################

# Async version below is WIP

# Returns a JSON once loaded
async def load_json(file_path):
  print(f"Loading JSON from: {file_path}")
  async with aiofiles.open(file_path, "r") as file:
    content = await file.read()
    print(f"Loaded content from {file_path}: {content[:100]}...")  # Print first 100 chars for sanity check
    return json.loads(content)

# Yields a merged prompt from a template prompt and replacement tokens
async def merge_prompts(prompts, arguments):
  for arg_set in arguments:
    print(f"Merging prompt with arguments: {arg_set}")
    merged_prompt = prompts.format(**arg_set)
    print(f"Merged prompt: {merged_prompt[:100]}...")  # Print first 100 chars for sanity check
    yield merged_prompt

# Sends a prompt to OpenAI to generate an image
async def process_prompt(prompt, openai_aclient):
  # Call to OpenAI here
  try:
    print("Sending prompt to OpenAI...")
    response = await openai_aclient.images.generate(
      model="dall-e-3",
      prompt=prompt,
      size="1792x1024",
      quality="standard",
      n=1
    )
    image_url = response.json()["data"][0]["url"]
    print(f"Received image URL: {image_url}")
    return image_url
  except Exception as e:
    print(f"Failed to generate image. Error: {str(e)}")
    return None 

# Function to save image
async def save_image(image_url, filename):
  print(f"Saving image from URL: {image_url} to filename: {filename}")
  async with aiohttp.ClientSession() as session:
    async with session.get(image_url) as response:
      if response.status == 200:
        async with aiofiles.open(filename, 'wb') as file:
          await file.write(await response.read())
        print(f"Saved image as {filename}")
      else:
        print(f"Failed to download image from {image_url}. HTTP Status Code: {response.status}")

# Loads the template and tokens and produces an array of prompts
async def co_produce_prompt(prompt_key, prompts_file, arguments_file):
  print(f"Producing prompt with key: {prompt_key}")
  prompts_data = await load_json(prompts_file)
  arguments_data = await load_json(arguments_file)

  # Check the provided prompt key is valid
  if prompt_key not in prompts_data or prompt_key not in arguments_data:
    print(f"Error: Key '{prompt_key}' not found in JSON file.")
    raise ValueError(f"Key '{prompt_key}' not found in JSON file.")
  
  # A template string from the provided prompt key (eg: "gothfembust")
  prompt = prompts_data[prompt_key]["prompt"]
  print(f"Loaded prompt template: {prompt[:100]}...")  # Print first 100 chars for sanity check
  # An array of template replacement tokens
  arguments = arguments_data[prompt_key]
  print(f"Loaded arguments: {arguments}")

  # Yield a merged prompt to the consumer (co-routine)
  async for prompt in merge_prompts(prompt, arguments):
    yield prompt, arguments

# Obtains an image URL and produces a filename for saving an image
async def co_consume_prompt(producer_coroutine, process_prompt, openai_aclient):
  async for prompt, arguments in producer_coroutine:
    print(f"Processing prompt...")
    image_url = await process_prompt(prompt, openai_aclient)
    if not image_url:
      print(f"Skipping prompt due to failed image generation.")
      continue
    print(f"Image generated: {image_url}")

    timestamp = datetime.now(timezone.utc).strftime("%Y%m%d%H%M%S")
    filename = f"{timestamp}_{arguments.get('arg0')}_{arguments.get('arg1')}.png"
    print(f"Generated filename: {filename}")

    # save_image(image_url, filename) # Synchronous version
    await save_image(image_url, filename)

# Coordination function for image producer
async def DEL_run_images():
  prompts_file = "prompts.json"
  arguments_file = "args.json"
  config_file = "config.json"

  print("Initializing OpenAI")
  config_data = await load_json(config_file)
  openai_key = config_data["openai_key"]
  openai_aclient = AsyncOpenAI(api_key=openai_key)

  producer_coroutine = co_produce_prompt("gothfembust", prompts_file, arguments_file)
  await co_consume_prompt(producer_coroutine, process_prompt, openai_aclient)

################################################################################

#asyncio.run(DEL_run_images())
