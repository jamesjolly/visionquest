"""
reverse_image_search 0.1
Copyright (C) 2012, James Jolly (jamesjolly@gmail.com)
See MIT-LICENSE.txt for legalese and README.md for usage.
"""
from math import sqrt

def dist(vectA, vectB):
   d = 0.0
   for fid in range(1, 5):
      d += (vectA[fid] - vectB[fid])**2
   return sqrt(d)

def get_nearest_k(qvect, vects, k):
   pq = [ ]
   for vect in vects:
      if qvect[0] != vect[0]:
         heappush(pq, (dist(qvect, vect), vect))
   closest = [ ]
   for kcount in range(0, k):
      closest.append(heappop(pq))
   return closest

