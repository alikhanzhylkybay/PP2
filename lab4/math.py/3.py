import math
ns = int(input())
lofs = float(input())
area = (ns * lofs**2)/(4*math.tan(math.pi/ns))
print(round(area))
