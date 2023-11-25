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