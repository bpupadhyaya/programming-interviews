import asyncio
import random


async def my_worker():
    print('my_worker - sleep')
    await asyncio.sleep(1)
    result = random.randint(1, 10)
    print('my_worker - done')
    return result


async def do_something():
    print('do_something - wait for my_workder')
    # Run three calls to my_worker concurrently and collect results
    results = await asyncio.gather(my_worker(), my_worker(), my_worker())
    print('results from calls: ', results)


def main():
    print('Main - starting')
    asyncio.run(do_something())
    print('Main - done')


if __name__ == '__main__':
    main()
