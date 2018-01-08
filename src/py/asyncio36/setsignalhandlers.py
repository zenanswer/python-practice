#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import asyncio
import functools
import os
import signal


def ask_exit(signame):
    print("got signal %s: exit" % signame)
    loop.stop()


loop = asyncio.get_event_loop()
for signame in ('SIGINT', 'SIGTERM'):
    # AbstractEventLoop.add_signal_handler(signum, callback, *args)
    loop.add_signal_handler(getattr(signal, signame),
                            # ask_exit('SIGINT') and ask_exit('SIGTERM')
                            functools.partial(ask_exit, signame))
    # AbstractEventLoop.remove_signal_handler(sig)

print("Event loop running forever, press Ctrl+C to interrupt.")
print("pid %s: send SIGINT or SIGTERM to exit." % os.getpid())
try:
    loop.run_forever()
finally:
    loop.close()
