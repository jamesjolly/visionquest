"""
reverse_image_search 0.2
Copyright (C) 2012, James Jolly (jamesjolly@gmail.com)
See MIT-LICENSE.txt for legalese and README.md for usage.
"""
import Image
from math import sqrt
import pylab as py

c_R, c_G, c_B = 0, 1, 2

def vect_to_str(vect):
   vectstr = ""
   for field in vect:
      vectstr += (str(field) + " ")
   vectstr += "\n"
   return vectstr

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

