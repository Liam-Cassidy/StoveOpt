
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


def test_edit_velocity_strings():
    Q_100 = 12.5757
    num_cases_initial = 4
    velocity_dictionary, velocity_floats, k_tot = compute_initial_velocities(Q_100, num_cases_initial)
    velocity_case_names = edit_velocity_strings(velocity_dictionary, k_tot)

    assert velocity_case_names == ['00', '12575', '25151', '37727', '50302']
