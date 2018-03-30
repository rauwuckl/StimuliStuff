import os
import loading
import combine_stims
import preprocessing

def apply_fun_to_all_stim(input_folder, output_folder, fun, **kwargs):
    image_folder = input_folder
    output_folder = output_folder

    image_names = [img for img in os.listdir(image_folder) if img[-4:]==".png"]

    print(image_names)

    for img_name in image_names:
        old_img = loading.load_img(image_folder+"/"+img_name)

        newimg = fun(old_img, **kwargs)

        newimg_path = output_folder + "/" + img_name
        loading.save_img(newimg_path, newimg)



def round_all_imgs(input_f, output_f):
    apply_fun_to_all_stim(input_f, output_f, preprocessing.round_stimulus)

def merge_multiple(input_f, output_f, name_tuples):
    """name tuple is a list of two element tuples that will be merged"""

    tmp_load_stim = lambda name: loading.load_img("{}/{}.png".format(input_f, name))

    for name_a, name_b in name_tuples:
        stim_a = tmp_load_stim(name_a)
        stim_b = tmp_load_stim(name_b)

        combined = combine_stims.merge_stimuli(stim_a, stim_b)

        loading.save_img("{}/{}_{}.png".format(output_f, name_a, name_b), combined)



merge_multiple("training_rounded", "training_rounded_multiStim_secondHalf", [
    # ("1bcl", "1bcr"), ("1wcl", "1wcr"), ("1bdl", "1bdr"), ("1wdl", "1wdr"), #full at loc 1
    # ("2bcl", "2bcr"), ("2wcl", "2wcr"), ("2bdl", "2bdr"), ("2wdl", "2wdr"), #full at loc 2
    ("1bcr", "2bcr"), ("1wcr", "2wcr"), ("1bdr", "2bdr"), ("1wdr", "2wdr"), #loc1 with incongurent distractor
    ("1bcr", "2bcl"), ("1wcr", "2wcl"), ("1bdr", "2bdl"), ("1wdr", "2wdl"),  # loc1 with incongurent distractor
])
