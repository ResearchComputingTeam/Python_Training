import math

x = 2

sinh = math.sinh(x)

sinh1 = 0.5 * (math.exp(x) - math.exp(-x))

sinh2 = 0.5 * (math.e**x - math.e**(-x))

print(sinh)
print(sinh1)
print(sinh2)


