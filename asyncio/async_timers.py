import asyncio


async def my_timer_05():
    count = 0
    while True:
        count += 1
        if count > 300:
            break
        await asyncio.sleep(0.5)
        print('Run my timer 1 {}'.format(count))


async def my_timer_2():
    count = 0
    while True:
        count += 1
        if count > 10:
            break
        await asyncio.sleep(2)
        print('Run my timer 2 {}'.format(count))


async def main():
    tasks = []
    tasks.append(asyncio.ensure_future(my_timer_05()))
    tasks.append(asyncio.ensure_future(my_timer_2()))
    await asyncio.gather(*tasks)


loop = asyncio.get_event_loop()
try:
    # loop.run_forever()
    loop.run_until_complete(main())
except KeyboardInterrupt:
    pass
finally:
    print('Closing loop.')
    loop.close()
