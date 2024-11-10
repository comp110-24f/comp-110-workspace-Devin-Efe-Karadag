"""This file is for challenge question 5."""

__author__ = "730813763"

def manual_append(list: list[int], value: int) -> None:
    list[len(list):] = [value]

def double(list: list[int]) -> None:
    i: int = 0
    while i < len(list):
        list[i] *= 2

def double2(list: list[int]) -> list[int]:
    c: int = 0 
    list_2 = list
    while c < len(list_2):
        list_2[c] *= 2
    return list_2

a = [1, 2, 3, 4]
double(a)
print(a)

