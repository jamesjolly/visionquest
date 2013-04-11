"""
visionquest 0.2
Copyright (C) 2012-2013, James Jolly
See MIT-LICENSE.txt for legalese and README.md for usage.
"""
from math import sqrt
from heapq import heappush, nsmallest

def dist(vect_A, vect_B):
   d = 0.0
   for val_A, val_B in zip(vect_A, vect_B):
      d += (val_A - val_B)**2
   return sqrt(d)

def get_nearest_k(query_vector, dataset, K):
   pq = [ ]
   for dataset_label, dataset_vector in dataset:
       heappush(pq, (dist(query_vector, dataset_vector), (dataset_label, dataset_vector)))
   return nsmallest(K, pq)

def normalize(vector, mins, maxes):
    v_out = [ ]
    for feat, fmin, fmax in zip(vector, mins, maxes):
        v_out.append((feat - fmin)/(fmax - fmin))
    return tuple(v_out)

