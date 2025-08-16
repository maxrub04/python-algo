import asyncio

async def fetch_data():
    await asyncio.sleep(2) #  Immediate pause that does not block the event loop
    return "Data fetched"
async def main():
    # Tasks are performed in parallel
    # we use create_task for parallel start more than one coroutines
    task1 = asyncio.create_task(fetch_data())
    task2 = asyncio.create_task(fetch_data())
    result1 = await task1
    result2 = await task2
    print(result1, result2)

asyncio.run(main())