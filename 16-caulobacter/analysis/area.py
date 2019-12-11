# Example on calulating the bacteria area. im_bw is an image of true/false, where
# true signifies background and false signifies the bacterium
def find_area(im):
    total_area = len(im) * len(im[0])
    bacteria_area = 0
    for i in im:
        for j in i:
            if j == False:
                bacteria_area += 1
    return(bacteria_area/total_area)


def collect_area(i, arr):
    # Read in the image using skimage
    tiff_stack = skimage.io.imread(i)
    for j in tiff_stack:
        frame, k = bebi103_thresh(j, selem, k_range=(0.901, 0.902), min_size=100)
        arr.append(find_area(frame))