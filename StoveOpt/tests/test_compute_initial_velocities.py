# Test the initial velocity computation

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
    return velocity_dictionary, velocity_floats


def test_compute_initial_velocities():
    Q_100 = 100.676767
    num_cases_initial = 4

    velocity_dictionary, velocity_floats, k_tot = compute_initial_velocities(Q_100, num_cases_initial, k_tot)

    assert velocity_dictionary == ['0.0', '100.67', '201.35', '302.03', '402.70']
    assert velocity_floats == [0.0, 100.676767, 201.353534, 302.030301, 402.707068]
