from typing import List, Set, Tuple


# classes


class SampleClass:
    def __init__(self, x):
        self.x = x


# vars

alpha: str = "Alpha"
beta: str = "Beta"
s1: SampleClass = SampleClass(1)
s2: SampleClass = SampleClass(2)
plist: List[int] = [0, 1, 2, 3]
aList: List[int] = [0]
pSet: Set[str] = {"apple", "banana", "cherry"}
pTuple: Tuple[int, int, int] = 1, 2, 3


# methods


def method1():
    print("A")


def method2():
    print("B")


def method3():
    pass


# ---- EXECUTION ----


print("HelloWorld")
