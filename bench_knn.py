#!/usr/bin/python
"""
reverse_image_search 0.1
Copyright (C) 2012, James Jolly (jamesjolly@gmail.com)
See MIT-LICENSE.txt for legalese and README.md for usage.
"""
import sys
from heapq import heappush, heappop
from collections import defaultdict
import knn

c_benchmark_k_start = 1
c_benchmark_k_end = 8

def get_lbl(filename):
    return filename.split('_')[0]

if __name__ == "__main__":

   if len(sys.argv) != 2:
      print "processdir.py infile"
      sys.exit(0)

   vects = [ ]
   infile = open(sys.argv[1], "r")
   for line in infile:
      fields = line.split()
      vects.append((fields[0], float(fields[1]), float(fields[2]), float(fields[3]), float(fields[4])))
   
   for k in range(c_benchmark_k_start, c_benchmark_k_end + 1):
      precision_sum = 0.0
      recall_sum = 0.0
      for qvect in vects:
         closest = knn.get_nearest_k(qvect, vects, k)
         vect_lbls = defaultdict(int)
         for vect in closest:
            vect_lbls[get_lbl(vect[1][0])] += 1
         class_guess = sorted(vect_lbls.items(), key=lambda item: item[1]).pop()[0]
         precision_sum += float(class_guess == get_lbl(qvect[0]))
         recall_sum += vect_lbls[get_lbl(qvect[0])]/2.0
      print k, precision_sum/float(len(vects)), recall_sum/float(len(vects))

