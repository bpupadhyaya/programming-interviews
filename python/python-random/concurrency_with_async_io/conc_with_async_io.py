import asyncio
import time


async def my_worker():
    print('Worker - will take some time')
    time.sleep(3)
    print('worker - done')
    return 42


async def do_something():
    print('do_something - will wait for worker')
    result = await my_worker()
    print('do_something - result', result)


def main():
    print('Main - starting')
    asyncio.run(do_something())
    print('Main - done')


if __name__ == '__main__':
    main()
