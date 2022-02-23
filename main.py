import asyncio
import async1
import async2


async def count1():
    print("count1 start 等待1s")
    await asyncio.sleep(1)
    print("count1 done")


async def count2():
    print("count2 start 等待2s")
    await asyncio.sleep(2)
    print("count2 done")


async def main():
    await asyncio.gather(count1(), count2(), async1.fn(), async2.main())


asyncio.run(main())
