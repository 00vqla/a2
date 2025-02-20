import enum

# enumerate funciton

l1 = ["sleep", "wake up", "repeat"]
s1 = "geek"

# creating enumerate objects
obj1 = enumerate(l1)
obj2 = enumerate(s1)

print("Return type:", type(obj1))
print(list(enumerate(l1)))

# changing start index to 2 from 0
print(list(enumerate(s1, 4)))

###
x = ("cat", "dog", "monkey")
y = enumerate(x)

print(list(y))

from enum import Enum


class Direction(Enum):
    North = 1
    South = 2
    East = 3
    West = 4


print(Direction(4).name)
print(Direction["West"].value)
