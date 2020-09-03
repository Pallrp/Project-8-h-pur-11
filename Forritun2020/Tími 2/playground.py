import math 
pi = math.pi
#math.pow (x, í veldinu y)
print(pi)

n_str = int(input('Input n: '))
n_dub = n_str * 2
n_trip = n_str * 3
print(n_dub + n_trip)

import math

x1_str = input("Input x1: ")  # do not change this line
y1_str = input("Input y1: ")  # do not change this line
x2_str = input("Input x2: ")  # do not change this line
y2_str = input("Input y2: ")  # do not change this line

x1 = int(x1_str)
y1 = int(y1_str)
x2 = int(x2_str)
y2 = int(y2_str)
d = math.sqrt((x1 - y1 )**2 + (x2 - y2)**2)
print(d)
