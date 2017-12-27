from optparse import OptionParser
import numpy as np
import os


def main():
    parser = OptionParser()
    parser.add_option("-c", "--count", dest="count", help="number of random stimuli", action="store")
    options, args = parser.parse_args()

    if not options.count is None:
        n_stimuli = int(options.count)
        print("Generating {} random stimuli".format(n_stimuli))
        generated_random_stimuli(n_stimuli)
    else:
        print("no count given")


def generated_random_stimuli(n_stimuli, stimulus_info=None):
    """generated n_stimuli many completely random white noise stimuli, for each pixel in each filter the value is independentliy choosen uniformaly between [0,1]"""

    if stimulus_info is None:
        stimulus_info = dict(phases=[0, 180], scales=[2], orientations=[0, 45, 90, 135], dims=[128], filter_file_string="{obj_name}.{scale}.{orientation}.{phase}.gbo")


    output_folder_name = "Filtered"

    # make folder
    os.mkdir(output_folder_name)

    # make stimuli
    stimuli_list = list()

    #make stimuli
    for i in range(n_stimuli):
        stim_name = "random_{:04}".format(i)
        make_stimulus(output_folder_name, stim_name, stimulus_info)

        stimuli_list.append(stim_name)

    # make filter paremeter txt
    with open("{}/Filter_Parameters.txt".format(output_folder_name), "w") as f:
        f.write(\
        """
        {phases} Phases
        {scales} Scales
        {orientations} Orientations
        {dims} Dimension
        """.format(**stimulus_info))

    with open("{}/File_List.txt".format(output_folder_name), "w") as f:
        stuff = "\n".join(stimuli_list + ["*"])
        f.write(stuff)



def make_stimulus(folder, obj_name, stimulus_info):
    dimension = stimulus_info['dims'][0]
    file_name = stimulus_info['filter_file_string']

    stimulus_path = "{}/{}.flt".format(folder, obj_name)
    os.mkdir(stimulus_path)
    for phase in stimulus_info['phases']:
        for scale in stimulus_info['scales']:
            for orientation in stimulus_info['orientations']:
                values = np.random.rand(dimension**2).astype(np.float32)
                with open(stimulus_path + "/" + file_name.format(obj_name=obj_name, scale=scale, phase=phase, orientation=orientation), "wb") as f:
                    values.tofile(f)




if __name__ == "__main__":
    main()