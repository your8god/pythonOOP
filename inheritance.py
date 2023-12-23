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


from abc import ABC, abstractmethod

class ChessPiece(ABC):
    _transform = {j: i for i, j in enumerate('abcdefgh')}

    @classmethod
    def transform(cls, x, y):
        return cls._transform[x], 8 - y 

    def __init__(self, x, y):
        self.horizontal, self.vertical = x, y
        self.x, self.y = self.__class__.transform(x, y)

    @abstractmethod
    def can_move(self):
        pass

class King(ChessPiece):
    def can_move(self, x, y):
        x, y = self.__class__.transform(x, y)
        check_first = abs(self.x - x) == 1 and \
                      abs(self.y - y) in (0, 1)
        check_second = abs(self.x - y) == 1 and \
                      abs(self.y - x) in (0, 1)
        return any([check_first, check_second])
    
class Knight(ChessPiece):
    def can_move(self, x, y):
        x, y = self.__class__.transform(x, y)
        check_first = abs(self.x - x) == 1 and \
                      abs(self.y - y) == 2
        check_second = abs(self.x - x) == 2 and \
                      abs(self.y - y) == 1
        return any([check_first, check_second])


from abc import ABC, abstractmethod

class Validator(ABC):
    def __set_name__(self, cls, attr):
        self.attr = attr

    def __get__(self, obj, cls):
        if obj is None:
            return self
        if self.attr in obj.__dict__:
            return obj.__dict__[self.attr]
        return AttributeError('Атрибут не найден')
    
    def __set__(self, obj, val):
        if self.validate(val):
            obj.__dict__[self.attr] = val

    @abstractmethod
    def validate(self, obj):
        pass

class Number(Validator):
    def __init__(self, minvalue=None, maxvalue=None):
        self.minvalue = minvalue
        self.maxvalue = maxvalue

    def validate(self, obj):
        if not isinstance(obj, (int, float)):
            raise TypeError('Устанавливаемое значение должно быть числом')
        if not self.minvalue is None and obj < self.minvalue:
            raise ValueError(f'Устанавливаемое число должно быть больше или равно {self.minvalue}')
        if not self.maxvalue is None and obj > self.maxvalue:
            raise ValueError(f'Устанавливаемое число должно быть меньше или равно {self.maxvalue}')
        return True

class String(Validator):
    def __init__(self, minsize=None, maxsize=None, predicate=None):
        self.minsize = minsize
        self.maxsize = maxsize
        self.predicate = predicate

    def validate(self, obj):
        if not isinstance(obj, str):
            raise TypeError('Устанавливаемое значение должно быть строкой')
        if not self.minsize is None and len(obj) < self.minsize:
            raise ValueError(f'Длина устанавливаемой строки должна быть больше или равна {self.minsize}')
        if not self.maxsize is None and len(obj) > self.maxsize:
            raise ValueError(f'Длина устанавливаемой строки должна быть меньше или равна {self.maxsize}')
        if not self.predicate is None and not self.predicate(obj):
            raise ValueError('Устанавливаемая строка не удовлетворяет дополнительным условиям')
        return True
    

from collections.abc import Iterable, Iterator

def is_iterator(obj):
    return isinstance(obj, Iterator)

def is_iterable(obj):
    return isinstance(obj, Iterable)


from collections.abc import Sequence

class CustomRange(Sequence):
    def __init__(self, *args):
        self.seq = []
        for i in args:
            self.seq.extend(
                [i] if type(i) == int
                else range(int(i.split('-')[0]), int(i.split('-')[1]) + 1)
            )

    def __len__(self):
        return len(self.seq)
    
    def __getitem__(self, key):
        return self.seq[key]
        

class BitArray(Sequence):
    def __init__(self, o=[]):
        self.seq = []
        self.seq.extend(o)

    def __len__(self):
        return len(self.seq)
    
    def __getitem__(self, key):
        return self.seq[key]
    
    def __repr__(self):
        return f'{self.seq!r}'
    
    def __invert__(self):
        return BitArray(map(lambda x: 1 - x, self.seq))
    
    def __or__(self, other):
        if isinstance(other, BitArray) and len(self) == len(other):
            return BitArray([int(any([i, j])) for i, j in zip(self.seq, other.seq)])
        return NotImplemented
    
    def __and__(self, other):
        if isinstance(other, BitArray) and len(self) == len(other):
            return BitArray([int(all([i, j])) for i, j in zip(self.seq, other.seq)])
        return NotImplemented
            

class DNA(Sequence):
    base = {
        'A': 'T',
        'T': 'A',
        'G': 'C',
        'C': 'G',
    }

    def __init__(self, chain):
        self.chain = chain

    def __len__(self):
        return len(self.chain)
    
    def __str__(self):
        return self.chain
    
    def __getitem__(self, key):
        return self.chain[key], __class__.base[self.chain[key]]
    
    def __contains__(self, value):
        return value in self.chain
    
    def __eq__(self, other):
        if isinstance(other, __class__):
            return self.chain == other.chain
        return NotImplemented
    
    def __add__(self, other):
        if isinstance(other, __class__):
            return __class__(self.chain + other.chain)
        return NotImplemented
    

from collections.abc import MutableSequence

class SortedList(MutableSequence):
    def __init__(self, o=[]):
        self.seq = []
        self.seq.extend(o)
        self.seq.sort()
        
    def add(self, item):
        self.seq.append(item)
        self.seq.sort()

    def discard(self, item):
        while self.seq.count(item):
            self.seq.remove(item)
        self.seq.sort()

    def update(self, other):
        self.seq.extend(other)
        self.seq.sort()
    
    def insert(self, item, ind):
        raise NotImplementedError

    def __reversed__(self):
        raise NotImplementedError
    
    def __repr__(self):
        return f'{__class__.__name__}({self.seq!r})'
    
    def __len__(self):
        return len(self.seq)
    
    def __getitem__(self, key):
        return self.seq[key]
    
    def __delitem__(self, key):
        del self.seq[key]

    def __setitem__(self, key, val):
        raise NotImplementedError
    
    def __add__(self, other):
        if isinstance(other, __class__):
            return __class__(self.seq + other.seq)
        return NotImplemented
    
    def __iadd__(self, other):
        if isinstance(other, __class__):
            self.seq += other.seq
            self.seq.sort()
            return self
        return NotImplemented
    
    def __mul__(self, n):
        if isinstance(n, int):
            return __class__(self.seq * n)
        return NotImplemented
    
    def __imul__(self, n):
        if isinstance(n, int):
            self.seq *= n
            self.seq.sort()
            return self
        return NotImplemented
    

class A:
    pass

class B(A):
    pass

class C(A):
    pass

class D(A):
    pass

class E(B, D):
    pass


class H:
    pass

class D(H):
    pass

class E(H):
    pass

class F(H):
    pass

class G(H):
    pass

class B(D, E):
    pass

class C(F, G):
    pass

class A(B, C):
    pass


def get_method_owner(cls, method):
    for item in cls.__mro__:
        if method in item.__dict__:
            return item
        

from abc import ABC, abstractmethod

class Person(ABC):
    def __init__(self, mood='neutral'):
        self.mood = mood

    @abstractmethod
    def greet(self):
        raise NotImplementedError

class Father(Person):
    def greet(self):
        return 'Hello!'
    
    def be_strict(self):
        self.mood = 'strict'

class Mother(Person):
    def greet(self):
        return 'Hi, honey!'
    
    def be_kind(self):
        self.mood = 'kind'

class Daughter(Mother, Father):
    pass

class Son(Father, Mother):
    pass


class MROHelper:
    @staticmethod
    def len(cls):
        return len(cls.__mro__)
    
    @staticmethod
    def class_by_index(cls, n=0):
        return cls.__mro__[n]
    
    @staticmethod
    def index_by_class(child, parent):
        return child.__mro__.index(parent)
    

from datetime import date

class MyDate:
    def __init__(self, year, month, day):
        self.data = date(year, month, day)

    def iso_format(self):
        return self.data.isoformat()

class USADate(MyDate):
    def format(self):
        return self.data.strftime('%m-%d-%Y')
    
class ItalianDate(MyDate):
    def format(self):
        return self.data.strftime('%d/%m/%Y')
    

from abc import ABC, abstractmethod 

class Stat(ABC):
    def __init__(self, iterable=[]):
        self.stat = []
        self.stat.extend(iterable)

    def add(self, item):
        self.stat.append(item)

    def clear(self):
        self.stat.clear()

    @abstractmethod
    def result(self):
        raise NotImplemented

class MinStat(Stat):
    def result(self):
        return min(self.stat, default=None)
    
class MaxStat(Stat):
    def result(self):
        return max(self.stat, default=None)

class AverageStat(Stat):
    def result(self):
        return None if not self.stat else sum(self.stat) / len(self.stat)
    

class Paragraph:
    def __init__(self, n):
        self.length = n
        self.text = []

    def add(self, text):
        text = ' '.join(self.text) + ' ' + text
        self.text.clear()
        text = text.split()
        while text:
            sentense = ''
            while text and len(sentense + ' ' + text[0]) <= self.length:
                sentense += ' ' + text[0]
                text.pop(0)
            self.text.append(sentense.lstrip())

class LeftParagraph(Paragraph):
    def end(self):
        print(*self.text, sep='\n')
        self.text.clear()

class RightParagraph(Paragraph):
    def end(self):
        for i in self.text:
            print(f'{i:>{self.length}}')
        self.text.clear()


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f'{self.x, self.y}'
    
class Circle:
    def __init__(self, radius, center):
        self.radius = radius
        self.center = center

    def __str__(self):
        return f'{self.center}, r = {self.radius}'
    

class Item:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return f'{self.name}, {self.price}$'
    
    def __eq__(self, other):
        return self.name == other
    
class ShoppingCart(list):
    add = list.append

    def total(self):
        return 0 if not self else sum(i.price for i in self)
    
    def remove(self, item):
        while self.count(item):
            super().remove(item)

    def __str__(self):
        return '\n'.join(str(i) for i in self)
    

from random import shuffle
from itertools import product

class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return f'{self.suit}{self.rank}'
    
class Deck(list):
    __suits = ("♣", "♢", "♡", "♠")
    __ranks = ("2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A")
    def __init__(self):
        super().__init__(Card(i, j) for i, j in product(self.__suits, self.__ranks))

    def shuffle(self):
        if len(self) != 52:
            raise ValueError('Перемешивать можно только полную колоду')
        shuffle(self)

    def deal(self):
        if not len(self):
            raise ValueError('Все карты разыграны')
        return self.pop()
    
    def __str__(self):
        return f'Карт в колоде: {len(self)}'
    

from collections import deque

class Queue:
    def __init__(self, items=[]):
        self.queue = deque(items)

    def add(self, item):
        self.queue = deque([i for i in self.queue if i[0] != item[0]])
        self.queue.append(item)

    def pop(self):
        if not len(self.queue):
            raise KeyError('Очередь пуста')
        return self.queue.popleft()
    
    def __str__(self):
        return f'{str(self.queue).replace("deque", __class__.__name__)}'
    
    def __len__(self):
        return len(self.queue)
    

from datetime import timedelta, datetime

class Lecture:
    def __init__(self, topic, start_time, duration):
        self.topec = topic
        self.duration = datetime.strptime(duration, '%H:%M')
        self.start_time = datetime.strptime(start_time, '%H:%M')
        self.end_time = timedelta(hours=self.duration.hour, minutes=self.duration.minute) + self.start_time

    def __eq__(self, other):
        if not isinstance(other, __class__):
            return NotImplemented
        return self.start_time >= other.end_time or self.end_time <= other.start_time

class Conference:
    def __init__(self):
        self.list = []

    def add(self, topic):
        if all([i == topic for i in self.list]):
            self.list.append(topic)
        else:
            raise ValueError('Провести выступление в это время невозможно')
        
    def total(self):
        res = sum([timedelta(hours=i.duration.hour, minutes=i.duration.minute) for i in self.list],
                    start=datetime.strptime('00:00', '%H:%M'))
        return res.strftime('%H:%M')
    
    def longest_lecture(self):
        return max([i.duration for i in self.list]).strftime('%H:%M')
    
    def longest_break(self):
        self.list.sort(key=lambda x: x.start_time)
        breaks = []
        for i in range(1, len(self.list)):
            breaks.append(self.list[i].start_time - self.list[i-1].end_time)
        return max([i.duration for i in breaks]).strftime('%H:%M')