#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import asyncio


async def slow_operation(future):
    await asyncio.sleep(1)
    future.set_result('Future is done!')

loop = asyncio.get_event_loop()
future = asyncio.Future()
asyncio.ensure_future(slow_operation(future))
print('run_until_complete start')
loop.run_until_complete(future)
print('run_until_complete end')
print(future.result())
loop.close()
