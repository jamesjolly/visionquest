#!/usr/bin/python
"""
visionquest 0.2
Copyright (C) 2012-2013, James Jolly
See MIT-LICENSE.txt for legalese and README.md for usage.
"""
import commands
import sys
import process_img

def run(cmd):
   status, output = commands.getstatusoutput(cmd)
   if status != 0:
       print "problem running: ", cmd
   return output

if len(sys.argv) != 3:
   print "process_dir.py datadir outfile"
   sys.exit(0)

if __name__ == "__main__":

   datadirpath = sys.argv[1]
   outfile = open(sys.argv[2], "w")
   for imgdir in run("ls " + datadirpath).split():
      imgdirpath = datadirpath + "/" + imgdir
      for img in run("ls " + imgdirpath).split():
         imgpath = imgdirpath + "/" + img
         vect = process_img.get_img_vect(imgpath)
         print vect
         outfile.write(process_img.vect_to_str(vect))
   outfile.close()

