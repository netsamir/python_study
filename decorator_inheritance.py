#!/usr/bin/env python

from abc import ABCMeta, abstractmethod
from functools import wraps

def cleaning_logs():
    print("Cleaning logs")

def backup_db():
    print("backup_db")

def fullsystem_backup():
    print("fullsystem_backup")

def post_stop(func):
    @wraps(func)
    def enhanced_func(*args, **kwargs):
        action = kwargs['action']
        if action == 'stop':
            func(*args, **kwargs)
            fullsystem_backup()
            backup_db()
            cleaning_logs()
        else:
            func(*args, **kwargs)
    return enhanced_func

def maintenance(cls):
    setattr(cls, '__call__', post_stop(cls.__call__))
    return cls

class AI(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def stop():
        raise NotImplemtedError('NotImplemtedError')

    @abstractmethod
    def start():
        raise NotImplemtedError('NotImplemtedError')

    def __call__(self, action):
        if action == 'start':
            self.start()
        elif action == 'stop':
            self.stop()
        else:
            return ValueError('Action not defined')

        print("Executing the common AI task")

@maintenance
class A(AI):
    def start(self):
        print("Starting A")

    def stop(self):
        print("Stopping A")

class B(AI):
    def stop(self):
        print("Stopping B")

    def start(self):
        print("Starting B")

