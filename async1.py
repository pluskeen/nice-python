import asyncio


async def fn():
    print('async1 fn start 等待4s')
    await asyncio.sleep(4)
    print('async1 fn done')

