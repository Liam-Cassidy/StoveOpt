# Open, edit, and move the control dict file
import shutil
from shutil import copyfile
from shutil import copy
import os


def locate_controldit_template():
    """the function uses the StoveOpt path and controldict template name to open the
    template version of the controldict file for editing in the system folder

    Args:
    None

    Returns:
    controldict_template (str): full file path where controldict template lives
    """
    path_StoveOpt_master = os.getcwd()
    # Steps to system folder
    dir_steps = "//controlDict_foamfile//template//controlDict_template"
    controldict_template = path_StoveOpt_master + dir_steps # location and path name of blockmesh template
    print("controldict template located at:")
    print(controldict_template)
    return controldict_template

#controldict_template = locate_controldit_template()
# For test
start_time = 0
end_time = 5
delta_t =0.001
write_interval = 0.5
write_format = "ascii"
max_co = 0.4


def write_controldict_template(controldict_template, start_time, end_time, delta_t, write_interval, write_format, max_co, pt10str, pt11str, pt9str, pt48str, pt44str, pt14str, pt20str, pt6str, pt21str, pt7str, pt46str, pt15str, pt8str, pt50str, pt12str, pt13str):
    """Open and write to the control dict template
    Args:
    controldict_template (str): full file path where controldict template lives
    start_time (int): Start time for the simulation
    end_time (int): Final time step of the simulation
    delta_t (double): time step of simulation
    write_interval (double): Interval for the file writing
    write_format (str): ascii format for file writing
    max_co (double): maximum courant number assigned

    Returns:
    None
    """

    # Convert the inputs to string
    start_time_str = str(start_time)
    end_time_str = str(end_time)
    delta_t_str = str(delta_t)
    write_interval_str = str(write_interval)
    write_format_str = str(write_format)
    max_co_str = str(max_co)


    with open(controldict_template,'r+') as f:
            f.seek(611) #where writing begins
            f.write("application reactingFoam;" + "\n")
            f.write("\n")
            f.write("startFrom startTime;" +"\n")
            f.write("\n")
            f.write("startTime " + start_time_str + ";" + "\n")
            f.write("\n")
            f.write("stopAt endTime;" + "\n")
            f.write("\n")
            f.write("endTime " + end_time_str + ";" + "\n")
            f.write("\n")
            f.write("deltaT " + delta_t_str + ";" + "\n")
            f.write("\n")
            f.write("writeControl adjustableRunTime;" + "\n")
            f.write("\n")
            f.write("writeInterval " + write_interval_str + ";" + "\n")
            f.write("\n")
            f.write("purgeWrite 0;" + "\n")
            f.write("\n")
            f.write("writeFormat " + write_format_str + ";" + "\n")
            f.write("\n")
            f.write("writePrecision 6;" + "\n")
            f.write("\n")
            f.write("writeCompression off;" +"\n")
            f.write("\n")
            f.write("timeFormat general;" + "\n")
            f.write("\n")
            f.write("timePrecision 6;" + "\n")
            f.write("\n")
            f.write("runTimeModifiable true;" + "\n")
            f.write("\n")
            f.write("adjustTimeStep yes;" + "\n")
            f.write("\n")
            f.write("maxCo " + max_co_str + ";" + "\n")
            f.write("\n")
            f.write("functions" + "\n")
            f.write("{" + "\n")
            f.write("probes" + "\n")
            f.write("{" + "\n")
            f.write("functionObjectLibs ( \"libsampling.so\" );" + "\n")
            f.write("\n")
            f.write("type probes;" + "\n")
            f.write("\n")
            f.write("name probes;" + "\n")
            f.write("\n")
            f.write("outputControl outputTime;" + "\n")
            f.write("outputInterval 1;" + "\n")
            f.write("\n")
            f.write("fields" + "\n")
            f.write("(" + "\n")
            f.write("T" + "\n")
            f.write(");" + "\n")
            f.write("\n")
            f.write("probeLocations" + "\n")
            f.write("(" + "\n")

            # THIS IS WHERE THE VERTICE STRINGS NEED TO GO
            # FOR PURPOSES OF DEVELOPMENT, GOING TO JUST USE THE VALUES FROM THE CONTROLDICT FILES OF OLD
            f.write(pt10str + "\n" + pt11str +"\n" +  pt9str + "\n" + pt48str + "\n" + pt44str + "\n" + pt14str + "\n" + pt20str + "\n" + pt6str + "\n" + pt21str + "\n" + pt7str + "\n" + pt46str + "\n" + pt15str + "\n" + pt8str + "\n" + pt50str + "\n" + pt12str + "\n" + pt13str + "\n")
            f.write(");")

#write_controldict_template(controldict_template, start_time, end_time, delta_t, write_interval, write_format, max_co)



def move_controldict(controldict_template):
    """purpose is to move the edited blockmesh template to the run folder prior to relocating to the case files. rename the file blockMeshDict for OF convention. Additionally, move the empty template from backup to the template folder
    Args:
    controldict_template (str): path where the NOW edited controlDict file lives

    Returns:
    controldict_for_run (str): path where the controlDict file for run is located prior to case runs.
    """
    # Running directory
    current_dir = os.getcwd()
    steps_for_run = "//controlDict_foamfile//Run//"
    filename_for_run = "controlDict"  #Rename
    controldict_for_run = current_dir + steps_for_run + filename_for_run #controlDict to be relocated to the case files

    # backup directory
    steps_for_backup = "//controlDict_foamfile//Backup//"
    filename_for_backup = "controlDict_template_backup"
    controldict_for_backup = current_dir + steps_for_backup + filename_for_backup #blockmesh to be relocated to the case files

    copy(controldict_template, controldict_for_run) # move to running directory
    copy(controldict_for_backup, controldict_template) # Move the backup blockmeshdict file to the template folder to re-produce original file convention

    return controldict_for_run

#controldict_for_run = move_controldict(controldict_template)
