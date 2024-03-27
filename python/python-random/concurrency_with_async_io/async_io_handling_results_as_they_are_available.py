import asyncio
import random


async def my_worker(label):
    print('my_worker - sleep')
    await asyncio.sleep(1)
    result = random.randint(1, 10)
    print('my_worker - done')
    return label + str(result)


async def do_something():
    print('do_something - wait for my_worker')
    # Run three calls to my_worker concurrently and collect results
    for async_func in asyncio.as_completed((my_worker('A'), my_worker('B'), my_worker('C'))):
        result = await async_func
        print('do_something - result:', result)


def main():
    print('Main - starting')
    asyncio.run(do_something())
    print('Main - done')


if __name__ == '__main__':
    main()
