import asyncio, aiohttp, aiofiles
from module_clients import LUMAAI, LUMAFADES

async def a_download_generation(video_url, filename):
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
async def a_get_lumacuts(key: str) -> list:
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

async def a_get_keyframes(start_asset, end_asset):
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

async def a_generate_video(start_asset, end_asset):
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
