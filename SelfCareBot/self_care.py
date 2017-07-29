#!/usr/bin/python3
# -*- encoding: utf-8 -*-

"""Holds the inner workings of the self-care bot."""

import random
import os
import time

def get_phrase():
    """Returns a phrase from phrases.txt"""

    # Seeding
    random.seed(os.urandom(random.randint(0, 1000)))
    with open("phrases.txt", 'r') as phrasefile:
        content = phrasefile.readlines()

    msg = random.choice(content)
    return msg

def periodic_reminder(interval, msg_func, **kwargs):
    """Returns a phrase in the interval specified."""
    start_time = time.time()

    # Infinite loop
    while True:
        print("Current time: %s" % (time.time() - start_time))
        if ((time.time() - start_time) > interval):
            msg_func(kwargs)
            start_time = time.time()
        time.sleep(1)
