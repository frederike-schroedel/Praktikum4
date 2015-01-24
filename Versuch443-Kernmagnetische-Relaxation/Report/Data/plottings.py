# -*- coding: utf-8 -*-

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





def ImportData():
    print ("Importing CSV Data...")
    
    files = ["Carr-Purcel/print_032", "Carr-Purcel/print_033",
             "Carr-Purcel/print_034", "Carr-Purcel/print_035",
             "Carr-Purcel/print_036",
             "FID/print_002", "FID/print_028", "FID/print_029",
             "Homogene_Translations_Relaxation/print_030",
             "Homogene_Translations_Relaxation/print_031",
             "Meiboom-Gill/print_037", "Meiboom-Gill/print_038",
             "Meiboom-Gill/print_039", "Meiboom-Gill/print_040",
             "Ohne_Puls/print_003",
             "Rabi/print_004", "Rabi/print_005", "Rabi/print_006",
             "Rabi/print_007", "Rabi/print_008", "Rabi/print_009",
             "Rabi/print_010", "Rabi/print_011", "Rabi/print_012",
             "Rabi/print_013", "Rabi/print_014", "Rabi/print_015",
             "Rabi/print_016", "Rabi/print_017", "Rabi/print_018",
             "Rabi/print_019", "Rabi/print_020", "Rabi/print_021",
             "Rabi/print_022", "Rabi/print_023", "Rabi/print_024",
             "Rabi/print_025", "Rabi/print_026", "Rabi/print_027",
             "Rabi/Rabi_freq1", "Rabi/Rabi_freq2",
             "Roh_Puls/print_000", "Roh_Puls/print_001",
             "Homogene_Translations_Relaxation/HomoTransRelaxHahn",
             "Polarisations_Zurueckgewinnung/Polarisation",
             "Saettigungs_Zurueckgewinnung/Saettigung"]
    
    (p32, p33, p34, p35, p36, p02, p28, p29, p30, p31, p37, p38, p39, p40,
     p03, p04, p05, p06, p07, p08, p09, p10, p11, p12, p13, p14, p15, p16,
     p17, p18, p19, p20, p21, p22, p23, p24, p25, p26, p27,
     Rabi_freq1, Rabi_freq2,
     p00, p01,
     HomoTransRelaxHahn, Polarisation, Saettigung) = dh.load_nArrays(files)
    
    Bilder = [p00, p01, p02, p03, p04, p05, p06, p07, p08, p09, p10, p11, p12,
              p13, p14, p15, p16, p17, p18, p19, p20, p21, p22, p23, p24, p25,
              p26, p27, p28, p29, p30, p31, p32, p33, p34, p35, p36, p37, p38,
              p39, p40]
    Rabi = [Rabi_freq1, Rabi_freq2]
    
    print ("    ======== Done ========\n")
    
    return Bilder, Rabi, HomoTransRelaxHahn, Polarisation, Saettigung




"""========================================================================="""
plt.savefig_pdf = 0
plt.savefig_png = 1

fsize = 13.0
msize = 5.0
opac = 0.8
location = 5


FIDONOFF = 0    # ========== FERTIG ==========
RabiONOFF = 0    # ========== FERTIG ==========
OffsetONOFF = 0    # ========== FERTIG ==========
Roh_PulsONOFF = 0    # ========== FERTIG ==========
SaettigungONOFF = 1    # ========== FERTIG ========== sieht aber scheisse aus und gibt einen overflow
PolarisationONOFF = 1    # ========== FERTIG ========== sieht aber scheisse aus
HomoTransRelaxONOFF = 0    # ========== FERTIG ========== sieht aber scheisse aus

ALLES = 1

if ALLES == 1:
    FIDONOFF = 1
    RabiONOFF = 1
    OffsetONOFF = 1
    Roh_PulsONOFF = 1
    SaettigungONOFF = 1
    PolarisationONOFF = 1
    HomoTransRelaxONOFF = 1



# Import Data
Bild, Rabi, HomoTransRelaxHahn, Polarisation, Saettigung = ImportData()

# Calculate Offset
aveEnv = [np.mean(Bild[3][1]), np.sqrt(np.var(Bild[3][1])/len(Bild[3][1]))]
aveQ   = [np.mean(Bild[3][2]), np.sqrt(np.var(Bild[3][2])/len(Bild[3][2]))]
aveI   = [np.mean(Bild[3][3]), np.sqrt(np.var(Bild[3][3])/len(Bild[3][3]))]


# Offset (ohne pulse)
if OffsetONOFF == 1:
    print ("Offset...")
    
    style = "-"
    location = 1
    
    plt.plot_x3y_averages("Offset", Bild[3][0]*1e6,
                          r"Zeit $/\SI{}{\micro\second}$",
                          Bild[3][1], "Envelope", Bild[3][2], "Q",
                          Bild[3][3], "I",
                          r"Spannung $/\SI{}{\volt}$",
                          r"Bestimmung des Offset -- Messung " +
                          "ohne Puls: " + r"$f=\SI{21.16158}{\mega\hertz}$",
                          style, fsize+3, msize, opac, location, False, False)
    
    print ("    ======== Done ========\n")

# Roh_Puls
if Roh_PulsONOFF == 1:
    print ("Rabi-Oszillation...")
    
    style = "-"
    location = 1
    
    Roh_Puls = [Bild[0], Bild[1]]
    
    i = 0
    while i < len(Roh_Puls):
        plt.plot_x2y("RohPuls" + str(i),
                     Roh_Puls[i][0]*1e6, r"Zeit $/\SI{}{\micro\second}$",
                     Roh_Puls[i][1], "Envelope",
                     Roh_Puls[i][2], "Signal Direkt",
                     r"Magnetisierung $/\SI{}{\volt}$",
                     "Bild des rohen Pulses",
                     style, fsize, msize, opac, location, False, False)
        i += 1
    
    print ("    ======== Done ========\n")

# Rabi-Oszillation
if RabiONOFF == 1:
    print ("Rabi-Oszillation...")
    style = "."
    location = 3
    Rabi_freq1, Rabi_freq2 = Rabi
    
    plt.plot_xy_errorlist("Rabi_freq1",
                          [Rabi_freq1[0], Rabi_freq1[0]],
                          r"$A_{len} / \SI{}{\micro\second}$",
                          [Rabi_freq1[1]-aveEnv[0], Rabi_freq1[3]-aveI[0]],
                          r"Magnetisierung $/\SI{}{\volt}$",
                          [Rabi_freq1[2], Rabi_freq1[4]],
                          ["Envelope", "I"],
                          r"Rabi-Oszillation -- Frequenz: " +
                          r"$\SI{21.16158}{\mega\hertz}$",
                          style, fsize, msize, opac, location, False, False)
    
    plt.plot_xy_errorlist("Rabi_freq2",
                          [Rabi_freq2[0], Rabi_freq2[0]],
                          r"$A_{len} / \SI{}{\micro\second}$",
                          [Rabi_freq2[1]-aveEnv[0], Rabi_freq2[3]-aveI[0]],
                          r"Magnetisierung $/\SI{}{\volt}$",
                          [Rabi_freq2[2], Rabi_freq2[4]],
                          ["Envelope", "I"],
                          r"Rabi-Oszillation -- Frequenz: " +
                          r"$\SI{21.15158}{\mega\hertz}$",
                          style, fsize, msize, opac, location, False, False)
    
    plt.plot_xy_errorlist("Rabi_freq12",
                          [Rabi_freq1[0], Rabi_freq1[0],
                          Rabi_freq2[0], Rabi_freq2[0]],
                          r"$A_{len} / \SI{}{\micro\second}$",
                          [Rabi_freq1[1]-aveEnv[0], Rabi_freq1[3]-aveI[0],
                           Rabi_freq2[1]-aveEnv[0], Rabi_freq2[3]-aveI[0]],
                          r"Magnetisierung $/\SI{}{\volt}$",
                          [Rabi_freq1[2], Rabi_freq1[4],
                           Rabi_freq2[2], Rabi_freq2[4]],
                          [r"Envelope $f=\SI{21.16158}{\mega\hertz}$",
                           r"I $f=\SI{21.16158}{\mega\hertz}$",
                           r"Envelope $f=\SI{21.15158}{\mega\hertz}$",
                           r"I $f=\SI{21.15158}{\mega\hertz}$"],
                          r"Rabi-Oszillation -- Frequenzen: " +
                          r"$\SI{21.16158}{\mega\hertz}$ und " +
                          r"$\SI{21.15158}{\mega\hertz}$",
                          style, fsize, msize, opac, location, False, False)
    
    print ("    ======== Done ========\n")

# Sättigungs Zurückgewinnung
if SaettigungONOFF == 1:
    print ("Sättigungs-Zurückgewinnung...")
    
    style = "."
    location = 5
    
    plt.plot_xy_error("SaettigungsZurueckgewinnung",
                      Saettigung[0],
                      r"Verzögerungszeit $/\SI{}{\milli\second}$",
                      Saettigung[1]-aveEnv[0], r"Magnetisierung $/\SI{}{\volt}$",
                      Saettigung[2], "Envelope",
                      r"Sättigungs -- Zurückgewinnung: " +
                      r"$f=\SI{21.16158}{\mega\hertz}$",
                      style, fsize+3, msize, opac, location, False, False)
    
    print ("    ======== Done ========\n")

# Polarisation Zurückgewinnung
if PolarisationONOFF == 1:
    print ("Polarisations-Zurückgewinnung...")
    
    style = "."
    location = 5
    
    plt.plot_xy_error("PolarisationsZurueckgewinnung",
                      Polarisation[0],
                      r"Verzögerungszeit $/\SI{}{\micro\second}$",
                      Polarisation[1]-aveEnv[0], r"Magnetisierung $/\SI{}{\volt}$",
                      Polarisation[2], "Envelope",
                      r"Polarisations -- Zurückgewinnung: " +
                      r"$f=\SI{21.16158}{\mega\hertz}$",
                      style, fsize+3, msize, opac, location, False, False)
    
    print ("    ======== Done ========\n")

# Homogene Transversale Relaxationszeit
if HomoTransRelaxONOFF == 1:
    print ("Homogene Transversale Relaxationszeit...")
    
    style = "-"
    location = 1
    
    plt.plot_xy_error("HomoTransRelax_Hahn",
                      HomoTransRelaxHahn[0],
                      r"Verzögerungszeit $/\SI{}{\milli\second}$",
                      HomoTransRelaxHahn[1]-aveEnv[0], r"Magnetisierung $/\SI{}{\volt}$",
                      HomoTransRelaxHahn[2], "Envelope",
                      "Homogene Transversale Relaxationszeit $T_2$: " +
                      r"$f=\SI{21.16133}{\mega\hertz}$" +
                      "\nHahn-Spinecho-Sequenz",
                      ".", fsize+3, msize, opac, location, False, False)
    HomoTransRelaxHahn_bsp= [Bild[30], Bild[31]]
    i = 0
    while i < len(HomoTransRelaxHahn_bsp):
        plt.plot_xy("HomoTransRelax_Hahn_beispiel" + str(i),
                     HomoTransRelaxHahn_bsp[i][0]*1e3,
                     r"Zeit $/\SI{}{\milli\second}$",
                     HomoTransRelaxHahn_bsp[i][1]-aveEnv[0], "Envelope",
                     r"Magnetisierung $/\SI{}{\volt}$",
                     "Homogene Transversale Relaxationszeit $T_2$: " +
                     r"$f=\SI{21.16133}{\mega\hertz}$" +
                     "\nHahn-Spinecho-Sequenz: Beispiel %g" % (i+1),
                     style, fsize, msize, opac, location, False, False)
        i += 1
    
    HomoTransRelaxCarr= [Bild[32], Bild[33], Bild[34], Bild[35], Bild[36]]
    tau = [r"$\tau=\SI{1.7}{\micro\second}$",
           r"$\tau=\SI{2.0}{\micro\second}$",
           r"$\tau=\SI{2.6}{\micro\second}$",
           r"$\tau=\SI{2.6}{\micro\second}$",
           r"$\tau=\SI{2.6}{\micro\second}$"]
    zusatzinfo = [r"Verzögerungszeit: ", r"Verzögerungszeit: ",
                  r"Verzögerungszeit: ",
                  r"Z-Gradient invertiert; Verzögerungszeit: ",
                  r"X-Gradient invertiert; Verzögerungszeit: "]
    i = 0
    while i < len(HomoTransRelaxCarr):
        plt.plot_xy_maxfit("HomoTransRelax_Carr" + str(i),
                     HomoTransRelaxCarr[i][0]*1e3,
                     r"Zeit $/\SI{}{\milli\second}$",
                     HomoTransRelaxCarr[i][1]-aveEnv[0], "Envelope",
                     r"Magnetisierung $/\SI{}{\volt}$",
                     "Homogene Transversale Relaxationszeit $T_2$: " +
                     r"$f=\SI{21.16133}{\mega\hertz}$" +
                     "\nCarr-Purcell-Sequenz: " + zusatzinfo[i] + tau[i],
                     style, fsize, msize, opac, location, False, False)
        i += 1
    
    HomoTransRelaxMG= [Bild[37], Bild[38], Bild[39], Bild[40]]
    tau = [r"$\tau=\SI{1.6}{\micro\second}$",
           r"$\tau=\SI{1.6}{\micro\second}$",
           r"$\tau=\SI{3.0}{\micro\second}$",
           r"$\tau=\SI{3.0}{\micro\second}$"]
    zusatzinfo = [r"Ohne MG-Sequenz; Verzögerungszeit: ",
                  r"Mit MG-Sequenz; Verzögerungszeit: ",
                  r"Ohne MG-Sequenz; Verzögerungszeit: ",
                  r"Mit MG-Sequenz; ; Verzögerungszeit: "]
    i = 0
    while i < len(HomoTransRelaxMG):
        plt.plot_xy_maxfit("HomoTransRelax_MG_env" + str(i),
                     HomoTransRelaxMG[i][0]*1e3,
                     r"Zeit $/\SI{}{\milli\second}$",
                     HomoTransRelaxMG[i][1]-aveEnv[0], "Envelope",
                     r"Magnetisierung $/\SI{}{\volt}$",
                     "Homogene Transversale Relaxationszeit $T_2$: " +
                     r"$f=\SI{21.16133}{\mega\hertz}$" +
                     "\nMeiboom-Gill-Sequenz: " + zusatzinfo[i] + tau[i],
                     style, fsize, msize, opac, location, False, False)
        plt.plot_x3y("HomoTransRelax_MG_env_Q_I" + str(i),
                     HomoTransRelaxMG[i][0]*1e3,
                     r"Zeit $/\SI{}{\milli\second}$",
                     HomoTransRelaxMG[i][1]-aveEnv[0], "Envelope",
                     HomoTransRelaxMG[i][2]-aveQ[0], "Q",
                     HomoTransRelaxMG[i][3]-aveI[0], "I",
                     r"Magnetisierung $/\SI{}{\volt}$",
                     "Homogene Transversale Relaxationszeit $T_2$: " +
                     r"$f=\SI{21.16133}{\mega\hertz}$" +
                     "\nMeiboom-Gill-Sequenz: " + zusatzinfo[i] + tau[i],
                     style, fsize, msize, opac, location, False, False)
        i += 1
    
    print ("    ======== Done ========\n")

# FID
if FIDONOFF == 1:
    print ("Free Induction Decay...")
    
    style = "-"
    location = 1
    
    FID = [Bild[2], Bild[28], Bild[29]]
    i = 0
    plt.plot_x3y("FID_env_Q_I" + str(i),
                 FID[i][0]*1e3,
                 r"Zeit $/\SI{}{\milli\second}$",
                 FID[i][1]-aveEnv[0], "Envelope",
                 FID[i][2]-aveQ[0], "Q",
                 FID[i][3]-aveI[0], "I",
                 r"Magnetisierung $/\SI{}{\volt}$",
                 "Free Induction Decay: " +
                 r"$f=\SI{21.16158}{\mega\hertz}$",
                 style, fsize, msize, opac, location, False, False)
    
    i = 1
    while i < len(FID):
        plt.plot_xy_decay("FID_env" + str(i),
                          FID[i][0]*1e3,
                          r"Zeit $/\SI{}{\milli\second}$",
                          FID[i][1]-aveEnv[0], "Envelope",
                          r"Magnetisierung $/\SI{}{\volt}$",
                          "Free Induction Decay: " +
                          r"$f=\SI{21.16133}{\mega\hertz}$",
                          "-", fsize, 2, opac, location, False, False)
        i += 1
    
    print ("    ======== Done ========\n")














