from functools import total_ordering

@total_ordering
class Shape:
    __slots__ = ("name", "color", "area")

    def __init__(self, name, color, area):
        self.area = area
        self.name = name
        self.color = color

    def __eq__(self, other):
        if not isinstance(other, __class__):
            return NotImplemented
        return self.area == other.area
    
    def __lt__(self, other):
        if not isinstance(other, __class__):
            return NotImplemented
        return self.area < other.area
    
    def __str__(self):
        return f'{self.color} {self.name} ({self.area})'
    

from enum import Enum

class HTTPStatusCodes(Enum):
    CONTINUE = 100
    OK = 200
    USE_PROXY = 305
    NOT_FOUND = 404
    BAD_GATEWAY = 502

    def info(self):
        return self.name, self.value
    
    def code_class(self):
        match self:
            case __class__.CONTINUE:
                return 'информация'
            case __class__.OK:
                return 'успех'
            case __class__.USE_PROXY:
                return 'перенаправление'
            case __class__.NOT_FOUND:
                return 'ошибка клиента'
            case __class__.BAD_GATEWAY:
                return 'ошибка сервера'
            

from enum import auto

class Seasons(Enum):
    WINTER = auto()
    SPRING = auto()
    SUMMER = auto()
    FALL = auto()

    def text_value(self, code):
        if code == 'en':
            return self.name.lower()
        return ['зима', 'весна', 'лето', 'осень'][self.value]
    

from datetime import date, timedelta
from calendar import weekday

Weekday = Enum('Weekday', [
    'MONDAY',
    'TUESDAY',
    'WEDNESDAY',
    'THURSDAY',
    'FRIDAY',
    'SATURDAY',
    'SUNDAY',
    ], start=0)

class NextDate:
    def __init__(self, today, weekday, after_today=False):
        self.today = today
        self.weekday = weekday
        self.after_today = after_today

    def date(self):
        if self.after_today and self.today.weekday() == self.weekday.value:
            return self.today
        return self.today + timedelta(
            days=self.days_until())

    def days_until(self):
        if self.after_today and self.today.weekday() == self.weekday.value:
            return 0
        cnt = 1
        for i in range(self.today.weekday() + 1, 7):
            if Weekday(i) is self.weekday:
                return cnt
            cnt += 1
        else:
            for i in range(7):
                if Weekday(i) is self.weekday:
                    return cnt
                cnt += 1


from enum import Flag, auto

class OrderStatus(Flag):
    ORDER_PLACED = auto()
    PAYMENT_RECEIVED = auto()
    SHIPPING_COMPLETE = auto()


class MovieGenres(Flag):
    ACTION = auto()
    COMEDY = auto()
    DRAMA = auto()
    FANTASY = auto()
    HORROR = auto()

class Movie:
    def __init__(self, name, genres):
        self.name = name
        self.genres = genres

    def __str__(self):
        return self.name
    
    def in_genre(self, genre):
        return genre in self.genres
    

import functools

class reverse_args:
    def __init__(self, f):
        functools.update_wrapper(self, f)
        self.f = f

    def __call__(self, *args, **kwargs):
        return self.f(*reversed(args), **kwargs)
    

class MaxCallsException(Exception):
    pass

class limited_calls:
    def __init__(self, n):
        self.n = n

    def __call__(self, f):
        @functools.wraps(f)
        def wrapper(*args, **kwargs):
            self.n -= 1
            if self.n < 0:
                raise MaxCallsException('Превышено допустимое количество вызовов')
            return f(*args, **kwargs)
        return wrapper
    

class takes_numbers:
    def __init__(self, f):
        function.update_wrapper(self, f)
        self.f = f

    def __call__(self, *args, **kwargs):
        for i in args + tuple(kwargs.values()):
            if not isinstance(i, (int, float)):
                raise TypeError('Аргументы должны принадлежать типам int или float')
            
        return self.f(*args, **kwargs)
    

class returns:
    def __init__(self, datatype):
        self.datatype = datatype

    def __call__(self, f):
        @function.wraps(f)
        def wrapper(*args, **kwargs):
            res = f(*args, **kwargs)
            if isinstance(res, self.datatype):
                return res
            raise TypeError
        return wrapper
    

class exception_decorator:
    def __init__(self, f):
        functools.update_wrapper(self, f)
        self.f = f

    def __call__(self, *args, **kwargs):
        try:
            res = self.f(*args, **kwargs)
            return res, None
        except Exception as e:
            return None, e.__class__
        

class ignore_exception:
    def __init__(self, *args):
        self.exceptions = args

    def __call__(self, f):
        @functools.wraps(f)
        def wrapper(*args, **kwargs):
            try:
                return f(*args, **kwargs)
            except self.exceptions as e:
                print(f'Исключение {e.__class__.__name__} обработано')
        return wrapper
    

class type_check:
    def __init__(self, types):
        self.types = types

    def __call__(self, f):
        @functools.wraps(f)
        def wrapper(*args, **kwargs):
            if all([type(i) == j for i, j in zip(args, self.types)]):
                return f(*args, **kwargs)
            raise TypeError
        return wrapper
    

def track_instances(cls):
    cls.instances = []
    my_init = cls.__init__

    def init(self, *args, **kwargs):
        my_init(self, *args, **kwargs)
        cls.instances.append(self)

    cls.__init__ = init
    return cls


def add_attr_to_class(**kwargs):
    def decorator(cls):
        for k, v in kwargs.items():
            setattr(cls, k, v)
        return cls
    return decorator


import json

def jsonattr(filename):
    f = open(filename)
    d = json.load(f)
    f.close()
    def wrapper(cls):
        for k, v in d.items():
            setattr(cls, k, v)
        return cls
    return wrapper

with open('test.json', 'w') as file:
    file.write('{"x": 1, "y": 2}')

@jsonattr('test.json')
class MyClass:
    pass
    
print(MyClass.x)
print(MyClass.y)



def singleton(cls):
    my_new = cls.__new__
    cls._obj = None

    @functools.wraps(my_new)
    def new(cls, *args, **kwargs):
        if cls._obj is None:
            cls._obj = my_new(cls)
        return cls._obj
    cls.__new__ = new
    return cls

@singleton
class Person:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f'Person({self.name!r})'


instances = [Person('John Doe') for _ in range(1000)]
person = Person('Doe John')
print(person)
print(instances[389])
print(all(instance is person for instance in instances))


import re

def to_snake(string):
    return re.sub(r'([a-z])([A-Z])', r'\1_\2', string).lower()

def snake_case(attrs=False):
    def wrapper(cls):
        self_dict = dict(cls.__dict__)
        for k, v in self_dict.items():
            if k.startswith('__') and k.endswith('__'):
                continue
            if not callable(v) and not attrs:
                continue
            delattr(cls, k)
            setattr(cls, to_snake(k), v)
        return cls
    return wrapper

@snake_case(attrs=True)
class MyClass:
    FirstAttr = 1
    superSecondAttr = 2

print(MyClass.first_attr)
print(MyClass.super_second_attr)


def auto_repr(args, kwargs):
    def wrapper(cls):
        @functools.wraps(cls.__repr__)
        def repr(self):
            my_args = ', '.join(f"{v!r}" for k, v in self.__dict__.items() if k in args)
            my_kwargs = ', '.join(f"{k}={v!r}" for k, v in self.__dict__.items() if k in kwargs)
            return f"{cls.__name__}({my_args}{', ' if my_args and my_kwargs else ''}{my_kwargs})"
        cls.__repr__ = repr
        return cls
    return wrapper



def limiter(limit, unique, lookup):
    def wrapper(cls):
        cls.instances = []
        def creator(*args, **kwargs):
            item = cls(*args, **kwargs)
            for i in cls.instances:
                if getattr(i, unique) == getattr(item, unique):
                    return i
                
            if len(cls.instances) >= limit:
                if lookup == 'FIRST':
                    return cls.instances[0]
                else:
                    return cls.instances[-1]

            cls.instances.append(item)
            return item
        return creator
    return wrapper

print()

@limiter(2, 'ID', 'FIRST')
class MyClass:
    def __init__(self, ID, value):
        self.ID = ID
        self.value = value


obj1 = MyClass(1, 5)          # создается экземпляр класса с идентификатором 1
obj2 = MyClass(2, 8)          # создается экземпляр класса с идентификатором 2

obj3 = MyClass(1, 20)         # возвращается obj1, так как экземпляр с идентификатором 1 уже есть
obj4 = MyClass(3, 0)          # превышено ограничение limit, возвращается первый созданный экземпляр

print(obj3 is obj1, obj3.value)
print(obj4.value)


from dataclasses import dataclass, field

@dataclass
class City:
    name: str
    population: int
    founded: int


@dataclass(frozen=True)
class MusicAlbum:
    title: str
    artist: str
    genre: str = field(repr=False, compare=False)
    year: int = field(repr=False)


@dataclass
class Point:
    x: float = 0.0
    y: float = 0.0
    quadrant: int = 0

    def __post_init__(self):
        if self.x == 0.0 or self.y == 0.0:
            self.quadrant = 0
        elif self.x > 0 and self.y < 0:
            self.quadrant = 4
        elif self.x < 0 and self.y > 0:
            self.quadrant = 2
        elif self.x > 0 and self.y > 0:
            self.quadrant = 1
        else:
            self.quadrant = 3

    def symmetric_x(self):
        return Point(self.x, self.y * -1)
    
    def symmetric_y(self):
        return Point(self.x * -1, self.y)
    

@dataclass(order=True)
class FootballPlayer:
    name: str = field(compare=False)
    surname: str = field(compare=False)
    value: int = field(repr=False)

@dataclass
class FootballTeam:
    name: str
    players: list = field(default_factory=list, repr=False, compare=False)

    def add_players(self, *args):
        self.players.extend(args)