import itertools
from itertools import chain

nested_list1 = [
	['a', 'b', 'c'],
	['d', 'e', 'f', 'h', False,[7, 8, 9],4],
	[1, 2, None],
]
nested_list = [
	['a', 'b', 'c'],
	['d', 'e', 'f', 'h', False],
	[1, 2, None],
]

class FlatIterator:
    def __init__(self, nlist):
        self.nlist = nlist
        self.cursor = -1
        self.ncursor = 0
        self.nlist_len = len(self.nlist)

    def __iter__(self):
        self.cursor += 1
        self.ncursor = 0
        return self

    def __next__(self):
        # print("Iterator", self.nlist[self.cursor], self.cursor, self.ncursor, len(self.nlist[self.cursor]))
        if self.ncursor == len(self.nlist[self.cursor]):
            iter(self)
        if self.cursor == self.nlist_len:
            raise StopIteration
        self.ncursor += 1
        return self.nlist[self.cursor][self.ncursor - 1]

class Flat_iter_recurse:

    def __init__(self, nlist):
        self.cursor = -1
        self.nlist  = nlist

    def __iter__(self):
        self.cursor += 1
        self.ncursor = 0
        return self

    def __next__(self):
        if self.ncursor == len(self.nlist[self.cursor]):
            iter(self)

        if self.cursor == len(self.nlist):
            raise StopIteration
        result_nlist = self.nlist[self.cursor][self.ncursor]
        if isinstance(result_nlist, list):
            result_nlist = Flat_iter_recurse(result_nlist)
        self.ncursor += 1
        return result_nlist

def flat_generator(nlist):
    for l in nlist:
        for i in l:
            yield i

def flat_generator_recursive(nlist, tree_types=(list, tuple)):
    if isinstance(nlist, tree_types):
        for value in nlist:
            for subvalue in flat_generator_recursive(value, tree_types):
                yield subvalue
    else:
        yield nlist



for item in FlatIterator(nested_list):
    print(item)

flat_list = [item for item in FlatIterator(nested_list)]
print(flat_list)

for item in  flat_generator(nested_list):
    print(item)


for item in  flat_generator_recursive(nested_list1):
    print(item)


flat_to = [item for item in Flat_iter_recurse(nested_list1)]
print("iter_cursor")
print(flat_to)
