#!/usr/bin/python
"""
reverse_image_search 0.2
Copyright (C) 2012, James Jolly (jamesjolly@gmail.com)
See MIT-LICENSE.txt for legalese and README.md for usage.
"""
import sys
from collections import defaultdict
import knn

c_benchmark_k_start = 3
c_benchmark_k_end = 3
c_class_size = 2

def get_class(filename):
   # ex. input: 'simpledata/421/421_c.png'
   return filename.split('_')[0]

def get_feature_ranges(labeled_vectors):
   # needed for normalization
   feature_mins, feature_maxes = [ ], [ ]
   labels, feature_vectors = zip(*labeled_vectors)
   feature_values = zip(*feature_vectors)
   for values in feature_values:
       feature_mins.append(min(values))
       feature_maxes.append(max(values))
   return feature_mins, feature_maxes

def load_labeled_vectors(infile):
   labeled_vectors = [ ]
   for line in infile:
      fields = line.split()
      label = fields[0]
      fields = tuple([float(field) for field in fields[1:]])
      labeled_vectors.append((label, fields))
   return labeled_vectors

def normalize_vectors(feature_vectors, feat_mins, feat_maxes):
   normalized_vectors = [ ]
   for label, vector in feature_vectors:
      normalized_vector = knn.normalize(vector, feat_mins, feat_maxes)
      normalized_vectors.append((label, normalized_vector))
   return normalized_vectors

if __name__ == "__main__":

   if len(sys.argv) != 2:
      print "bench_knn.py infile"
      sys.exit(0)

   infile = open(sys.argv[1], "r")
   feature_vectors = load_labeled_vectors(infile)
   feature_mins, feature_maxes = get_feature_ranges(feature_vectors)
   norm_vects = normalize_vectors(feature_vectors, feature_mins, feature_maxes)

   for k in range(c_benchmark_k_start, c_benchmark_k_end + 1):
      precision_sum = 0.0
      recall_sum = 0.0
      for query_label, query_vector in feature_vectors:
         normalized_query_vector = knn.normalize(query_vector, feature_mins, feature_maxes)
         closest = knn.get_nearest_k(normalized_query_vector, norm_vects, k)

         label_scores = defaultdict(float)
         for distance, labeled_vector in closest[1:]:
             label, vector = labeled_vector
             label_scores[get_class(label)] += 1.0/(1.0 + distance)

         guess_label, guess_vector = sorted(label_scores.items(), key=lambda item: item[1]).pop()
         precision_sum += float(guess_label == get_class(query_label))
         num_vectors = float(len(feature_vectors))

      print k, precision_sum/num_vectors

