# -*- coding: utf-8 -*-
"""
Created on Mon May 13 18:14:56 2019

@author: Lee
"""

def points_to_strings(pt1x, pt1z, pt1y, pt2x, pt2z, pt2y, pt3x, pt3z, pt3y, pt4x, pt4z, pt4y, pt5x, pt5z, pt5y, pt6x, pt6z, pt6y, pt7x, pt7z, pt7y, pt8x, pt8z, pt8y, pt9x, pt9z, pt9y, pt10x, pt10z, pt10y, pt11x, pt11z, pt11y, pt12x, pt12z, pt12y, pt13x, pt13z, pt13y,  pt14x, pt14z, pt14y, pt15x, pt15z, pt15y, pt0x, pt0z, pt0y, pt17x, pt18x, pt19x, pt16x, pt17z, pt18z, pt19z, pt16z, pt17y, pt18y, pt19y, pt16y, pt20x, pt20z, pt20y, pt21x, pt21z, pt21y, pt44x, pt44z, pt44y, pt46x, pt46z, pt46y, pt48x, pt48y, pt48z, pt50x, pt50y, pt50z):
    """
    Take in the raw vertice information from spreadsheet, and format the floats into strings->For front vertices

    Args:
        points (float): all front coordinates

    Returns:
        points as strings (str): Coordinates converted to strings compatible with openfoam convention (length 5).


    """
    pt0xstr= str(pt0x)[:5]
    pt0zstr = str(pt0z)[:5]
    pt0ystr = str(pt0y)[:5]
    pt1xstr= str(pt1x)[:5]
    pt1zstr = str(pt1z)[:5]
    pt1ystr = str(pt1y)[:5]
    pt2xstr= str(pt2x)[:5]
    pt2zstr = str(pt2z)[:5]
    pt2ystr = str(pt2y)[:5]
    pt3xstr= str(pt3x)[:5]
    pt3zstr = str(pt3z)[:5]
    pt3ystr = str(pt3y)[:5]
    pt4xstr= str(pt4x)[:5]
    pt4zstr = str(pt4z)[:5]
    pt4ystr = str(pt4y)[:5]
    pt5xstr= str(pt5x)[:5]
    pt5zstr = str(pt5z)[:5]
    pt5ystr = str(pt5y)[:5]
    pt6xstr= str(pt6x)[:5]
    pt6zstr = str(pt6z)[:5]
    pt6ystr = str(pt6y)[:5]
    pt7xstr= str(pt7x)[:5]
    pt7zstr = str(pt7z)[:5]
    pt7ystr = str(pt7y)[:5]
    pt8xstr= str(pt8x)[:5]
    pt8zstr = str(pt8z)[:5]
    pt8ystr = str(pt8y)[:5]
    pt9xstr= str(pt9x)[:5]
    pt9zstr = str(pt9z)[:5]
    pt9ystr = str(pt9y)[:5]
    pt10xstr= str(pt10x)[:5]
    pt10zstr = str(pt10z)[:5]
    pt10ystr = str(pt10y)[:5]
    pt11xstr= str(pt11x)[:5]
    pt11zstr = str(pt11z)[:5]
    pt11ystr = str(pt11y)[:5]
    pt12xstr= str(pt12x)[:5]
    pt12zstr = str(pt12z)[:5]
    pt12ystr = str(pt12y)[:5]
    pt13xstr= str(pt13x)[:5]
    pt13zstr = str(pt13z)[:5]
    pt13ystr = str(pt13y)[:5]
    pt14xstr= str(pt14x)[:5]
    pt14zstr = str(pt14z)[:5]
    pt14ystr = str(pt14y)[:5]
    pt15xstr= str(pt15x)[:5]
    pt15zstr = str(pt15z)[:5]
    pt15ystr = str(pt15y)[:5]

    pt16xstr= str(pt16x)[:5]
    pt16zstr = str(pt16z)[:5]
    pt16ystr = str(pt16y)[:5]
    pt17xstr= str(pt17x)[:5]
    pt17zstr = str(pt17z)[:5]
    pt17ystr = str(pt17y)[:5]
    pt18xstr= str(pt18x)[:5]
    pt18zstr = str(pt18z)[:5]
    pt18ystr = str(pt18y)[:5]
    pt19xstr= str(pt19x)[:5]
    pt19zstr = str(pt19z)[:5]
    pt19ystr = str(pt19y)[:5]

    pt20xstr= str(pt20x)[:5]
    pt20zstr = str(pt20z)[:5]
    pt20ystr = str(pt20y)[:5]
    pt21xstr= str(pt21x)[:5]
    pt21zstr = str(pt21z)[:5]
    pt21ystr = str(pt21y)[:5]
    pt44xstr= str(pt44x)[:5]
    pt44zstr = str(pt44z)[:5]
    pt44ystr = str(pt44y)[:5]
    pt46xstr= str(pt46x)[:5]
    pt46zstr = str(pt46z)[:5]
    pt46ystr = str(pt46y)[:5]

    pt48xstr= str(pt48x)[:5]
    pt48zstr = str(pt48z)[:5]
    pt48ystr = str(pt48y)[:5]

    pt50xstr= str(pt50x)[:5]
    pt50zstr = str(pt50z)[:5]
    pt50ystr = str(pt50y)[:5]
    return pt1xstr, pt1zstr, pt1ystr, pt2xstr, pt2zstr, pt2ystr, pt3xstr, pt3zstr, pt3ystr, pt4xstr, pt4zstr, pt4ystr, pt5xstr, pt5zstr, pt5ystr, pt6xstr, pt6zstr, pt6ystr, pt7xstr, pt7zstr, pt7ystr, pt8xstr, pt8zstr, pt8ystr, pt9xstr, pt9zstr, pt9ystr, pt10xstr, pt10zstr, pt10ystr, pt11xstr, pt11zstr, pt11ystr, pt12xstr, pt12zstr, pt12ystr, pt13xstr, pt13zstr, pt13ystr,  pt14xstr, pt14zstr, pt14ystr, pt15xstr, pt15zstr, pt15ystr, pt0xstr, pt0zstr, pt0ystr, pt16xstr, pt16zstr, pt16ystr, pt17xstr, pt17zstr, pt17ystr, pt18xstr, pt18zstr, pt18ystr, pt19xstr, pt19zstr, pt19ystr, pt20xstr, pt20zstr, pt20ystr, pt21xstr, pt21zstr, pt21ystr, pt44xstr, pt44zstr, pt44ystr, pt46xstr, pt46zstr, pt46ystr, pt48xstr, pt48zstr, pt48ystr, pt50xstr, pt50zstr, pt50ystr
