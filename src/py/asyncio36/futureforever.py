#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import asyncio


async def slow_operation(future):
    await asyncio.sleep(1)
    future.set_result('Future is done!')


def got_result(future):
    print(future.result())
    loop.stop()


loop = asyncio.get_event_loop()
future = asyncio.Future()
# asyncio.ensure_future(coro_or_future, *, loop=None)
# Schedule the execution of a coroutine object: wrap it in a future.
# Return a Task object.
# If the argument is a Future, it is returned directly.
asyncio.ensure_future(slow_operation(future))
future.add_done_callback(got_result)
try:
    loop.run_forever()
finally:
    loop.close()
