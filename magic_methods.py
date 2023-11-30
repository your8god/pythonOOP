#singleton

class Config:
    _obj = None

    def __new__(cls, *args, **kwargs):
        if cls._obj is None:
            cls._obj = super().__new__(cls)
            # cls._obj = object.__new__(cls)
        return cls._obj
    
    def __init__(self):
        self.program_name = "GenerationPy"
        self.environment = "release"
        self.loglevel = "verbose"
        self.version = "1.0.0"

#####################################################################################################

class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def __repr__(self):
        return f"Book('{self.title}', '{self.author}', {self.year})"

    def __str__(self):
        return f'{self.title} ({self.author}, {self.year})'
    

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def __repr__(self):
        return f'Rectangle({self.length}, {self.width})'


class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f'Vector({self.x}, {self.y})'
    
    def __str__(self):
        return f'Вектор на плоскости с координатами ({self.x}, {self.y})'
    

from functools import singledispatchmethod
from typing import Any

class IPAddress:
    @singledispatchmethod
    def __init__(self, o):
        self.addr = o

    @__init__.register(list)
    @__init__.register(tuple)
    def _list__init__(self, o):
        self.addr = '.'.join(map(str, o))

    def __str__(self):
        return self.addr
    
    def __repr__(self):
        return f"IPAddress('{self.addr}')"
    

class PhoneNumber:
    def __init__(self, num):
        self.num = num.replace(' ', '')

    def __str__(self):
        return f'({self.num[:3]}) {self.num[3:6]}-{self.num[6:]}'
    
    def __repr__(self):
        return f"{self.__class__.__name__}('{self.num}')"
    

class AnyClass:
    def __init__(self, **kwargs):
        self.__dict__ = {**self.__dict__, **kwargs}
        
    def _join(self):
        return ', '.join(f"{k}={v!r}" for k, v in self.__dict__.items())

    def __str__(self):
        return f"{self.__class__.__name__}: {self._join()}"
    
    def __repr__(self):
        return f"{self.__class__.__name__}({self._join()})"
    


class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f'Vector{self.x, self.y}'
    
    def __eq__(self, other):
        if isinstance(other, Vector):
            return self.x == other.x and self.y == other.y
        elif isinstance(other, tuple):
            return (self.x, self.y) == other
        return NotImplemented
    

from functools import total_ordering

@total_ordering
class Word:
    def __init__(self, word):
        self.word = word

    def __repr__(self):
        return f'Word({self.word!r})'
    
    def __str__(self):
        return self.word.title()
    
    def __eq__(self, other):
        if isinstance(other, Word):
            return len(self.word) == len(other.word)
        return NotImplemented
    
    def __lt__(self, other):
        if isinstance(other, Word):
            return len(self.word) < len(other.word)
        return NotImplemented
    

@total_ordering
class Month:
    def __init__(self, y, m):
        self.year = y
        self.month = m

    def __repr__(self):
        return f'Month{self.year, self.month}'
    
    def __str__(self):
        return f'{self.year}-{self.month}'
    
    def __eq__(self, other):
        if isinstance(other, Month):
            return self.year == other.year and self.month == other.month
        elif isinstance(other, tuple):
            return (self.year, self.month) == other
        return NotImplemented
    
    def __lt__(self, other):
        if isinstance(other, Month):
            return (self.year, self.month) < (other.year, other.month)
        elif isinstance(other, tuple):
            return (self.year, self.month) < other
        return NotImplemented
    

@total_ordering
class Version:
    def __init__(self, ver):
        self.ver = list(map(int, ver.split('.')))
        self.ver.extend((3 - len(self.ver)) * [0])

    def __repr__(self):
        return f'Version({".".join(str(i) for i in self.ver)!r})'
    
    def __str__(self):
        return ".".join(str(i) for i in self.ver)
    
    def __eq__(self, other):
        if isinstance(other, Version):
            return self.ver == other.ver
        return NotImplemented
    
    def __lt__(self, other):
        if isinstance(other, Version):
            return self.ver < other.ver
        return NotImplemented
    

class ReversibleString:
    def __init__(self, string):
        self.string = string

    def __pos__(self):
        return ReversibleString(self.string)
    
    def __neg__(self):
        return ReversibleString(self.string[::-1])
    
    def __str__(self):
        return self.string
    

class Money:
    def __init__(self, amount):
        self.amount = amount

    def __str__(self):
        return f'{self.amount} руб.'
    
    def __pos__(self):
        return Money(abs(self.amount))
    
    def __neg__(self):
        return Money(-abs(self.amount))
    

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f'{self.x, self.y}'
    
    def __repr__(self):
        return f'Vector{self.x, self.y}'
    
    def __pos__(self):
        return Vector(self.x, self.y)
    
    def __neg__(self):
        return Vector(-self.x, -self.y)
    
    def __abs__(self):
        return (self.x**2 + self.y**2)**0.5
    

class ColoredPoint:
    def __init__(self, x, y, color=(0, 0, 0)):
        self.x = x
        self.y = y
        self.color = color

    def __repr__(self):
        return f'ColoredPoint{self.x, self.y, self.color}'
    
    def __str__(self):
        return f'{self.x, self.y}'
    
    def __pos__(self):
        return ColoredPoint(self.x, self.y, self.color)
    
    def __neg__(self):
        return ColoredPoint(-self.x, -self.y, self.color)
    
    def __invert__(self):
        return ColoredPoint(self.y, self.x, tuple(map(lambda x: 255 - x, self.color)))
    

from copy import deepcopy

class Matrix:
    def __init__(self, row, col, value=0, mat=None):
        self.rows = row
        self.cols = col
        self._mat = [[value] * col for _ in range(row)]
        if not mat is None:
           self._mat = mat

    def __str__(self):
        return '\n'.join([' '.join(str(i) for i in row) for row in self._mat])
    
    def __repr__(self):
        return f'Matrix{self.rows, self.cols}'
    
    def get_value(self, row, col):
        return self._mat[row][col]
    
    def set_value(self, row, col, val):
        self._mat[row][col] = val

    def __pos__(self):
        return Matrix(self.rows, self.cols, mat=self._mat) 
    
    def __neg__(self):
        copy_map = deepcopy(self._mat)
        for i in range(len(copy_map)):
            for j in range(len(copy_map[i])):
               copy_map[i][j] *= -1
        return Matrix(self.rows, self.cols, mat=copy_map)

    def __invert__(self):
        copy_map = deepcopy(self._mat)
        copy_map = list(map(list, zip(*copy_map)))
        return Matrix(self.cols, self.rows, mat=copy_map)
    
    def __round__(self, n=None):
        copy_map = deepcopy(self._mat)
        for i in range(len(copy_map)):
            for j in range(len(copy_map[i])):
                 copy_map[i][j] = round(copy_map[i][j], n)
        return Matrix(self.rows, self.cols, mat=copy_map)
    


class FoodInfo:
    def __init__(self, proteins, fats, carbohydrates):
        self.proteins = proteins
        self.fats = fats
        self.carbohydrates = carbohydrates

    def __repr__(self):
        return f'FoodInfo{self.proteins, self.fats, self.carbohydrates}'
    
    def __add__(self, other):
        if isinstance(other, FoodInfo):
            return FoodInfo(self.proteins + other.proteins, self.fats + other.fats, self.carbohydrates + other.carbohydrates)
        return NotImplemented

    def __truediv__(self, other):
        if isinstance(other, (int, float)):
            return FoodInfo(self.proteins / other, self.fats / other, self.carbohydrates / other)
        return NotImplemented
    
    def __mul__(self, other):
        if isinstance(other, (int, float)):
            return FoodInfo(self.proteins * other, self.fats * other, self.carbohydrates * other)
        return NotImplemented
    
    def __floordiv__(self, other):
        if isinstance(other, (int, float)):
            return FoodInfo(self.proteins // other, self.fats // other, self.carbohydrates // other)
        return NotImplemented
    


class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f'Vector{self.x, self.y}'
    
    def __add__(self, other):
        if isinstance(other, Vector):
            return Vector(self.x + other.x, self.y + other.y)
        return NotImplemented

    def __sub__(self, other):
        if isinstance(other, Vector):
            return Vector(self.x - other.x, self.y - other.y)
        return NotImplemented
    
    def __mul__(self, other):
        if isinstance(other, (int, float)):
            return Vector(self.x * other, self.y * other)
        return NotImplemented
    
    def __rmul__(self, other):
        return self.__mul__(other)
    
    def __truediv__(self, other):
        if isinstance(other, (int, float)):
            return Vector(self.x / other, self.y / other)
        return NotImplemented
    
    def __rtruediv__(self, other):
        return self.__truediv__(other)
    

class SuperString:
    def __init__(self, string):
        self.string = string

    def __str__(self):
        return self.string
    
    def __add__(self, other):
        if isinstance(other, SuperString):
            return SuperString(self.string + other.string)
        return NotImplemented
    
    def __mul__(self, other):
        if isinstance(other, int):
            return SuperString(self.string * other)
        return NotImplemented
    
    def __rmul__(self, other):
        return self.__mul__(other)
    
    def __truediv__(self, other):
        if isinstance(other, int):
            return SuperString(self.string[:len(self.string) // other])
        return NotImplemented
    
    def __lshift__(self, other):
        if isinstance(other, int):
            return SuperString(self.string[:other])
        return NotImplemented
    
    def __rshift__(self, other):
        if isinstance(other, int):
            return SuperString(self.string[other:])
        return NotImplemented
    

class Time:
    def __init__(self, hours, minutes):
        self.hours = (hours + minutes // 60) % 24
        self.minutes = minutes % 60

    def __str__(self):
        return f'{self.hours:02}:{self.minutes:02}'

    def __add__(self, other):
        if isinstance(other, Time):
            return Time(self.hours + other.hours, self.minutes + other.minutes)
        return NotImplemented
    
    def __iadd__(self, other):
        if not isinstance(other, Time):
            return NotImplemented
        self.hours = (self.hours + other.hours + (self.minutes + other.minutes) // 60) % 24
        self.minutes = (self.minutes + other.minutes) % 60
        return self


from collections import deque
from itertools import islice

class Queue:
    def __init__(self, *args):
        self.queue = deque(args)

    def add(self, *args):
        self.queue.extend(args)

    def pop(self):
        if len(self.queue):
            return self.queue.popleft()
    
    def __str__(self):
        return ' -> '.join(map(str, self.queue))
    
    def __eq__(self, other):
        if isinstance(other, Queue):
            return self.queue == other.queue
        return NotImplemented
    
    def __add__(self, other):
        if isinstance(other, Queue):
            return Queue(*self.queue, *other.queue)
        return NotImplemented
    
    def __iadd__(self, other):
        if isinstance(other, Queue):
            self.queue.extend(other.queue)
            return self
        return NotImplemented
    
    def __rshift__(self, other):
        if isinstance(other, int):
            return Queue(*islice(self.queue, other, None))
        return NotImplemented
    

class Calculator:
    def __call__(self, a, b, op):
        try:
            return eval(f'{a} {op} {b}')
        except ZeroDivisionError:
            raise ValueError('Деление на ноль невозможно')
        

class RaiseTo:
    def __init__(self, degree):
        self.degree = degree

    def __call__(self, x):
        return x**self.degree
    

from random import randint

class Dice:
    def __init__(self, sides):
        self.sides = sides

    def __call__(self):
        return randint(1, self.sides)
    

class QuadraticPolynomial:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def __call__(self, x):
        return self.a*x**2 + self.b*x + self.c
    

class Strip:
    def __init__(self, chars):
        self.chars = chars

    def __call__(self, string):
        return string.strip(self.chars)
    

class Filter:
    def __init__(self, f):
        if f is None:
            self.predicate = bool
        else:
            self.predicate = f

    def __call__(self, iterable):
        return list(filter(self.predicate, iterable))
    

from datetime import date

class DateFormatter:
    __data = {
        "ru": r"%d.%m.%Y",
        "us": r"%m-%d-%Y",
        "ca": r"%Y-%m-%d",
        "br": r"%d/%m/%Y",
        "fr": r"%d.%m.%Y",
        "pt": r"%d-%m-%Y",
    }

    def __init__(self, code):
        self.country_code = DateFormatter.__data[code]

    def __call__(self, d):
        return d.strftime(self.country_code)
    

class CountCalls:
    def __init__(self, f):
        self.f = f
        self.calls = 0

    def __call__(self, *args, **kwargs):
        self.calls += 1
        return self.f(*args, **kwargs)
    

from functools import lru_cache

class CachedFunction:
    def __init__(self, f):
        self.cache = {}
        self.f = f

    @lru_cache
    def __call__(self, *args):
        res = self.f(*args)
        self.cache[args] = res
        return res
    

class SortKey:
    def __init__(self, *args):
        self.args = args

    def __call__(self, x):
        return [getattr(x, attr) for attr in self.args] 
    

class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f'User({self.name}, {self.age})'

users = [User('Gvido', 67), User('Timur', 30), User('Arthur', 20), User('Timur', 45), User('Gvido', 60)]

print(sorted(users, key=SortKey('name')))
print(sorted(users, key=SortKey('name', 'age')))
print(sorted(users, key=SortKey('age')))
print(sorted(users, key=SortKey('age', 'name')))


class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f'{self.x, self.y}'
    
    def __bool__(self):
        return self.x != 0 or self.y != 0
    
    def __abs__(self):
        return (self.x**2 + self.y**2)**0.5

    def __int__(self):
        return int(abs(self))
    
    def __float__(self):
        return float(abs(self))
    
    def __complex__(self):
        return complex(self.x, self.y)
    

class Temperature:
    def __init__(self, t):
        self.temperature = t

    def to_fahrenheit(self):
        return 9/5 * self.temperature + 32
    
    @classmethod
    def from_fahrenheit(cls, t):
        return cls(5/9 * (t - 32))
    
    def __str__(self):
        return f'{round(self.temperature, 2)}°C'
    
    def __bool__(self):
        return self.temperature > 0
    
    def __int__(self):
        return int(self.temperature)
    
    def __float__(self):
        return float(self.temperature)
    

from functools import total_ordering

@total_ordering
class RomanNumeral:
    _roman = {'M': 1000, 'CM': 900, 'D': 500, 'CD': 400, 'C': 100, 'XC': 90, 'L': 50, 'XL': 40, 'X': 10, 'IX': 9, 'V': 5, 'IV': 4, 'I': 1}
    _arabic = {1000:'M', 900:'CM', 500:'D', 400:'CD', 100:'C', 90:'XC', 50:'L', 40:'XL', 10:'X', 9:'IX', 5:'V', 4:'IV', 1:'I'}

    def __init__(self, num):
        self.number = num

    def __str__(self):
        return self.number
    
    def __int__(self):
        res, s_num = 0, self.number
        while s_num:
            for k, v in self._roman.items():
                if s_num.startswith(k):
                    res += v
                    s_num = s_num.replace(k, '', 1)
                    break
        return res
    
    def __eq__(self, other):
        if isinstance(other, RomanNumeral):
            return int(self) == int(other)
        return NotImplemented
    
    def __lt__(self, other):
        if isinstance(other, RomanNumeral):
            return int(self) < int(other)
        return NotImplemented
    
    def _to_roman(self, num):
        res = ''
        while num:
            for k, v in self._arabic.items():
                if num // k != 0:
                     res += (num // k) * v
                     num %= k
                     break
        return res

    def __add__(self, other):
        return RomanNumeral(self._to_roman(int(self) + int(other)))
    
    def __sub__(self, other):
        return RomanNumeral(self._to_roman(int(self) - int(other)))
    

class Item:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def __getattribute__(self, name):
        if name == 'total': 
            return  object.__getattribute__(self, 'price') *  object.__getattribute__(self, 'quantity')
        elif name == 'name':
            return  object.__getattribute__(self, 'name').title()
        return object.__getattribute__(self, name)
    

class Logger:
    def __setattr__(self, name, value):
        print(f'Изменение значения атрибута {name} на {value}')
        object.__setattr__(self, name, value)

    def __delattr__(self, name):
        print(f'Удаление атрибута {name}')
        object.__delattr__(self, name)


class Ord():
    def __getattr__(self, attr):
        return ord(attr)
    

class DefaultObject:
    def __init__(self, default=None, **kwargs):
        self.default = default
        self.__dict__ |= kwargs

    def __getattr__(self, name):
        return self.default
    

class NonNegativeObject:
    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            self.__setattr__(k, v)

    def __setattr__(self, name, value):
        if isinstance(value, (float, int)) and value < 0:
            value *= -1
        object.__setattr__(self, name, value)


class AttrsNumberObject:
    def __init__(self, **kwargs):
        self.__dict__ |= kwargs

    @property
    def attrs_num(self):
        return len(self.__dict__) + 1
    

class Const:
    def __init__(self, **kwargs):
        self.__dict__ |= kwargs

    def __setattr__(self, name, value):
        if name in self.__dict__:
            raise AttributeError('Изменение значения атрибута невозможно')
        object.__setattr__(self, name, value)

    def __delattr__(self, name):
        raise AttributeError('Удаление атрибута невозможно')
    

class ProtectedObject:
    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            object.__setattr__(self, k, v)

    def __getattribute__(self, name):
        if name.startswith('_'):
            raise AttributeError('Доступ к защищенному атрибуту невозможен')
        return object.__getattribute__(self, name)
    
    def __setattr__(self, name, value):
        if name.startswith('_'):
            raise AttributeError('Доступ к защищенному атрибуту невозможен')
        return object.__setattr__(self, name, value)
    
    def __delattr__(self, name): 
        if name.startswith('_'):
            raise AttributeError('Доступ к защищенному атрибуту невозможен')
        object.__delattr__(self, name)


def hash_function(o):
    o, tmp1, tmp2 = str(o), 0, 0
    for i in range(len(o) // 2):
        tmp1 += ord(o[i]) * ord(o[-(i + 1)])

    if len(o) % 2 != 0:
        tmp1 += ord(o[len(o) // 2])

    for i, v in enumerate(o, 1):
        tmp2 += (i * ord(v)) * (-1)**(i + 1)

    return (tmp1 * tmp2) % 123456791
    

def limited_hash(left, right, hash_function=hash):
    def f(o):
        h = int(hash_function(o))
        while h > right:
            h = left + (h - right - 1)
        while h < left:
            h = right - (left - h - 1)
        return h
    return f


class ColoredPoint:
    def __init__(self, x, y, color):
        self._x = x
        self._y = y
        self._color = color

    @property
    def x(self):
        return self._x
    
    @property
    def y(self):
        return self._y
    
    @property
    def color(self):
        return self._color
    
    def __repr__(self):
        return f'{self.__class__.__name__}{self.x, self.y, self.color!r}'
    
    def __eq__(self, other):
        if isinstance(other, ColoredPoint):
            return self.x == other.x and self.y == other.y and self.color == other.color
        return NotImplemented
    
    def __hash__(self):
        return hash((self.x, self.y, self.color))
    

class Row:
    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            object.__setattr__(self, k, v)

    def __setattr__(self, name, val):
        if hasattr(self, name):
            raise AttributeError('Изменение значения атрибута невозможно')
        raise AttributeError('Установка нового атрибута невозможна')
        
    def __delattr__(self, name):
        raise AttributeError('Удаление атрибута невозможно')
    
    def _join(self):
        return ', '.join(f"{k}={v!r}" for k, v in self.__dict__.items())
    
    def __repr__(self):
        return f"{self.__class__.__name__}({self._join()})"
    
    def __eq__(self, other):
        if isinstance(other, Row):
            return self.__repr__() == other.__repr__()
        return NotImplemented
    
    def __hash__(self):
        return hash(self.__repr__())