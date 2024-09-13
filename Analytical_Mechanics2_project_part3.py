import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint
m1=5
m2=1
g=9.81
l=1
k=100
b=0.8
A=1
w=2
def dS1dt(S, t):
    x1, x2, y1, y2=S
    return [x2, 
            ((0.75*m2*g*np.sin(y1)*np.cos(y1))+(0.5*m2*l*(y2**2)*np.sin(y1))-(k*x1))/(m1 + m2*(1-0.75*((np.cos(y1))**2))),
            y2,
            -(3/l)*((0.5*np.cos(y1)*(((0.75*m2*g*np.sin(y1)*np.cos(y1))+(0.5*m2*l*(y2**2)*np.sin(y1))-(k*x1))/(m1 + m2*(1-0.75*((np.cos(y1))**2)))))+(0.5*g*np.sin(y1)))]
S1_0=(0, 0, 0.5, 0)
t=np.linspace(0, 20, 1000)
def dS2dt(S, t):
    x1, x2, y1, y2=S
    return [x2, 
            ((0.75*m2*g*np.sin(y1)*np.cos(y1))+(0.5*m2*l*(y2**2)*np.sin(y1))-(k*x1)-(b*x2)+(A*np.sin(w*t)))/(m1 + m2*(1-0.75*((np.cos(y1))**2))),
            y2,
            -(3/l)*((0.5*np.cos(y1)*(((0.75*m2*g*np.sin(y1)*np.cos(y1))+(0.5*m2*l*(y2**2)*np.sin(y1))-(k*x1)-(b*x2)+(A*np.sin(w*t)))/(m1 + m2*(1-0.75*((np.cos(y1))**2)))))+(0.5*g*np.sin(y1)))]
S2_0=(0, 0, 0.5, 0)
X1_1, X2_1, Y1_1, Y2_1=odeint(dS1dt, S1_0, t).T
X1_2, X2_2, Y1_2, Y2_2=odeint(dS2dt, S2_0, t).T
plt.figure()
plt.plot(t, X1_1, label='case 1 - without damping')
plt.plot(t, X1_2, '--', label='case 2 - with damping', color='black')
plt.title('Figure 9 _ x(t) for case 1 & case 2')
plt.xlabel('t (s)')
plt.ylabel('x (m)')
plt.legend()
plt.grid()
plt.show()
#
plt.figure()
plt.plot(t, X2_1, label='case 1 - without damping', color='red')
plt.plot(t, X2_2, '--', label='case 2 - with damping', color='purple')
plt.title('Figure 10 _ $\Theta$ (t) for case 1 & case 2')
plt.xlabel('t (s)')
plt.ylabel('$\Theta$ (radian)')
plt.legend()
plt.grid()
plt.show()