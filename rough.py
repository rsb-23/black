# import timeit
from sys import getsizeof

from blib2to3.pytree import Leaf, LeafPattern, Node

insts = LeafPattern(120), Node(332, []), Leaf(21, "sjdhc")

for inst in insts:
    print(repr(inst), getsizeof(inst))

y = insts[-1]
print(hasattr(y, "__dict__"))
for x in y.__dir__():
    print(x, getsizeof(x))
