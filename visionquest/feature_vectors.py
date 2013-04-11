"""
visionquest 0.2
Copyright (C) 2012-2013, James Jolly
See MIT-LICENSE.txt for legalese and README.md for usage.
"""
from collections import defaultdict
from knn import normalize
from image_ops import get_class

def load_vectors(infile):
   vectors = [ ]
   for line in infile:
      fields = line.split()
      label, features = fields[0], tuple([float(field) for field in fields[1:]])
      vectors.append((label, features))
   return vectors

def normalize_vectors(vectors, feat_mins, feat_maxes):
    # scales each vector in feature_vectors to [0, 1] based upon ranges
    # established by feat_mins, feat_maxes
    normalized_vectors = [ ]
    for label, vector in vectors:
       normalized_vectors.append((label, normalize(vector, feat_mins, feat_maxes)))
    return normalized_vectors

def get_feature_ranges(vectors):
   # needed for normalization
   feature_mins, feature_maxes = [ ], [ ]
   labels, features = zip(*vectors)
   for values in zip(*features):
       feature_mins.append(min(values))
       feature_maxes.append(max(values))
   return feature_mins, feature_maxes

def get_class_counts(labeled_vectors):
    # returns dict of class name to instance count
    class_counts = defaultdict(int)
    for label, vector in labeled_vectors:
        class_counts[get_class(label)] += 1
    return class_counts

