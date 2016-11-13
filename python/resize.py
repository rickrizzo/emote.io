import os, sys
import Image

size = 48, 48
jpgfile = Image.open("test.png")
images = ["test.png"]

for infile in images:
    outfile = "test2.png"
    if infile != outfile:
        try:
            im = Image.open(infile)
            im.thumbnail(size, Image.ANTIALIAS)
            im.save(outfile, "PNG")
        except IOError:
            print "cannot create thumbnail for '%s'" % infile