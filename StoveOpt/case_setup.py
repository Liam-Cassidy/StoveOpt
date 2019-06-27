# Test the initial velocity computation
import os
from shutil import copytree

Q_100 = 12.5757
num_cases_initial = 4

def compute_initial_velocities(Q_100, num_cases_initial):
    """Create four cases on each side of the seconday draft input by user. two velocities on each side of the initial U_100
    Computing the velocities based on equal spacing, where lower limit velocity is zero

    Args:

    U_100 (float): User-defined secondary air flow velocity_col
    num_cases_intial (int): initial number of surrounding cases defined by user. should be an equal integer.

    Returns:

    velocity_dictionary (dict): list of velocities defined by intial range. Each should be string of length 6

    """

    velocity_dictionary = [] # empty velocity dictionary intially--final product is each entry of type string length 6
    velocity_floats = [] # empty velocity vector--final product is floats for computed velocities

    difference = Q_100 - 0 # Full left and right hand side interval
    cases_per_side = num_cases_initial/2 # this is why we want an even number here
    intervals = difference/cases_per_side
    k_tot = num_cases_initial+1 # for indexing purposes--to include the input flow

    k = 0
    while k < k_tot:
        #Create the velocity dictionary, and float vector
        v_add = k*(Q_100)
        v_add_str = str(v_add)[:6] # string of length 6
        velocity_floats.append(v_add)
        velocity_dictionary.append(v_add_str)
        k = k + 1 # next index

    print("Velocity dictionary")
    print(velocity_dictionary)

    print("Velocity floats")
    print(velocity_floats)
    return velocity_dictionary, velocity_floats, k_tot

#velocity_dictionary, velocity_floats, k_tot = compute_initial_velocities(Q_100, num_cases_initial)

def edit_velocity_strings(velocity_dictionary, k_tot):
    """Purpose is solely to omit the period character from velocity dictionary strings for filenaming
    Args:

    velocity_dictionary (dict): list of velocities defined by intial range. Each should be string of length 6

    k_tot (int): number of cases total written initially
    Returns:

    velocity_case_names (dict): list of strings corresponding to the list of velocities without periods
    """
    locate_char = "."
    replace_char = ""
    p = 0 # looping index
    velocity_case_names = [] # empty dictionary for the edited strings
    while p < k_tot:
        v_str = velocity_dictionary[p].replace(locate_char, replace_char)
        velocity_case_names.append(v_str)
        p =  p + 1
    print("edited case names")
    print(velocity_case_names)
    return velocity_case_names

#velocity_case_names = edit_velocity_strings(velocity_dictionary, k_tot)


def create_case_directories(velocity_case_names, k_tot):
    """Create the file folders within foamfiles//counterFlowFlame2D// directories iteratively
    Args:
    velocity_case_names (dict): list of strings corresponding to the list of velocities without periods
    k_tot (int): number of cases total written initially

    Returns:
    case_folder_names (dict): list of names of case folders
    case_full_paths (dict): list of full strings of case folders for future use
    """

    current_directory = os.getcwd()
    base_dir = current_directory + "//" + "foamfiles//" + "//" + "counterFlowFlame2D//"

    # Iteratively make the new case directories
    x = 0 # intialize looping
    case_folder_names = []
    case_full_paths = []
    while x < k_tot:
        new_case_folder_name_entry = "case_" + velocity_case_names[x]
        case_folder_names.append(new_case_folder_name_entry)
        case_full_paths.append(base_dir + case_folder_names[x])
        os.mkdir(case_full_paths[x])
        x = x + 1
    return case_full_paths, case_folder_names

#case_full_paths, case_folder_names = create_case_directories(velocity_case_names, k_tot)

# Create system, constant, 0 folders
def add_foam_directories(case_full_paths, k_tot):
    """Loop through the new case directories and add the system, constant, and 0 folder
    Args:
    case_full_paths (dict): list of full strings of case folders for future use
    k_tot (int): number of cases total written initially

    Returns:
    case_zero_paths (dict): list of the full paths for 0 foam paths
    case_system_paths (dict): list of the full paths for system foam paths
    case_constant_paths (dict): of the full paths for constant foam paths
    """

    constant_dir_add = "//constant//"
    system_dir_add = "//system//"
    zero_dir_add    = "//0//"

    #initialize paths
    case_zero_paths = []
    case_system_paths = []
    case_constant_paths = []
    y = 0

    while y < k_tot:
        const = case_full_paths[y] + constant_dir_add
        zero = case_full_paths[y] + zero_dir_add
        system = case_full_paths[y] + system_dir_add

        # add to dictionaries
        case_zero_paths.append(zero)
        case_system_paths.append(system)
        case_constant_paths.append(const)

        y = y + 1
    #print("case_zero_paths dictionary")
    #print(case_zero_paths)
    #print("case_constant_paths dictionary")
    #print(case_constant_paths)
    #print("case_system_paths dictionary")
    #print(case_system_paths)
    return case_zero_paths, case_system_paths, case_constant_paths

#case_zero_paths, case_system_paths, case_constant_paths = add_foam_directories(case_full_paths, k_tot)

def paste_static_foam_files(case_zero_paths, case_system_paths, case_constant_paths, k_tot):
    """copy and paste static OpenFOAM solver files into the constant, 0, system directories
    Location for static files is in StoveOpt master directory
    k_tot (int): number of cases total written initially

    Args:
    case_zero_paths (dict): list of the full paths for 0 foam paths
    case_system_paths (dict): list of the full paths for system foam paths
    case_constant_paths (dict): of the full paths for constant foam paths

    Returns:
    None
    """
    current_dir = os.getcwd()
    static_zero_files = current_dir + "//static_foamfiles//" + "0"
    static_constant_files = current_dir + "//static_foamfiles//" + "constant"
    static_system_files = current_dir + "//static_foamfiles//" + "system"

    # Copytree--Moves all contents from a directory to location specified
    # Loop will change the destination based on index, and paste from the static sources
    i = 0 # initialize loop
    while i < k_tot:
        copytree(static_zero_files, case_zero_paths[i])
        copytree(static_constant_files, case_constant_paths[i])
        copytree(static_system_files, case_system_paths[i])
        i = i + 1

#paste_static_foam_files(case_zero_paths, case_system_paths, case_constant_paths, k_tot)



def blockmesh_case_move(blockmesh_for_run, case_system_paths, k_tot):
    """relocated the blockmesh ready for run to the case files iteratively
    Args:
    blockmesh_for_run (str): path where the blockMeshDict file for run is located prior to case runs.
    case_system_paths (dict): list of the full paths for system foam paths
    k_tot (int): number of cases total written initially

    Returns:
    blockmesh_case_paths (dict): list of strings representing the full paths associated with the relocated blockmesh files (for run)
    """
    blockmesh_file = "//blockMeshDict"
    i = 0 # loop initialize
    blockmesh_case_paths=  []
    while i < k_tot:
        # iteratively move the blockmesh file to the case system locations
        blockmesh_destination = case_system_paths[i] + blockmesh_file #destination iteratively changing
        destination = blockmesh_destination
        source = blockmesh_for_run
        blockmesh_case_paths.append(destination)
        copy(source, destination)
        i = i + 1
    print("here is the blockmesh case paths")
    print(blockmesh_case_paths)
    return blockmesh_case_paths
