import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint
from scipy.interpolate import interp1d
from scipy.misc import derivative
m=43
p=1.225
R=0.0775
def drdt(r, t):
    x, vx, y, vy=r
    return [vx,
            -((p*np.pi*R**2)/(4*m))*np.sqrt(vx**2 + vy**2)*vx,
            vy,
            -9.81 - ((p*np.pi*R**2)/(4*m))*np.sqrt(vx**2 + vy**2)*vy]
r0=(0, 400, 0, 300)
t=np.linspace(0, 100, 10000)
x, vx, y, vy=odeint(drdt, r0, t).T
#plt.plot(t, vx, label='v_x')
#plt.plot(t, vy, label='v_y')
plt.plot(x, y)
plt.grid()
#plt.xlabel('t (s)')
#plt.ylabel('v (m/s)')
plt.xlabel('x (m)')
plt.ylabel('y (m)')
#plt.legend()
plt.title('Figure 2 - trajectory of the projectile in case 2')
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