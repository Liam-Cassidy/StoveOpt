# -*- coding: utf-8 -*-
"""
Created on Tue Jun 18 11:50:39 2019

@author: Lee
"""
import yaml

def pull_input_data(input_file):
    """
    Goal is to convert the geometry file argument to working syntax: Single quote, back slash

    Args:

        args (dictionary): Object contains the contents of the input file specified by the user

    """

    with open(input_file, 'r') as f:
        doc = yaml.load(f)
        path = doc['case']['geometry_file_directory'] # pulling path
        fname = doc['case']['geometry_file_name'] #pulling filename
        Q_100 = doc['case']['secondary_air_flow_rate'] # 100% flow rate [m^3/s]
        Q_primary = doc['case']['primary_air_flow_rate'] # maximum primary airflow rate
        max_delta_x = doc['case']['max_grid_spacing'] # maximum grid spacing selected [m]
        delta_t = doc['case']['time_step'] # time step for simulation
        temporal_choice = doc['case']['temporal'] # choice for eithe ss or transient
        n_cases_surr = doc['case']['number_intial_surrounding_cases'] # number of cases to be run surrounding the 100% flow
        ss_tol = doc['case']['ss_tolerance'] # Tolerance for iteration convergence
        OS = doc['case']['OS'] # operating system of the user. Used for fpath manipulation

    return path, fname, Q_100, Q_primary, max_delta_x, delta_t, temporal_choice, n_cases_surr, ss_tol, OS


def test_pullInputData():
    """Write a test input.yaml file for pulling data (set the file equal to "args"). Assert values"""
    input_file = "//mnt//c//Oregon_State//Spring_2019//Soft_dev_eng//StoveOpt//StoveOpt//tests//input_test_1.yaml"
    path, fname, Q_100, Q_primary, max_delta_x, delta_t, temporal_choice, n_cases_surr, ss_tol, OS = pull_input_data(input_file)
    assert path == "/mnt/c/Oregon_State/Spring_2019/Soft_dev_eng/StoveOpt/StoveOpt/tests/"
    assert fname == "Stove_test_Geometry.xlsx"
    assert Q_100 == 100
    assert Q_primary == 20
    assert max_delta_x == 0.01
    assert delta_t == 0.0001
    assert temporal_choice == "STEADY"
    assert n_cases_surr == 7
    assert ss_tol == 0.001
    assert OS == "LINUX"
