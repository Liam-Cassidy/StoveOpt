# testing the num_cells computation
def compute_num_cells(max_delta_x, pt0x, pt1x):
    """compute the number of blocks associated with the max_delta_x for the largest spatial step (combustion chamber)

    Args:
    max_delta_x (double): User defined maximum grid spacing.
    pt0x (double): x-coordinate of bottom LHS cookstove combustion chamber
    pt1x (double): x-coordinate of bottom RHS cookstove combustion chamber


    Returns:
    num_cells_int (int): number of cells to be written to the openfoam blockmesh file for entire domain
    num_cells_double (double): number of cells to be written to the openfoam blockmesh file for entire domain BEFORE INT ROUNDING


    """

    max_space = abs(pt1x-pt0x) # maximum spatial step in domain defined by coordinates
    num_cells_double = max_space/max_delta_x # unrounded number of cells per block
    num_cells_int = round(num_cells_double) # round to integer value

    print("number of cells double")
    print(num_cells_double)

    print("Number of cells rounded to int value")
    print(num_cells_int)
    return num_cells_int, num_cells_double



def test_compute_num_cells():
    # arbitrary for testing
    max_delta_x = 0.04
    pt1x = 0.87
    pt0x = 0
    num_cells_int, num_cells_double = compute_num_cells(max_delta_x, pt0x, pt1x)
    assert num_cells_int == 22
    assert num_cells_double == 21.75
