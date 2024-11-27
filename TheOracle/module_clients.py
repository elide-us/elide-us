import os
import discord
from discord.ext import commands
from openai import AsyncOpenAI
from lumaai import LumaAI
from AsyncSingleton import AsyncSingleton, a_load_json

CONFIG = AsyncSingleton(lambda: a_load_json("config.json"))

TEMPLATES = AsyncSingleton(lambda: a_load_json("templates.json"))

ANNOTATIONS = AsyncSingleton(lambda: a_load_json("annocations.json"))
TTSLINES = AsyncSingleton(lambda: a_load_json("text.json"))
LUMACUTS = AsyncSingleton(lambda: a_load_json("lumacuts.json"))

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

async def a_init_discord():
  """
  Creates and initializes the Discord bot.
  """
  print("Initializing Discord bot.")
  intents = discord.Intents.default()
  intents.messages = True
  intents.message_content = True
  bot = commands.Bot(command_prefix='!', intents=intents)
  token = a_get_discord_token
  channel = a_get_discord_channel
  return bot, token, channel

LUMAAI = AsyncSingleton(a_init_lumaai)
DISCORD = AsyncSingleton(a_init_discord)
OPENAI = AsyncSingleton(a_init_openai)