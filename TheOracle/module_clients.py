import os
import discord
from discord.ext import commands
from openai import AsyncOpenAI
from lumaai import LumaAI
from AsyncSingleton import AsyncSingleton, a_load_json

# General config.json dictionary with various values for local run
CONFIG = AsyncSingleton(lambda: a_load_json("config.json"))
TEMPLATES = AsyncSingleton(lambda: a_load_json("templates.json"))
DATA = AsyncSingleton(lambda: a_load_json("data.json"))

async def a_load_lumafades() -> list:
  data = DATA.get()
  lumafades = data["lumafades"]
  return lumafades

async def a_load_annotations() -> list:
  data = DATA.get()
  annotations = data["annotations"]
  return annotations

async def a_load_ttslines() -> list:
  data = DATA.get()
  ttslines = data["ttslines"]
  return ttslines

LUMAFADES = AsyncSingleton(lambda: a_load_lumafades())
ANNOTATIONS = AsyncSingleton(lambda: a_load_annotations())
TTSLINES = AsyncSingleton(lambda: a_load_ttslines())

async def a_get_openai_token() -> str:
  """
  Gets the OpenAI bearer token from the environment or config.json.
  """
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

OPENAI = AsyncSingleton(a_init_openai)

async def a_get_lumaai_token() -> str:
  """
  Gets the LumaAI API bearer token from the environment or config.json.
  """
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

LUMAAI = AsyncSingleton(a_init_lumaai)

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

async def a_get_discord_token() -> str:
  """
  Gets the Discord bot token from the environment or config.json.
  """
  secret = os.getenv('DISCORD_SECRET')
  if secret:
    return secret
  else:
    config = await CONFIG.get()
    return config["tokens"]["discord"]

async def a_get_discord_channel() -> int:
  channel = os.getenv('DISCORD_CHANNEL')
  if channel:
    return channel ## This probably needs to be converted from a string...
  else:
    config = await CONFIG.get()
    return config["apps"]["imagen"]

DISCORD = AsyncSingleton(a_init_discord)
DISCORD_TOKEN = AsyncSingleton(a_get_discord_token)
DISCORD_CHANNEL = AsyncSingleton(a_get_discord_channel)
