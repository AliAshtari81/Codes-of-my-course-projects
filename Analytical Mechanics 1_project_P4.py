import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint
from scipy.interpolate import interp1d
from scipy.misc import derivative
p=1.225
m=43
R=0.0775
P0=101325
T0=288.15
g=9.81
Rg=8.314
M=0.0289652
L=0.0065
def dr3dt(r, t):
    x, vx, y, vy=r
    return [vx,
            -((np.pi * R**2 * P0*M)/(4*Rg*T0*m))*pow((1-(L*y/T0)),(g*M/Rg*L)-1)*np.sqrt(vx**2 + vy**2)*vx,
            vy,
            -g-((np.pi * R**2 * P0*M)/(4*Rg*T0*m))*pow((1-(L*y/T0)),(g*M/Rg*L)-1)*np.sqrt(vx**2 + vy**2)*vy]
r0=(0, 400, 0, 300)
t=np.linspace(0, 100, 10000)
x3, vx3, y3, vy3= odeint(dr3dt, r0, t).T
def dr2dt(r, t):
    x, vx, y, vy=r
    return [vx,
            -((p*np.pi*R**2)/(4*m))*np.sqrt(vx**2 + vy**2)*vx,
            vy,
            -g - ((p*np.pi*R**2)/(4*m))*np.sqrt(vx**2 + vy**2)*vy]
x2, vx2, y2, vy2=odeint(dr2dt, r0, t).T
def dr1dt(r, t):
    x1, vx1, y1, vy1=r
    return [vx1, 0, vy1, -g]
x1, vx1, y1, vy1=odeint(dr1dt, r0, t).T
# y(x)
#plt.plot(x1, y1, label='case 1')
#plt.plot(x2, y2, label='case 2')
#plt.plot(x3, y3, '--', label='case 3')
#plt.grid()
#plt.title('Figure 4 - comparying trajectories of three cases')
#plt.xlabel('x (m)')
#plt.ylabel('y (m)')
#plt.legend()
# vx(t)
#plt.plot(t, vx1, label='case 1')
#plt.plot(t, vx2, label='case 2')
#plt.plot(t, vx3, '--', label='case 3')
#plt.grid()
#plt.legend()
#plt.title('Figure 5 - comparying x-component of velocities of three cases')
#plt.xlabel('t (s)')
#plt.ylabel('v_x (m/s)')
# vy(t)
plt.plot(t, vy1, label='case 1')
plt.plot(t, vy2, label='case 2')
plt.plot(t, vy3, '--', label='case 3')
plt.grid()
plt.legend()
plt.title('Figure 6 - comparying y-component of velocoties of three cases')
plt.xlabel('t (s)')
plt.ylabel('v_y (m/s)')
plt.show()