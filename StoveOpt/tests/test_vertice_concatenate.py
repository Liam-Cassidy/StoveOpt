# -*- coding: utf-8 -*-
"""
Created on Tue Apr 23 10:12:40 2019

@author: Lee
"""

# Goal is to make sure that the fuel vertices are the following:
# type = str
# max length = 3x4 (3 coords), + 2(spaces) + 2 parens = 16

def vertice_concatenate(pt1xstr, pt1zstr, pt1ystr, pt2xstr, pt2zstr, pt2ystr, pt3xstr, pt3zstr, pt3ystr, pt4xstr, pt4zstr, pt4ystr, pt5xstr, pt5zstr, pt5ystr, pt6xstr, pt6zstr, pt6ystr, pt7xstr, pt7zstr, pt7ystr, pt8xstr, pt8zstr, pt8ystr, pt9xstr, pt9zstr, pt9ystr, pt10xstr, pt10zstr, pt10ystr, pt11xstr, pt11zstr, pt11ystr, pt12xstr, pt12zstr, pt12ystr, pt13xstr, pt13zstr, pt13ystr,  pt14xstr, pt14zstr, pt14ystr, pt15xstr, pt15zstr, pt15ystr, pt0xstr, pt0zstr, pt0ystr, pt16xstr, pt16zstr, pt16ystr, pt17xstr, pt17zstr, pt17ystr, pt18xstr, pt18zstr, pt18ystr, pt19xstr, pt19zstr, pt19ystr, pt20xstr, pt20zstr, pt20ystr, pt21xstr, pt21zstr, pt21ystr, pt44xstr, pt44zstr, pt44ystr, pt46xstr, pt46zstr, pt46ystr, pt48xstr, pt48zstr, pt48ystr, pt50xstr, pt50zstr, pt50ystr):
    """
    Convert the individual vertex strings and concatenate to the format required for blockmeshdict file

    Args:
        points as strings (str): Coordinates converted to strings compatible with openfoam convention (length 5).

    Returns:
        concatenated front points (str): The x,y,z values of front points concatenated into single vertice location

    """
    # Stove Body
    pt0str = "(" + pt0ystr + " " + pt0xstr + " " + pt0zstr + ")"
    pt1str = "(" + pt1ystr + " " + pt1xstr + " " + pt1zstr + ")"
    pt2str = "(" + pt2ystr + " " + pt2xstr + " " + pt2zstr + ")"
    pt3str = "(" + pt3ystr + " " + pt3xstr + " " + pt3zstr + ")"
    pt4str = "(" + pt4ystr + " " + pt4xstr + " " + pt4zstr + ")"
    pt5str = "(" + pt5ystr + " " + pt5xstr + " " + pt5zstr + ")"
    pt6str = "(" + pt6ystr + " " + pt6xstr + " " + pt6zstr + ")"
    pt7str = "(" + pt7ystr + " " + pt7xstr + " " + pt7zstr + ")"
    pt8str = "(" + pt8ystr + " " + pt8xstr + " " + pt8zstr + ")"
    pt9str = "(" + pt9ystr + " " + pt9xstr + " " + pt9zstr + ")"
    pt10str = "(" + pt10ystr + " " + pt10xstr + " " + pt10zstr + ")"
    pt11str = "(" + pt11ystr + " " + pt11xstr + " " + pt11zstr + ")"
    pt12str = "(" + pt12ystr + " " + pt12xstr + " " + pt12zstr + ")"
    pt13str = "(" + pt13ystr + " " + pt13xstr + " " + pt13zstr + ")"
    pt14str = "(" + pt14ystr + " " + pt14xstr + " " + pt14zstr + ")"
    pt15str = "(" + pt15ystr + " " + pt15xstr + " " + pt15zstr + ")"

    # Wood
    pt16str = "(" + pt16ystr + " " + pt16xstr + " " + pt16zstr + ")"
    pt17str = "(" + pt17ystr + " " + pt17xstr + " " + pt17zstr + ")"
    pt18str = "(" + pt18ystr + " " + pt18xstr + " " + pt18zstr + ")"
    pt19str = "(" + pt19ystr + " " + pt19xstr + " " + pt19zstr + ")"

    # Additional front pts
    pt20str = "(" + pt20ystr + " " + pt20xstr + " " + pt20zstr + ")"
    pt21str = "(" + pt21ystr + " " + pt21xstr + " " + pt21zstr + ")"
    pt44str = "(" + pt44ystr + " " + pt44xstr + " " + pt44zstr + ")"
    pt46str = "(" + pt46ystr + " " + pt46xstr + " " + pt46zstr + ")"
    pt48str = "(" + pt48ystr + " " + pt48xstr + " " + pt48zstr + ")"
    pt50str = "(" + pt50ystr + " " + pt50xstr + " " + pt50zstr + ")"


    return pt0str, pt1str, pt2str, pt3str, pt4str, pt5str, pt6str, pt7str, pt8str, pt9str, pt10str, pt11str, pt12str, pt13str, pt14str, pt15str, pt16str, pt17str, pt18str, pt19str, pt20str, pt21str, pt44str, pt46str, pt48str, pt50str



def test_vertice_concatenate():
    """Create a series of strings ensure they match expected string output--only doing this for a small handful of them"""
    pt1xstr = "0.0"
    pt1zstr = "0.156"
    pt1ystr = "0.77769"
    pt2xstr = "0"
    pt2zstr = "1000"
    pt2ystr = "-1256"
    pt3xstr = "1"
    pt3zstr = "1.00"
    pt3ystr =  "0"
    pt4xstr =  "90"
    pt4zstr = "12"
    pt4ystr = "22"
    pt5xstr = "0.11"
    pt5zstr = "0.76"
    pt5ystr =  "0.00000"
    pt6xstr =  "0.76"
    pt6zstr =  "0.911"
    pt6ystr = "90"
    pt7xstr =  "1000000"
    pt7zstr =  "89"
    pt7ystr =  "0808"
    pt8xstr =  "8787"
    pt8zstr =  "1"
    pt8ystr =  "2"
    pt9xstr =  "0.3"
    pt9zstr = "0.04"
    pt9ystr = "0.005"
    pt10xstr =  "0.006"
    pt10zstr = "7"
    pt10ystr =  "8"
    pt11xstr =  "9999"
    pt11zstr =  "90"
    pt11ystr = "12"
    pt12xstr =  "1"
    pt12zstr =  "0000"
    pt12ystr =  "090"
    pt13xstr =  "1"
    pt13zstr = "1"
    pt13ystr = "1"
    pt14xstr = "1"
    pt14zstr = "1"
    pt14ystr = "1"
    pt15xstr = "1"
    pt15zstr = "1"
    pt15ystr = "1"
    pt0xstr = "1"
    pt0zstr = "1"
    pt0ystr = "1"
    pt16xstr = "1"
    pt16zstr = "1"
    pt16ystr = "1"
    pt17xstr = "1"
    pt17zstr = "1"
    pt17ystr = "1"
    pt18xstr ="1"
    pt18zstr ="1"
    pt18ystr = "1"
    pt19xstr = "1"
    pt19xstr = "1"
    pt19ystr = "1"
    pt19zstr = "1"
    pt19ystr = "1"
    pt20zstr = "1"
    pt20xstr = "1"
    pt20ystr = "1"
    pt21xstr = "1"
    pt21zstr = "1"
    pt21ystr = "1"
    pt44xstr = "1"
    pt44zstr = "1"
    pt44ystr = "1"
    pt46xstr = "1"
    pt46ystr = "1"
    pt46zstr = "1"
    pt48xstr ="1"
    pt48zstr ="1"
    pt48ystr = "1"
    pt50xstr = "1"
    pt50zstr ="1"
    pt50ystr = "1"

    pt0str, pt1str, pt2str, pt3str, pt4str, pt5str, pt6str, pt7str, pt8str, pt9str, pt10str, pt11str, pt12str, pt13str, pt14str, pt15str, pt16str, pt17str, pt18str, pt19str, pt20str, pt21str, pt44str, pt46str, pt48str, pt50str = vertice_concatenate(pt1xstr, pt1zstr, pt1ystr, pt2xstr, pt2zstr, pt2ystr, pt3xstr, pt3zstr, pt3ystr, pt4xstr, pt4zstr, pt4ystr, pt5xstr, pt5zstr, pt5ystr, pt6xstr, pt6zstr, pt6ystr, pt7xstr, pt7zstr, pt7ystr, pt8xstr, pt8zstr, pt8ystr, pt9xstr, pt9zstr, pt9ystr, pt10xstr, pt10zstr, pt10ystr, pt11xstr, pt11zstr, pt11ystr, pt12xstr, pt12zstr, pt12ystr, pt13xstr, pt13zstr, pt13ystr,  pt14xstr, pt14zstr, pt14ystr, pt15xstr, pt15zstr, pt15ystr, pt0xstr, pt0zstr, pt0ystr, pt16xstr, pt16zstr, pt16ystr, pt17xstr, pt17zstr, pt17ystr, pt18xstr, pt18zstr, pt18ystr, pt19xstr, pt19zstr, pt19ystr, pt20xstr, pt20zstr, pt20ystr, pt21xstr, pt21zstr, pt21ystr, pt44xstr, pt44zstr, pt44ystr, pt46xstr, pt46zstr, pt46ystr, pt48xstr, pt48zstr, pt48ystr, pt50xstr, pt50zstr, pt50ystr)

    assert pt0str == "(1 1 1)"
    assert pt1str == "(0.77769 0.0 0.156)"
    assert pt2str == "(-1256 0 1000)" # y x z
    assert pt3str == "(0 1 1.00)"
    assert pt4str == "(22 90 12)" # y x z
    assert pt5str == "(0.00000 0.11 0.76)"
    assert pt6str == "(90 0.76 0.911)"
    assert pt7str == "(0808 1000000 89)"
    assert pt8str == "(2 8787 1)"
    assert pt9str == "(0.005 0.3 0.04)"
    assert pt10str == "(8 0.006 7)"
    assert pt11str == "(12 9999 90)"
    assert pt12str == "(090 1 0000)"
    assert pt13str == "(1 1 1)"
    assert pt14str =="(1 1 1)"
    assert pt15str =="(1 1 1)"
    assert pt16str =="(1 1 1)"
    assert pt17str =="(1 1 1)"
    assert pt18str =="(1 1 1)"
    assert pt19str =="(1 1 1)"
    assert pt20str =="(1 1 1)"
    assert pt21str =="(1 1 1)"
    assert pt44str =="(1 1 1)"
    assert pt46str =="(1 1 1)"
    assert pt48str =="(1 1 1)"
    assert pt50str =="(1 1 1)"
