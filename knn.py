"""
reverse_image_search 0.2
Copyright (C) 2012, James Jolly (jamesjolly@gmail.com)
See MIT-LICENSE.txt for legalese and README.md for usage.
"""
from math import sqrt
from heapq import heappush, heappop

def dist(vect_A, vect_B):
   d = 0.0
   for val_A, val_B in zip(vect_A, vect_B):
      d += (val_A - val_B)**2
   return sqrt(d)

def get_nearest_k(query_vector, dataset, k):
   pq = [ ]
   for label, vector in dataset:
       heappush(pq, (dist(query_vector, vector), (label, vector)))
   closest = [ ]
   for kcount in range(0, k):
      closest.append(heappop(pq))
   return closest

def normalize(vector, mins, maxes):
    v_out = [ ]
    for feat, fmin, fmax in zip(vector, mins, maxes):
        v_out.append((feat - fmin)/(fmax - fmin))
    return tuple(v_out)

