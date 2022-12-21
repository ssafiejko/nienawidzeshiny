import math
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
fig = plt.figure()
ax = fig.add_subplot(111, projection="3d")

k=250

#zielona choinka
Z = [i for i in range(k)]
X = [math.sin(i/5)*(k-i) for i in range(k)]
Y = [math.cos(i/5)*(k-i) for i in range(k)]
ax.scatter(X,Y,Z, c="green", marker="d")

#zloty lancuch
Z1 = [x+10 for x in Z]
X = [math.sin(i/6)*(k-i) for i in range(k)]
Y = [math.cos(i/6)*(k-i) for i in range(k)]
ax.scatter(X,Y,Z1, c="gold", marker="*")
plt.xlim(-400,400)
plt.ylim(-400,400)

#bombki
max = 5
Z = [i for i in range(1,k-10,max)]
X = [math.cos(i/5+2)*(k-i+10) for i in range(1,k-10,max)]
Y = [math.sin(i/5+2)*(k-i+10) for i in range(1,k-10,max)]
ax.scatter(X,Y,Z, c="red", marker="o")

#gwiazda
plt.xlim(-400,400)
plt.ylim(-400,400)
ax.scatter(0,0,k+10, c="gold", marker="*", s=500)





plt.show()