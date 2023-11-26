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