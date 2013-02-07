"""
visionquest 0.2
Copyright (C) 2012-2013, James Jolly
See MIT-LICENSE.txt for legalese and README.md for usage.
"""
import Image
from math import sqrt

c_R, c_G, c_B = 0, 1, 2

def get_class(imgpath):
   # ex. input: 'simpledata/421/421_c.png'
   # (class is '421')
   return imgpath.split('/')[-2:][0]

def vect_to_str(vect):
    return " ".join([str(feature) for feature in vect]) + "\n"

def grayscale(pixel):
    return (pixel[c_R] + pixel[c_G] + pixel[c_B])/3.0

def get_img_vect(imgpath):
   im = list(Image.open(imgpath).getdata())
   imlen = len(im)

   redsum, greensum, bluesum, graysum = 0.0, 0.0, 0.0, 0.0
   for pixel in im:
      redsum += pixel[c_R]
      greensum += pixel[c_G]
      bluesum += pixel[c_B]
      graysum += grayscale(pixel)

   redavg = redsum/imlen
   greenavg = greensum/imlen
   blueavg = bluesum/imlen
   grayavg = graysum/imlen

   graysumsqr = 0.0
   for pixel in im:
      graysumsqr += (grayscale(pixel) - grayavg)**2
   graystddev = sqrt(graysumsqr/imlen)

   return (imgpath, redavg, greenavg, blueavg, graystddev)

