from optparse import OptionParser
import os
import matplotlib.image as mpimg
import numpy as np
import matplotlib.pyplot as plt


def main():
    parser = OptionParser()
    parser.add_option("-s", "--source", dest="source",
                      help="Folder Containing the input images that should be changed", action="store")
    parser.add_option("-o", "--output",
                      dest="output", action="store",
                      help="where the changed files should be stored")
    parser.add_option("-n", "--name", dest="name", action="store", help="Name that will be appended to the original filename")
    parser.add_option("-p", "--pixel", dest="pixel", type=int, action="store", help="move Stimuli this many pixel to the center")

    options, args = parser.parse_args()
    options_ok = True
    if options.source is None:
        print("please specify source folder")
        options_ok = False
    if options.output is None:
        print("please specify target")
        options_ok = False
    elif not os.path.isdir(options.output):
        print("output dir {} does not exist".format(options.output))
        options_ok = False

    if options.pixel is None:
        options_ok = False
        print("please speciry pixel")

    if not options_ok:
        return

    image_folder = options.source
    output_folder = options.output

    image_names = [img for img in os.listdir(image_folder) if img[-4:]==".png"]

    print(image_names)
    move_image(image_folder+'/'+image_names[0], options.pixel)

    for img_name in image_names:
        newimg = move_image(image_folder + "/" + img_name, options.pixel)

        if options.name is not None:
            newName = img_name[:-4] + options.name + ".png"
        else:
            newName = img_name

        newimg_path = output_folder + "/" + newName
        mpimg.imsave(newimg_path, newimg)
    print("All done")

def move_image(imagepath, displace, display=False):
    img = mpimg.imread(imagepath)
    newimg = np.empty(img.shape)


    height, width, depth = img.shape
    if width%2 != 0:
        raise ValueError("Image does not have even width")
    middle = width/2

    newimg[:, :displace, :] = img[:, middle-displace: middle, :]
    newimg[:, displace:middle, :] = img[:, :middle-displace, :]
    newimg[:, middle: -displace, :] = img[:, middle+displace:, :]

    newimg[:,  -displace:, :] = img[:, middle:middle+displace, :]

    if display:
        fig = plt.figure()
        ax1 = fig.add_subplot(1,2,1)
        ax1.imshow(img)
        ax2 = fig.add_subplot(1,2,2)
        ax2.imshow(newimg)
        plt.show()

    return newimg





if __name__ == "__main__":
    main()
