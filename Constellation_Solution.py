from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
#x, y, z co-ordinates for Orion consellation
x = [-0.41, 0.57, 0.07, 0.00, -0.29, -0.32,-0.50,-0.23, -0.23]
y = [4.12, 7.71, 2.36, 9.10, 13.35, 8.13, 7.19, 13.25,13.43]
z = [2.06, 0.84, 1.56, 2.07, 2.36, 1.72, 0.66, 1.25,1.38]
#x, y, z co-ordinates for Libra consellaton
x1 = [137.7315,43.9380,38.6121, 39.0741, 37.6384, 17.5603, 72.4597, 52.5994, 120.9114, 37.6384, 72.4597]

y1 = [-8.6981,-4.9713,-5.0676,-5.8294,-5.2750,-6.2786,-30.4261,-17.2077,-41.4816, -5.2750, -30.4261]

z1 = [75.3425,23.2325,22.5977,22.5977,31.0349,14.5746,42.8795,22.2983,47.6619, 31.0349,42.8795]
fig = plt.figure()
ax = plt.subplot(1,2,1,projection='3d')
ax.scatter(x,y)

ax1 = plt.subplot(1,2,2,projection='3d')
ax1.scatter(x1,y1,z1)
plt.show()
