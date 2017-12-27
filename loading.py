import matplotlib.image as mpimg
import numpy as np


def load_img(filename):
    img = mpimg.imread(filename)

    dimY, dimX, _channels = img.shape
    assert(dimY == dimX)
    assert(_channels == 4) #// rgb alpha

    clean_img = np.zeros((dimY, dimX), dtype=np.float32)

    # check alpha is 1 everywhere
    assert(np.all(img[:, :, 3] == 1))

    clean_img = img[:, :, 0] # assumes all channels have same value -> gray scale


    for color in range(3):
        assert(np.all(clean_img == img[:, :, color]))


    return clean_img

def save_img(filename, img):
    assert(len(img.shape) == 2) #to make sure its a gray scale img
    dimY, dimX = img.shape
    assert(dimY == dimX)

    ones = np.ones((dimY, dimX), dtype=np.float32)

    result = np.stack([img, img, img, ones], axis=2)

    return result
    mpimg.imsave(filename, img)



i = load_img("play_around/1bhl.png")