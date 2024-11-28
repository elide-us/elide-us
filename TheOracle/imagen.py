import asyncio
from module_clients import DISCORD, DISCORD_TOKEN, DISCORD_CHANNEL
from module_openai import a_generate_audio, a_generate_text, co_run_images, simple_parser
from module_lumaai import a_generate_video

################################################################################
## Dispatch Handlers
################################################################################

async def a_handle_audio_generate(args: str, channel: str):
  if len(args) < 3:
    raise ValueError("Audio generate requires at least 3 arguments.")
  session, voice = args[0], args[1]
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
  if len(args) < 2:
    raise ValueError("Image generate requires at least 1 arguments.")
  
  template = args[0]
  arguments_str = " ".join(args[1:])

  print(f"Starting image generation for args: {arguments_str}")
  arguments = simple_parser(arguments_str)
  return await co_run_images(template, arguments, channel)

async def a_handle_video_generate(args: str, channel: str):
  if len(args) < 1:
    raise ValueError("Video generate requires at least 1 argument.")
  if len(args) > 2:
    raise ValueError("Video generation requires no more than 2 arguments.")
  if len(args) == 1:
    start_asset = args
    asyncio.create_task(a_generate_video(start_asset))
  if len(args) == 2:
    start_asset, end_asset = args
    asyncio.create_task(a_generate_video(start_asset, end_asset))

################################################################################
## Event Dispatcher
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
  ,"video": {
    "generate": lambda args, channel: a_handle_video_generate(args, channel)
    # ,"append": lambda args: handle_video_append(args)
    # ,"list": lambda args: handle_video_list(args)
    # ,"delete": lambda args: handle_video_delete(args)
  }
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
## Entry Point
################################################################################

async def main():
  print("Starting imagen")
  bot = await DISCORD.get()
  bot_token = await DISCORD_TOKEN.get()
  bot_channel = await DISCORD_CHANNEL.get()

  @bot.event
  async def on_ready():
    #channel = bot.get_channel(1306414351598747709)
    channel = bot.get_channel(bot_channel)
    if channel:
      await channel.send("imagen Online.")

  @bot.command(name="imagen")
  async def imagen(ctx, *args):
    command_str = " ".join(args)
    try:
      channel = ctx.channel
      response = await a_parse_and_dispatch(command_str, channel)
      if response:
        await ctx.send(response)
    except ValueError as e:
      await ctx.send(f"Error: {str(e)}")
    except Exception as e:
      await ctx.send(f"An unexpected error occurred: {str(e)}")

  await bot.start(bot_token)

if __name__ == "__main__":
  try:
    asyncio.run(main())
  except KeyboardInterrupt:
    print("Bot terminated by user.")
  except Exception as e:
    print(f"ERROR: {str(e)}")
