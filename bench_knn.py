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
c_benchmark_k_end = 6

def get_class(filename):
   # ex. input: 'simpledata/421/421_c.png'
   # (class is '421')
   return filename.split('/')[-2:][0]

def get_feature_ranges(labeled_vectors):
   # needed for normalization
   feature_mins, feature_maxes = [ ], [ ]
   labels, feature_vectors = zip(*labeled_vectors)
   feature_values = zip(*feature_vectors)
   for values in feature_values:
       feature_mins.append(min(values))
       feature_maxes.append(max(values))
   return feature_mins, feature_maxes

def get_class_counts(labeled_vectors):
    # returns dict of class name to instance count
    class_counts = defaultdict(int)
    for label, vector in labeled_vectors:
        class_counts[get_class(label)] += 1
    return class_counts

def load_labeled_vectors(infile):
   labeled_vectors = [ ]
   for line in infile:
      fields = line.split()
      label = fields[0]
      fields = tuple([float(field) for field in fields[1:]])
      labeled_vectors.append((label, fields))
   return labeled_vectors

def normalize_vectors(feature_vectors, feat_mins, feat_maxes):
    # scales each vector in feature_vectors to [0, 1] based upon ranges
    # established by feat_mins, feat_maxes
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
   class_counts = get_class_counts(feature_vectors)
   num_vectors = float(len(feature_vectors))

   print "K\tPRECISION\tRECALL\n- - - - - - - - - - - - - - - -"

   # issue search for each vector (see get_nearest_k)
   # compute average precision and recall over all vectors for each k
   for k in range(c_benchmark_k_start, c_benchmark_k_end + 1):
      precision_sum, recall_sum = 0.0, 0.0
      for query_label, query_vector in feature_vectors:
         normalized_query_vector = knn.normalize(query_vector, feature_mins, feature_maxes)
         closest = knn.get_nearest_k(normalized_query_vector, norm_vects, k)

         correct = 1.0
         class_scores = defaultdict(float)
         for distance, labeled_vector in closest[1:]: # don't consider closest vector, itself
             label, vector = labeled_vector
             if get_class(label) == get_class(query_label):
                 correct += 1.0
         precision_sum += correct/float(k)
         recall_sum += correct/class_counts[get_class(query_label)]

      print "%d\t%f\t%f" % (k, precision_sum/num_vectors, recall_sum/num_vectors)

