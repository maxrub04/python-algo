"""import aiohttp #library for async work with HTTP
import asyncio

async def fetch_url(session, url):
        async with session.get(url) as response:
            return await response.text()

async def main():
    urls = [
        "https://example.com",
        "https://httpbin.org/get",
        "https://api.github.com"
        ]
    async with aiohttp.ClientSession() as session:
        tasks = [asyncio.create_task(fetch_url(session, url)) for url in urls]
        responses = await asyncio.gather(*tasks)
        for url, content in zip(urls, responses):
            print(f"Content from {url} (first 100 symbols): {content[:100]}")

asyncio.run(main())"""

import asyncio
import ssl
import certifi
from aiohttp import ClientSession, TCPConnector


async def fetch_url(url: str):
    ssl_context = ssl.create_default_context(cafile=certifi.where())
    connector = TCPConnector(ssl=ssl_context)

    async with ClientSession(connector=connector) as session:
        async with session.get(url) as response:
            return await response.text()


async def main():
    url = "https://example.com"
    result = await fetch_url(url)
    print(result[:200])  #


asyncio.run(main())