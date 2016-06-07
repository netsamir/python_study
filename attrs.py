#!/usr/bin/env python


import timeit
import shelve

class SO(object):
    def __init__(self, id):
        self.id = str(id)
        self.sum = 0

    def loop(self):
        self.sum = 0
        for i in self.x:
            self.sum += i
        for i in self.y:
            self.sum += i
        for i in self.z:
            self.sum += i

        print("My Sum for %s is %d" % (self.__class__.__name__, self.sum))

    def save_this(self):
        name = self.__class__.__name__.lower() + ".db"
        db = shelve.open(name)
        print("storing data for %s" % self.id)
        db[self.id] = self
        db.close()

    def read_this(self):
        name = self.__class__.__name__.lower() + ".db"
        db = shelve.open(name)
        for item in db.values():
            print("The value of %s is %d" % (item.id, item.sum))

        db.close()


class SO1(SO):
    """A class to test dynamic init"""
    def __init__(self, id):
        super(SO1, self).__init__(id)
        self._attr = ['x', 'y', 'z']

    def __getattr__(self, name):
        print("%s : Entering  __getattr__ with %s" % (self.__class__.__name__, name))
        if self.__dict__ == {}:
            return super(SO1, self).__getattr__(name)
        if name in self._attr:
            if name == 'x':
                value = range(1, 100)
            elif name == 'y':
                value = range(100, 200)
            elif name == 'z':
                value = range(200, 300)
            else:
                print("call super with %s" % self.__class__)
                return super(SO1, self).__getattr__(name)

            setattr(self, name, value)
            return value
        else:
            print("Attribute does not exists !")
            return super(SO1, self).__getattr__(name)
            #raise AttributeError('%s is not defined' % name)


class SO2(SO):
    """A class to test dynamic init"""
    def __init__(self, id):
        super(SO2, self).__init__(id)
        self.x = None
        self.y = None
        self.z = None

    def __getattribute__(self, name):
        try:
            if super(SO2, self).__getattribute__(name) == None:
                if name == 'x':
                    value = range(1, 100)
                if name == 'y':
                    value = range(100, 200)
                else:
                    value = range(200, 300)
                setattr(self, name, value)
                return super(SO2, self).__getattribute__(name)

            return super(SO2, self).__getattribute__(name)

        except AttributeError:
            print("No my man, you can't do that")
            raise


if __name__ == '__main__':
    for id in range(1, 300):
        so = SO1(str(id))
        so.loop()
        so.save_this()

    print("Retrieving the information ...")
    db = shelve.open("so1.db")
    for item in db.values():
        print("The values stored for %s is %d" % (item.id, item.sum))

    #so2 = SO2("so2")
    #t1 = timeit.Timer(so1.loop).timeit(number=20)
    #t2 = timeit.Timer(so2.loop).timeit(number=20)
    #print ("SO1: %f" % t1)
    #print ("SO2: %f" % t2)
