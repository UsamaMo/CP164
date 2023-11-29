"""
-------------------------------------------------------
[Assignment 1 Task 3]
-------------------------------------------------------
Author:  Usama Mohiuddin
ID:            212090340
Email:    mohi0340@mylaurier.ca
__updated__ = "2022-02-11"
-------------------------------------------------------
"""

from functions import file_analyze

filename = "hello"
fv = open(filename, 'r', encoding='utf-8')

u, l, d, w, r = file_analyze(fv)
print(f"""u: {u}
l: {l}
d: {d}
w: {w}
r: {r}""")


fv.close()
