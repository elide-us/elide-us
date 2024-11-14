import requests
import time
import json
from lumaai import LumaAI
from openai import OpenAI

def load_config():
  with open("config.json", "r") as file:
    config = json.load(file)
  print(f"Loaded config.json")
  return config

################################################################################

def run_luma():
  config = load_config()

  print("Initializing LumaAI")
  luma = LumaAI(auth_token=config["lumaai_key"])

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

  generation = luma.generations.create(
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
    generation = luma.generations.get(id=generation.id)
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

#run_tts()

run_luma()
