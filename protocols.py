test = list(range(10))

for i in test:
    print(i)

print()

iterator = iter(test)
while True:
    try:
        print(next(iterator))
    except StopIteration:
        break


class Point:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __repr__(self):
        return f'{self.__class__.__name__}{self.x, self.y, self.z}'

    def __iter__(self):
        return iter((self.x, self.y, self.z))


class DevelopmentTeam:
    def __init__(self):
        self._juniors, self._seniors = [], []

    def add_junior(self, *args):
        self._juniors.extend(args)

    def add_senior(self, *args):
        self._seniors.extend(args)

    def __iter__(self):
        yield from ((item, 'junior') for item in self._juniors)
        yield from ((item, 'senior') for item in self._seniors)


class AttrsIterator:
    def __init__(self, obj):
        self.values = list(obj.__dict__.items())

    def __iter__(self):
        return self
    
    def __next__(self):
        try:
            return self.values.pop(0)
        except:
            raise StopIteration
    

from itertools import islice

class SkipIterator:
    def __init__(self, data, n):
        self.data = iter(islice(data, 0, None, n + 1))

    def __iter__(self):
        return self
    
    def __next__(self):
        return next(self.data)


from itertools import chain

RandomLooper = chain


from itertools import tee

class Peekable:
    def __init__(self, iterable):
        self.iterable = iter(iterable)

    def __iter__(self):
        return self
    
    def peek(self, default='Default'):
        copy = tee(self.iterable)
        self.iterable = copy[1]
        if default == 'Default':
            return next(copy[0])
        return next(copy[0], default)

    def __next__(self):
        return next(self.iterable) 
    


class LoopTracker:
    def __init__(self, obj):
        self._o = tuple(obj)
        self._accesses = 0
        self._empty_accesses = 0
        self._first = None
        self._last = None

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.is_empty():
            self._empty_accesses += 1
            raise StopIteration
        self._accesses += 1
        return self._o[self._accesses - 1]
    
    def is_empty(self):
        return self._accesses >= len(self._o)
    
    @property
    def accesses(self):
        return self._accesses
    
    @property
    def empty_accesses(self):
        return self._empty_accesses
    
    @property
    def first(self):
        try:
            return self._o[0]
        except IndexError:
            raise AttributeError('Исходный итерируемый объект пуст')
    
    @property
    def last(self):
        if self._accesses == 0: 
            raise AttributeError('Последнего элемента нет')
        return self._o[self.accesses - 1]


class ReversedSequence:
    def __init__(self, seq):
        self.sequence = seq

    def __len__(self):
        return len(self.sequence)
    
    def __getitem__(self, key):
        return self.sequence[~key]

    def __iter__(self):
        yield from self.sequence[::-1]


class SparseArray:
    def __init__(self, default):
        self._array = {}
        self.default = default

    def __getitem__(self, key):
        return self._array.get(key, self.default)
    
    def __setitem__(self, key, value):
        self._array[key] = value


from itertools import cycle

class CyclicList:
    def __init__(self, obj=()):
        self.obj = list(obj) or []
    
    def __len__(self):
        return len(self.obj)
    
    def __iter__(self):
        return cycle(self.obj)
    
    def __getitem__(self, key):
        return self.obj[key % len(self)]
    
    def append(self, obj):
        self.obj.append(obj)

    def pop(self, key=-1):
        return self.obj.pop(key)
    

from copy import deepcopy

class SequenceZip:
    def __init__(self, *args):
        self.items = deepcopy(args)

    def __len__(self):
        return len(min(self.items, key=len, default=''))
    
    def __iter__(self):
        return zip(*self.items)

    def __getitem__(self, key):
        return tuple(item[key] for item in self.items)
    

class OrderedSet:
    def __init__(self, obj=()):
        self.items = dict.fromkeys(obj, None) or {}

    def __len__(self):
        return len(self.items)
    
    def __iter__(self):
        yield from self.items.keys()
    
    def __contains__(self, item):
        return item in self.items
    
    def __eq__(self, other):
        if isinstance(other, OrderedSet):
            return tuple(self.items.keys()) == tuple(other.items.keys())
        if isinstance(other, set):
            return set(self.items.keys()) == other
        return NotImplemented
    
    def add(self, obj):
        self.items[obj] = None

    def discard(self, obj):
        if self.__contains__(obj):
            del self.items[obj]


class AttrDict:
    def __init__(self, data={}):
        self.__dict__ |= data
        self.keys = list(data.keys())

    def __len__(self):
        return len(self.keys)
    
    def __iter__(self):
        yield from self.keys
    
    def __getitem__(self, key):
        if key in self.keys:
            return self.__dict__[key]
        raise KeyError
    
    def __setitem__(self, key, value):
        self.__dict__[key] = value
        if not key in self.keys:
            self.keys.append(key)


class PermaDict(dict):
    def __setitem__(self, key, value):
        if key in self:
            raise KeyError('Изменение значения по ключу невозможно')
        super().__setitem__(key, value)


from collections import defaultdict

class HistoryDict(dict):
    def __init__(self, data={}):
        self._history = defaultdict(list, {k: [v] for k, v in data.items()})
        super().__init__(data)

    def __setitem__(self, key, val):
        self._history[key].append(val)
        super().__setitem__(key, val) 

    def __delitem__(self, key):
        self._history.pop(key)
        super().__delitem__(key)

    def all_history(self):
        return dict(self._history)
    
    def history(self, key):
        if key in self._history:
            return self._history[key]
        return []
    

class MutableString:
    def __init__(self, string=''):
        self.string = list(string)

    def lower(self):
        self.string = list(map(str.lower, self.string))

    def upper(self):
        self.string = list(map(str.upper, self.string))

    def __str__(self):
        return ''.join(self.string)
    
    def __repr__(self):
        return f'MutableString({str(self)!r})'
    
    def __len__(self):
        return len(self.string)
    
    def __add__(self, other):
        if isinstance(other, MutableString):
            return MutableString(str(self) + str(other))
        return NotImplemented
    
    def __getitem__(self, key):
        if isinstance(key, slice):
            return MutableString(self.string[key])
        return self.string[key]
    
    def __setitem__(self, key, value):
        if len(value) != 1 and isinstance(key, int):
            self.string[key:] = value
        else:
            self.string[key] = value

    def __delitem__(self, key):
        del self.string[key]


class Grouper():
    def __init__(self, iterable, key):
        self.func = key
        self.items = {}
        for item in iterable:
            self.add(item)

    def add(self, val):
        self.items.setdefault(self.func(val), []).append(val)

    def group_for(self, val):
        return self.func(val)

    def __len__(self):
        return len(self.items)
    
    def __iter__(self):
        yield from ((k, v) for k, v in self.items.items())

    def __getitem__(self, key):
        return self.items[key]
    
    def __contains__(self, key):
        return key in self.items
    

from os.path import exists

def print_file_content(filename):
    if not exists(filename):
        print('Файл не найден')
        return
    file = open(filename, encoding='utf-8')
    print(file.read())
    file.close()


def non_closed_files(files):
    return [file for file in files if not file.closed]
    

def log_for(logfile, date_str):
    with (
        open(logfile, encoding='utf-8') as input, 
        open(f'log_for_{date_str}.txt', 'w', encoding='utf-8') as output
    ):
        for line in input:
            if date_str in line:
                output.write(line.replace(f'{date_str} ', ''))


def is_context_manager(obj):
    return '__enter__' in dir(obj) and '__exit__' in dir(obj)


class SuppressAll:
    def __enter__(self):
        pass

    def __exit__(self, *args, **kwargs):
        return True
    

class Greeter:
    def __init__(self, name):
        self.name = name

    def __enter__(self):
        print(f'Приветствую, {self.name}!')
        return self

    def __exit__(self, err_type, err_var, trace):
        print(f'До встречи, {self.name}!')


class Closer:
    def __init__(self, obj):
        self.obj = obj

    def __enter__(self):
        return self.obj
    
    def __exit__(self, err_type, err_val, trace):
        if not hasattr(self.obj, 'close'):
            print('Незакрываемый объект')
        else:
            self.obj.close()
        return True
    

class ReadableTextFile:
    def __init__(self, filename):
        self.filename = filename

    def __enter__(self):
        self.file = open(self.filename, encoding='utf-8')
        return map(str.rstrip, self.file)
    
    def __exit__(self, err_type, err_val, trace):
        self.file.close()


class Reloopable:
    def __init__(self, file):
        self.data = file
        self.file = file.readlines()

    def __enter__(self):
        return self.file
    
    def __exit__(self, *args, **kwargs):
        self.data.close()


import sys

class UpperPrint:
    def __enter__(self):
        self.default_writter = sys.stdout.write
        sys.stdout.write = lambda x: self.default_writter(x.upper())
        
    def __exit__(self, *args, **kwargs):
        sys.stdout.write = self.default_writter


class Suppress:
    def __init__(self, *args):
        self.exceptions = args
        self.exception = None

    def __enter__(self):
        return self
    
    def __exit__(self, err_type, err_val, trace):
        if err_type in self.exceptions:
            self.exception = err_val
            return True
        return False


class WriteSpy:
    def __init__(self, file1, file2, to_close=False):
        self.file1 = file1
        self.file2 = file2
        self.to_close = to_close

    def __enter__(self):
        return self
    
    def __exit__(self, err_type, err_val, trace):
        if self.to_close:
            self.close()

    def write(self, text):
        if self.file1.closed or self.file2.closed or not self.writable():
            raise ValueError('Файл закрыт или недоступен для записи')
        self.file1.write(text)
        self.file2.write(text)

    def close(self):
        self.file1.close()
        self.file2.close()

    def writable(self):
        if self.file1.closed or self.file2.closed:
            return False
        return self.file1.writable() and self.file2.writable()
    
    def closed(self):
        return self.file1.closed and self.file2.closed


import copy

class Atomic:
    def __init__(self, data, deep=False):
        self.copy_data = copy.deepcopy(data) if deep  else copy.copy(data)
        self.data = data

    def __enter__(self):
        return self.copy_data
    
    def __exit__(self, err_type, err_val, trace):
        if not err_type:
            if isinstance(self.data, list):
                self.data[:] = self.copy_data
            else:
                self.data.clear()
                self.data |= self.copy_data
        return True
    

import time

class AdvancedTimer:
    def __init__(self):
        self.last_run, self.min, self.max = [None] * 3
        self.runs = []

    def __enter__(self):
        self.start = time.perf_counter()
        return self
    
    def __exit__(self, *args, **kwargs):
        self.runs.append(time.perf_counter() - self.start)
        self.max = max(self.runs)
        self.min = min(self.runs)
        self.last_run = self.runs[-1]


class HtmlTag:
    level = 0

    def __init__(self, tag, inline=False):
        self.tag = tag
        self.end = '' if inline else '\n'

    def print(self, text):
        print(f'{HtmlTag.level * "  " if self.end else ""}{text}', end=self.end)

    def __enter__(self):
        print(f'{HtmlTag.level * "  "}<{self.tag}>', end=self.end)
        HtmlTag.level += 1
        return self
    
    def __exit__(self, *args, **kwargs):
        HtmlTag.level -= 1
        print(f'{HtmlTag.level * "  " if self.end else ""}</{self.tag}>')


class TreeBuilder:
    def __init__(self):
        self.data = []
        self.cur_data = self.data
        self.previos = []

    def add(self, obj):
        self.cur_data.append(obj)

    def structure(self):
        return self.data

    def __enter__(self):
        self.previos.append(self.cur_data)
        self.cur_data = []
        self.previos[-1].append(self.cur_data)

    def __exit__(self, *args, **kwargs):
        self.cur_data = self.previos[-1]
        if not self.cur_data[-1]:
            self.cur_data.pop()
        self.previos.pop()


tree = TreeBuilder()

tree.add('1st')

with tree:
    tree.add('2nd')
    with tree:
        tree.add('3rd')
        with tree:
            tree.add('4th')
            with tree:
                tree.add('5th')
    with tree:
        pass

tree.add('6th')
print(tree.structure())

tree = TreeBuilder()
print(tree.structure())

tree.add('1st')
print(tree.structure())

with tree:
    tree.add('2nd')
    with tree:
        tree.add('3rd')
    tree.add('4th')
    with tree:
        pass
        
print(tree.structure())


from contextlib import contextmanager

@contextmanager
def make_tag(tag):
    print(tag)
    yield
    print(tag)


import sys

@contextmanager
def reversed_print():
    default_writter = sys.stdout.write
    sys.stdout.write = lambda x: default_writter(''.join(reversed(x)))
    yield
    sys.stdout.write = default_writter


@contextmanager
def safe_write(filename):
    try:
        w = open(filename, 'a')
        r = open(filename, 'r')
        data = r.read()
        r.close()
        yield w
    except Exception as e:
        w.close()
        w = open(filename, 'w')
        w.write(f'Во время записи в файл было возбуждено исключение {e.__class__.__name__}\n')
        w.write(data)
    finally:
        w.close()


@contextmanager
def safe_open(filename, mode='r'):
    try:
        f = open(filename, mode)
        yield f, None
        f.close()
    except BaseException as e:
        yield None, e


from keyword import kwlist

class NonKeyword:
    def __init__(self, val):
        self._val = val

    def __get__(self, obj, cls):
        if obj is None:
            return self
        if self._val in obj.__dict__:
            return obj.__dict__[self._val]
        raise AttributeError('Атрибут не найден')
    
    def __set__(self, obj, val):
        if val in kwlist:
            raise ValueError('Некорректное значение')
        obj.__dict__[self._val] = val


class NonNegativeInteger:
    def __init__(self, name, default=None):
        self.name = name
        self.default = default

    def __get__(self, obj, cls):
        if obj is None:
            return self
        if self.name in obj.__dict__:
            return obj.__dict__[self.name]
        if self.default is None:
            raise AttributeError('Атрибут не найден')
        return self.default
    
    def __set__(self, obj, val):
        if isinstance(val, int) and val >= 0:
            obj.__dict__[self.name] = val
        else:
            raise ValueError('Некорректное значение')


class MaxCallsException(Exception):
    pass   


class LimitedTakes:
    def __init__(self, times):
        self.times = times
    
    def __set_name__(self, cls, val):
        self.val = val

    def __get__(self, obj, cls):
        if obj is None:
            return self
        if self.val in obj.__dict__:
            self.times -= 1
            if self.times < 0:
                raise MaxCallsException('Превышено количество доступных обращений')
            return obj.__dict__[self.val]
        raise AttributeError('Атрибут не найден')
    
    def __set__(self, obj, val):
        obj.__dict__[self.val] = val



class TypeChecked:
    def __init__(self, *args):
        self.types = tuple(args)

    def __set_name__(self, cls, attr):
        self.attr = attr

    def __get__(self, obj, cls):
        if obj is None:
            return self
        if self.attr in obj.__dict__:
            return obj.__dict__[self.attr]
        raise AttributeError('Атрибут не найден')
    
    def __set__(self, obj, val):
        if isinstance(val, self.types):
            obj.__dict__[self.attr] = val
        else:
            raise TypeError('Некорректное значение')
        

import random

class RandomNumber:
    def __init__(self, start, end, cache=False):
        if cache:
            self.value = random.randint(start, end)
        else:
            self.start = start
            self.end = end

    def __set_name__(self, cls, attr):
        self.attr = attr

    def __get__(self, obj, cls):
        if obj is None:
            return self
        
        if hasattr(self, 'value'):
            return self.value
        return random.randint(self.start, self.end)
    
    def __set__(self, obj, val):
        raise AttributeError('Изменение невозможно')


class Versioned:
    def __set_name__(self, cls, attr):
        self.attr = attr

    def __get__(self, obj, cls):
        if obj is None:
            return self
        if self.attr in obj.__dict__:
            return obj.__dict__[self.attr]
        raise AttributeError('Атрибут не найден')

    def __set__(self, obj, val):
        if not hasattr(obj, '_versions'):
            obj.__dict__['_versions'] = []
        obj.__dict__['_versions'].append(val)
        obj.__dict__[self.attr] = val

    def get_version(self, obj, n):
        return obj.__dict__['_versions'][n - 1]

    def set_version(self, obj, n):
        obj.__dict__[self.attr] = obj.__dict__['_versions'][n - 1]


class Student:
    age = Versioned()


student1 = Student()
student2 = Student()

student1.age = 18
student1.age = 19
student1.age = 20

student2.age = 30
student2.age = 31
student2.age = 32

print(student1.age)
print(student2.age)
Student.age.set_version(student1, 1)
Student.age.set_version(student2, 2)
print(student1.age)
print(student2.age)