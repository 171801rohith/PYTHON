# AsyncIO

import time
import asyncio


async def func1():
    await asyncio.sleep(2)
    print("func1")
    return "harry"


async def func2():
    await asyncio.sleep(1)
    print("func2")
    return "rohith"


async def func3():
    await asyncio.sleep(4)
    print("func3")
    return "Nothing"

async def main():
    # task = asyncio.create_task(func1())
    # await func2()
    # await func3()

    L = await asyncio.gather(func1(), func2(), func3())
    print(L)

asyncio.run(main())


