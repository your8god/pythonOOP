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


