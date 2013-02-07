#!/usr/bin/python
"""
visionquest 0.2
Copyright (C) 2012-2013, James Jolly
See MIT-LICENSE.txt for legalese and README.md for usage.

This script helps find the best K for your dataset.
"""
import sys
from collections import defaultdict
from process_img import get_class
from knn import normalize, get_nearest_k
from feature_vectors import load_labeled_vectors, normalize_vectors, \
                            get_feature_ranges, get_class_counts

c_benchmark_k_start = 2
c_benchmark_k_end = 6

if __name__ == "__main__":

   if len(sys.argv) != 2:
      print "bench_knn.py infile"
      sys.exit(0)

   print "\nsearching for best K between %s and %s..." % (c_benchmark_k_start, c_benchmark_k_end)

   infile = open(sys.argv[1], "r")
   feature_vectors = load_labeled_vectors(infile)
   feature_mins, feature_maxes = get_feature_ranges(feature_vectors)
   norm_vects = normalize_vectors(feature_vectors, feature_mins, feature_maxes)
   class_counts = get_class_counts(feature_vectors)
   num_vectors = float(len(feature_vectors))

   print "K\tPRECISION\tRECALL\n- - - - - - - - - - - - - - - -"

   # for a range of possible k values, issues a search for each vector 
   # (see get_nearest_k) and then compute average precision and recall
   for k in range(c_benchmark_k_start, c_benchmark_k_end + 1):
      precision_sum, recall_sum = 0.0, 0.0
      for query_label, query_vector in feature_vectors:
         normalized_query_vector = normalize(query_vector, feature_mins, feature_maxes)
         closest = get_nearest_k(normalized_query_vector, norm_vects, k)

         correct = 1.0
         class_scores = defaultdict(float)
         for distance, labeled_vector in closest[1:]: # don't consider closest vector, itself
             label, vector = labeled_vector
             if get_class(label) == get_class(query_label):
                 correct += 1.0
         precision_sum += correct/float(k)
         recall_sum += correct/class_counts[get_class(query_label)]

      print "%d\t%f\t%f" % (k, precision_sum/num_vectors, recall_sum/num_vectors)

