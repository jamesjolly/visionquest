"""
visionquest 0.2
Copyright (C) 2012-2013, James Jolly
See MIT-LICENSE.txt for legalese and README.md for usage.
"""
from collections import defaultdict
from knn import normalize
from image_ops import get_class

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
       normalized_vector = normalize(vector, feat_mins, feat_maxes)
       normalized_vectors.append((label, normalized_vector))
    return normalized_vectors

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

