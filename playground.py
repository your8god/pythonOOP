class User:
    def __init__(self, name, age):
        self.set_name(name)
        self.set_age(age)
        
    def get_name(self):
        return self._name
    
    def get_age(self):
        return self._age
    
    def set_name(self, name):
        if type(name) == str and name.isalpha():
            self._name = name
        else:
            raise ValueError('Некорректное имя')
        
    def set_age(self, age):
        if type(age) == int and 0 <= age <= 110:
            self._age = age
        else:
            raise ValueError('Некорректный возраст')
        


class Rectangle:
    def __init__(self, l, w):
        self.length = l
        self.width = w

    @property
    def perimeter(self):
        return self.width * 2 + self.length * 2
    
    @property
    def area(self):
        return self.width * self.length


class HourClock:
    def __init__(self, hours):
        self.hours = hours

    def get_hours(self):
        return self._hours
    
    def set_hours(self, h):
        if isinstance(h, int) and 1 <= h <= 12:
            self._hours = h
        else:
            raise ValueError('Некорректное время')
        
    hours = property(get_hours, set_hours)


class Person:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
    
    def get_fullname(self):
        return '{} {}'.format(self.name, self.surname)

    def set_fullname(self, name):
        self.name, self.surname = name.split()
        
    fullname = property(get_fullname, set_fullname)


def hash_function(password):
    hash_value = 0
    for char, index in zip(password, range(len(password))):
         hash_value += ord(char) * index
    return hash_value % 10**9


class Account:
    def __init__(self, login, password):
        self._login = login
        self._password = hash_function(password)
        
    @property
    def login(self):
        return self._login
    
    @login.setter
    def login(self, val):
        raise AttributeError('Изменение логина невозможно')
        
    @property
    def password(self):
        return self._password
    
    @password.setter
    def password(self, pas):
        self._password = hash_function(pas)


from math import sqrt


class QuadraticPolynomial:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    @property
    def d(self):
        return self.b**2 - 4 * self.a * self.c

    @property
    def x1(self):
        if self.d < 0:
            return None
        return (-self.b - sqrt(self.d)) / (2 * self.a)
    
    @property
    def x2(self):
        if self.d < 0:
            return None
        return (-self.b + sqrt(self.d)) / (2 * self.a)
    
    @property
    def coefficients(self):
        return self.a, self.b, self.c
    
    @coefficients.setter
    def coefficients(self, coef):
        self.a, self.b, self.c = coef

    @property
    def view(self):
        return f'{self.a}x^2 + {self.b}x + {self.c}'.replace('+ -', '- ')
    

class Color:
    def __init__(self, hexcode):
        self.hexcode = hexcode

    @property
    def hexcode(self):
        return self._hexcode
    
    @hexcode.setter
    def hexcode(self, hexcode):
        self._hexcode = hexcode
        self.r = int(hexcode[0:2], 16)
        self.g = int(hexcode[2:4], 16)
        self.b = int(hexcode[4:6], 16)



class Circle:
    def __init__(self, r):
        self.radius = r

    @classmethod
    def from_diameter(cls, d):
        return cls(d / 2)
    

class Rectangle:
    def __init__(self, l, w):
        self.length = l
        self.width = w

    @classmethod
    def square(cls, side):
        return cls(side, side)
    

class QuadraticPolynomial:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    @classmethod
    def from_iterable(cls, iterable):
        return cls(*iterable)
    
    @classmethod
    def from_str(cls, string):
        return cls(*map(float, string.split()))
    

class Pet:
    pets = []

    def __init__(self, name):
        self.name = name
        Pet.pets.append(self)

    @classmethod
    def first_pet(cls):
        return cls.pets[0] if cls.pets else None
    
    @classmethod
    def last_pet(cls):
        return cls.pets[-1] if cls.pets else None
    
    @classmethod
    def num_of_pets(cls):
        return len(cls.pets)
    


from re import sub, I

class StrExtension:
    @staticmethod
    def remove_vowels(string):
        return sub(rf'[{"aeiouy"}]', '', string, flags=I)
    
    @staticmethod
    def leave_alpha(string):
        return sub(rf'[^a-zA-Z]', '', string, flags=I)
    
    @staticmethod
    def replace_all(string, chars, char):
        return sub(rf'[{chars}]', char, string)
    

import re

class CaseHelper():
    @staticmethod
    def is_snake(string):
        return bool(re.fullmatch(r'[a-z][_a-z]*[a-z]$', string))
    
    @staticmethod
    def is_upper_camel(string):
        return bool(re.fullmatch(r'[A-Z][a-zA-Z]*', string))
    
    @staticmethod
    def to_snake(string):
        return re.sub(r'([a-z])([A-Z])', r'\1_\2', string).lower()
    
    @staticmethod
    def to_upper_camel(string):
        return ''.join(i.title() for i in string.split('_'))