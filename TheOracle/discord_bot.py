import os
import json
import requests
import asyncio
import aiofiles
import aiohttp
import discord
from discord.ext import commands
from datetime import datetime, timezone
from lumaai import LumaAI
from openai import AsyncOpenAI

################################################################################
## Functional Section                                                         ##
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
                    print(f"Loading value for {self._loader_func.__name__}")
                    self._value = await self._loader_func()
        return self._value

################################################################################

async def a_load_json(file_path: str) -> dict:
    """
    Loads a JSON file asynchronously.
    """
    print(f"Loading JSON file: {file_path}.")
    async with aiofiles.open(file_path, "r") as file:
        data = await file.read()
    return json.loads(data)

# Global configuration singleton
CONFIG = AsyncSingleton(lambda: a_load_json("config.json"))

################################################################################

async def a_get_openai_token() -> str:
    """
    Gets the OpenAI API token from the environment or config.json.
    """
    print("Fetching OpenAI token.")
    secret = os.getenv('OPENAI_SECRET')
    if secret:
        return secret
    else:
        config = await CONFIG.get()
        return config["tokens"]["openai"]

async def a_get_lumaai_token() -> str:
    """
    Gets the LumaAI API token from the environment or config.json.
    """
    print("Fetching LumaAI token.")
    secret = os.getenv('LUMAAI_SECRET')
    if secret:
        return secret
    else:
        config = await CONFIG.get()
        return config["tokens"]["lumaai"]

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

async def a_init_openai():
    """
    Creates and initializes the OpenAI client.
    """
    print("Initializing OpenAI client.")
    token = await a_get_openai_token()
    return AsyncOpenAI(api_key=token)

async def a_init_lumaai():
    """
    Creates and initializes the LumaAI client.
    """
    print("Initializing LumaAI client.")
    token = await a_get_lumaai_token()
    return LumaAI(auth_token=token)

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

# Singletons for APIs
LUMAAI = AsyncSingleton(a_init_lumaai)
OPENAI = AsyncSingleton(a_init_openai)
DISCORD = AsyncSingleton(a_init_discord)

################################################################################

async def a_generate_text(prompt: str) -> str:
    """
    Generates text using OpenAI ChatGPT.
    """
    print("Sending text prompt to OpenAI.")
    client = await OPENAI.get()
    completion = await client.chat.completions.create(
        model="chatgpt-4o-latest",
        max_tokens=250,
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ]
    )
    print("Received response from OpenAI.")
    return completion.choices[0].message.content

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
        channel = bot.get_channel(1306414351598747709)  # Replace with your channel ID
        if channel:
            await channel.send("Bot is online!")
    await bot.start(token)

# Run the bot
if __name__ == "__main__":
  try:
    asyncio.run(main())
  except KeyboardInterrupt:
    print("Bot terminated by user.")
  except Exception as e:
    print(f"Critical error: {str(e)}")