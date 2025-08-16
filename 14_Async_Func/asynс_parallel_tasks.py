import asyncio

async def process_data(i):
    await asyncio.sleep(1)
    print(f"Data processing {i} done")

async def main():
    tasks = [asyncio.create_task(process_data(i)) for i in range(10)]
    await asyncio.gather(*tasks)
asyncio.run(main())