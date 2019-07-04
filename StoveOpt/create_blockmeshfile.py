# -*- coding: utf-8 -*-
"""
Created on Thu Apr 25 11:26:04 2019

@author: Lee
"""

""" Goal is to take inputs from the import_geometry module and edit a blockmesh file template"""
import shutil
from shutil import copyfile
from shutil import copy
import os


def locate_blockmesh_template():
    """the function uses the StoveOpt path and blockmesh template name to open the
    template version of the blockMeshDict file for editing in the system folder

    Args:
    None

    Returns:
    blockmesh_template (str): full file path where blockmesh template lives


    """
    # Current working dir for stove opt master
    path_StoveOpt_master = os.getcwd()
    # Steps to system folder
    dir_steps = "//blockMeshDict_foamfile//template//blockMeshDict_template"
    blockmesh_template = path_StoveOpt_master + dir_steps # location and path name of blockmesh template
    print("blockmesh template located at:")
    print(blockmesh_template)
    return blockmesh_template

#blockmesh_template = locate_blockmesh_template()



def compute_num_cells(max_delta_x, pt0x, pt1x):
    """compute the number of blocks associated with the max_delta_x for the largest spatial step (combustion chamber)

    Args:
    max_delta_x (double): User defined maximum grid spacing.
    pt0x (double): x-coordinate of bottom LHS cookstove combustion chamber
    pt1x (double): x-coordinate of bottom RHS cookstove combustion chamber


    Returns:
    num_cells_int (int): number of cells to be written to the openfoam blockmesh file for entire domain
    num_cells_double (double): number of cells to be written to the openfoam blockmesh file for entire domain BEFORE INT ROUNDING
    num_cells_int_str (str): number of cells to be written to the openfoam blockmesh file for entire domain, converted to string type for f.write
    num_cells_int_str_concat (str): cells formatted for OF
    """

    max_space = abs(pt1x-pt0x) # maximum spatial step in domain defined by coordinates
    num_cells_double = max_space/max_delta_x # unrounded number of cells per block
    num_cells_int = int(round(num_cells_double)) # round to integer value
    num_cells_int_str = str(num_cells_int)
    num_cells_int_str_concat = "(" + num_cells_int_str + " " + num_cells_int_str + " " + num_cells_int_str + ")"

    print("num cells int")
    print(num_cells_int)

    print("num cells int converted to str")
    print(num_cells_int_str)

    print("num cells int str concat")
    print(num_cells_int_str_concat)
    return num_cells_int, num_cells_double, num_cells_int_str, num_cells_int_str_concat

#num_cells_int, num_cells_double, num_cells_int_str, num_cells_int_str_concat = compute_num_cells(max_delta_x, pt0x, pt1x)

def write_blockmesh(num_cells_int_str_concat, blockmesh_template, num_cells_int, pt0str, pt1str, pt2str, pt3str, pt4str, pt5str, pt6str, pt7str, pt8str, pt9str, pt10str, pt11str, pt12str, pt13str, pt14str, pt15str, pt16str, pt17str, pt18str, pt19str, pt20str, pt21str, pt22str, pt23str, pt24str, pt25str, pt26str, pt27str, pt28str, pt29str, pt30str, pt31str, pt32str, pt33str, pt34str, pt35str, pt36str, pt37str, pt38str, pt39str, pt40str, pt41str, pt42str, pt43str, pt44str, pt45str, pt46str, pt47str, pt48str, pt49str, pt50str, pt51str):
    """Open the blockmesh template, edit and move to the Run folder
    Args:
    vertices defined as strings
    blockmesh_template (str): full file path where blockmesh template lives

    Returns:
    block_mesh_run_path (str): file path with the blockmesh file saved for running cases
    """
    with open(blockmesh_template,'r+') as f:
            f.seek(602) #where writing begins
            f.write("convertToMeters 1;"+"\n")
            f.write("\n")
            f.write("vertices"+"\n")
            f.write("("+"\n")

            # Write vertice strings
            f.write(pt0str +'\n')
            f.write(pt1str +'\n')
            f.write(pt2str+'\n')
            f.write(pt3str+'\n')
            f.write(pt4str+'\n')
            f.write(pt5str+'\n')
            f.write(pt6str+'\n')
            f.write(pt7str+'\n')
            f.write(pt8str+'\n')
            f.write(pt9str+'\n')
            f.write(pt10str+'\n')
            f.write(pt11str+'\n')
            f.write(pt12str+'\n')
            f.write(pt13str+'\n')
            f.write(pt14str+'\n')
            f.write(pt15str+'\n')
            f.write(pt16str+'\n')
            f.write(pt17str+'\n')
            f.write(pt18str+'\n')
            f.write(pt19str+'\n')
            f.write(pt20str+'\n')
            f.write(pt21str+'\n')
            f.write(pt22str +'\n')
            f.write(pt23str +'\n')
            f.write(pt24str+'\n')
            f.write(pt25str+'\n')
            f.write(pt26str+'\n')
            f.write(pt27str+'\n')
            f.write(pt28str+'\n')
            f.write(pt29str+'\n')
            f.write(pt30str+'\n')
            f.write(pt31str+'\n')
            f.write(pt32str+'\n')
            f.write(pt33str+'\n')
            f.write(pt34str+'\n')
            f.write(pt35str+'\n')
            f.write(pt36str+'\n')
            f.write(pt37str+'\n')
            f.write(pt38str+'\n')
            f.write(pt39str+'\n')
            f.write(pt40str+'\n')
            f.write(pt41str+'\n')
            f.write(pt42str+'\n')
            f.write(pt43str+'\n')
            f.write(pt44str+'\n')
            f.write(pt45str+'\n')
            f.write(pt46str+'\n')
            f.write(pt47str+'\n')
            f.write(pt48str+'\n')
            f.write(pt49str+'\n')
            f.write(pt50str+'\n')
            f.write(pt51str+'\n')
            f.write("\n")
            f.write(");"+"\n")
            f.write("\n")
            f.write("blocks"+"\n")
            f.write("(")
            f.write("\n")

            # write the blocks, with
            f.write("hex (16 17 39 38 19 18 40 41) " + num_cells_int_str_concat + " " +   "simpleGrading (1 1 1)" + "\n")
            f.write("hex (0 1 23 22 2 3 25 24) " + num_cells_int_str_concat + " " +   "simpleGrading (1 1 1)" + "\n")
            f.write("hex (5 4 26 27 6 7 29 28) " + num_cells_int_str_concat + " " +   "simpleGrading (1 1 1)" + "\n")
            f.write("hex (2 3 25 24 5 4 26 27) " + num_cells_int_str_concat + " " +   "simpleGrading (1 1 1)" + "\n")
            f.write("hex (6 7 29 28 20 21 43 42) " + num_cells_int_str_concat + " " +   "simpleGrading (1 1 1)" + "\n")
            f.write("hex (7 46 47 29 21 15 37 43) " + num_cells_int_str_concat + " " +   "simpleGrading (1 1 1)" + "\n")
            f.write("hex (44 6 28 45 14 20 42 36) " + num_cells_int_str_concat + " " +   "simpleGrading (1 1 1)" + "\n")
            f.write("hex (9 44 45 31 48 14 36 49) " + num_cells_int_str_concat + " " +   "simpleGrading (1 1 1)" + "\n")
            f.write("hex (48 14 36 49 10 11 33 32) " + num_cells_int_str_concat + " " +   "simpleGrading (1 1 1)" + "\n")
            f.write("hex (46 8 30 47 15 50 51 37) " + num_cells_int_str_concat + " " +   "simpleGrading (1 1 1)" + "\n")
            f.write("hex (15 50 51 37 12 13 35 34) " + num_cells_int_str_concat + " " +   "simpleGrading (1 1 1)" + "\n")
            f.write(");" + "\n")
            f.write("\n")

            # edges
            f.write("edges" + "\n")
            f.write("(" + "\n")
            f.write(");" + "\n")
            f.write("\n")

            #Boundaries
            # Fuel
            f.write("boundary" + "\n")
            f.write("(" + "\n")
            f.write("fuel" + "\n")
            f.write("{"+  "\n")
            f.write("type patch;" + "\n")
            f.write("faces" + "\n")
            f.write("(" + "\n")
            f.write("(19 18 40 41)" + "\n" + "(16 17 39 38)" + "\n" + "(38 16 19 41)" + "\n" + "(17 39 40 18)" + "\n")
            f.write(");" + "\n")
            f.write("}" + "\n")

            # Primary air -- will need edits for air tray
            f.write("primary_air"+"\n")
            f.write("{"+"\n")
            f.write("type patch;" + "\n")
            f.write("faces" + "\n")
            f.write("(" + "\n")
            f.write("(0 1 23 22)" + "\n")
            f.write(");" + "\n")
            f.write("}" + "\n")

            #Secondary air RHS
            f.write("Secondary_air_RHS"+ "\n")
            f.write("{"+"\n")
            f.write("type patch;" + "\n")
            f.write("faces" + "\n")
            f.write("(" + "\n")
            f.write("(3 25 26 4)" + "\n")
            f.write(");" + "\n")
            f.write("}" + "\n")

            #Secondary air LHS
            f.write("Secondary_air_LHS" + "\n")
            f.write("{"+"\n")
            f.write("type patch;" + "\n")
            f.write("faces" + "\n")
            f.write("(" + "\n")
            f.write("(2 24 27 5)" + "\n")
            f.write(");" + "\n")
            f.write("}" + "\n")

            #Outlet
            f.write("outlet"+"\n")
            f.write("{"+"\n")
            f.write("type patch;" + "\n")
            f.write("faces" + "\n")
            f.write("(" + "\n")
            f.write("(12 13 35 34)" + "\n" + "(10 11 33 32)" + "\n")
            f.write(");" + "\n")
            f.write("}" + "\n")

            #Stove Body
            f.write("stove_body" + "\n")
            f.write("{"+"\n")
            f.write("type patch;" + "\n")
            f.write("faces" + "\n")
            f.write("(" + "\n")
            f.write("(22 0 2 24)" + "\n" + "(1 23 25 3)" + "\n" + "(5 27 28 6)" + "\n" + "(4 26 29 7)" + "\n" + "(20 21 43 42)" + "\n" + "(14 20 42 36)" + "\n" + "(44 6 28 45)" + "\n" + "(21 15 37 43)" + "\n" + "(7 46 47 29)" + "\n" + "(14 36 33 11)" + "\n" + "(48 49 32 10)" + "\n" + "(9 44 45 31)" + "\n" + "(15 37 34 12)" + "\n" + "(50 51 35 13)" + "\n" + "(46 8 30 47)" + "\n" + "(8 30 51 50)" + "\n" + "(9 31 49 48)" + "\n")
            f.write(");" + "\n")
            f.write("}" + "\n")

            #Empty front and back faces
            f.write("\n")
            f.write("frontAndBack" + "\n")
            f.write("{" + "\n")
            f.write("type empty;" + "\n")
            f.write("faces" + "\n")
            f.write("(" + "\n")
            f.write("(16 17 18 19)" + "\n" + "(38 39 40 41)" + "\n" + "(0 1 3 2)" + "\n" + "(22 23 25 24)" + "\n" + "(2 3 4 5)" + "\n" + "(24 25 26 27)" + "\n" + "(5 4 7 6)" + "\n" + "(27 28 29 26)" + "\n" + "(6 7 21 20)" + "\n" + "(28 29 43 42)" + "\n" + "(44 6 20 14)" + "\n" + "(45 28 42 36)" + "\n" + "(29 47 37 43)" + "\n" + "(7 46 15 21)" + "\n" + "(9 44 14 48)" + "\n" + "(48 14 11 10)" + "\n" + "(31 45 36 49)" + "\n" + "(49 36 33 32)" + "\n" + "(46 8 50 15)" + "\n" + "(15 50 13 12)" + "\n" + "(47 30 51 37)" + "\n" + "(37 51 35 34)" + "\n")
            f.write(");" + "\n")
            f.write("}" + "\n")
            f.write(");" + "\n")
            f.write("\n")
            f.write("mergePatchPairs" + "\n")
            f.write("(" + "\n")
            f.write(");" + "\n")
            f.write("// ************************************************************************* //")

#write_blockmesh(blockmesh_template, num_cells_int, pt0str, pt1str, pt2str, pt3str, pt4str, pt5str, pt6str, pt7str, pt8str, pt9str, pt10str, pt11str, pt12str, pt13str, pt14str, pt15str, pt16str, pt17str, pt18str, pt19str, pt20str, pt21str, pt22str, pt23str, pt24str, pt25str, pt26str, pt27str, pt28str, pt29str, pt30str, pt31str, pt32str, pt33str, pt34str, pt35str, pt36str, pt37str, pt38str, pt39str, pt40str, pt41str, pt42str, pt43str, pt44str, pt45str, pt46str, pt47str, pt48str, pt49str, pt50str, pt51str)

def move_blockmesh(blockmesh_template):
    """purpose is to move the edited blockmesh template to the run folder prior to relocating to the case files. rename the file blockMeshDict for OF convention. Additionally, move the empty template from backup to the template folder
    Args:
    blockmesh_template (str): path where the NOW edited blockmeshDict file lives

    Returns:
    blockmesh_for_run (str): path where the blockMeshDict file for run is located prior to case runs.
    """
    # Running directory
    current_dir = os.getcwd()
    steps_for_run = "//blockMeshDict_foamfile//Run//"
    filename_for_run = "blockMeshDict"
    blockmesh_for_run = current_dir + steps_for_run + filename_for_run #blockmesh to be relocated to the case files

    # backup directory
    steps_for_backup = "//blockMeshDict_foamfile//Backup//"
    filename_for_backup = "blockMeshDict_template_backup"
    blockmesh_for_backup = current_dir + steps_for_backup + filename_for_backup #blockmesh to be relocated to the case files

    copy(blockmesh_template, blockmesh_for_run) # move to running directory
    copy(blockmesh_for_backup, blockmesh_template) # Move the backup blockmeshdict file to the template folder to re-produce original file convention

    return blockmesh_for_run
