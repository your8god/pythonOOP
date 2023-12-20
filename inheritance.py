class BasicPlan:
    can_stream = True
    can_download = True
    has_SD = True
    has_HD = False
    has_UHD = False
    num_of_devices = 1
    price = '8.99$'

class SilverPlan(BasicPlan):
    has_HD = True
    num_of_devices = 2
    price = '12.99$'

class GoldPlan(BasicPlan):
    has_HD = True
    has_UHD = True
    num_of_devices = 4
    price = '15.99$'


class WeatherWarning:
    def rain(self):
        print('Ожидаются сильные дожди и ливни с грозой')

    def snow(self):
        print('Ожидается снег и усиление ветра')

    def low_temperature(self):
        print('Ожидается сильное понижение температуры')

from collections.abc import Iterable
from datetime import date
from typing import Any

class WeatherWarningWithDate(WeatherWarning):
    def print_date(self, data):
        print(data.strftime('%d.%m.%Y'))

    def rain(self, data):
        self.print_date(data)
        super().rain()

    def snow(self, data):
        self.print_date(data)
        super().snow()

    def low_temperature(self, data):
        self.print_date(data)
        super().low_temperature()


class Triangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def perimeter(self):
        return self.a + self.b + self.c
    
class EquilateralTriangle(Triangle):
    def __init__(self, side):
        super().__init__(side, side, side)


class Counter:
    def __init__(self, start=0):
        self.value = start

    def inc(self, val=1):
        self.value += val

    def dec(self, val=1):
        self.value = max(0, self.value - val)

class DoubledCounter(Counter):
    def inc(self, val=1):
        for _ in range(2):
            super().inc(val)

    def dec(self, val=1):
        for _ in range(2):
            super().dec(val)


class Summator:
    def total(self, n, deg=1):
        return sum(i**deg for i in range(n + 1))
    
class SquareSummator(Summator):
    def total(self, n):
        return super().total(n, 2)
    
class QubeSummator(Summator):
    def total(self, n):
        return super().total(n, 3)
    
class CustomSummator(Summator):
    def __init__(self, m):
        self.m = m

    def total(self, n):
        return super().total(n, self.m)
    

class FieldTracker:
    def __init__(self):
        self.save()

    def __setattr__(self, name, value):
        if name in self.__dict__:
            self.changes.append(name)
        super().__setattr__(name, value)

    def base(self, attr):
        return self.data[attr]
    
    def has_changed(self, attr):
        return attr in self.changes
    
    def changed(self):
        return {k: self.data[k] for k in self.changes}
    
    def save(self):
        self.data = {**self.__dict__}
        self.changes = []

class Point(FieldTracker):
    fields = ('x', 'y', 'z')

    def __init__(self, x, y, z):
        self.x, self.y, self.z = x, y, z
        super().__init__()

point = Point(1, 2, 3)

print(point.base('x'))
print(point.has_changed('x'))
print(point.changed())


class UpperPrintString(str):
    def __str__(self):
        return super().__str__().upper()
    

class LowerString(str):
    def __new__(cls, obj=''):
        return super().__new__(cls, str(obj).lower())
    
print(LowerString(['GGf']))


class FuzzyString(str):
    def __eq__(self, other):
        if isinstance(other, str): 
            return self.lower() == other.lower()
        return NotImplemented
    
    def __ne__(self, other):
        if isinstance(other, str): 
            return self.lower() != other.lower()
        return NotImplemented
    
    def __lt__(self, other):
        if isinstance(other, str): 
            return self.lower() < other.lower()
        return NotImplemented
    
    def __le__(self, other):
        if isinstance(other, str): 
            return self.lower() <= other.lower()
        return NotImplemented
    
    def __gt__(self, other):
        if isinstance(other, str): 
            return self.lower() > other.lower()
        return NotImplemented
    
    def __ge__(self, other):
        if isinstance(other, str): 
            return self.lower() >= other.lower()
        return NotImplemented
    
    def __contains__(self, key):
        return key.lower() in self.lower()
    

class TitledText(str):
    def __new__(cls, content, text_title):
        instance = super().__new__(cls, content)
        instance._title = text_title
        return instance
    
    def title(self):
        return self._title
    

class SuperInt(int):
    def is_neg(self):
        return "-" if self < 0 else ""

    def repeat(self, n=2):
        return SuperInt(f'{self.is_neg()}{str(abs(self)) * n}')
    
    def to_bin(self):
        return f'{self.is_neg()}{bin(abs(self))[2:]}'
    
    def next(self):
        return SuperInt(self + 1)
    
    def prev(self):
        return SuperInt(self - 1)
    
    def __iter__(self):
        return map(SuperInt, str(abs(self)))
    

class RoundedInt(int):
    def __new__(cls, num, even=True):
        return super().__new__(cls, num + num % 2 if even else num + ~(num % 2))
    

class AdvancedTuple(tuple):
    def __add__(self, other):
        return AdvancedTuple(list(self) + list(other))
    
    def __radd__(self, other):
        return AdvancedTuple(list(other) + list(self))
    

class ModularTuple(tuple):
    def __new__(cls, iterable=(), size=100):
        return super().__new__(cls, map(lambda x: x % size, list(iterable)))
    

from collections import UserList

class DefaultList(UserList):
    def __init__(self, iterable=[], default=None):
        self.default = default
        super().__init__(iterable)

    def __getitem__(self, key):
        try:
            return self.data[key]
        except IndexError:
            return self.default
        

class EasyDict(dict):
    def __getattribute__(self, name):
        return super().__getitem__(name)
    

from collections import UserDict

class TwoWayDict(UserDict):
    def __setitem__(self, key, value):
        self.data[key] = value
        self.data[value] = key
        

class AdvancedList(list):
    def join(self, sep=' '):
        return sep.join(str(item) for item in self)
    
    def map(self, func):
        self[:] = AdvancedList(map(func, self))
        
    def filter(self, func):
        self[:] = AdvancedList(filter(func, self))


class NumberList(UserList):
    def __init__(self, iterable=[]):
        for i in iterable:
            if not isinstance(i, (int, float)):
                raise TypeError('Элементами экземпляра класса NumberList должны быть числа')
        super().__init__(iterable)

    def __setitem__(self, key, item):
        if not isinstance(item, (int, float)):
            raise TypeError('Элементами экземпляра класса NumberList должны быть числа')
        self.data[key] = item

    def append(self, item):
        if not isinstance(item, (int, float)):
            raise TypeError('Элементами экземпляра класса NumberList должны быть числа')
        self.data.append(item)

    def extend(self, item):
        for i in item:
            if not isinstance(i, (int, float)):
                raise TypeError('Элементами экземпляра класса NumberList должны быть числа')
        self.data.extend(item)

    def insert(self, ind, item):
        if not isinstance(item, (int, float)):
            raise TypeError('Элементами экземпляра класса NumberList должны быть числа')
        self.data.insert(ind, item)

    def __add__(self, other):
        if not isinstance(other, (NumberList, list)):
            return NotImplemented
        if type(other) == list:
            for i in other:
                if not isinstance(i, (int, float)):
                    raise TypeError('Элементами экземпляра класса NumberList должны быть числа')
        return NumberList(self.data + other.data)

    def __iadd__(self, other):
        if not isinstance(other, (NumberList, list)):
            return NotImplemented
        if type(other) == list:
            for i in other:
                if not isinstance(i, (int, float)):
                    raise TypeError('Элементами экземпляра класса NumberList должны быть числа')
        self.data += other.data
        return self


class ValueDict(dict):
    def key_of(self, value):
        for k, v in self.items():
            if v == value:
                return k
        return None
    
    def keys_of(self, value):
        return filter(lambda x: self[x] == value, self)
    

from datetime import date

class BirthdayDict(UserDict):
    def __setitem__(self, key, item):
        if item in self.data.values():
            print(f'Хей, {key}, не только ты празднуешь день рождения в этот день!')
        self.data[key] = item


from collections import UserString

class MutableString(UserString):
    def lower(self):
        self.data = self.data.lower()

    def upper(self):
        self.data = self.data.upper()

    def sort(self, key=None, reverse=False):
        self.data = ''.join(sorted(self.data, reverse=reverse, key=key))

    def __setitem__(self, key, val):
        self.data = self.data[:key] + val + self.data[key + 1:]

    def __delitem__(self, key):
        self.data = self.data[:key] + self.data[key + 1:]