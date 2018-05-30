import os
import pathlib
galary = 'images/galary/'

g = os.listdir(galary)
e = os.path.dirname(galary)
f = next(os.walk(galary))[1]
print(f)