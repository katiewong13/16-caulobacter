# Exploration for Thresholding

# Look through lal the images
def display_image(frame = 0):
    '''Displays the image at the frame dictated.'''
    return bebi103.image.imshow(ic[frame], colorbar = True, flip=False)

# Plot histogram to determine thresholding level
def plot_hist(im, title, logy=False):
    """Make plot of image histogram."""
    counts, vals = skimage.exposure.histogram(im)
    if logy:
        inds = counts > 0
        log_counts = np.log(counts[inds])
        return hv.Spikes(
            data=(vals[inds], log_counts),
            kdims=['pixel values'],
            vdims=['log₁₀ count'],
            label=title,
        ).opts(
            frame_height=100,
        )

    return hv.Spikes(
        data=(vals, counts),
        kdims=['pixel values'],
        vdims=['count'],
        label=title,
    ).opts(
        frame_height=100,
    )


# Edge detection
def zero_crossing_filter(im, thresh):
    selem = skimage.morphology.square(3)

    # Do max filter and min filter
    im_LoG_max = scipy.ndimage.filters.maximum_filter(im, footprint = selem)
    im_LoG_min = scipy.ndimage.filters.minimum_filter(im, footprint = selem)
    im_grad = skimage.filters.sobel(im)
    
    im_edge = (((im_LoG >= 0) & (im_LoG_min < 0)) | ((im_LoG <= 0) & (im_LoG_max > 0)))  & (im_grad >= thresh)
    im_edge = skimage.morphology.skeletonize(im_edge)
    return im_edge