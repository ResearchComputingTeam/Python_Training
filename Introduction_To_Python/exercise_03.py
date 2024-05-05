import  math

v0 = 5              # Initial Velocity
g = 9.81            # g is Acceleration of gravity
yc = 0.2            # Vertical height


t1 = (v0 - math.sqrt(v0**2-2 *g*yc))/g

print('At t={0}s, the height of the ball is {1}m'.format(t1,yc))


