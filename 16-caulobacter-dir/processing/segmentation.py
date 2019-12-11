#Processing

import glob
import os

import numpy as np
import pandas as pd

# Image processing tools
import skimage
import skimage.feature
import skimage.io
import skimage.filters
import skimage.filters.rank
import skimage.segmentation
import skimage.morphology

import scipy.ndimage


import bebi103

import colorcet

import panel as pn
pn.extension()

import bokeh
bokeh.io.output_notebook()

import holoviews as hv
hv.extension('bokeh')
bebi103.hv.set_defaults()



# Final choice of segmentation
def bacteria_thresh(im):
    '''Returns plots of the original image and thresholded images of the image provided.
    Also includes three different zooms into the three groups of bacteria we are interested in using for long time course imaging.'''
    selem = skimage.morphology.disk(25)
    im_mean = skimage.filters.rank.mean(im, selem)
    im_bw = im < 0.85 * im_mean
    im_bw = skimage.segmentation.clear_border(im_bw)
    
    selem_open = skimage.morphology.disk(2)
    im_bw = skimage.morphology.binary_opening(im_bw, selem_open)
    
    full = show_two_ims(im, im_bw, titles = ['original', 'thresholded'])
    zoomed_cluster = show_two_ims(im[zoom_cluster], im_bw[zoom_cluster])
    zoomed_boi = show_two_ims(im[zoom_boi], im_bw[zoom_boi])
    zoomed_single = show_two_ims(im[zoom_single], im_bw[zoom_single])
    bokeh.io.show(bokeh.layouts.column([full, zoomed_cluster, zoomed_boi, zoomed_single]))
    
   
# Find threshold for image
def bebi103_thresh(im, selem, white_true=True, k_range=(0.5, 1.5), min_size=100):
    """
    Threshold an images based on changes in number of pixels
    included in binary image. Morphological mean filter is
    applied using selem.
    """
    # Determine comparison operator
    if white_true:
        compare = np.greater
        sign = -1
    else:
        compare = np.less
        sign = 1
        
     # Do the mean filter
    im_mean = skimage.filters.rank.mean(im, selem)

    # Compute number of pixels in binary image as a function of k
    k = np.linspace(k_range[0], k_range[1], 100)
    n_pix = np.empty_like(k)
    for i in range(len(k)):
        n_pix[i] = compare(im, k[i] * im_mean).sum()

    # Compute rough second derivative
    dn_pix_dk2 = np.diff(np.diff(n_pix))

    # Find index of maximal second derivative
    max_ind = np.argmax(sign * dn_pix_dk2)
    
    # Use this index to set k
    k_opt = k[max_ind - sign * 2]

    # Threshold with this k
    im_bw = compare(im, k_opt * im_mean)

    # Remove all the small objects
    im_bw = skimage.morphology.remove_small_objects(im_bw, min_size=min_size)

    return im_bw, k_opt

# Make the structuring element 5 pixel radius disk - works best for this size
selem = skimage.morphology.disk(5)

# As defined in the problem statement
ip = 0.052