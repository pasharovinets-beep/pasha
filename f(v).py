from math import *
import matplotlib.pyplot as plt
y0=200
v0=0.0
m=1.0
k=0.5
g=9.81
dt=0.01
t=[0]
v=[v0]
y=[y0]
a=[g]
while y[-1]>0:
    a.append(-k/m*v[-1]+g)
    v.append(v[-1]+a[-1]*dt)
    y.append(y[-1]-v[-1]*dt)
    t.append(t[-1]+dt)
print(y, v, t, sep='\n')
plt.figure(figsize=(16,8))
plt.subplot(1,3,1)
plt.plot(t,v, 'b-')
plt.xlabel('Время, с')
plt.ylabel('Скорость, м/с')
plt.title('v(t)')
plt.grid(True)

plt.subplot(1,3,2)
plt.plot(t,y,'r-')
plt.xlabel('Время, с')
plt.ylabel('Высота, м')
plt.title('y(t)')
plt.grid(True)

plt.subplot(1,3,3)
plt.plot(t,a,'h-')
plt.xlabel('Время, с')
plt.ylabel('Ускорение, м*с^-2')
plt.title('a(t)')
plt.grid(True)

plt.tight_layout()
plt.show()
