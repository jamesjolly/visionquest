#!/usr/bin/python
"""
visionquest 0.2
Copyright (C) 2012-2013, James Jolly
See MIT-LICENSE.txt for legalese and README.md for usage.

This script finds the top K most similar images in dataset_vectors for
each vector in query vectors. The output will be like...

dat/class1/4.jpg found dat/class1/3.jpg dat/class1/2.jpg   
dat/class2/4.jpg found dat/class2/5.jpg dat/class2/3.jpg 

Here K=2, with the first image on each line being a search vector
(dat/class1/4.jpg and dat/class2/4.jpg), and the remaining images on 
the line after 'found' the top K most similar vectors in the dataset 
queried (ordered from most to least similar).
"""
import sys
from visionquest.knn import normalize, get_nearest_k
from visionquest.feature_vectors import load_vectors, \
                                        normalize_vectors, \
                                        get_feature_ranges

c_K = 3 # K, number of results to be returned

if __name__ == "__main__":

   if len(sys.argv) != 3:
      print "batch_search.py query_vectors dataset_vectors"
      sys.exit(0)

   try:
       query_infile = open(sys.argv[1], "r")
   except IOError:
       print "problem opening query vectors file:", sys.argv[1]
       sys.exit(0)

   try:
       dataset_infile = open(sys.argv[2], "r")
   except IOError:
       print "problem opening dataset vectors file:", sys.argv[2]
       sys.exit(0)

   query_vectors, dataset_vectors = load_vectors(query_infile), load_vectors(dataset_infile)
   feature_mins, feature_maxes = get_feature_ranges(dataset_vectors)
   norm_vects = normalize_vectors(dataset_vectors, feature_mins, feature_maxes)
   num_vectors = float(len(dataset_vectors))

   for query_label, query_vector in query_vectors:
      normalized_query_vector = normalize(query_vector, feature_mins, feature_maxes)
      nearest_k = get_nearest_k(normalized_query_vector, norm_vects, c_K)
      print query_label, "found",
      for distance, labeled_vector in nearest_k:
         label, vector = labeled_vector
         print label,
      print ""

