import aiofiles #library for async for with files
import asyncio


async def read_file_async(filename):
    async with aiofiles.open(filename, mode='r') as f:
        contents = await f.read()
        return contents


async def main():
    data = await read_file_async("example.txt")
    print("File contents:", data)

asyncio.run(main())