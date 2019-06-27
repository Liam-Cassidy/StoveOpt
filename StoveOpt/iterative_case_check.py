# Navigate to the case directory

import os
import numpy as np

def navigate_to_cases():
    """Purpose is to navigate to the directory where case files exists

    Args:
        None

    Returns:
        case_path (str): full file path where directories exists
    """
    current_dir = os.getcwd() # Get current directory
    dir_steps = "foamfiles//counterFlowFlame2D//"
    case_path = current_dir + dir_steps # full path with case folders
    return cases_path

def count_cases_to_run(cases_path):
    """Purpose is to identify the number of cases to be run, and the name of the case path for run_surrounding_cases

    Args:
        case_path (str): full file path where directories exists

    Returns:
        num_cases (int): Number of cases needed to be run
        case_list_for_run (dictionary): list of strings corresponding to the full case paths to be run
    """
# WHILE LOOP CONTAINING THIS AND RUNNER.
# LOOP CONDITION IS THE NUM CASES, WHERE THE INDEX OPENS THE case_list_for_run ENTRY
# CURRENTLY SETUP FOR NON PARALLEL RUNS
def navigate_case_dictionary(case_list_for_run, num_cases):
    """Loop through the case directories, and run temporal_choice---runner should be within a loop with this function
    Args:
        num_cases (int): Number of cases needed to be run
        case_list_for_run (dictionary): list of strings corresponding to the full case paths to be run
    Returns:
        None
    """
