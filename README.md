reverse_image_search
====================

Search a collection of images for similar images given a query image.

The validation pipeline is:
input_img_dir --> process_dir.py --> feature_vector_file --> bench_knn.py

input_img_dir should contain subdirs that each represent an image class,
containing examples in .png format.  Initial testing has been against
a subset of the Amsterdam Library of Object Images.

This uses KNN under the hood (see get_nearest_k in knn.py). It doesn't
leverage an index yet so it will not scale to large datasets.

I'd like this to work against most image collections, so I'm using 
the most primitive scale-invariant features imaginable: the means of
the red, green, and blue components of the image pixel values as well 
as the standard deviation of the grayscale version of each pixel.
