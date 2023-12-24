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