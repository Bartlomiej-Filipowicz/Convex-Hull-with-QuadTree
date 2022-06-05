from quadtree import QuadTree

myfileName = 'convex_hull.png' # input image file

qtree = QuadTree(myfileName)

qtree.divide(qtree.nw, qtree.ne, qtree.sw, qtree.se)
