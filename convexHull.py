import numpy
from scipy.spatial import ConvexHull, convex_hull_plot_2d
import matplotlib.pyplot as plt
rng = numpy.random.default_rng()
points = 3.33 * rng.random((10, 2))   # 10 random points in 2-D
hull = ConvexHull(points)

points2 = 3.33 * rng.random((10, 2)) + 3.33  # 10 random points in 2-D
hull2 = ConvexHull(points2)

points3 = 3.33 * rng.random((10, 2)) + 6.66  # 10 random points in 2-D
hull3 = ConvexHull(points3)


# plot
plt.plot(points[:,0], points[:,1], '#000000') # insert '#000000' if you want to get rid of colorful dots
# ^^^ insert 'o' if you want to have colorful dots
for simplex in hull.simplices:
    plt.plot(points[simplex, 0], points[simplex, 1], 'k-')



plt.plot(points2[:,0], points2[:,1], '#000000') # insert '#000000' if you want to get rid of colorful dots
# ^^^ insert 'o' if you want to have colorful dots
for simplex in hull2.simplices:
    plt.plot(points2[simplex, 0], points2[simplex, 1], 'k-')


plt.plot(points3[:,0], points3[:,1], '#000000') # insert '#000000' if you want to get rid of colorful dots
# ^^^ insert 'o' if you want to have colorful dots
for simplex in hull3.simplices:
    plt.plot(points3[simplex, 0], points3[simplex, 1], 'k-')

x=[1,2,3,4,5,6,7,8,9,10]
y=[1,2,3,4,5,6,7,8,9,10]
values = range(len(x))

plt.yticks(values,y)
plt.xlabel("axis X")
plt.ylabel("axis Y")
plt.title("Convex hull + quadTree")
plt.xticks(values,x)

#filling
plt.fill(points[hull.vertices,0], points[hull.vertices,1], '#000000')
plt.fill(points2[hull2.vertices,0], points2[hull2.vertices,1], '#000000')
plt.fill(points3[hull3.vertices,0], points3[hull3.vertices,1], '#000000')

plt.savefig('convex_hull.png')
