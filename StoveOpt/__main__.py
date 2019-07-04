# -*- coding: utf-8 -*-
"""
Created on Mon Apr 22 15:52:06 2019

@author: Lee
"""
"""Last test successful 4/26 12:19"""

"""The purpose of master.py is to call the functions in sequence from the varipus modules"""

#from import_geometry import *
import os
import fileinput
import shutil

""" Command line arguments:"""
# Import necessary packages
import sys
import argparse
import yaml

import import_geometry
import create_blockmeshfile
import new_case_setup
import post_processor
import run_surrounding_cases
import case_setup
import create_controldict

from import_geometry import *
from create_blockmeshfile import *
from run_surrounding_cases import *
from new_case_setup import *
from post_processor import *
from case_setup import *
from create_controldict import *


def main():
    """ Main script"""
    # Construct the argument parse and parse the arguments
    parser = argparse.ArgumentParser(description='Stove Optimization')
    # File directory argument
    parser.add_argument(
    '-i', '--inputfile', required=True, help='Please enter the full file path (directory and filename.extension) for the input.yaml file in LINUX format. For example, /mnt/c/Oregon_State/Spring_2019/Soft_dev_eng/StoveOpt/StoveOpt/inputFiles/input.yaml')

    args = parser.parse_args(sys.argv[1:])

    # Ensure the args all work-->string vs non string, slash variations, quotation marks
    #correct_arguments(args)
    print('args printed:')
    print(args)

    # Convert namespace to a usable input file convention
    input_file = convert_namespace(args)

    # EXTRACT DATA FROM THE INPUT FILE
    path, fname, Q_100, Q_primary, max_delta_x, start_time, end_time, delta_t, num_cases_initial, write_interval, write_format, max_co, OS = pull_input_data(input_file)


    # extract the excel filename and path from the input file--pass to locate geometry module
    file_path = locate_geometry(path, fname)
    print("Here is your filepath!")
    print(file_path)

    # prints the file path of the input file -- the argument
    input_file = args.inputfile
    print("input file value within import geometry module")
    print(input_file)


    # Extract geometry
    pt0x, pt0z, pt0y, pt1x, pt1z, pt1y, pt2x, pt2z, pt2y, pt3x, pt3z, pt3y, pt4x, pt4z, pt4y, pt5x, pt5z, pt5y, pt6x, pt6z, pt6y, pt7x, pt7z, pt7y, pt8x, pt8z, pt8y, pt9x, pt9z, pt9y, pt10x, pt10z, pt10y, pt11x, pt11z, pt11y, pt12x, pt12z, pt12y, pt13x, pt13z, pt13y,  pt14x, pt14z, pt14y, pt15x, pt15z, pt15y = extract_geometry(file_path) #unformatted list of (x,z,y) vertices


    # Create Fuel Blocks
    pt17x, pt18x, pt19x, pt16x, pt17z, pt18z, pt19z, pt16z, pt17y, pt18y, pt19y, pt16y = create_fuel_blocks(pt0x, pt1x)

    # Create additional front points
    pt48x, pt48z, pt48y, pt20x, pt20z, pt20y, pt21x, pt21z, pt21y, pt44x, pt44z, pt44y, pt46x, pt46z, pt46y, pt50x, pt50z, pt50y = create_additional_front_points(pt6x, pt7x, pt14x, pt9z, pt15x, pt8z, pt14z, pt9x, pt8x, pt15z)

    # convert front points to strings
    pt1xstr, pt1zstr, pt1ystr, pt2xstr, pt2zstr, pt2ystr, pt3xstr, pt3zstr, pt3ystr, pt4xstr, pt4zstr, pt4ystr, pt5xstr, pt5zstr, pt5ystr, pt6xstr, pt6zstr, pt6ystr, pt7xstr, pt7zstr, pt7ystr, pt8xstr, pt8zstr, pt8ystr, pt9xstr, pt9zstr, pt9ystr, pt10xstr, pt10zstr, pt10ystr, pt11xstr, pt11zstr, pt11ystr, pt12xstr, pt12zstr, pt12ystr, pt13xstr, pt13zstr, pt13ystr,  pt14xstr, pt14zstr, pt14ystr, pt15xstr, pt15zstr, pt15ystr, pt0xstr, pt0zstr, pt0ystr, pt16xstr, pt16zstr, pt16ystr, pt17xstr, pt17zstr, pt17ystr, pt18xstr, pt18zstr, pt18ystr, pt19xstr, pt19zstr, pt19ystr, pt20xstr, pt20zstr, pt20ystr, pt21xstr, pt21zstr, pt21ystr, pt44xstr, pt44zstr, pt44ystr, pt46xstr, pt46zstr, pt46ystr, pt48xstr, pt48zstr, pt48ystr, pt50xstr, pt50zstr, pt50ystr = points_to_strings(pt1x, pt1z, pt1y, pt2x, pt2z, pt2y, pt3x, pt3z, pt3y, pt4x, pt4z, pt4y, pt5x, pt5z, pt5y, pt6x, pt6z, pt6y, pt7x, pt7z, pt7y, pt8x, pt8z, pt8y, pt9x, pt9z, pt9y, pt10x, pt10z, pt10y, pt11x, pt11z, pt11y, pt12x, pt12z, pt12y, pt13x, pt13z, pt13y,  pt14x, pt14z, pt14y, pt15x, pt15z, pt15y, pt0x, pt0z, pt0y, pt17x, pt18x, pt19x, pt16x, pt17z, pt18z, pt19z, pt16z, pt17y, pt18y, pt19y, pt16y, pt20x, pt20z, pt20y, pt21x, pt21z, pt21y, pt44x, pt44z, pt44y, pt46x, pt46z, pt46y, pt48x, pt48y, pt48z, pt50x, pt50y, pt50z)



    # concatenate all front point strings
    pt0str, pt1str, pt2str, pt3str, pt4str, pt5str, pt6str, pt7str, pt8str, pt9str, pt10str, pt11str, pt12str, pt13str, pt14str, pt15str, pt16str, pt17str, pt18str, pt19str, pt20str, pt21str, pt44str, pt46str, pt48str, pt50str = vertice_concatenate(pt1xstr, pt1zstr, pt1ystr, pt2xstr, pt2zstr, pt2ystr, pt3xstr, pt3zstr, pt3ystr, pt4xstr, pt4zstr, pt4ystr, pt5xstr, pt5zstr, pt5ystr, pt6xstr, pt6zstr, pt6ystr, pt7xstr, pt7zstr, pt7ystr, pt8xstr, pt8zstr, pt8ystr, pt9xstr, pt9zstr, pt9ystr, pt10xstr, pt10zstr, pt10ystr, pt11xstr, pt11zstr, pt11ystr, pt12xstr, pt12zstr, pt12ystr, pt13xstr, pt13zstr, pt13ystr,  pt14xstr, pt14zstr, pt14ystr, pt15xstr, pt15zstr, pt15ystr, pt0xstr, pt0zstr, pt0ystr, pt16xstr, pt16zstr, pt16ystr, pt17xstr, pt17zstr, pt17ystr, pt18xstr, pt18zstr, pt18ystr, pt19xstr, pt19zstr, pt19ystr, pt20xstr, pt20zstr, pt20ystr, pt21xstr, pt21zstr, pt21ystr, pt44xstr, pt44zstr, pt44ystr, pt46xstr, pt46zstr, pt46ystr, pt48xstr, pt48zstr, pt48ystr, pt50xstr, pt50zstr, pt50ystr)


    # Create concatenated strings for the back points
    shift = 0.1
    pt22str, pt23str, pt24str, pt25str, pt26str, pt27str, pt28str, pt29str, pt30str, pt31str, pt32str, pt33str, pt34str, pt35str, pt36str, pt37str, pt38str, pt39str, pt40str, pt41str, pt42str, pt43str, pt45str, pt47str, pt49str, pt51str = create_back_points(shift, pt1xstr, pt1zstr, pt1ystr, pt2xstr, pt2zstr, pt2ystr, pt3xstr, pt3zstr, pt3ystr, pt4xstr, pt4zstr, pt4ystr, pt5xstr, pt5zstr, pt5ystr, pt6xstr, pt6zstr, pt6ystr, pt7xstr, pt7zstr, pt7ystr, pt8xstr, pt8zstr, pt8ystr, pt9xstr, pt9zstr, pt9ystr, pt10xstr, pt10zstr, pt10ystr, pt11xstr, pt11zstr, pt11ystr, pt12xstr, pt12zstr, pt12ystr, pt13xstr, pt13zstr, pt13ystr,  pt14xstr, pt14zstr, pt14ystr, pt15xstr, pt15zstr, pt15ystr, pt0xstr, pt0zstr, pt0ystr, pt16xstr, pt16zstr, pt16ystr, pt17xstr, pt17zstr, pt17ystr, pt18xstr, pt18zstr, pt18ystr, pt19xstr, pt19zstr, pt19ystr, pt20xstr, pt20zstr, pt20ystr, pt21xstr, pt21zstr, pt21ystr, pt44xstr, pt44zstr, pt44ystr, pt46xstr, pt46zstr, pt46ystr, pt48xstr, pt48zstr, pt48ystr, pt50xstr, pt50ystr, pt50zstr)


    # Compute the initial velocity field
    velocity_dictionary, velocity_floats, k_tot = compute_initial_velocities(Q_100, num_cases_initial)
    # Create velocity strings for files
    velocity_case_names = edit_velocity_strings(velocity_dictionary, k_tot)
    # Solve for strings of case files
    case_full_paths, case_folder_names = create_case_directories(velocity_case_names, k_tot)
    # Add strings for foam file directories--NOT MAKEING DIRS YET
    case_zero_paths, case_system_paths, case_constant_paths = add_foam_directories(case_full_paths, k_tot)
    print("case system paths from main:")
    print(case_system_paths)
    # Creating foam directories in cases
    paste_static_foam_files(case_zero_paths, case_system_paths, case_constant_paths, k_tot)




    # WRITE AND RELOCATE THE CONTROLDICT File
    controldict_template = locate_controldit_template()
    write_controldict_template(controldict_template, start_time, end_time, delta_t, write_interval, write_format, max_co, pt10str, pt11str, pt9str, pt48str, pt44str, pt14str, pt20str, pt6str, pt21str, pt7str, pt46str, pt15str, pt8str, pt50str, pt12str, pt13str)
    controldict_for_run = move_controldict(controldict_template)
    controldict_case_paths = controldict_case_move(controldict_for_run, case_system_paths, k_tot)

    # CREATE ALL THE INITIAL SURROUNDING CASES
    blockmesh_template = locate_blockmesh_template()

    num_cells_int, num_cells_double, num_cells_int_str, num_cells_int_str_concat = compute_num_cells(max_delta_x, pt0x, pt1x)

    write_blockmesh(num_cells_int_str_concat, blockmesh_template, num_cells_int, pt0str, pt1str, pt2str, pt3str, pt4str, pt5str, pt6str, pt7str, pt8str, pt9str, pt10str, pt11str, pt12str, pt13str, pt14str, pt15str, pt16str, pt17str, pt18str, pt19str, pt20str, pt21str, pt22str, pt23str, pt24str, pt25str, pt26str, pt27str, pt28str, pt29str, pt30str, pt31str, pt32str, pt33str, pt34str, pt35str, pt36str, pt37str, pt38str, pt39str, pt40str, pt41str, pt42str, pt43str, pt44str, pt45str, pt46str, pt47str, pt48str, pt49str, pt50str, pt51str)

    # move written blockmesh to the run folder, and the backup empty template to the tmplate directory
    blockmesh_for_run = move_blockmesh(blockmesh_template)






    # Move the blockmesh edited files to the case files
    blockmesh_case_paths = blockmesh_case_move(blockmesh_for_run, case_system_paths, k_tot)

    # Write the details files
    case_details_files = write_details_file(case_zero_paths, velocity_dictionary, k_tot)

    # Edit Boundary condition files
    case_U_files = write_velocity_files(velocity_dictionary, case_zero_paths, Q_primary, k_tot)

    # FILES ARE FULLY DEFINED AT THIS POINT, NOW NEED TO RUN ITERATIVELY, PRIOR TO POST PROCESSING
    



    # Edit the Boundary conditions for the 5 secondary flow cases
    #U_25_RHS_str, U_50_RHS_str, U_100_RHS_str, U_125_RHS_str, U_150_RHS_str, U_25_LHS_str, U_50_LHS_str, U_100_LHS_str, U_125_LHS_str, U_150_LHS_str = compute_velocities(U_100)

    #path_100, path_25, path_50, path_125, path_150 = locate_directories()

    # locate zero directories
    #fname_0_100, fname_0_25, fname_0_50, fname_0_125, fname_0_150, path_0_100, path_0_25, path_0_50, path_0_125, path_0_150 = locate_zero_files(path_100, path_25, path_50, path_125, path_150)

    """ If the files have already been edited, then pass over the edits----THIS IS CRUCIAL"""
    # write the velocity files in the zero folder
    #details_file_25, details_file_50, details_file_100, details_file_125, details_file_150 = write_velocity_files(U_25_RHS_str, U_50_RHS_str, U_100_RHS_str, U_125_RHS_str, U_150_RHS_str, U_25_LHS_str, U_50_LHS_str, U_100_LHS_str, U_125_LHS_str, U_150_LHS_str, path_0_100, path_0_125, path_0_150, path_0_25, path_0_50)

    # edit the boundary conditions
    #U_RHS_25, U_RHS_50, U_RHS_100, U_RHS_125, U_RHS_150, U_LHS_25, U_LHS_50, U_LHS_100, U_LHS_125, U_LHS_150 = edit_boundary_conditions(fname_0_100, fname_0_25, fname_0_50, fname_0_125, fname_0_150, U_25_RHS_str, U_50_RHS_str, U_100_RHS_str, U_125_RHS_str, U_150_RHS_str, U_25_LHS_str, U_50_LHS_str, U_100_LHS_str, U_125_LHS_str, U_150_LHS_str)

    # Edit the controlDict file
    #modify_controlDict(pt10str, pt11str, pt9str, pt48str, pt44str, pt14str, pt20str, pt6str, pt21str, pt7str, pt46str, pt15str, pt8str, pt50str, pt12str, pt13str)

    """At this point, the 25-150 cases are defined.
    This is where running the cases would go"""

    # Navigate to directories in loop, check if the the folder created by the runner exists (if not, initiate the simulation), wait until finished...







    # -----------------------------------POST PROCESSING MODULE-------------------------------------

    """Looping would likely begin here"""
    # pull in the data from files with label "case"
    foamfile_path = find_case_files()

    dir_list, case_list, length_case_list, list_temps, list_velocities = data_import(foamfile_path)

    # pull velocity, temperature, and case data from the case files. Create np array new_recarr
    new_recarr = average_pot_temperature(list_temps, length_case_list, list_velocities, case_list)

    # parse and sort
    array_sorted = parse_and_sort_array(new_recarr, length_case_list)


    # Evaluate the optimal
    T_max, velocity_max, T_max_index, velocity_column, temperature_column = evaluate_optimal(array_sorted, length_case_list)

    # plotting
    plot_variables(array_sorted, T_max, velocity_max, T_max_index, velocity_column, temperature_column)

    # compute neighboring velocities
    v_cases_added, v_cases_total_vector = compute_neighboring_velocities(array_sorted, T_max, velocity_max, T_max_index, length_case_list, velocity_column, temperature_column)


    #---------------------------------------------NEW CASE SETUP---------------------------------


    case_name_list, v_cases_total_vector_string, v_boundary_strings = define_new_case_names(v_cases_total_vector)

    full_case_paths = create_case_directories(case_name_list)

    zero_file_paths, constant_file_paths, system_file_paths = add_templates(full_case_paths)


    edit_details_files(zero_file_paths, v_boundary_strings)

    edit_iterative_boundary_conditions(zero_file_paths, constant_file_paths, system_file_paths, v_boundary_strings)




if __name__ == "__main__":
    main()
