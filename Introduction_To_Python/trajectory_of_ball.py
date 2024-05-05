import math
import matplotlib.pyplot as plt
 
teta = math.radians(60)
g = 9.81
v0 = 45
y0 = 0
y_list = []
x_list = list(range(0, 150))
 
for x in x_list:
    y = x*math.tan(teta) - (g*x**2) / (2 * v0**2 * (math.cos(teta))**2) + y0
    y_list.append(y)


plt.plot(x_list, y_list)
plt.show()