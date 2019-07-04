# Test the initial velocity computation
import os
from shutil import copytree
from shutil import copy


def compute_initial_velocities(Q_100, num_cases_initial):
    """Create four cases on each side of the seconday draft input by user. two velocities on each side of the initial U_100
    Computing the velocities based on equal spacing, where lower limit velocity is zero

    Args:

    U_100 (float): User-defined secondary air flow velocity_col
    num_cases_intial (int): initial number of surrounding cases defined by user. should be an even integer.

    Returns:

    velocity_dictionary (dict): list of velocities defined by intial range. Each should be string of length 6

    """

    velocity_dictionary = [] # empty velocity dictionary intially--final product is each entry of type string length 6
    velocity_floats = [] # empty velocity vector--final product is floats for computed velocities

    difference = Q_100 - 0 # Full left and right hand side interval
    cases_per_side = num_cases_initial/2 # this is why we want an even number here
    intervals = difference/cases_per_side
    k_tot = num_cases_initial+1 # for indexing purposes--to include the input flow
    print("cases per side")
    print(cases_per_side)
    k = 0
    while k < k_tot:
        #Create the velocity dictionary, and float vector
        v_add = k*Q_100/cases_per_side
        print("v_add")
        print(v_add)
        v_add_str = str(v_add)[:6] # string of length 6
        print("v_add_str")
        print(v_add_str)
        velocity_floats.append(v_add)
        velocity_dictionary.append(v_add_str)
        print("k")
        print(k)
        print('velocity dictionary within loop')
        print(velocity_dictionary)
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

        # Make locate_directories
        #os.mkdir(const)
        #os.mkdir(zero)
        #os.mkdir(system)
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

def controldict_case_move(controldict_for_run, case_system_paths, k_tot):
    """relocated the blockmesh ready for run to the case files iteratively
    Args:
    controldict_for_run (str): path where the controldict file for run is located prior to case runs.
    case_system_paths (dict): list of the full paths for system foam paths
    k_tot (int): number of cases total written initially

    Returns:
    controldict_case_paths (dict): list of strings representing the full paths associated with the relocated blockmesh files (for run)
    """
    controldict_file = "//controlDict"
    i = 0 # loop initialize
    controldict_case_paths=  []
    while i < k_tot:
        # iteratively move the blockmesh file to the case system locations
        controldict_destination = case_system_paths[i] + controldict_file #destination iteratively changing
        destination = controldict_destination
        source = controldict_for_run
        controldict_case_paths.append(destination)
        copy(source, destination)
        i = i + 1
    print("here is the controldict case paths")
    print(controldict_case_paths)
    return controldict_case_paths


# SETTING UP BCs, and other things -- taking from run_surrounding_cases.property.py
def write_details_file(case_zero_paths, velocity_dictionary, k_tot):
    """Loop through each of the new case directories and create the details file used in post_processor
    Args:
    case_zero_paths (dict): Dictionary containing full case zero paths as strings
    velocity_dictionary (dict): Dictionary containing the velocities computed for initial surrounding cases
    k_tot (int): Number of cases to edit

    Returns:
    case_details_files (dict): Dictionary containing full paths to all of the details files written
    """
    fname = "details"
    case_details_files = []
    j = 0
    while j < k_tot:
        # Iteratively add the details FILES
        details_file = case_zero_paths[j] + "//" + fname
        with open(details_file, 'w+') as f:
            f.write('Velocity' +'\n')
            f.write(velocity_dictionary[j])
        case_details_files.append(details_file)
        j = j + 1

    return case_details_files

# Boundary conditions
def write_velocity_files(velocity_dictionary, case_zero_paths, Q_primary, k_tot):
    """Write  the U-initial condition files for the cases created
    Args:
    case_zero_paths (dict): Dictionary containing full case zero paths as strings
    velocity_dictionary (dict): Dictionary containing the velocities computed for initial surrounding cases
    Q_primary (double): Primary air flow rate required for the U-BC file

    Returns:
    case_U_files (dict): Dictionary containing paths to the case U files
    """

    #Loop through the full case zero paths, and add zero filename string to each str
    k = 0 # Initialize
    U_fname = "//U"
    case_U_files = []
    while k < k_tot:
        # Add the U_fname to the case_zero_paths[k]
        case_append = case_zero_paths[k] + U_fname
        case_U_files.append(case_append) # appending to the
        print("case_U_files within loop")
        print(case_U_files)
        k = k + 1

    # Loop through case U_files and write the files iteratively.
    # IMPORTANT: The iterative variable that needs to be added is the velocity_dictionary[k]
    j = 0 # Loop for writing the actual U files
    while j < k_tot:
        # Open jth file
        with open(case_U_files[j], 'r+') as f:
            f.seek(600)
            f.write("dimensions" + " " + "[0 1 -1 0 0 0 0]" + ";" + "\n")
            f.write("internalField" + " " + "uniform" + " " + "(0 0 0)" + ";" + "\n")
            f.write("boundaryField" + "\n")
            f.write("{" + "\n")
            f.write("fuel" + "\n")
            f.write("{" + "\n")
            f.write("type" + " " + "fixedValue" + ";" + "\n")
            f.write("value" + " " + "uniform" + " " + "(0 0 0.25)" + ";" + "\n")
            f.write("}" + "\n")
            f.write("primary_air" + "\n")
            f.write("{" + "\n")
            f.write("type" + " " + "fixedValue" + ";" + "\n")
            f.write("value" + " " + "uniform" + " " + "(0 0" + " " + str(Q_primary) + ")" + ";" + "\n")
            f.write("}" + "\n")
            f.write("Secondary_air_RHS" + "\n")
            f.write("{" + "\n")
            f.write("type" + " " + "fixedValue" + ";" + "\n")
            f.write("value" + " " + "uniform" + " " + "(0" + " " + velocity_dictionary[j] + " " + "0)" + ";" + "\n")
            f.write("}" + "\n")
            f.write("Secondary_air_LHS" + "\n")
            f.write("{" + "\n")
            f.write("type" + " " + "fixedValue" + ";" + "\n")
            f.write("value" + " " + "uniform" + " " + "(0" + " " + "-" + velocity_dictionary[j] + " " + "0)" + ";" + "\n")
            f.write("}" + "\n")
            f.write("outlet" + "\n")
            f.write("{" + "\n")
            f.write("type pressureInletOutletVelocity;" + "\n")
            f.write("value $internalField;" + "\n")
            f.write("}" + "\n")
            f.write("frontAndBack" + "\n")
            f.write("{" + "\n")
            f.write("type empty;" + "\n")
            f.write("}" + "\n")
            f.write("stove_body" + "\n")
            f.write("{" + "\n")
            f.write("type noSlip;" + "\n")
            f.write("}" + "\n")
            f.write("}" + "\n")
            f.write("// ************************************************************************* //")
        j = j + 1
    return case_U_files
