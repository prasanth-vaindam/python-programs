class Toy:

    someVariable = "This is a class variable"

    def __init__(self, name, price):
        self.name = name
        self.price = price
        self.someVariable = "This is a variable"

    def __str__(self):
        return f"{self.name} costs {self.price}"

    def __repr__(self):
        return f"Toy(name={self.name}, price={self.price})"
    def get_variable(self):
        return self.someVariable
    def set_variable(self, value):
        self.someVariable = value
    def del_variable(self):
        del self.someVariable
    variable = property(get_variable, set_variable, del_variable, "This is a property for someVariable")
    def __del__(self):
        print(f"{self.name} is being deleted")
    def __eq__(self, other):
        if isinstance(other, Toy):
            return self.name == other.name and self.price == other.price
        return False
    def __ne__(self, other):
        return not self.__eq__(other)
    def __lt__(self, other):
        if isinstance(other, Toy):
            return self.price < other.price
        return NotImplemented
    def __le__(self, other):
        if isinstance(other, Toy):
            return self.price <= other.price
        return NotImplemented
    def __gt__(self, other):
        if isinstance(other, Toy):
            return self.price > other.price
        return NotImplemented
    def __ge__(self, other):
        if isinstance(other, Toy):
            return self.price >= other.price
        return NotImplemented
    def __hash__(self):
        return hash((self.name, self.price))
    def __bool__(self):
        return bool(self.name) and self.price > 0
    def __len__(self):
        return len(self.name)
    def __contains__(self, item):
        if isinstance(item, str):
            return item in self.name
        return False
    def __call__(self, *args, **kwargs):
        return f"{self.name} is called with args: {args} and kwargs: {kwargs}"
    def __getitem__(self, key):
        if key == 'name':
            return self.name
        elif key == 'price':
            return self.price
        else:
            raise KeyError(f"Key '{key}' not found in Toy attributes")
    def __setitem__(self, key, value):
        if key == 'name':
            self.name = value
        elif key == 'price':
            self.price = value
        else:
            raise KeyError(f"Key '{key}' not found in Toy attributes")
    def __delitem__(self, key):
        if key == 'name':
            del self.name
        elif key == 'price':
            del self.price
        else:
            raise KeyError(f"Key '{key}' not found in Toy attributes")
    def __dir__(self):
        return super().__dir__() + ['variable']
    def __getattr__(self, name):
        if name == 'variable':
            return self.get_variable()
        raise AttributeError(f"{self.__class__.__name__} has no attribute '{name}'")
    def __setattr__(self, name, value):
        if name == 'variable':
            self.set_variable(value)
        else:
            super().__setattr__(name, value)
    def __delattr__(self, name):
        if name == 'variable':
            self.del_variable()
        else:
            super().__delattr__(name)
    def __format__(self, format_spec):
        if format_spec == 'name':
            return self.name
        elif format_spec == 'price':
            return f"${self.price:.2f}"
        return super().__format__(format_spec)
    def __sizeof__(self):
        import sys
        return sys.getsizeof(self.name) + sys.getsizeof(self.price) + sys.getsizeof(self.someVariable)
    def __getstate__(self):
        return {'name': self.name, 'price': self.price, 'someVariable': self.someVariable}
    def __setstate__(self, state):
        self.name = state['name']
        self.price = state['price']
        self.someVariable = state['someVariable']
    def __reduce__(self):
        return (self.__class__, (self.name, self.price), self.__getstate__())
    def __reduce_ex__(self, protocol):
        return self.__reduce__()
    def __copy__(self):
        return Toy(self.name, self.price)
    def __deepcopy__(self, memo):
        from copy import deepcopy
        new_toy = Toy(deepcopy(self.name, memo), deepcopy(self.price, memo))
        new_toy.someVariable = deepcopy(self.someVariable, memo)
        return new_toy
    def __enter__(self):
        print(f"Entering context with {self.name}")
        return self
    def __exit__(self, exc_type, exc_value, traceback):
        print(f"Exiting context with {self.name}")
        if exc_type is not None:
            print(f"An exception occurred: {exc_value}")
        return False
    def __reversed__(self):
        return reversed(self.name)
    def __next__(self):
        if not hasattr(self, '_iter_index'):
            self._iter_index = 0
        if self._iter_index < len(self.name):
            result = self.name[self._iter_index]
            self._iter_index += 1
            return result
        else:
            raise StopIteration
    def __iter__(self):
        self._iter_index = 0
        return self
    def __copy__(self):
        from copy import copy
        new_toy = Toy(copy(self.name), copy(self.price))
        new_toy.someVariable = copy(self.someVariable)
        return new_toy

