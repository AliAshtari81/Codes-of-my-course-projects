import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint
from scipy.interpolate import interp1d
from scipy.misc import derivative
def dxdt(x, t):
    x1, x2= x
    return [x2, 0]
t=np.linspace(0, 100, 10000)
x0=(0,400)
x1, x2=odeint(dxdt, x0, t).T
def dydt(y, t):
    y1, y2=y
    return [y2, -9.8]
y0=(0, 300)
y1, y2=odeint(dydt, y0, t).T
plt.plot(x1, y1)
plt.xlabel('x (m)')
plt.ylabel('y (m)')
plt.grid()
plt.title('Figure 1 - trajectory of the projectile in case 1')
plt.show()
F=interp1d(x1, y1, kind='cubic')
x=20000
delta=F(x)
while abs(delta)>0.01:
    x=x-(F(x)/derivative(F, x, dx=0.1))
    delta=F(x)
X=interp1d(t, y1, kind='cubic')
T=60
delta_t=X(T)
while abs(delta_t)>0.01:
    T=T-(X(T)/derivative(X, T, dx=0.1))
    delta_t=X(T)
print("R=", x, "T=", T)