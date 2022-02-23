import time
import asyncio

arr = [('a', 1), ('b', 3)]


async def count(xn):
    print('count start', time.localtime().tm_sec)
    print('sleep %s 秒' % xn[1])
    await asyncio.sleep(xn[1])
    print('print param', xn)
    print('count end', time.localtime().tm_sec)


async def main():
    for item in arr:
        await count(item)


asyncio.run(main())
