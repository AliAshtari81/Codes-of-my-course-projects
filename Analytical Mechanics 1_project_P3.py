import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint
from scipy.interpolate import interp1d
from scipy.misc import derivative
m=43
R=0.0775
P0=101325
T0=288.15
g=9.81
Rg=8.314
M=0.0289652
L=0.0065
def drdt(r, t):
    x, vx, y, vy=r
    return [vx,
            -((np.pi * R**2 * P0*M)/(4*Rg*T0*m))*pow((1-(L*y/T0)),(g*M/Rg*L)-1)*np.sqrt(vx**2 + vy**2)*vx,
            vy,
            -g-((np.pi * R**2 * P0*M)/(4*Rg*T0*m))*pow((1-(L*y/T0)),(g*M/Rg*L)-1)*np.sqrt(vx**2 + vy**2)*vy]
r0=(0, 400, 0, 300)
t=np.linspace(0, 100, 10000)
x, vx, y, vy= odeint(drdt, r0, t).T
plt.plot(x, y)
plt.grid()
plt.xlabel('x (m)')
plt.ylabel('y (m)')
plt.title('Figure 3 - trajectory of the projectile in case 3')
plt.show()
F=interp1d(x, y, kind='cubic')
x=8000
delta=F(x)
while abs(delta)>0.01:
    x=x-(F(x)/derivative(F, x, dx=0.1))
    delta=F(x)
Y=interp1d(t, y, kind='cubic')
T=40
delta_t=Y(T)
while abs(delta_t)>0.01:
    T=T-(Y(T)/derivative(Y, T, dx=0.1))
    delta_t=Y(T)
print("R=", x, "T=", T)