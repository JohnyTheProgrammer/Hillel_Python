import sys
import dis
import os
import sys


class Point:
    def __init__(self, x, y=-1):
        self.x = x
        self.y = y


p = Point(0, 0)

print('dir(Point):{}'.format(dir(Point)))
print("_______________________________________")
print('dir(p):{}'.format(dir(p)))
# s = 23435
# число ссылок на объект
print(sys.getrefcount(p))
"""размер объекта"""
print(sys.getsizeof(p))


def spam(a):
    x = 42
    return (x > a)


print(spam.__code__.co_code)
print(spam.__code__.co_argcount)
print(spam.__code__.co_varnames)
print(spam.__code__.co_consts)

# Disassembler
print(dis.dis(spam))
