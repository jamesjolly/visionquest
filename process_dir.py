#!/usr/bin/python
"""
visionquest 0.2
Copyright (C) 2012-2013, James Jolly
See MIT-LICENSE.txt for legalese and README.md for usage.

This script crawls a directory of image files grouped
into classes and computes features for each image. It
then writes them to outfile.
"""
import commands
import sys
from visionquest.image_ops import get_img_vect, vect_to_str

def run(cmd):
   status, output = commands.getstatusoutput(cmd)
   if status != 0:
       print "problem running: ", cmd
   return output

if __name__ == "__main__":

   if len(sys.argv) != 3:
      print "process_dir.py datadir outfile"
      sys.exit(0)

   datadirpath = sys.argv[1]
   outfile = open(sys.argv[2], "w")
   for imgdir in run("ls " + datadirpath).split():
      imgdirpath = datadirpath + "/" + imgdir
      for img in run("ls " + imgdirpath).split():
         imgpath = imgdirpath + "/" + img
         vect = get_img_vect(imgpath)
         print "processed", vect
         outfile.write(vect_to_str(vect))
   outfile.close()

