v0 = 5
g = 9.81
t = 0.6

y = v0 * t - 0.5 * g * t ** 2

print("At t={}s, the height of the ball is {}m".format(t,y))

# Formatting height to 2 decimal places

print("At t={0}s, the height of the ball is {1:.2f}m".format(t,y))


