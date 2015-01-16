#-*- coding: utf-8 -*-
# Import all neccessary packages
import numpy as np

screenlogging = True




"""============================================================================
Import n Arrays from file. takes list of string values (names)
===============================================================================
"""
def load_nArrays(files):
    i = 0
    while i < len(files):
        files[i] = load_Array(files[i])
        i += 1
    return files



"""============================================================================
Import an Array from file. takes ONE string (name)
===============================================================================
"""
def load_Array(filename):
    if screenlogging == True:
        print ("        Loading: %-65s" %  filename, "Shape: ", end="")
    data = np.loadtxt("../Data/" + filename + ".csv", unpack=True,
                      delimiter=",", skiprows=2)
    if screenlogging == True:
        print (str(data.shape), " DONE!")
    return data



"""============================================================================
============================  WRITE DATA TO FILES  ============================
===============================================================================
"""

"""============================================================================
save a 1D Array to file
===============================================================================
"""
def save_array1D(Arr, filename):
    filename = "../Data/" + filename
    if screenlogging == True:
        print ("        Writing: %-65s" % filename, "Shape: " + str(Arr.shape))
    out = open(filename + ".txt", "wb+")
    i = 0
    while i < len(Arr):
        line = "%e\n" % Arr[i]
        out.write(line)
        i += 1



"""============================================================================
save a 2D Array to file
===============================================================================
"""
def save_array2D(Arr, filename):
    filename = "../Data/" + filename
    if screenlogging == True:
        print ("        Writing: %-65s" % filename, "Shape: " + str(Arr.shape))
    out = open(filename + ".txt", "wb+")
    i = 0
    while i < len(Arr[0]):
        j = 0
        while j < len(Arr):
            line = "%e " % Arr[j][i]
            out.write(line)
            j += 1
        line = "\n"
        out.write(line)
        i += 1


































