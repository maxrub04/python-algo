"""
1. Asynchronous execution of HTTP requests:
    Write a function that asynchronously requests data from 5 different APIs (e.g.,
    public news or weather APIs) and outputs the first 100 characters of the response. Use aiohttp.

2. Reading and writing files:
    Use aiofiles to asynchronously read a large text file and write its contents
    to another file. Measure the execution time and compare it with the synchronous variant.

3. Parallel task processing:
    Create a script that launches 20 asynchronous tasks (e.g., simulating data retrieval
    from an API) with different delays. Use asyncio.gather to execute them in parallel and
    display the total execution time.

4. Integration with a trading system:
    Develop a small module for asynchronous data retrieval from an API (e.g., Binance) and
    updating technical indicators. Use this system to send notifications via
    Telegram if certain conditions are detected."""