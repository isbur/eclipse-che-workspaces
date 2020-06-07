from fix import prefix, infix
from galushktory import place


@prefix
def Place(x):
    return place(*x)

@infix
def to(a, b):
    return (a, b)