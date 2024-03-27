import asyncio


async def my_worker():
    print('my_worker - await sleep')
    await asyncio.sleep(1)
    print('my_worker - done')
    return 44


def print_it(task):
    print('print_it result: ', task.result())


async def do_something():
    print('do_something - create task for my_worker')
    task = asyncio.create_task(my_worker())
    print('do_something - add a callback')
    task.add_done_callback(print_it)
    await task
    # Task info
    print('do_something - task.cancelled()', task.cancelled())
    print('do_something - task.done()', task.done())
    print('do_something - task.result()', task.result())
    print('do_something - task.exception()', task.exception())
    print('do_something - done')


def main():
    print('Main - starting')
    asyncio.run(do_something())
    print('Main - done')


if __name__ == '__main__':
    main()

