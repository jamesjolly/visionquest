reverse_image_search
====================

Search a collection of images for similar images given a query image.

The validation pipeline is:
input_img_dir --> process_dir.py --> feature_vector_file --> bench_knn.py

input_img_dir should contain subdirs that each represent an image class,
containing examples in .png format.  For example...

input_img_dir/class1/example1.png
input_img_dir/class1/example2.png
input_img_dir/class1/example3.png
input_img_dir/class2/example1.png
input_img_dir/class2/example2.png

... could be labels extracted from a input_img_dir. In other words, each 
label from input_img_dir contains both a class name (like 'class1') and 
an example name ('like example3.png').

Initial testing has been against a subset of the Amsterdam Library of 
Object Images.

This uses KNN under the hood (see get_nearest_k in knn.py). It doesn't
leverage an index (yet) so it will not scale to large datasets.

I'd like this to work against most image collections, so I'm using 
the most primitive scale-invariant features imaginable: the means of
the red, green, and blue components of the image pixel values as well 
as the standard deviation of the grayscale version of each pixel.

