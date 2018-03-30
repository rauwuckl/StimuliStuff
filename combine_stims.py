import loading
from matplotlib import pyplot as plt
import numpy as np

edge_positions = [37, 90]

def concat(imgs, axis=0):
    """concatentate 2d matrices imgs along the axis"""
    first_shape = imgs[0].shape
    assert(len(first_shape)==2)
    for i in imgs:
        assert(i.shape == first_shape)

    expanded = [np.expand_dims(i, axis) for i in imgs]

    return np.concatenate(expanded, axis)

def merge_stimuli(a, b):
    """
    Take two numpy arrays a, b and merge the stimuli
    :return:
    """
    assert(a.shape == b.shape)

    assert(a[0, 0] == b[0, 0]) # make sure they have same polarity

    background_black = (a[0,0] == np.min(a)) # upper left pixel is the background colour

    a_exp = np.expand_dims(a, 0)
    b_exp = np.expand_dims(b, 0)
    both = np.concatenate((a_exp, b_exp), axis=0)


    if background_black:
        one_img = np.max(both, axis=0)
    else:
        one_img = np.min(both, axis=0)

    #correct for overlap
    for edge in edge_positions:
        left_of_edge = one_img[:, edge-1]
        right_of_edge = one_img[:, edge+1]
        if(np.all(left_of_edge == right_of_edge)):
            print("Correcting for edge")
            one_img[:, edge] = left_of_edge
        else:
            print("its different at the edges")

    return one_img

def load_and_merge(file_a, file_b):
    """
    take two filenames and merge them
    :param file_a:
    :param file_b:
    :return:
    """
    a = loading.load_img(file_a)
    b = loading.load_img(file_b)

    res = merge_stimuli(a, b)
    plt.imshow(res, cmap='gray', vmin=0, vmax=1)
    plt.show()




