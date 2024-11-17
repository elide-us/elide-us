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
  template_data = s_load_json("templates.json")
  if key not in template_data:
    raise ValueError(f"Key '{key}' not found in JSON file.")
  template = template_data[key]
  return template

def s_get_arguments_list(key):
  print("Getting template key map")
  argument_data = s_load_json("arguments.json")
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

asyncio.run(co_run_images("gothfembust", "sevenschools"))
#asyncio.run(co_run_images("dreamfembust", "sevenschools"))

#run_tts()

#run_luma()

################################################################################
