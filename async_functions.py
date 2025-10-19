import asyncio


async def fetch_data(delay):
    print(f"Fetching data with delay {delay}...")
    await asyncio.sleep(delay)
    print("enos test")
    print(f"Data fetched after {delay} seconds.")
    return f"Data from delay {delay}"

async def test_data(delay):
    print(f"I dont even know what to do")

async def main():
    data1 = int(input(print(f"Enter data 1 : \n")))
    #print(data1)
    data2 = int(input(print(f"Enter data 2 : \n")))

    task1 = asyncio.create_task(fetch_data(data1))
    task2 = asyncio.create_task(fetch_data(data2))
    #task3 = asyncio.create_task(test_data())

    result1 = await task1
    result2 = await task2
   # result3 = await task3

    print(result1)
    print(result2)

asyncio.run(main())