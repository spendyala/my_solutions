import asyncio  
import time  
from datetime import datetime


async def custom_sleep():  
    print('SLEEP {}\n'.format(datetime.now()))
    await asyncio.sleep(0)

async def factorial(name, number):  
    f = 1
    for i in range(2, number+1):
        print('Task {}: Compute factorial({})'.format(name, i))
        await custom_sleep()
        f *= i
    print('Task {}: factorial({}) is {}\n'.format(name, number, f))


start = time.time()  
loop = asyncio.get_event_loop()

tasks = [  
    asyncio.ensure_future(factorial("A", 3)),
    asyncio.ensure_future(factorial("B", 4)),
]
def main():
    loop.run_until_complete(asyncio.wait(tasks))  

main()
#tasks = [  
#    asyncio.ensure_future(factorial("C", 8)),
#    asyncio.ensure_future(factorial("D", 5)),
#]
#loop.run_until_complete(asyncio.wait(tasks))  
#tasks = [  
#    asyncio.ensure_future(factorial("E", 1)),
#    asyncio.ensure_future(factorial("F", 9)),
#]
#loop.run_until_complete(asyncio.wait(tasks))  
#loop.close()
#
#end = time.time()  
#print("Total time: {}".format(end - start))
