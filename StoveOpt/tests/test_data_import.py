# Testing data import from the post_processor Module

import numpy as np
from numpy import hstack, vstack, sort, transpose, argsort, append
import os

def data_import(foamfile_path):
    """input a list of filenames to be pulled, put out an array of temperature data. search the foamfiles directory for fnames that start with case_ and tally the number for looping through the file. loop through each and pull data from the files (3) convert to numpy arrays (4) store.

    Args:
        None

    Returns:
        dir_list (dict): Dictionary of directory titles in the 'foamfiles' directory that begin with string 'case_'

        case_list (dir): Dictionary of case file paths. Appended iteratively with dir_list entries.

        length_case_list (int): Number of excecuted case files existing in foamfiles directory

        list_temps (array): Populated with results from probing the CFD simulation around entire pot geometry

        list_velocities (array): Populated with velocity values written to "details" file in individual case files
    """
    # navigate to the foamfiles directory
    #current_directory = os.getcwd()
    #foamfile_steps = "foamfiles\counterFlowFlame2D\"
    #foamfile_path = current_directory + foamfile_steps
    #foamfile_path = current_directory + "\\foamfiles\\counterFlowFlame2D\\"
    dir_list = [directory for directory in os.listdir(foamfile_path) if os.path.isdir(foamfile_path+directory)]
    length_dir_list = len(dir_list)
    detect_prefix = 'case' # look for case prefix

    i = 0 # for looping
    case_counter = 0
    case_list = [None] # empty vector
    k = 0 # case list indices
    while i < length_dir_list:
        if dir_list[i].startswith(detect_prefix):
            case_list_append = dir_list[i]
            case_list[k] = case_list.append(str(dir_list[i]))
            case_list[k] = dir_list[i]
            k = k+1
        i = i+1

    # remove the final entry of the case_list vector
    case_list_length = len(case_list)
    omitted_value= case_list.pop(case_list_length-1)

    # extract and go read data from each of the files
    """(1) Loop through the case_list produced, (2) pull the strings and
    (3) add to the correct file extension. (4) open and read the data in.
    (5) create tables in numpy (potentially). (6) return the arrays in the overall function"""

    length_case_list = len(case_list)
    print("case list length: " + str(length_case_list))
    j = 0
    Temps = []
    Velocities = [] # reading in the 25-150 velocities
    list_temps = []
    list_velocities = []
    while j < length_case_list:
        fname = str(case_list[j]) # pull the case file name
        dir_steps = "//postProcessing//probes//0//"
        U_dir_steps = "//0//"
        U_fname = "details"
        Temp_fname = "T"
        full_path = foamfile_path + fname + dir_steps + Temp_fname # this will need to be edited for a more advanced file loc
        U_full_path = foamfile_path + fname + U_dir_steps + U_fname # varies for the cases (fname)
        with open(U_full_path, 'r') as f:
            f.seek(10) # position 10 is the beginning of line 2
            Velocity = f.readlines() # read line 2nd line
            globals()['Velocities%s' % j] = Velocity # putting this into the Velocity matrix, renaming based on j to match cases
            list_velocities.append(globals()['Velocities%s' % j])

        globals()['Temps%s' % j] = np.loadtxt(fname = full_path)
        list_temps.append(globals()['Temps%s' % j])
        j = j+1
    type_Temps1 = type(Temps1)
    shape_Temp1 = Temps1.shape

    # Concatenate all the temperatures
    """while the index is under the length of case list (# of temp vars)
            add the temperature arrays to a list  (list temps)"""

    # Create list of the arrays
    """Temp_array_list = []
    while x < length_case_list:"""

    # Validates the list_temp is a group of the arrays
    first_temp_list_entry = list_temps[0]
    return dir_list, case_list, length_case_list, list_temps, list_velocities


def test_data_import():
    current_dir = os.getcwd()
    test_steps = "//tests//test_results//"
    foamfile_path = current_dir + test_steps # move to the test file in the test suite


    temps_case3333 = [288.892,288.393,294.837,294.187,294.944,295.242,296.637,299.569,296.73,299.72,294.747 ,       295.19    ,   294.956  ,      294.34      , 288.394 ,       295.19]
    temps_case4166 = [291.637,       290.698   ,    302.601,       303.537 ,      301.986      , 302.728  ,     302.612    ,    319.92  ,     306.314    ,   324.578,       303.063,       306.691,       303.168,       304.173 ,       290.78,       306.691]
    temps_case4722 = [291.86,       291.184,       304.151 ,      304.193 ,      303.371 ,      304.168,       305.271 ,      352.947,       306.333,       338.665,       300.683,       310.614  ,     300.393 ,      299.093  ,     303.653,       310.614]
    temps_case5277 = [292.116 ,      291.355 ,      301.759   ,    302.154 ,      302.719,         305.5 ,      344.022 ,      550.076  ,     335.291 ,      1327.38,        300.55,       300.654 ,      300.564 ,      300.857,       291.684 ,      300.654]
    temps_case6666 = [291.589,       291.462,       299.943,       300.095 ,      299.967,       300.089 ,      299.793 ,      300.252,       299.507,       299.447,        299.37  ,     299.387  ,     299.678,       299.566  ,     291.301 ,      299.387]

    expected_temp_list = vstack((temps_case3333, temps_case4166, temps_case4722, temps_case5277, temps_case6666)) # stack the temps
    expected_case_list = ['case_3333333333', 'case_4166666667', 'case_4722222222', 'case_5277777778', 'case_6666666667']
    expected_velocities = [33.33333333, 41.66666667, 47.22222222, 52.77777778, 66.66666667]
    expected_length_case_list = 5

    dir_list, case_list, length_case_list, list_temps, list_velocities = data_import(foamfile_path)

    assert expected_temp_list == list_temps
    assert expected_case_list == case_list
    assert expected_velocities == list_velocities
    assert expected_length_case_list == length_case_list
