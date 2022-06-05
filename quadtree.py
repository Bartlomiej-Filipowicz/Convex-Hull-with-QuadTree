from PIL import Image, ImageDraw

class QuadTree:
    """A class implementing a quadtree."""

    def __init__(self, fileName):
        """Take an image file name as an argument.

        I will conduct the quadTree algorithm by operating on single pixels.
        It will work by implementing recursion on it.
        The image will be divided recursively into four smaller parts(squares) on the boundaries of the figures created 
        as a result of the convex hull program (convexHull.py).

        """

        self.im = Image.open(fileName) # Can be many different formats.
        self.pix = self.im.load() # loading pixels of an image
        print(self.im.size)  # Get the width and hight of the image for iterating over
        # set north west, north east, south west, south east for the computing area
        # I do not want to have the quadTree over the entire image, only where the figures are
        self.nw = [81,59]   # north west of an image
        self.ne = [575,59]  # north east of an image
        self.sw = [81,426]  # south west of an image
        self.se = [575,426] # south east of an image

    def __del__(self):
        print('Destructor called.')
        self.im.save('quadtree.png')  # Save the modified pixels as .png

    def divide(self, nw, ne, sw, se):
        """Divide a square by creating four subsquares."""

        # if nw[0] == ne[0] == sw[0] == se[0] or nw[1] == ne[1] == sw[1] == se[1]:
        #     return
        if nw == se:
            return

        black = 0 # number of black pixels
        white = 0 # number of white pixels
        for y in range(nw[1],sw[1] + 1):
            for x in range(nw[0],ne[0] + 1):
                if self.pix[x,y][:3] == (0,0,0): # Get the RGBA Value of the a pixel of an image
                    black += 1
                else:
                    white += 1

                # do the division only if there are black and white pixels in the current square
                # because the quadtree is conducted only for edges of figures (not for the enitire figures)
                if black >= 1 and white >= 1:
                    self.draw(nw, ne, sw, se)
                    # red lines are excluded from the computing area
                    # subtract -1 because a red line takes one pixel

                    # north west subsquare
                    self.divide(nw,[int(((ne[0] - nw[0]) / 2 ) + nw[0] ) - 1, ne[1]], [nw[0], int(((sw[1] - nw[1]) / 2 ) + nw[1] ) - 1 ], 
                    [ int(((ne[0] - nw[0]) / 2 ) + nw[0] ) - 1,  int(((sw[1] - nw[1]) / 2 ) + nw[1] ) - 1 ])
                    # north east subsquare
                    self.divide([int(((ne[0] - nw[0]) / 2 ) + nw[0] ) + 1, ne[1]], ne, [ int(((ne[0] - nw[0]) / 2 ) + nw[0] ) + 1,  int(((sw[1] - nw[1]) / 2 ) + nw[1] ) - 1 ],
                    [ne[0], int(((sw[1] - nw[1]) / 2 ) + nw[1] ) - 1 ] )
                    # south west subsquare
                    self.divide([nw[0], int(((sw[1] - nw[1]) / 2 ) + nw[1] ) + 1 ], [ int(((ne[0] - nw[0]) / 2 ) + nw[0] ) - 1,  int(((sw[1] - nw[1]) / 2 ) + nw[1] ) + 1 ],
                    sw, [ int(((ne[0] - nw[0]) / 2 ) + nw[0] ) - 1, sw[1]])
                    # south east subsquare
                    self.divide([ int(((ne[0] - nw[0]) / 2 ) + nw[0] ) + 1,  int(((sw[1] - nw[1]) / 2 ) + nw[1] ) + 1 ], [ne[0], int(((sw[1] - nw[1]) / 2 ) + nw[1] ) + 1 ],
                    [ int(((ne[0] - nw[0]) / 2 ) + nw[0] ) + 1, sw[1]], se)

                    return




    def draw(self, nw, ne, sw, se):
        """Draw a representation of the quadtree on the image."""

        imgLine = ImageDraw.Draw(self.im)
        imgLine.line([ (int(((ne[0] - nw[0]) / 2 ) + nw[0] ), ne[1]) , (int(((ne[0] - nw[0]) / 2 ) + nw[0] ), se[1]) ], fill='red', width=0 )
        imgLine.line([ (nw[0], int(((sw[1] - nw[1]) / 2 ) + nw[1] )) , (ne[0], int(((sw[1] - nw[1]) / 2 ) + nw[1] )) ], fill='red', width=0 )