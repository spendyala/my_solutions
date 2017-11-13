import asyncio
import uvloop

loop = uvloop.new_event_loop()
asyncio.set_event_loop(loop)


import asyncio

async def cor1(loop):
    print('Hello cor1')
    await asyncio.sleep(0)

async def cor2(loop):
    print('Hello cor2')
    await asyncio.sleep(0)

async def main(loop):
    await asyncio.sleep(0)
    t1 = loop.create_task(cor1(loop))
    await cor2(loop)
    await t1

loop = asyncio.get_event_loop()
loop.run_until_complete(main(loop))
loop.close()

