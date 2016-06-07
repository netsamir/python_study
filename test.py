#!/usr/bin/env python

import subprocess
from functools import wraps
import getpass
import os

#class Command(object):
def options(f):
    return check(f, " -l")

def check(f, option):
    @wraps(f)
    def real_cmd(*args, **kwargs):
        return "%s %s" % (f(), option)
    return real_cmd

@options
def start_mfp():
    cmd = "ls"
    return cmd

if __name__ == '__main__':
    cmd = str(start_mfp())
    subprocess.call(cmd)
