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