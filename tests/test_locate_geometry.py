# -*- coding: utf-8 -*-
"""
Created on Tue Apr 23 10:06:08 2019

@author: Lee
"""
import tkinter as tk
from tkinter import filedialog

expected_filename = "C:/Oregon_State/Spring_2019/Soft_dev_eng/StoveOpt/stovegeom/Stove_Geometry.xlsx" # Known filename
def test_locate_geometry():
    """ output the file location of stove geometry as a string"""
    root = tk.Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename()
    if file_path == None:
        print("file path is not defined---null. Please retry")
    else: 
        print("File path successfully located")
        print(file_path)
    if file_path == expected_filename:
        print("file names match--pass")
        exp = 1 # 1 indicates the filename matches the expected --in test assert expecation = 1 (pass)
    else:
        exp = 0 # filenames do not match   
    return exp
    assert exp == 1  
test_locate_geometry()
