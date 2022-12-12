import matplotlib.pyplot as plt
from sympy import true
import math

f = open('DS1.txt', 'r')
x_list =[]
y_list = []
while true:
    x = f.read(3)
    if x!='':
        f.read(1)
        y = f.read(3)
        f.read(1)
        x_rotated = 480 + (int(x)-480)*math.cos(math.pi / 9)-(int(y)-480)*math.sin(math.pi / 9)
        y_rotated = 480 + (int(x)-480)*math.sin(math.pi / 9)+(int(y)-480)*math.cos(math.pi / 9)
        x_list.append(x_rotated)
        y_list.append(y_rotated)
    else:
        break
plt.figure(figsize=(10,10))
plt.scatter(x_list, y_list, c ="blue", s = 1)
plt.show()
f.close


