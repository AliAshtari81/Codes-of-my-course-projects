import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint
m1=5
m2=1
g=9.81
l=1
k=100
def dSdt(S, t):
    x1, x2, y1, y2=S
    return [x2, 
            ((0.75*m2*g*np.sin(y1)*np.cos(y1))+(0.5*m2*l*(y2**2)*np.sin(y1))-(k*x1))/(m1 + m2*(1-0.75*((np.cos(y1))**2))),
            y2,
            -(3/l)*((0.5*np.cos(y1)*(((0.75*m2*g*np.sin(y1)*np.cos(y1))+(0.5*m2*l*(y2**2)*np.sin(y1))-(k*x1))/(m1 + m2*(1-0.75*((np.cos(y1))**2)))))+(0.5*g*np.sin(y1)))]
S_0=(0, 0, 0.5, 0)
t=np.linspace(0, 20, 1000)
X1, X2, Y1, Y2=odeint(dSdt, S_0, t).T
plt.figure()
plt.plot(t, X1)
plt.xlabel('t (s)')
plt.ylabel('x (m)')
plt.title('Figure 2 _ x(t) for case 1')
plt.grid()
plt.show()
print('The amplitude of x is ', max(X1), 'meter')
plt.figure()
plt.plot(t, Y1, color='red')
plt.xlabel('t (s)')
plt.ylabel('$\Theta$ (radian)')
plt.title('Figure 3 _ $\Theta$ (t) for case 1')
plt.grid()
plt.show()
print('The amplitude of theta is ', max(Y1), ' radian')