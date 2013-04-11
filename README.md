visionquest
====================

visionquest searches a collection of images for similar images given a 
query image.

To get started, you will need to make feature vectors from your image
collection. You can do this with process_dir.py, like...

./process_dir.py input_img_dir feature_vector_file

input_img_dir should contain subdirs that each represent an image class,
containing examples in .png format. For example...

input_img_dir/class1/example1.png

input_img_dir/class1/example2.png

input_img_dir/class2/example1.png

... could be labels extracted from a input_img_dir. In other words, each
label from input_img_dir contains both a class name (like 'class2') and
an example name (like 'example1.png'). Grouping your images into classes 
like this will allow you to gauge the how well the search is doing in terms
of precision and recall.

You can issue a series of searches with...

batch_search.py query_vector_file feature_vector_file

... where you wish to find the top K most similar images in
feature_vector_file for each vector in query_vector_file (both formatted
by process_dir.py).

You may wish to tune the K-value to a particular precision/recall level
for your dataset. You can do this using benchmark_k.py, which computes
these levels for a range of K-values (c_benchmark_k_start to 
c_benchmark_k_end)...

./benchmark_k.py feature_vector_file

Most of my testing has been against subsets of this dataset...

J. M. Geusebroek, G. J. Burghouts, and A. W. M. Smeulders,
The Amsterdam Library of Object Images,
IJCV, 61(1), 103-112, January, 2005.

... where each class is an object they have photographed with a 
variety of different angles, lighting conditions, etc. To robustly work 
with an image collection as diverse as the above, I'm using very primitive 
scale-invariant features: the means of the red, green, and blue 
components of the image pixel values as well as the standard deviation of 
the grayscale version of each pixel.

visionquest doesn't leverage an index (yet) so it will not scale to 
large datasets. If you find it useful or have a suggestion for an 
improvement, let me know!

