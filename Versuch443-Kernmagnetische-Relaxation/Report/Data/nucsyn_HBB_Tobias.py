#-*- coding: utf-8 -*-
"""
Program to find the individual Model Numbers of each thermal pulse
"""
#from __future__ import print_function
import sys
import numpy as np
import scipy as sp
import plot_functions as plt
import calculations as calc
import data_handling as dh
import pdfkit
import pyPdf




"""============================================================================
Crutial functions
===============================================================================
"""
# Create evolution plots
def create_Evo_plots():
    (Mod_Nr, Age, Radius_Solar, Temperature_Effective, Lum_Solar, Lum_H,
     Lum_He) = dh.collect_data_plot()
    
    print '    Creating EVOLUTION Plots...'
    
    directory = "Evolution/"
    
    plt.plot_xy(directory + "Mod_LumH",
                Mod_Nr, "Model Number",
                Lum_H, "H Luminosity",
                "Model Number against H Luminosity",
                "-", fsize, msize, opac, location,
                False, False, True)
    plt.plot_xy(directory + "Mod_LumHe",
                Mod_Nr, "Model Number",
                Lum_He, "He Luminosity",
                "Model Number against He Luminosity",
                "-", fsize, msize, opac, location,
                False, False, True)
    plt.plot_xy(directory + "Mod_Rad",
                Mod_Nr, "Model Number",
                Radius_Solar, "Solar Radius",
                "Model Number against Solar Radius",
                "-", fsize, msize, opac, location,
                False, False, True)
    plt.plot_xy(directory + "Mod_Lum",
                Mod_Nr, "Model Number",
                Lum_Solar, "Solar Luminosity",
                "Model Number against Solar Luminosity",
                "-", fsize, msize, opac, location,
                False, False, True)
    plt.plot_xy(directory + "Mod_Temp",
                Mod_Nr, "Model Number",
                Temperature_Effective, "Temperature Effective",
                "Model Number against Temperature",
                "-", fsize, msize, opac, location,
                False, False, True)
    plt.plot_x2y(directory + "Mod_LumH_LumHe",
                 Mod_Nr, "Model Number",
                 Lum_H, "H Luminosity",
                 Lum_He, "He Luminosity",
                 "Model Number against H and He Luminosity",
                "-", fsize, msize, opac, location,
                 False, False, True)
    plt.plot_x3y(directory + "Mod_LumH_LumHe_Lum",
                 Mod_Nr, "Model Number",
                 Lum_H, "H Luminosity",
                 Lum_He, "He Luminosity",
                 Lum_Solar, "Solar Luminosity",
                 "Model Number against H and He and Solar Luminosity",
                "-", fsize, msize, opac, location,
                 False, False, True)
    plt.plot_xy(directory + "Age_LumH",
                Age, "Age", 
                Lum_H, "H Luminosity",
                "Age against H Luminosity",
                "-", fsize, msize, opac, location,
                False, False, True)
    plt.plot_xy(directory + "Age_LumHe",
                Age, "Age",
                Lum_He, "He Luminosity",
                "Age against He Luminosity",
                "-", fsize, msize, opac, location,
                False, False, True)
    plt.plot_xy(directory + "Age_Rad",
                Age, "Age",
                Radius_Solar, "Solar Radius",
                "Age against Solar Radius",
                "-", fsize, msize, opac, location,
                False, False, True)
    plt.plot_xy(directory + "Age_Lum",
                Age, "Age",
                Lum_Solar, "Solar Luminosity",
                "Age against Solar Luminosity",
                "-", fsize, msize, opac, location,
                False, False, True)
    plt.plot_xy(directory + "Age_Temp",
                Age, "Age",
                Temperature_Effective, "Temperature Effective",
                "Age against Temperature",
                "-", fsize, msize, opac, location,
                False, False, True)
    plt.plot_x2y(directory + "Age_LumH_LumHe",
                 Age, "Age",
                 Lum_H, "H Luminosity",
                 Lum_He, "He Luminosity",
                 "Age against H and He Luminosity",
                "-", fsize, msize, opac, location,
                 False, False, True)
    plt.plot_x3y(directory + "Age_LumH_LumHe_Lum",
                 Age, "Age",
                 Lum_H, "H Luminosity",
                 Lum_He, "He Luminosity",
                 Lum_Solar, "Solar Luminosity",
                 "Age against H and He and Solar Luminosity",
                "-", fsize, msize, opac, location,
                 False, False, True)
    
    print '        ==== Done ====\n'

# Create shell plots
def create_Shell_plots():
    print '    Creating SHELL Plots...'
    
    directory = "Shell/"
    
    Mod_Nr, K, P, Density, Temp, Radius, GrGa, Mass = ImportPulseData()
    (K_BCE, P_BCE, Density_BCE, Temp_BCE, Radius_BCE, GrGa_BCE,
     Mass_BCE) = ImportBCEData()
    
    PulseNr, HeFlash, PulseStart, InterpulseStart = dh.load_Array("TPIP")
    
    plt.plot_xy_vlines(directory + "Mod_K_BCE", Mod_Nr, "Model Number",
                       K_BCE, "K BCE",
                       "Model Number against BCE position K",
                       PulseNr, HeFlash, PulseStart, InterpulseStart,
                       ".", fsize, msize, opac, location,
                       False, False, True)
    plt.plot_xy_vlines(directory + "Mod_P_BCE", Mod_Nr, "Model Number",
                       P_BCE, "P BCE",
                       "Model Number against Pressure at BCE",
                       PulseNr, HeFlash, PulseStart, InterpulseStart,
                       ".", fsize, msize, opac, location,
                       False, False, True)
    plt.plot_xy_vlines(directory + "Mod_Density_BCE", Mod_Nr, "Model Number",
                       Density_BCE, "Density BCE",
                       "Model Number against Density at BCE",
                       PulseNr, HeFlash, PulseStart, InterpulseStart,
                       ".", fsize, msize, opac, location,
                       False, False, True)
    plt.plot_xy_vlines(directory + "Mod_Temp_BCE", Mod_Nr, "Model Number",
                       Temp_BCE, "Temperature BCE",
                       "Model Number against Temperature at BCE",
                       PulseNr, HeFlash, PulseStart, InterpulseStart,
                       ".", fsize, msize, opac, location,
                       False, False, True)
    plt.plot_xy_vlines(directory + "Mod_Radius_BCE", Mod_Nr, "Model Number",
                       Radius_BCE, "Radius BCE",
                       "Model Number against Radius of the BCE",
                       PulseNr, HeFlash, PulseStart, InterpulseStart,
                       ".", fsize, msize, opac, location,
                       False, False, True)
    plt.plot_xy_vlines(directory + "Mod_GrGa_BCE", Mod_Nr, "Model Number",
                       GrGa_BCE, "GrGa BCE",
                       "Model Number against GrGa at BCE",
                       PulseNr, HeFlash, PulseStart, InterpulseStart,
                       ".", fsize, msize, opac, location,
                       False, False, True)
    plt.plot_xy_vlines(directory + "BCE_Mod_Mass", Mod_Nr, "Model Number",
                       Mass_BCE, "Mass element",
                       "Massposition of the edge of the convective envelope " +
                       "over Model Number",
                       PulseNr, HeFlash, PulseStart, InterpulseStart,
                       ".", fsize, msize, opac, location, False, False, True)
    
    plt.plot2_xy_list(directory + "Shell_Mass_Density_Temp",
                      np.log10(Mass), "Mass",
                      np.log10(Density), "Density",
                      np.log10(Temp), "Temperature",
                      "Density and Temperature development through shells",
                      -0.075, -0.06, 100, "-", fsize, msize, opac, location,
                      False, False, True)
    
    
    print '        ==== Done ====\n'

# Create ALL Fit parameter plots
def create_all_Parameter_plots():
    print '    Creating ALL PARAMETER Plots...'
    done = True
    
    directory = "Shell/Fitting/Parameters/ALL/ALL_"
    
    (Density_f1, Density_df1, Density_f2, Density_df2,
     Temperature_f1, Temperature_df1, Temperature_f2,
     Temperature_df2) = ImportFITparametersALL()
    
    Mod_Nr = Density_f1[0]
    Age = convert_Mod_Age_list(Mod_Nr)
    
    para1  = ["a1", "b1", "m1", "n1"]
    dpara1 = ["da1", "db1", "dm1", "dn1"]
    para2  = ["a2", "b2", "m2", "n2"]
    dpara2 = ["da2", "db2", "dm2", "dn2"]
    
    i = 1
    while i < len(Density_f1):
        plt.plot2_xy(directory + "Parameters_Mod_Density_" + para1[i-1],
                     Mod_Nr, "Model Number",
                     Density_f1[i], para1[i-1],
                     Density_df1[i], dpara1[i-1],
                     "Fitting parameters for Density",
                     ".", fsize, msize, opac, location, False, False, done)
        plt.plot2_xy(directory + "Parameters_Mod_Density_" + para2[i-1],
                     Mod_Nr, "Model Number",
                     Density_f2[i], para2[i-1],
                     Density_df2[i], dpara2[i-1],
                     "Fitting parameters for Density",
                     ".", fsize, msize, opac, location, False, False, done)
        
        plt.plot2_xy(directory + "Parameters_Mod_Temp_" + para1[i-1],
                     Mod_Nr, "Model Number",
                     Temperature_f1[i], para1[i-1],
                     Temperature_df1[i], dpara1[i-1],
                     "Fitting parameters for Temperature",
                     ".", fsize, msize, opac, location, False, False, done)
        plt.plot2_xy(directory + "Parameters_Mod_Temp_" + para2[i-1],
                     Mod_Nr, "Model Number",
                     Temperature_f2[i], para2[i-1],
                     Temperature_df2[i], dpara2[i-1],
                     "Fitting parameters for Temperature",
                     ".", fsize, msize, opac, location, False, False, done)
        i += 1
    
    i = 1
    while i < len(Density_f1):
        plt.plot2_xy(directory + "Parameters_Age_Density_" + para1[i-1],
                     Age, "Age",
                     Density_f1[i], para1[i-1],
                     Density_df1[i], dpara1[i-1],
                     "Fitting parameters for Density",
                     ".", fsize, msize, opac, location, False, False, done)
        plt.plot2_xy(directory + "Parameters_Age_Density_" + para2[i-1],
                     Age, "Age",
                     Density_f2[i], para2[i-1],
                     Density_df2[i], dpara2[i-1],
                     "Fitting parameters for Density",
                     ".", fsize, msize, opac, location, False, False, done)
        
        plt.plot2_xy(directory + "Parameters_Age_Temp_" + para1[i-1],
                     Age, "Age",
                     Temperature_f1[i], para1[i-1],
                     Temperature_df1[i], dpara1[i-1],
                     "Fitting parameters for Temperature",
                     ".", fsize, msize, opac, location, False, False, done)
        plt.plot2_xy(directory + "Parameters_Age_Temp_" + para2[i-1],
                     Age, "Age",
                     Temperature_f2[i], para2[i-1],
                     Temperature_df2[i], dpara2[i-1],
                     "Fitting parameters for Temperature",
                     ".", fsize, msize, opac, location, False, False, done)
        i += 1
    
    print '        ==== Done ====\n'

# Create INT Fit parameter plots
def create_int_Parameter_plots():
    print '    Creating INT PARAMETER Plots...'
    done = True
    
    directory = "Shell/Fitting/Parameters/INT/INT_"
    
    (Density_f1, Density_df1, Density_f2, Density_df2,
     Temperature_f1, Temperature_df1, Temperature_f2,
     Temperature_df2) = ImportFITparametersINT()
    
    Mod_Nr = Density_f1[0]
    Age = convert_Mod_Age_list(Mod_Nr)
    
    para1  = ["a1", "b1", "m1", "n1"]
    dpara1 = ["da1", "db1", "dm1", "dn1"]
    para2  = ["a2", "b2", "m2", "n2"]
    dpara2 = ["da2", "db2", "dm2", "dn2"]
    
    i = 1
    while i < len(Density_f1):
        plt.plot2_xy(directory + "Parameters_Mod_Density_" + para1[i-1],
                     Mod_Nr, "Model Number",
                     Density_f1[i], para1[i-1],
                     Density_df1[i], dpara1[i-1],
                     "Fitting parameters for Density",
                     ".", fsize, msize, opac, location, False, False, done)
        plt.plot2_xy(directory + "Parameters_Mod_Density_" + para2[i-1],
                     Mod_Nr, "Model Number",
                     Density_f2[i], para2[i-1],
                     Density_df2[i], dpara2[i-1],
                     "Fitting parameters for Density",
                     ".", fsize, msize, opac, location, False, False, done)
        
        #plt.plot2_xy(directory + "Parameters_Mod_Temp_" + para1[i-1],
                     #Mod_Nr, "Model Number",
                     #Temperature_f1[i], para1[i-1],
                     #Temperature_df1[i], dpara1[i-1],
                     #"Fitting parameters for Temperature",
                     #".", fsize, msize, opac, location, False, False, done)
        #plt.plot2_xy(directory + "Parameters_Mod_Temp_" + para2[i-1],
                     #Mod_Nr, "Model Number",
                     #Temperature_f2[i], para2[i-1],
                     #Temperature_df2[i], dpara2[i-1],
                     #"Fitting parameters for Temperature",
                     #".", fsize, msize, opac, location, False, False, done)
        i += 1
    
    #i = 1
    #while i < len(Density_f1):
        #plt.plot2_xy(directory + "Parameters_Age_Density_" + para1[i-1],
                     #Age, "Age",
                     #Density_f1[i], para1[i-1],
                     #Density_df1[i], dpara1[i-1],
                     #"Fitting parameters for Density",
                     #".", fsize, msize, opac, location, False, False, done)
        #plt.plot2_xy(directory + "Parameters_Age_Density_" + para2[i-1],
                     #Age, "Age",
                     #Density_f2[i], para2[i-1],
                     #Density_df2[i], dpara2[i-1],
                     #"Fitting parameters for Density",
                     #".", fsize, msize, opac, location, False, False, done)
        
        #plt.plot2_xy(directory + "Parameters_Age_Temp_" + para1[i-1],
                     #Age, "Age",
                     #Temperature_f1[i], para1[i-1],
                     #Temperature_df1[i], dpara1[i-1],
                     #"Fitting parameters for Temperature",
                     #".", fsize, msize, opac, location, False, False, done)
        #plt.plot2_xy(directory + "Parameters_Age_Temp_" + para2[i-1],
                     #Age, "Age",
                     #Temperature_f2[i], para2[i-1],
                     #Temperature_df2[i], dpara2[i-1],
                     #"Fitting parameters for Temperature",
                     #".", fsize, msize, opac, location, False, False, done)
        #i += 1
    
    print '        ==== Done ====\n'

# Create THIN INT Fit parameter plots
def create_thin_int_Parameter_plots():
    print '    Creating THIN INT PARAMETER Plots...'
    done = True
    
    directory = "Shell/Fitting/Parameters/THIN_INT/THIN_INT_"
    
    (Density_a1, Density_a2, Density_b1, Density_b2, Density_m1, Density_m2,
     Density_n1, Density_n2, Temp_a1, Temp_a2, Temp_b1, Temp_b2, Temp_m1,
     Temp_m2, Temp_n1, Temp_n2) = ImportFITparametersTHININT()
    
    Density_f1 = np.array([Density_a1, Density_b1, Density_m1, Density_n1])
    Density_f2 = np.array([Density_a2, Density_b2, Density_m2, Density_n2])
    Temp_f1 = np.array([Temp_a1, Temp_b1, Temp_m1, Temp_n1])
    Temp_f2 = np.array([Temp_a2, Temp_b2, Temp_m2, Temp_n2])
    
    para1  = ["a1", "b1", "m1", "n1"]
    dpara1 = ["da1", "db1", "dm1", "dn1"]
    para2  = ["a2", "b2", "m2", "n2"]
    dpara2 = ["da2", "db2", "dm2", "dn2"]
    
    i = 0
    while i < len(Density_f1):
        plt.plot2_xy(directory + "Parameters_Mod_Density_" + para1[i],
                     Density_f1[i][0], "Model Number",
                     Density_f1[i][2], para1[i],
                     Density_f1[i][3], dpara1[i],
                     "Fitting parameters for Density",
                     ".", fsize, msize, opac, location, False, False, done)
        plt.plot2_xy(directory + "Parameters_Mod_Density_" + para2[i],
                     Density_f2[i][0], "Model Number",
                     Density_f2[i][2], para2[i],
                     Density_f2[i][3], dpara2[i],
                     "Fitting parameters for Density",
                     ".", fsize, msize, opac, location, False, False, done)
        
        #plt.plot2_xy(directory + "Parameters_Mod_Temp_" + para1[i],
                     #Temp_f1[i][0], "Model Number",
                     #Temp_f1[i][2], para1[i],
                     #Temp_f1[i][3], dpara1[i],
                     #"Fitting parameters for Temperature",
                     #".", fsize, msize, opac, location, False, False, done)
        #plt.plot2_xy(directory + "Parameters_Mod_Temp_" + para2[i],
                     #Temp_f2[i][0], "Model Number",
                     #Temp_f2[i][2], para2[i],
                     #Temp_f2[i][3], dpara2[i],
                     #"Fitting parameters for Temperature",
                     #".", fsize, msize, opac, location, False, False, done)
        i += 1
    
    #i = 0
    #while i < len(Density_f1):
        #plt.plot2_xy(directory + "Parameters_Age_Density_" + para1[i],
                     #Density_f1[i][1], "Age",
                     #Density_f1[i][2], para1[i],
                     #Density_f1[i][3], dpara1[i],
                     #"Fitting parameters for Density",
                     #".", fsize, msize, opac, location, False, False, done)
        #plt.plot2_xy(directory + "Parameters_Age_Density_" + para2[i],
                     #Density_f2[i][1], "Age",
                     #Density_f2[i][2], para2[i],
                     #Density_f2[i][3], dpara2[i],
                     #"Fitting parameters for Density",
                     #".", fsize, msize, opac, location, False, False, done)
        
        #plt.plot2_xy(directory + "Parameters_Age_Temp_" + para1[i],
                     #Temp_f1[i][1], "Age",
                     #Temp_f1[i][2], para1[i],
                     #Temp_f1[i][3], dpara1[i],
                     #"Fitting parameters for Temperature",
                     #".", fsize, msize, opac, location, False, False, done)
        #plt.plot2_xy(directory + "Parameters_Age_Temp_" + para2[i],
                     #Temp_f2[i][1], "Age",
                     #Temp_f2[i][2], para2[i],
                     #Temp_f2[i][3], dpara2[i],
                     #"Fitting parameters for Temperature",
                     #".", fsize, msize, opac, location, False, False, done)
        #i += 1
    
    print '        ==== Done ====\n'

# Create QUAD views
def create_Parameter_quad_plots():
    directory = "../Figures/Shell/Fitting/Parameters/"
        
    options = {
        "quiet":"",
        "orientation":"landscape"
        }
    
    print "        Writing: " + directory + "Parameters_ALL"
    pdfkit.from_file('quadview_ALL.html', directory +
                    'Parameters_ALL.pdf', options=options)
    
    print "        Writing: " + directory + "Parameters_INT"
    pdfkit.from_file('quadview_INT.html', directory +
                    'Parameters_INT.pdf', options=options)
    
    print "        Writing: " + directory + "Parameters_THIN_INT"
    pdfkit.from_file('quadview_INT_THIN.html', directory +
                    'Parameters_THIN_INT.pdf', options=options)

# Import stored Pulse data from "out_TP1-9"
def ImportPulseData():
    print 'Running Function: ImportPulseData...'
    liste = ["Mod_Nr", "K", "P", "Density", "Temp", "Radius", "GrGa", "Mass"]
    Mod_Nr, K, P, Density, Temp, Radius, GrGa, Mass = dh.load_nArrays(liste)
    print '        ==== Done ====\n'
    return Mod_Nr, K, P, Density, Temp, Radius, GrGa, Mass

# Import BCE data from files
def ImportBCEData():
    print 'Running Function: ImportBCEData...'
    liste = ["K_BCE", "P_BCE", "Density_BCE", "Temp_BCE", "Radius_BCE",
             "GrGa_BCE", "Mass_BCE"]
    (K_BCE, P_BCE, Density_BCE, Temp_BCE, Radius_BCE,
     GrGa_BCE, Mass_BCE)= dh.load_nArrays(liste)
    
    print '        ==== Done ====\n'
    return K_BCE, P_BCE, Density_BCE, Temp_BCE, Radius_BCE, GrGa_BCE, Mass_BCE

# Import stored ALL fit parameters from files returning as *_f1 = [a1, b1, m1, n1]
def ImportFITparametersALL():
    print 'Running Function: ImportFITparametersALL...'
    directory = "Shell/Fitting/Density/ALL_"
    liste = ["Density_f1", "Density_df1", "Density_f2", "Density_df2"]
    files = [directory + s for s in liste]
    (Density_f1, Density_df1, Density_f2,
     Density_df2) = dh.load_nArrays(files)
    
    directory = "Shell/Fitting/Temperature/ALL_"
    liste = ["Temperature_f1", "Temperature_df1", "Temperature_f2",
             "Temperature_df2"]
    files = [directory + s for s in liste]
    (Temperature_f1, Temperature_df1, Temperature_f2,
     Temperature_df2) = dh.load_nArrays(files)
    
    print '        ==== Done ====\n'
    return (Density_f1, Density_df1, Density_f2, Density_df2,
            Temperature_f1, Temperature_df1, Temperature_f2, Temperature_df2)

# Import stored INTERPULSE fit parameters from files returning as *_f1 = [a1, b1, m1, n1]
def ImportFITparametersINT():
    print 'Running Function: ImportFITparametersINT...'
    directory = "Shell/Fitting/Density/INT/INT_"
    liste = ["Density_f1", "Density_df1", "Density_f2", "Density_df2"]
    files = [directory + s for s in liste]
    (Density_f1, Density_df1, Density_f2,
     Density_df2) = dh.load_nArrays(files)
    
    directory = "Shell/Fitting/Temperature/INT/INT_"
    liste = ["Temperature_f1", "Temperature_df1", "Temperature_f2",
             "Temperature_df2"]
    files = [directory + s for s in liste]
    (Temperature_f1, Temperature_df1, Temperature_f2,
     Temperature_df2) = dh.load_nArrays(files)
    
    print '        ==== Done ====\n'
    return (Density_f1, Density_df1, Density_f2, Density_df2,
            Temperature_f1, Temperature_df1, Temperature_f2, Temperature_df2)

# Import stored THIN INTERPULSE fit parameters from files returning as *_f1 = [a1, b1, m1, n1]
def ImportFITparametersTHININT():
    print 'Running Function: ImportFITparametersTHININT...'
    directory ="Shell/Fitting/Parameters/THIN_INT/THIN_INT_Parameters_Density_"
    liste = ["a1", "a2", "b1", "b2", "m1", "m2", "n1", "n2"]
    files = [directory + s for s in liste]
    (Density_a1, Density_a2, Density_b1, Density_b2, Density_m1, Density_m2,
     Density_n1, Density_n2) = dh.load_nArrays(files)
    
    directory = "Shell/Fitting/Parameters/THIN_INT/THIN_INT_Parameters_Temp_"
    liste = ["a1", "a2", "b1", "b2", "m1", "m2", "n1", "n2"]
    files = [directory + s for s in liste]
    (Temp_a1, Temp_a2, Temp_b1, Temp_b2, Temp_m1, Temp_m2, Temp_n1,
     Temp_n2) = dh.load_nArrays(files)
    
    print '        ==== Done ====\n'
    return (Density_a1, Density_a2, Density_b1, Density_b2, Density_m1,
            Density_m2, Density_n1, Density_n2,
            Temp_a1, Temp_a2, Temp_b1, Temp_b2, Temp_m1, Temp_m2, Temp_n1,
            Temp_n2)

# Import Pulse positions from files
def ImportPulsePositions():
    print 'Running Function: ImportPulsePositions...'
    (PulseNr, HeFlash, PulseStart, InterpulseStart) = dh.load_Array("TPIP")
    print '        ==== Done ====\n'
    return (PulseNr, HeFlash, PulseStart, InterpulseStart)

# Convert ONE Model Number into Age
def convert_Mod_Age_single(Mod):
    data = np.loadtxt('../Data/plot_TP1-9')
    Mod_Nr = data[:, 0]
    Age = data[:, 1]
    
    i = 0
    while i < len(Mod_Nr):
        if Mod_Nr[i] == Mod:
            Age_of_Mod = Age[i]
            break
        i += 1
    
    return Age_of_Mod

# Convert list of Model Number into Age
def convert_Mod_Age_list(Mod):
    data = np.loadtxt('../Data/plot_TP1-9')
    Mod_Nr = data[:, 0]
    Age = data[:, 1]
    Age_of_Mod = []
    
    i = 0
    while i < len(Mod):
        j = 0
        while j < len(Mod_Nr):
            if Mod_Nr[j] == Mod[i]:
                Age_of_Mod.append(Age[j])
                break
            j += 1
        i += 1
    
    return Age_of_Mod




"""============================================================================
What to run...
===============================================================================
"""
# PLOTS and FORMATS
Evo_plots = 0
Shell_plots = 0
plt.savefig_pdf = 0
plt.savefig_png = 1

# Legend and Settings
fsize = 11.0
msize = 5.0
opac = 0.5
location = 1
save_every = 10

# Limits
upperMassLimit = -1.5
lowerMassLimit = -4.1

# PULSE FINDING
PulseFinding = 1    # FERTIG

# DATA FINDING or COLLECTING
CollectPulseData = 0    # FERTIG

# FITTINGS
p0_Density_ALL = [2.0, -3.0, -0.01, -5.0,       2.0, -3.0, -0.01, -5.0]
p0_Temp_ALL    = [2.0, -2.0, -0.01,  5.0,       2.0, -2.0, -0.01,  5.0]
FitPlot_polytrops_ALL_RAW = 0
FitPlot_polytrops_ALL = 0   # FERTIG --- TAKES VERY VERY VERY LONG.....

p0_Density_INT = [4.0, -2.70, -0.50, -3.00,     1.90, -2.27, -0.5, -6.00]
p0_Temp_INT    = [2.50, -2.5, -0.16,  6.60,      2.40, -2.22, -0.25,  4.96]
FitPlot_polytrops_INT_Density = 0
FitPlot_polytrops_INT_Temp = 0
Cloud_FIT_Density = 0
Cloud_FIT_Temp = 0

# DATA MANIPULATING i.e. Thinning out the fitted parameters
Thinning_Threshold = [[1e-1, 1e-1, 1e-1, 1e-1], [1e-1, 1e-1, 1e-1, 1e-1],
                      [1e-1, 1e-2, 1e-1, 5e-3], [1e-1, 1e-2, 1e-1, 5e-3]]
Thinout_INT = 0
Pre_ReFit_Plot_polytrops_INT_RAW = 0    # --- TAKES VERY VERY VERY LONG.....
Pre_ReFit_Plot_polytrops_THININT_Density = 0
Pre_ReFit_Plot_polytrops_THININT_Temp = 0

# DATA PLOTTING
Parameters_plots_ALL = 0
Parameters_plots_INT = 0
Parameters_plots_INT_THIN = 0
Parameter_Distribution_plot_ALL = 0
Parameter_Distribution_plot_Density = 0
Parameter_Distribution_plot_Temp = 0
png_to_pdf = 0

# SCREENLOGGING
screenlogging = True
calc.screenlogging = screenlogging
dh.screenlogging   = screenlogging
plt.screenlogging  = screenlogging


"""============================================================================
Running procedures
===============================================================================
"""
# Find locations of all the pulses through all Models
if PulseFinding == 1:
    print 'Running Function: Find_PulseInterpulse...'
    (Mod_Nr_plot, Age, Radius_Solar, Temperature_Effective, Lum_Solar, Lum_H,
     Lum_He) = dh.collect_data_plot()
    TPP_i,TPP_Mod,IPP_i,IPP_Mod = calc.Find_PulseInterpulse(Mod_Nr_plot,
                                                            Lum_H, Lum_He,
                                                            screenlogging)
    print '    ======== Done ========\n'

# Collect data from "out_TP1-9" and store it in seperate array files
if CollectPulseData == 1:
    print 'Running Function: Collect_PulseData...'
    (Mod_Nr, K, P, Density, Temp, Radius, GrGa, Mass) = dh.collect_PulseData()
    print '    ======== Done ========\n'
    
    print 'Running Function: FindBCEdata...'
    (K_BCE, P_BCE, Density_BCE, Temp_BCE, Radius_BCE, GrGa_BCE,
     Mass_BCE) = dh.CollectBCEData(K, P, Density, Temp, Radius, GrGa, Mass)
    print '    ======== Done ========\n'

# Plot elemental Plots
if Evo_plots == 1 or Shell_plots == 1:
    if Evo_plots == 1:
        print 'Running Function: create_Evo_plots...'
        create_Evo_plots()
        print '    ======== Done ========\n'
    
    if Shell_plots == 1:
        print 'Running Function: create_Shell_plots...'
        create_Shell_plots()
        print '    ======== Done ========\n'



# Plot and fit all shells
if FitPlot_polytrops_ALL == 1 or FitPlot_polytrops_ALL_RAW == 1:
    print 'Running Function: FitPlot_polytrops_ALL...'
    done = True
    
    fsize = 12
    msize = 5
    opac = 0.5
    location = 3
    
    Mod_Nr, K, P, Density, Temp, Radius, GrGa, Mass = ImportPulseData()
    (K_BCE, P_BCE, Density_BCE, Temp_BCE, Radius_BCE, GrGa_BCE,
     Mass_BCE) = ImportBCEData()
    
    if FitPlot_polytrops_ALL_RAW == 1:
        directory = "Shell/Fitting/Density/RAW/"
        calc.FindPlt_Conv(directory, "RAW_Density", Mod_Nr, Mass, Density,
                            "Density", Mass_BCE,
                            ".", fsize, msize, opac, location,
                            False, False, done)
        
        directory = "Shell/Fitting/Temperature/RAW/"
        calc.FindPlt_Conv(directory, "Raw_Temp", Mod_Nr, Mass, Temp,
                            "Temperature", Mass_BCE,
                            ".", fsize, msize, opac, location,
                            False, False, done)
    
    if FitPlot_polytrops_ALL == 1:
        directory = "Shell/Fitting/Density/ALL"
        p0 = p0_Density_ALL
        p = calc.Find_Ks_all(directory, "/FIT_Density", Mod_Nr, Mass,
                            Density, "Density", save_every,
                            Mass_BCE, lowerMassLimit, upperMassLimit,
                            p0,
                            fsize, msize, opac, location, False, False, done)
        
        directory = "Shell/Fitting/Temperature/ALL"
        p0 = p0_Temp_ALL
        p = calc.Find_Ks_all(directory, "/FIT_Temp", Mod_Nr, Mass, Temp,
                            "Temperature", save_every,
                            Mass_BCE, lowerMassLimit, upperMassLimit,
                            p0,
                            fsize, msize, opac, location, False, False, done)



# Fit Polytrops to Density and Temperature to determine K. plot K and dK
if (FitPlot_polytrops_INT_Density == 1 or FitPlot_polytrops_INT_Temp == 1):
    done = True
    
    fsize = 12
    msize = 5
    opac = 0.5
    location = 3
    
    Mod_Nr, K, P, Density, Temp, Radius, GrGa, Mass = ImportPulseData()
    (K_BCE, P_BCE, Density_BCE, Temp_BCE, Radius_BCE, GrGa_BCE,
     Mass_BCE) = ImportBCEData()
    
    if FitPlot_polytrops_INT_Density == 1:
        print 'Running Function: Fit_polytrops_plottingDensity_Interpulse...'
        
        p0 = p0_Density_INT
        
        directory = "Shell/Fitting/Density/INT/"
        p = calc.Find_Ks_Interpulse(directory, "FIT_Density", Mod_Nr, Mass,
                                    Density, "Density",
                                    Mass_BCE, lowerMassLimit, upperMassLimit,
                                    p0,
                                    fsize, msize, opac, location,
                                    False, False, done)
        
        print '    ======== Done ========\n'
    
    if FitPlot_polytrops_INT_Temp == 1:
        print 'Running Function: Fit_polytrops_plottingTemp_Interpulse...'
        
        p0 = p0_Temp_INT
        
        directory = "Shell/Fitting/Temperature/INT/"
        p = calc.Find_Ks_Interpulse(directory, "FIT_Temp", Mod_Nr, Mass,
                                    Temp, "Temperature",
                                    Mass_BCE, lowerMassLimit, upperMassLimit,
                                    p0,
                                    fsize, msize, opac, location,
                                    False, False, done)
        
        print '    ======== Done ========\n'
    
    print "Updating Parameter log files..."
    
    # get fitted Parameters for Density and Temperature
    #PARAMETERS = ImportFITparametersINT()
    #(Density_f1, Density_df1, Density_f2, Density_df2, Temp_f1, Temp_df1,
     #Temp_f2, Temp_df2) = PARAMETERS
    
    #f_D = []
    #df_D = []
    #f_T = []
    #df_T = []
    #i = 0
    #while i < len(Density_f1[0]):
        #f_D.append([Density_f1[1][i], Density_f1[2][i], Density_f1[3][i],
                    #Density_f1[4][i], Density_f2[1][i], Density_f2[2][i],
                    #Density_f2[3][i], Density_f2[4][i]])
        #df_D.append([Density_df1[1][i], Density_df1[2][i], Density_df1[3][i],
                     #Density_df1[4][i], Density_df2[1][i], Density_df2[2][i],
                     #Density_df2[3][i], Density_df2[4][i]])
        #f_T.append([Temp_f1[1][i], Temp_f1[2][i], Temp_f1[3][i],
                    #Temp_f1[4][i], Temp_f2[1][i], Temp_f2[2][i],
                    #Temp_f2[3][i], Temp_f2[4][i]])
        #df_T.append([Temp_df1[1][i], Temp_df1[2][i], Temp_df1[3][i],
                     #Temp_df1[4][i], Temp_df2[1][i], Temp_df2[2][i],
                     #Temp_df2[3][i], Temp_df2[4][i]])
        #i += 1
    
    #directory = "Shell/Fitting/Parameters/"
    #dh.save_array2D(np.array(f_D).T, directory +
                    #"CombinedParameters_Density_f")
    #dh.save_array2D(np.array(df_D).T, directory +
                    #"CombinedParameters_Density_df")
    #dh.save_array2D(np.array(f_T).T, directory +
                    #"CombinedParameters_Temp_f")
    #dh.save_array2D(np.array(df_T).T, directory +
                    #"CombinedParameters_Temp_df")
    
    print '    ======== Done ========\n'



# Thin out the fitting parameters
if Thinout_INT == 1:
    print 'Running Function: Thinout_INT...'
    done = True
    
    directory = "Shell/Fitting/Parameters/THIN_INT/THIN_INT_"
    
    PARAMETERS = ImportFITparametersINT()
    (Density_f1, Density_df1, Density_f2, Density_df2, Temp_f1, Temp_df1,
     Temp_f2, Temp_df2) = PARAMETERS
    
    Mod_Nr = PARAMETERS[0][0]
    Age = convert_Mod_Age_list(Mod_Nr)
    
    label  = ["Density_f1", "Density_f2", "Temperature_f1", "Temperature_f2"]
    para1  = ["a1", "b1", "m1", "n1"]
    dpara1 = ["da1", "db1", "dm1", "dn1"]
    para2  = ["a2", "b2", "m2", "n2"]
    dpara2 = ["da2", "db2", "dm2", "dn2"]
    
    # Plots against Model Number
    i = 1
    while i < len(Density_f1):
        THIN_PARAMETERS = dh.thinout_limit(Density_f1[i], Density_df1[i],
                                           Mod_Nr, Age,
                                           Thinning_Threshold[0][i-1],
                                           label[i-1] + para1[i-1])
        dh.save_array2D(THIN_PARAMETERS,
                        directory + "Parameters_Density_" + para1[i-1])
        (newDensity_mod, newDensity_age, newDensity_f1,
         newDensity_df1) = THIN_PARAMETERS
        
        THIN_PARAMETERS = dh.thinout_limit(Density_f2[i], Density_df2[i],
                                           Mod_Nr, Age,
                                           Thinning_Threshold[1][i-1],
                                           label[i-1] + para2[i-1])
        dh.save_array2D(THIN_PARAMETERS,
                        directory + "Parameters_Density_" + para2[i-1])
        (newDensity_f2, newDensity_df2, newDensity_mod,
         newDensity_age) = THIN_PARAMETERS
        #       <--- Density    ****|****   Temperature --->
        #THIN_PARAMETERS = dh.thinout_limit(Temp_f1[i], Temp_df1[i],
                                           #Mod_Nr, Age,
                                           #Thinning_Threshold[2][i-1],
                                           #label[i-1] + para1[i-1])
        #dh.save_array2D(THIN_PARAMETERS,
                        #directory + "Parameters_Temp_" + para1[i-1])
        #(newTemp_f1, newTemp_df1, newTemp_mod,
         #newTemp_age) = THIN_PARAMETERS
        
        #THIN_PARAMETERS = dh.thinout_limit(Temp_f2[i], Temp_df2[i],
                                           #Mod_Nr, Age,
                                           #Thinning_Threshold[3][i-1],
                                           #label[i-1] + para2[i-1])
        #dh.save_array2D(THIN_PARAMETERS,
                        #directory + "Parameters_Temp_" + para2[i-1])
        #(newTemp_f2, newTemp_df2, newTemp_mod,
         #newTemp_age) = THIN_PARAMETERS
        i += 1
    
    print '    ======== Done ========\n'
    
    # save average parameters
    print "Saving average THIN INT parameters..."
    # Thin fit parameters
    (Density_a1, Density_a2, Density_b1, Density_b2, Density_m1, Density_m2,
     Density_n1, Density_n2, Temp_a1, Temp_a2, Temp_b1, Temp_b2, Temp_m1,
     Temp_m2, Temp_n1, Temp_n2) = ImportFITparametersTHININT()
    
    directory = "Shell/Fitting/Parameters/THIN_INT/"
    
    # define initial fit parameters from thin arrays
    D_a1 = np.mean(Density_a1[2])
    D_b1 = np.mean(Density_b1[2])
    D_m1 = np.mean(Density_m1[2])
    D_n1 = np.mean(Density_n1[2])
    D_a2 = np.mean(Density_a2[2])
    D_b2 = np.mean(Density_b2[2])
    D_m2 = np.mean(Density_m2[2])
    D_n2 = np.mean(Density_n2[2])
    D_da1 = np.sqrt(np.var(Density_a1[2])/len(Density_a1[2]))
    D_db1 = np.sqrt(np.var(Density_b1[2])/len(Density_b1[2]))
    D_dm1 = np.sqrt(np.var(Density_m1[2])/len(Density_m1[2]))
    D_dn1 = np.sqrt(np.var(Density_n1[2])/len(Density_n1[2]))
    D_da2 = np.sqrt(np.var(Density_a2[2])/len(Density_a2[2]))
    D_db2 = np.sqrt(np.var(Density_b2[2])/len(Density_b2[2]))
    D_dm2 = np.sqrt(np.var(Density_m2[2])/len(Density_m2[2]))
    D_dn2 = np.sqrt(np.var(Density_n2[2])/len(Density_n2[2]))
    p0_D = np.array([D_a1, D_b1, D_m1, D_n1, D_a2, D_b2, D_m2, D_n2])
    p0_dD = np.array([D_da1, D_db1, D_dm1, D_dn1, D_da2, D_db2, D_dm2,
                    D_dn2])
    p0_DdD = np.array([p0_D, p0_dD])
    
    dh.save_array2D(p0_DdD, directory + "Average_THIN_Parameters_Density")

    T_a1 = np.mean(Temp_a1[2])
    T_b1 = np.mean(Temp_b1[2])
    T_m1 = np.mean(Temp_m1[2])
    T_n1 = np.mean(Temp_n1[2])
    T_a2 = np.mean(Temp_a2[2])
    T_b2 = np.mean(Temp_b2[2])
    T_m2 = np.mean(Temp_m2[2])
    T_n2 = np.mean(Temp_n2[2])
    T_da1 = np.sqrt(np.var(Temp_a1[2])/len(Temp_a1[2]))
    T_db1 = np.sqrt(np.var(Temp_b1[2])/len(Temp_b1[2]))
    T_dm1 = np.sqrt(np.var(Temp_m1[2])/len(Temp_m1[2]))
    T_dn1 = np.sqrt(np.var(Temp_n1[2])/len(Temp_n1[2]))
    T_da2 = np.sqrt(np.var(Temp_a2[2])/len(Temp_a2[2]))
    T_db2 = np.sqrt(np.var(Temp_b2[2])/len(Temp_b2[2]))
    T_dm2 = np.sqrt(np.var(Temp_m2[2])/len(Temp_m2[2]))
    T_dn2 = np.sqrt(np.var(Temp_n2[2])/len(Temp_n2[2]))
    p0_T = np.array([T_a1, T_b1, T_m1, T_n1, T_a2, T_b2, T_m2, T_n2])
    p0_dT = np.array([T_da1, T_db1, T_dm1, T_dn1, T_da2, T_db2, T_dm2,
                    T_dn2])
    p0_TdT = np.array([p0_T, p0_dT])
    
    dh.save_array2D(p0_TdT, directory + "Average_THIN_Parameters_Temperature")
    
    print '    ======== Done ========\n'

# ReFit the Function
if (Pre_ReFit_Plot_polytrops_THININT_Density == 1 or Pre_ReFit_Plot_polytrops_THININT_Temp == 1 or Pre_ReFit_Plot_polytrops_INT_RAW == 1):
    print 'Running Function: Pre_ReFit_Plot_polytrops...'
    done = True
    
    fsize = 12
    msize = 5
    opac = 0.5
    location = 3
    
    # import data to fit to
    Mod_Nr, K, P, Density, Temp, Radius, GrGa, Mass = ImportPulseData()
    (K_BCE, P_BCE, Density_BCE, Temp_BCE, Radius_BCE, GrGa_BCE,
     Mass_BCE) = ImportBCEData()
    
    # get fitted Parameters for Density and Temperature
    PARAMETERS = ImportFITparametersINT()
    (Density_f1, Density_df1, Density_f2, Density_df2, Temp_f1, Temp_df1,
     Temp_f2, Temp_df2) = PARAMETERS
    
    # Thin fit parameters
    (Density_a1, Density_a2, Density_b1, Density_b2, Density_m1, Density_m2,
     Density_n1, Density_n2, Temp_a1, Temp_a2, Temp_b1, Temp_b2, Temp_m1,
     Temp_m2, Temp_n1, Temp_n2) = ImportFITparametersTHININT()
    
    # ReFit it for the Density
    if Pre_ReFit_Plot_polytrops_INT_RAW == 1:
        print 'Running Function: Pre_ReFit_Plot_polytrops_plottingRAW_INT...'
        
        # define initial fit parameters from thin arrays
        i = 0
        while i < len(Density_f1[0]):
            D_a1 = Density_f1[1][i] #Density_a1[2][i] #np.mean(Density_a1[2])
            D_b1 = Density_f1[2][i] #Density_b1[2][i] #np.mean(Density_b1[2])
            D_m1 = Density_f1[3][i] #Density_m1[2][i] #np.mean(Density_m1[2])
            D_n1 = Density_f1[4][i] #Density_n1[2][i] #np.mean(Density_n1[2])
            D_a2 = Density_f2[1][i] #Density_a2[2][i] #np.mean(Density_a2[2])
            D_b2 = Density_f2[2][i] #Density_b2[2][i] #np.mean(Density_b2[2])
            D_m2 = Density_f2[3][i] #Density_m2[2][i] #np.mean(Density_m2[2])
            D_n2 = Density_f2[4][i] #Density_n2[2][i] #np.mean(Density_n2[2])
            D_da1 = Density_df1[1][i] #Density_a1[3][i] #np.mean(Density_a1[3])
            D_db1 = Density_df1[2][i] #Density_b1[3][i] #np.mean(Density_b1[3])
            D_dm1 = Density_df1[3][i] #Density_m1[3][i] #np.mean(Density_m1[3])
            D_dn1 = Density_df1[4][i] #Density_n1[3][i] #np.mean(Density_n1[3])
            D_da2 = Density_df2[1][i] #Density_a2[3][i] #np.mean(Density_a2[3])
            D_db2 = Density_df2[2][i] #Density_b2[3][i] #np.mean(Density_b2[3])
            D_dm2 = Density_df2[3][i] #Density_m2[3][i] #np.mean(Density_m2[3])
            D_dn2 = Density_df2[4][i] #Density_n2[3][i] #np.mean(Density_n2[3])
            p0_D = np.array([D_a1, D_b1, D_m1, D_n1, D_a2, D_b2, D_m2, D_n2])
            p0_dD = np.array([D_da1, D_db1, D_dm1, D_dn1, D_da2, D_db2, D_dm2,
                            D_dn2])
            p0_DdD = np.array([p0_D, p0_dD])

            T_a1 = Temp_f1[1][i] #Temp_a1[2][i] #np.mean(Temp_a1[2])
            T_b1 = Temp_f1[2][i] #Temp_b1[2][i] #np.mean(Temp_b1[2])
            T_m1 = Temp_f1[3][i] #Temp_m1[2][i] #np.mean(Temp_m1[2])
            T_n1 = Temp_f1[4][i] #Temp_n1[2][i] #np.mean(Temp_n1[2])
            T_a2 = Temp_f2[1][i] #Temp_a2[2][i] #np.mean(Temp_a2[2])
            T_b2 = Temp_f2[2][i] #Temp_b2[2][i] #np.mean(Temp_b2[2])
            T_m2 = Temp_f2[3][i] #Temp_m2[2][i] #np.mean(Temp_m2[2])
            T_n2 = Temp_f2[4][i] #Temp_n2[2][i] #np.mean(Temp_n2[2])
            T_da1 = Temp_df1[1][i] #Temp_a1[3][i] #np.mean(Temp_a1[3])
            T_db1 = Temp_df1[2][i] #Temp_b1[3][i] #np.mean(Temp_b1[3])
            T_dm1 = Temp_df1[3][i] #Temp_m1[3][i] #np.mean(Temp_m1[3])
            T_dn1 = Temp_df1[4][i] #Temp_n1[3][i] #np.mean(Temp_n1[3])
            T_da2 = Temp_df2[1][i] #Temp_a2[3][i] #np.mean(Temp_a2[3])
            T_db2 = Temp_df2[2][i] #Temp_b2[3][i] #np.mean(Temp_b2[3])
            T_dm2 = Temp_df2[3][i] #Temp_m2[3][i] #np.mean(Temp_m2[3])
            T_dn2 = Temp_df2[4][i] #Temp_n2[3][i] #np.mean(Temp_n2[3])
            p0_T = np.array([T_a1, T_b1, T_m1, T_n1, T_a2, T_b2, T_m2, T_n2])
            p0_dT = np.array([T_da1, T_db1, T_dm1, T_dn1, T_da2, T_db2, T_dm2,
                            T_dn2])
            p0_TdT = np.array([p0_T, p0_dT])
            
            directory = "Shell/Fitting/Density/Pre_ReFit/" + str(i) + "/"
            plt.Pre_ReFit_plots(directory, "Pre_ReFIT_Density", Mod_Nr, Mass,
                                Density, "Density",
                                Mass_BCE, lowerMassLimit, upperMassLimit,
                                p0_DdD[0], p0_DdD[1],
                                fsize, msize, opac, location,
                                False, False, done)
            
            directory = "Shell/Fitting/Temperature/Pre_ReFit/" + str(i) + "/"
            plt.Pre_ReFit_plots(directory, "Pre_ReFIT_Temperature", Mod_Nr,
                                Mass, Temp, "Temperature",
                                Mass_BCE, lowerMassLimit, upperMassLimit,
                                p0_TdT[0], p0_TdT[1],
                                fsize, msize, opac, location,
                                False, False, done)
            
            i += 1
        
        print '    ======== Done ========\n'
    
    # ReFit it for the Density
    if Pre_ReFit_Plot_polytrops_THININT_Density == 1:
        print 'Running Function: Pre_ReFit_Plot_polytrops_plotting_INT...'
        
        p0_DdD = dh.load_Array("Shell/Fitting/Parameters/THIN_INT/" +
                               "Average_THIN_Parameters_Density")
        
        directory = "Shell/Fitting/Density/"
        plt.ReFit_Combiplot(directory, "ReFIT_Combiplot_Density", Mod_Nr, Mass,
                            Density, "Density",
                            Mass_BCE, lowerMassLimit, upperMassLimit,
                            p0_DdD[0], p0_DdD[1],
                            "Overview: All Density Data-Sets as one cloud " +
                            "with Average Function",
                            fsize, 1, opac, location,
                            False, False, done)
        directory = "Shell/Fitting/Density/ReFit/"
        plt.Pre_ReFit_plots(directory, "ReFIT_Density", Mod_Nr, Mass,
                            Density, "Density",
                            Mass_BCE, lowerMassLimit, upperMassLimit,
                            p0_DdD[0], p0_DdD[1],
                            fsize, msize, opac, location,
                            False, False, done)
        
        print '    ======== Done ========\n'
    
    if Pre_ReFit_Plot_polytrops_THININT_Temp == 1:
        print 'Running Function: Pre_ReFit_Plot_polytrops_plotting_INT...'
        
        p0_TdT = dh.load_Array("Shell/Fitting/Parameters/THIN_INT/" +
                               "Average_THIN_Parameters_Temperature")
        
        directory = "Shell/Fitting/Temperature/"
        plt.ReFit_Combiplot(directory, "ReFIT_Combiplot_Temperature", Mod_Nr,
                            Mass, Temp, "Temperature",
                            Mass_BCE, lowerMassLimit, upperMassLimit,
                            p0_TdT[0], p0_TdT[1],
                            "Overview: All Temperature Data-Sets as one cloud"+
                            " with Average Function",
                            fsize, 1, opac, location,
                            False, False, done)
        directory = "Shell/Fitting/Temperature/ReFit/"
        plt.Pre_ReFit_plots(directory, "ReFIT_Temperature", Mod_Nr,
                            Mass, Temp, "Temperature",
                            Mass_BCE, lowerMassLimit, upperMassLimit,
                            p0_TdT[0], p0_TdT[1],
                            fsize, msize, opac, location,
                            False, False, done)
        
        print '    ======== Done ========\n'
    
    print '    ======== Done ========\n'



# Fit to CLOUD of Data-Sets
if Cloud_FIT_Density == 1 or Cloud_FIT_Temp == 1:
    done = True
        
    fsize = 12
    msize = 5
    opac = 0.5
    location = 3

    Mod_Nr, K, P, Density, Temp, Radius, GrGa, Mass = ImportPulseData()
    (K_BCE, P_BCE, Density_BCE, Temp_BCE, Radius_BCE, GrGa_BCE,
    Mass_BCE) = ImportBCEData()
    
    
    if Cloud_FIT_Density == 1:
        print 'Running Function: Cloud_FIT_Density...'
        
        p0 = p0_Density_INT

        directory = "Shell/Fitting/Density/CLOUD/"
        f, df = calc.Find_Ks_Interpulse_Cloud(directory, "Cloud_FIT_Density",
                                              Mod_Nr, Mass, Density, "Density",
                                              Mass_BCE,
                                              lowerMassLimit, upperMassLimit,
                                              p0,
                                              fsize, msize, opac, location,
                                              False, False, done)
        
        print '    ======== Done ========\n'
    
    if Cloud_FIT_Temp == 1:
        print 'Running Function: Cloud_FIT_Temp...'
        
        p0 = p0_Temp_INT
        
        directory = "Shell/Fitting/Temperature/CLOUD/"
        f, df = calc.Find_Ks_Interpulse_Cloud(directory, "Cloud_FIT_Temp",
                                              Mod_Nr, Mass, Temp,
                                              "Temperature", Mass_BCE,
                                              lowerMassLimit, upperMassLimit,
                                              p0,
                                              fsize, msize, opac, location,
                                              False, False, done)
        
        print '    ======== Done ========\n'



# Plot Parameters from the fitting Function
if Parameters_plots_ALL == 1 or Parameters_plots_INT == 1 or Parameters_plots_INT_THIN == 1 or png_to_pdf == 1:
    if Parameters_plots_ALL == 1:
        print 'Running Function: create_all_Parameter_plots...'
        create_all_Parameter_plots()
        print '    ======== Done ========\n'
        
    if Parameters_plots_INT == 1:
        print 'Running Function: create_int_Parameter_plots...'
        create_int_Parameter_plots()
        print '    ======== Done ========\n'
        
    if Parameters_plots_INT_THIN == 1:
        print 'Running Function: create_thin_int_Parameter_plots...'
        create_thin_int_Parameter_plots()
        print '    ======== Done ========\n'
        
    if png_to_pdf == 1:
        print 'Running Function: create_Parameter_quad_plots...'
        create_Parameter_quad_plots()
        print '    ======== Done ========\n'

# plot parameter distribution in one plot
if Parameter_Distribution_plot_ALL == 1 or Parameter_Distribution_plot_Density == 1 or Parameter_Distribution_plot_Temp == 1:
    done = True
    
    fsize = 10
    msize = 4
    opac = 0.5
    location = 3
    
    para = ["a1", "b1", "m1", "n1", "a2", "b2", "m2", "n2"]
    directory = "Shell/Fitting/Parameters/"
    
    if Parameter_Distribution_plot_ALL == 1:
        (ALL_Density_f1, ALL_Density_df1, ALL_Density_f2, ALL_Density_df2,
        ALL_Temp_f1, ALL_Temp_df1, ALL_Temp_f2,
        ALL_Temp_df2) = ImportFITparametersALL()
        
        plt.plot_Parameter_Dist_ALL(directory + "ParameterDistribution_ALL" +
                                    "_Density",
                                    ALL_Density_f1[1], ALL_Density_f1[2],
                                    ALL_Density_f1[3], ALL_Density_f1[4],
                                    ALL_Density_f2[1], ALL_Density_f2[2],
                                    ALL_Density_f2[3], ALL_Density_f2[4],
                                    para,
                                    "Distribution of fitting parameters " +
                                    "for Density",
                                    ".", fsize, msize, opac, location,
                                    False, False, done)
        plt.plot_Parameter_Dist_ALL(directory + "ParameterDistribution_ALL" +
                                    "_Temperature",
                                    ALL_Temp_f1[1], ALL_Temp_f1[2],
                                    ALL_Temp_f1[3], ALL_Temp_f1[4],
                                    ALL_Temp_f2[1], ALL_Temp_f2[2],
                                    ALL_Temp_f2[3], ALL_Temp_f2[4],
                                    para,
                                    "Distribution of fitting parameters " +
                                    "for Temperature",
                                    ".", fsize, msize, opac, location,
                                    False, False, done)
    
    if Parameter_Distribution_plot_Density == 1:
        PARAMETERS = ImportFITparametersINT()
        (Density_f1, Density_df1, Density_f2, Density_df2, Temp_f1, Temp_df1,
        Temp_f2, Temp_df2) = PARAMETERS
        
        # Thin fit parameters
        (Density_a1, Density_a2, Density_b1, Density_b2, Density_m1, Density_m2,
        Density_n1, Density_n2, Temp_a1, Temp_a2, Temp_b1, Temp_b2, Temp_m1,
        Temp_m2, Temp_n1, Temp_n2) = ImportFITparametersTHININT()
        
        plt.plot_Parameter_Dist_INT(directory + "ParameterDistribution_INT" +
                                    "_Density",
                                    Density_f1[1], Density_f1[2],
                                    Density_f1[3], Density_f1[4],
                                    Density_f2[1], Density_f2[2],
                                    Density_f2[3], Density_f2[4],
                                    Density_a1[2], Density_b1[2],
                                    Density_m1[2], Density_n1[2],
                                    Density_a2[2], Density_b2[2],
                                    Density_m2[2], Density_n2[2],
                                    para,
                                    "Distribution of fitting parameters " +
                                    "for Density",
                                    ".", fsize, msize, opac, location,
                                    False, False, done)
    
    if Parameter_Distribution_plot_Temp == 1:
        PARAMETERS = ImportFITparametersINT()
        (Density_f1, Density_df1, Density_f2, Density_df2, Temp_f1, Temp_df1,
        Temp_f2, Temp_df2) = PARAMETERS
        
        # Thin fit parameters
        (Density_a1, Density_a2, Density_b1, Density_b2, Density_m1, Density_m2,
        Density_n1, Density_n2, Temp_a1, Temp_a2, Temp_b1, Temp_b2, Temp_m1,
        Temp_m2, Temp_n1, Temp_n2) = ImportFITparametersTHININT()
        
        plt.plot_Parameter_Dist_INT(directory + "ParameterDistribution_INT" +
                                    "_Temperature",
                                    Temp_f1[1], Temp_f1[2],
                                    Temp_f1[3], Temp_f1[4],
                                    Temp_f2[1], Temp_f2[2],
                                    Temp_f2[3], Temp_f2[4],
                                    Temp_a1[2], Temp_b1[2], Temp_m1[2],
                                    Temp_n1[2], Temp_a2[2], Temp_b2[2],
                                    Temp_m2[2], Temp_n2[2],
                                    para,
                                    "Distribution of fitting parameters " +
                                    "for Temperature",
                                    ".", fsize, msize, opac, location,
                                    False, False, done)




































