import asyncio, aiofiles, aiohttp, asyncpg
import json, os
from lumaai import LumaAI
from AsyncSingleton import AsyncSingleton, a_load_json

async def load_json(file_path: str):
  try:
    async with aiofiles.open(file_path, mode='r') as file:
      return json.loads(await file.read())
  except FileNotFoundError:
    return None

CONFIG = AsyncSingleton(lambda: a_load_json("config.json"))
DATA = AsyncSingleton(lambda: a_load_json("data.json"))

async def a_load_lumafades() -> list:
  data = DATA.get()
  lumafades = data["lumafades"]
  return lumafades

LUMAFADES = AsyncSingleton(lambda: a_load_lumafades())

async def a_get_lumaai_token() -> str:
  secret = os.getenv('LUMAAI_SECRET')
  if secret:
    return secret
  else:
    config = await CONFIG.get()
    return config["tokens"]["lumaai"]

async def a_init_lumaai():
  print("Initializing LumaAI client.")
  token = await a_get_lumaai_token()
  return LumaAI(auth_token=token)

LUMAAI = AsyncSingleton(a_init_lumaai)

################################################################################
## LumaLabs API v1
################################################################################

async def a_download_generation1(video_url, filename):
  async with aiohttp.ClientSession() as session:
    #async with session.get(video_url, stream=True) as response:
    async with session.get(video_url) as response:
      if response.status == 200:
        file_path = f"{filename}.mp4"
        async with aiofiles.open(file_path, "wb") as file:
          await file.write(await response.read())
        print(f"{file_path} downloaded successfully.")
      else:
        print(f"Failed to download {file_path}. Status: {response.status}")

# Keys: fades (This is not implemented, just an idea for templating the prompts for Luma)
async def a_get_lumacuts1(key: str) -> list:
  """
  Loads a particular set of cut templates from lumacuts.json.
  """
  cuts_data = await LUMAFADES.get()
  if key not in cuts_data:
    raise ValueError(f"Key '{key}' not found in JSON file.")
  cuts = cuts_data[key]
  for cut in cuts:
    print(f"{cut["name"]}")
  return cuts

async def a_get_keyframes1(start_asset, end_asset):
  # if _asset is a URL (starts with https:), create type:image
  # else create type:generation (validate the GUID)
  keyframes = {
    "frame0":{
      "type":"generation",
      "id":"adc2e2c2-417c-4b33-bd35-5b3a20b9aae1"
    },
    "frame1":{
      "type":"image",
      "url":"https://theoraclesa.blob.core.windows.net/lumaai/key_black.jpg"
    }
  }

  if end_asset is None:
    # get JSON block
    return keyframes

  if start_asset is None:
    return keyframes  

  return keyframes

async def a_generate_video1(start_asset, end_asset):
  client = LUMAAI.get()

  keyframes = a_get_keyframes(start_asset=start_asset, end_asset=end_asset)

  generation = client.generations.create(
    aspect_ratio="16:9",
    loop="false",
    prompt="Fade out",
    keyframes=keyframes
  )

  while True:
    generation = client.generations.get(id=generation.id)
    if generation.state == "completed":
      break
    elif generation.state == "failed":
      raise RuntimeError(f"Generation failed: {generation.failure_reason}")
    print("Dreaming...")
    await asyncio.sleep(3)

  video_url = generation.assets.video
  filename = generation.id

  await a_download_generation(video_url, filename)

################################################################################
## LumaLabs API v2
################################################################################

async def a_download_generation2(video_url, filename):
  async with aiohttp.ClientSession() as session:
    #async with session.get(video_url, stream=True) as response:
    async with session.get(video_url) as response:
      if response.status == 200:
        file_path = f"{filename}.mp4"
        async with aiofiles.open(file_path, "wb") as file:
          await file.write(await response.read())
        print(f"{file_path} downloaded successfully.")
      else:
        print(f"Failed to download {file_path}. Status: {response.status}")

# Keys: fades (This is not implemented, just an idea for templating the prompts for Luma)
async def a_get_lumacuts2(key: str) -> list:
  """
  Loads a particular set of cut templates from lumacuts.json.
  """
  cuts_data = await LUMAFADES.get()
  if key not in cuts_data:
    raise ValueError(f"Key '{key}' not found in JSON file.")
  cuts = cuts_data[key]
  for cut in cuts:
    print(f"{cut["name"]}")
  return cuts

def is_url(asset):
  return isinstance(asset, str) and asset.startswith("https:")

def is_valid_guid(guid):
  guid_regex = re.compile(
    r'^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$'
  )
  return isinstance(guid, str) and guid_regex.match(guid)

async def a_get_keyframes2(start_asset, end_asset):
  keyframes = {}

  if start_asset:
    if is_url(start_asset):
      keyframes["frame0"] = {
        "type": "image",
        "url": start_asset
      }
    elif is_valid_guid(start_asset):
      keyframes["frame0"] = {
        "type": "generation",
        "id": start_asset
      }

  if end_asset:
    if is_url(end_asset):
      keyframes["frame1"] = {
        "type": "image",
        "url": end_asset
      }
    elif is_valid_guid(end_asset):
      keyframes["frame1"] = {
        "type": "generation",
        "id": end_asset
      }

  return keyframes

# prompt="Orbit right",
# prompt="Orbit left",
# prompt="Pan right",
# prompt="Pan left",
# prompt="Push in",
# prompt="Pull out",
async def a_generate_video2(prompt, start_asset, end_asset, channel):
  client = await LUMAAI.get()
  keyframes = await a_get_keyframes(start_asset, end_asset)

  generation = client.generations.create(
    aspect_ratio="16:9",
    loop="false",
    prompt=prompt,
    keyframes=keyframes
  )

  while (generation := client.generations.get(id=generation.id)).state != "completed":
    if generation.state == "failed":
      await channel.send(f"Generation failed: {generation.failure_reason}.")
    if channel:
      await channel.send(f"Dreaming... current state: {generation.state}.")
    await asyncio.sleep(5)

  video_url = generation.assets.video
  filename = generation.id

  if channel:
    await channel.send(f"Generation URL: {video_url}, Generation ID: {filename}")
  await a_download_generation(video_url, filename)

################################################################################
################################################################################

# Hardcoded connection string for testing purposes
CONNECTION_STRING = "postgresql://your_user:your_password@your_host:5432/your_database"

# Function to execute a query from a JSON file
async def run_query():
    try:
        # Connect to the PostgreSQL database
        conn = await asyncpg.connect(CONNECTION_STRING)

        # Read the query from the JSON file
        with open('query.json', 'r') as file:
            data = json.load(file)
            query = data.get('query', '')

        if not query:
            print("No query found in query.json")
            return

        # Execute the query and fetch results
        result = await conn.fetch(query)

        # Print the result
        if result:
            print("Query result:")
            for row in result:
                print(dict(row))
        else:
            print("Query executed successfully with no results.")

        # Close the connection
        await conn.close()

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
  asyncio.run(run_query())
