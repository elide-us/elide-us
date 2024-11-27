import aiofiles
import json
import asyncio

async def a_load_json(file_path: str) -> dict:
  """
  Loads a JSON file asynchronously.
  """
  print(f"Loading JSON: {file_path}.")
  async with aiofiles.open(file_path, "r") as file:
    data = await file.read()
  return json.loads(data)

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
