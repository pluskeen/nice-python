import asyncio


async def fn():
    print('async2 fn start 等待3s')
    await asyncio.sleep(3)
    print('async2 fn done')


async def main():
    print('async2 main start')
    await fn()


# asyncio.run(main())
