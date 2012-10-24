"""
reverse_image_search 0.1
Copyright (C) 2012, James Jolly (jamesjolly@gmail.com)
See MIT-LICENSE.txt for legalese and README.md for usage.
"""
import Image
from math import sqrt

def vect_to_str(vect):
   vectstr = ""
   for field in vect:
      vectstr += (str(field) + " ")
   vectstr += "\n"
   return vectstr

def get_img_vect(imgpath):
   im = list(Image.open(imgpath).getdata())
   imlen = len(im)

   redsum, greensum, bluesum = 0.0, 0.0, 0.0
   for pixel in im:
      redsum += pixel[0]
      greensum += pixel[1]
      bluesum += pixel[2]

   redavg = redsum/imlen
   greenavg = greensum/imlen
   blueavg = bluesum/imlen
   grayavg = (redavg + greenavg + blueavg)/3.0

   graysum = 0.0
   for pixel in im:
      graysum += ((pixel[0] + pixel[1] + pixel[2])/3.0 - grayavg)**2
   stddev = sqrt(graysum/imlen)

   return (imgpath, redavg, greenavg, blueavg, stddev)

