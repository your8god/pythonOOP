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