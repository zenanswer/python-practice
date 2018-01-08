#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import asyncio
import datetime


def display_date(end_time, loop):
    print(datetime.datetime.now())
    #  current time, as a float value
    if (loop.time() + 1.0) < end_time:
        # AbstractEventLoop.call_later(delay, callback, *args)
        # delay - seconds, int or float
        loop.call_later(1, display_date, end_time, loop)
    else:
        loop.stop()


loop = asyncio.get_event_loop()

# Schedule the first call to display_date()
end_time = loop.time() + 5.0
# AbstractEventLoop.call_soon(callback, *args)
loop.call_soon(display_date, end_time, loop)

# Blocking call interrupted by loop.stop()
loop.run_forever()
loop.close()
