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