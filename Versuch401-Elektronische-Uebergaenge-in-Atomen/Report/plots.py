#-*- coding: utf-8 -*-
import numpy as np
import scipy.optimize as op
import matplotlib.pyplot as plt


"""============================================================================
save a plot under given filename as .pdf as well as .png
===============================================================================
"""
def write_file(filename):
    filename = filename.replace(" ", "")
    filename = filename.replace(":", "")
    filename = filename.replace(".", "_")
    filename = filename.replace("---", "-")
    print "Writing: ", filename
    
    # show small side margins
    plt.margins(0.05, 0.05)
    
    plt.savefig("Figures/" + filename + ".pdf")
    plt.savefig("Figures/" + filename + ".png")

def set_legend(location):
    leg = plt.legend(prop={'size':9}, loc = location, numpoints=1,
                         fancybox=True)
    leg.get_frame().set_alpha(0.5)


"""============================================================================
Useful functions for plotting and fitting
===============================================================================
"""
def reduce_by_min(var):
    i=0
    varmin = min(var)
    while i < len(var):
        var[i] -= varmin
        i += 1
    return var

def gerade(x, m, b):
    y = m*x + b
    return y

def gauss_fkt_1(x, *p0):
    a1, p1, sigma1, y1 = p0
    f1 = a1/(sigma1*np.sqrt(np.pi/2.0)) * np.exp(-2.0*((x-p1)/sigma1)**2.0)+y1
    return f1 

def gauss_fkt_2(x, *p0):
    a1, p1, sigma1, y1, a2, p2, sigma2, y2 = p0
    f1 = a1/(sigma1*np.sqrt(np.pi/2.0)) * np.exp(-2.0*((x-p1)/sigma1)**2.0)+y1
    f2 = a2/(sigma2*np.sqrt(np.pi/2.0)) * np.exp(-2.0*((x-p2)/sigma2)**2.0)+y2
    return f1 +f2

def gauss_fkt_3(x, *p0):
    a1, p1, sigma1, y1, a2, p2, sigma2, y2, a3, p3, sigma3, y3 = p0
    f1 = a1/(sigma1*np.sqrt(np.pi/2.0)) * np.exp(-2.0*((x-p1)/sigma1)**2.0)+y1
    f2 = a2/(sigma2*np.sqrt(np.pi/2.0)) * np.exp(-2.0*((x-p2)/sigma2)**2.0)+y2
    f3 = a3/(sigma3*np.sqrt(np.pi/2.0)) * np.exp(-2.0*((x-p3)/sigma3)**2.0)+y3
    return f1 + f2 + f3

def plot_gaussian1_fit(x, y, ylabel, p0): # ich
    plt.figure()
    
    # gauss fit
    f, varianz = op.curve_fit(gauss_fkt_1, x, y, p0=p0)
    df = np.sqrt(np.sqrt(varianz.diagonal()**2))
    
    fitted_x = np.linspace(np.min(x), np.max(x), 1000)
    fitted_y = gauss_fkt_1(fitted_x, *f)
    
    # Plotte die Originaldaten. Da es Messdaten sind, werden sie nicht mit
    # einer Linie verbunden.
    plt.plot(x, y, ".", label=ylabel)

    # Plotte die Anpassungsfunktion. Diesmal ohne Punkte, aber mit einer Linie.
    plt.plot(fitted_x, fitted_y, label=u"Fit: \nPeak 1  : (%.1f±%.1f)" % 
             (f[1], df[1]) + u"\nFHMW 1: (%.1f±%.1f)" % (f[2], df[2]))
    
    # set axis labels
    plt.title("Versuch 402-2: Winkel - " + ylabel)
    plt.xlabel("Pixel")
    plt.ylabel("Intensitaet")
    
    
    # place a Legend in the plot
    set_legend(1)
    
    # display grid
    plt.grid(True)
    
    # save the plot in file
    filename = Gausstitle + ylabel
    write_file(filename)
    plt.close()
    
    return f, df

def plot_gaussian2_fit(x, y, ylabel, p0): # ich
    plt.figure()
    
    # gauss fit
    f, varianz = op.curve_fit(gauss_fkt_2, x, y, p0=p0)
    df = np.sqrt(np.sqrt(varianz.diagonal()**2))
    
    fitted_x = np.linspace(np.min(x), np.max(x), 1000)
    fitted_y = gauss_fkt_2(fitted_x, *f)
    
    # Plotte die Originaldaten. Da es Messdaten sind, werden sie nicht mit
    # einer Linie verbunden.
    plt.plot(x, y, ".", label=ylabel)

    # Plotte die Anpassungsfunktion. Diesmal ohne Punkte, aber mit einer Linie.
    plt.plot(fitted_x, fitted_y, label=u"Fit: \nPeak 1  : (%.1f±%.1f)" % 
             (f[1], df[1]) + u"\nFHMW 1: (%.1f±%.1f) \nPeak 2  : (%.1f±%.1f)"
             % (f[2], df[2], f[5], df[5]) + u"\nFHMW 2: (%.1f±%.1f)" % 
             (f[6], df[6] ) )
    
    # set axis labels
    plt.title("Versuch 402-2: Winkel - " + ylabel)
    plt.xlabel("Pixel")
    plt.ylabel("Intensitaet")
    
    
    # place a Legend in the plot
    set_legend(1)
    
    # display grid
    plt.grid(True)
    
    # save the plot in file
    filename = Gausstitle + ylabel
    write_file(filename)
    plt.close()
    
    return f, df

def plot_gaussian3_fit(x, y, ylabel, p0): # ich
    plt.figure()
    
    # gauss fit
    f, varianz = op.curve_fit(gauss_fkt_3, x, y, p0=p0)
    df = np.sqrt(np.sqrt(varianz.diagonal()**2))
    
    fitted_x = np.linspace(np.min(x), np.max(x), 1000)
    fitted_y = gauss_fkt_3(fitted_x, *f)
    
    # Plotte die Originaldaten. Da es Messdaten sind, werden sie nicht mit
    # einer Linie verbunden.
    plt.plot(x, y, ".", label=ylabel)

    # Plotte die Anpassungsfunktion. Diesmal ohne Punkte, aber mit einer Linie.
    plt.plot(fitted_x, fitted_y, label=u"Fit: \nPeak 1  : (%.1f±%.1f)" % 
             (f[1], df[1]) + u"\nFHMW 1: (%.1f±%.1f) \nPeak 2  : (%.1f±%.1f)"
             % (f[2], df[2], f[5], df[5]) + u"\nFHMW 2: (%.1f±%.1f)" % 
             (f[6], df[6]) + u"\nPeak 3: (%.1f±%.1f)" % (f[9], df[9]) +
             u"\nFHMW 3  : (%.1f±%.1f)" % (f[10], df[10]))
    
    # set axis labels
    plt.title(Gausstitle + ylabel)
    plt.xlabel(GaussXLabel)
    plt.ylabel(GaussYLabel)
    
    
    # place a Legend in the plot
    set_legend(1)
    
    # display grid
    plt.grid(True)
    
    # save the plot in file
    filename = Gausstitle + ylabel
    write_file(filename)
    plt.close()
    
    return f, df

def plot_data(x, y, title, xlabel, ylabel, plotcolor):
    plt.figure()
    
    # plot y against x 
    plt.plot(x, y, label=ylabel, color=plotcolor)
    
    # set axis labels
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    
    # place a Legend in the plot
    set_legend(1)
    
    # display grid
    plt.grid(True)
    
    # save the plot in file
    filename = title + "_" + xlabel + "_" + ylabel
    write_file(filename)
    plt.close()

def plot_data_error(x, y, title, xlabel, ylabel, yerror, plotcolor):
    plt.figure()
    
    # plot y against x 
    plt.errorbar(x, y, yerror, color=plotcolor, fmt=".")
    
    # set axis labels
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    
    # place a Legend in the plot
    set_legend(1)
    
    # display grid
    plt.grid(True)
    
    # save the plot in file
    filename = title + "_" + xlabel + "_" + ylabel
    write_file(filename)
    plt.close()



"""============================================================================
Plotting RAW data
===============================================================================
"""

def CCD(title, xlabel1, xlabel2, ylabel):
    """========================================================================
    Interferenzmuster aufgenommen mit CCD Kamera
    ===========================================================================
    """
    data = np.loadtxt('Data/CCD_ALL.csv')
    Amps = [0.0, 1.9, 3.0, 3.8, 4.4, 5.1, 6.1, 6.8, 7.5, 8.0, 8.7]
    Pixel = data[:, 0]
    Winkel = data[:, 1]
    Amp = [data[:, 2], data[:, 3], data[:, 4], data[:, 5], data[:, 6],
           data[:, 7],data[:, 8],data[:, 9],data[:, 10], data[:, 11],
           data[:, 12]]
    
    # plot RAW data
    if CCD_Pixel_plotting == 1:
        i = 0
        while i < 11:
            plot_data(Pixel, Amp[i], title + str(Amps[i]) + "A Magnetstrom",
                      xlabel1, ylabel, "red")
            i += 1
            
    if CCD_Winkel_plotting == 1:
        i = 0
        while i < 11:
            plot_data(Winkel, Amp[i], title + str(Amps[i]) + "A Magnetstrom",
                      xlabel2, ylabel,"red")
            i += 1

def FranckHertz(title, xlabel, ylabel):
    """========================================================================
    Franck Hertz Versuch - F�r unterschiedliche Bremsspannungen
    ===========================================================================
    """
    data = np.loadtxt('Data/FH_Bremsspannung.csv')
    Brems = [1.5, 2.0, 2.5, 3.0, 3.5]
    FH_B = [data[:, 0], data[:, 1], data[:, 2], data[:, 3], data[:, 4],
            data[:, 5], data[:, 6], data[:, 7], data[:, 8], data[:, 9]]
    
    """========================================================================
    Franck Hertz Versuch - F�r unterschiedliche Temperaturen
    ===========================================================================
    """
    data = np.loadtxt('Data/FH_Temperatur.csv')
    Temp = [130, 140, 150, 165, 175]
    FH_T = [data[:,0], data[:,1], data[:,2], data[:,3], data[:,4],
            data[:,5], data[:,6], data[:,7], data[:,8], data[:,9]]
    
    
    def SingleRAW():
        i = 0
        while i < 10:
            plot_data(FH_B[i], FH_B[i+1], title + str(Brems[i/2]) +
                      "V Bremsspannung", xlabel, ylabel, "red")
            i += 2
        i = 0
        while i < 10:
            plot_data(FH_T[i], FH_T[i+1], title + str(Temp[i/2])
                      + "C Temperatur", xlabel, ylabel, "red")
            i += 2
    
    """========================================================================
    Franck Hertz Versuch - Vergleiche der unterschiedlichen Bremsspannungen und
    Temperaturen
    ===========================================================================
    """
    
    def Vergleich_B():
        plt.figure()
        
        # plot y against x 
        i = 0
        while i < 10:
            plt.plot(FH_B[i], FH_B[i+1], label="Bremsspannung: " +
                     str(Brems[i/2]) + " V")
            i += 2
        
        # set axis labels
        plt.title(title + "Vergleich Bremsspannungen")
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
        
        # place a Legend in the plot
        set_legend(1)
        
        # display grid
        plt.grid(True)
        
        # save the plot in file
        filename =title + "Vergleich Bremsspannungen"
        write_file(filename)
        plt.close()
    
    def Vergleich_T():
        plt.figure()
        
        # plot y against x 
        i = 0
        while i < 10:
            plt.plot(FH_T[i], FH_T[i+1], label="Temperatur: " +
                     str(Temp[i/2]) + "C")
            i += 2
        
        
        # set axis labels
        plt.title(title + "Vergleich Temperaturen")
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
        
        # place a Legend in the plot
        set_legend(1)
        
        # display grid
        plt.grid(True)
        
        # save the plot in file
        filename = title + "Vergleich Temperaturen"
        write_file(filename)
        plt.close()
    
    def Vergleiche():
        Vergleich_B()
        Vergleich_T()
        
        plt.figure()
        fig, (ax1, ax2) = plt.subplots(2, sharex=True, sharey=True)
        
        # plot y against x 
        i = 0
        while i < 10:
            ax1.plot(FH_B[i], FH_B[i+1], label="Bremsspannung: " +
                     str(Brems[i/2]) + " V")
            i += 2
        
        i = 0
        while i < 10:
            ax2.plot(FH_T[i], FH_T[i+1], label="Temperatur: " +
                     str(Temp[i/2]) + "C")
            i += 2
        
        fig.subplots_adjust(hspace=0)
        
        # set axis labels
        ax1.set_title(title + "Vergleich Bremsspannungen - Temperaturen")
        ax2.set_xlabel(xlabel)
        ax1.set_ylabel(ylabel)
        ax2.set_ylabel(ylabel)
        
        # place a Legend in the plot
        leg1 = ax1.legend(prop={'size':9}, loc = 2, numpoints=1,
                         fancybox=True)
        leg1.get_frame().set_alpha(0.5)
        leg2 = ax2.legend(prop={'size':9}, loc = 2, numpoints=1,
                         fancybox=True)
        leg2.get_frame().set_alpha(0.5)
        
        # display grid
        ax1.grid(True)
        ax2.grid(True)
        
        # save the plot in file
        filename =title + "Vergleich Bremsspannungen - Temperaturen"
        write_file(filename)
        plt.close()
    
    
    if FH_SingleRAW_plotting == 1:
        SingleRAW()
    
    if FH_Vergleiche_plotting == 1:
        Vergleiche()

def Magnetfeld_Kalibrierung(title, xlabel, ylabel):
    """========================================================================
    Kalibrierung des Magnetfeldes
    ===========================================================================
    """
    data = np.loadtxt('Data/Magnetfeld_Kalibrierung.csv')
    MF = [data[:, 0], data[:, 1], data[:, 2], data[:, 3]]
    
    plt.figure()
    
    # plot y against x 
    plt.plot(MF[0], MF[1], label="Erste Messung zu" +
             "\nbeginn des Versuches")
    plt.plot(MF[2], MF[3], label="Zweite Messung nach" +
             "\nAbschluss des Versuches")
    
    # set axis labels
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    
    # place a Legend in the plot
    set_legend(1)
    
    # display grid
    plt.grid(True)
    
    # save the plot in file
    filename = title
    write_file(filename)
    plt.close()



"""============================================================================
Fitting functions, analysing data and calculating stuff
===============================================================================
"""

Gausstitle = ""
GaussXLabel = ""
GaussYLabel = ""

def CCD_ZoomFit(first, last, bottom, top, title, xlabel1, xlabel2, ylabel,
                legendlabel):
    """========================================================================
    Aufspaltung der Interferenzmuster bei angelegtem Magnetfeld.
    Aufgenommen mit der CCD Kamera.
    Ausschnitt vergr��ert
    ===========================================================================
    """
    data = np.loadtxt('Data/CCD_ALL.csv')
    Amps = [0.0, 1.9, 3.0, 3.8, 4.4, 5.1, 6.1, 6.8, 7.5, 8.0, 8.7]
    Pixel = data[first:last, 0]
    Winkel = data[first:last, 1]
    Amp = [data[first:last, 2], data[first:last, 3], data[first:last, 4],
           data[first:last, 5],data[first:last, 6],data[first:last, 7],
           data[first:last, 8],data[first:last, 9],data[first:last, 10],
           data[first:last, 11],data[first:last, 12]]
    
    def ZoomFit(x, y, title, xlabel, ylabel, plotcolor, p0):
        plt.figure()
        
        # gauss fit
        f, varianz = op.curve_fit(gauss_fkt_3, x, y, p0=p0)
        df = np.sqrt(np.sqrt(varianz.diagonal()**2))
        
        fitted_x = np.linspace(np.min(x), np.max(x), 1000)
        fitted_y = gauss_fkt_3(fitted_x, *f)
        
        # Plotte die Originaldaten. Da es Messdaten sind, werden sie nicht mit
        # einer Linie verbunden.
        plt.plot(x, y, ".", label=legendlabel, color=plotcolor)

        # Plotte die Anpassungsfunktion. Diesmal ohne Punkte, aber mit einer Linie.
        plt.plot(fitted_x, fitted_y, label=u"Fit: " + 
                 u"\nPeak 1: (%.1f±%.1f)" % (f[1], df[1]) +
                 u"\nFHMW 1: (%.1f±%.1f)" % (f[2], df[2]) +
                 u"\nPeak 2: (%.1f±%.1f)" % (f[5], df[5]) +
                 u"\nFHMW 2: (%.1f±%.1f)" % (f[6], df[6]) +
                 u"\nPeak 3: (%.1f±%.1f)" % (f[9], df[9]) +
                 u"\nFHMW 3: (%.1f±%.1f)" % (f[10], df[10]))
        
        # set axis labels
        plt.title(title)
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
        
        # set axis limits
        #plt.xlim([first,last])
        plt.ylim([bottom,top])
        
        # place a Legend in the plot
        set_legend(1)
        
        # display grid
        plt.grid(True)
        
        # save the plot in file
        filename = title + "_" + xlabel + "_" + ylabel
        write_file(filename)
        plt.close()
    
    # plot RAW data
    if CCD_ZoomFit_Pixel_plotting == 1:
        CCD_p0 = [40.0, 1210.0, 1.0, 10.0,
                  50.0, 1220.0, 1.0, 10.0,
                  40.0, 1225.0, 1.0, 10.0]
        CCD_p1 = [50.0, 1210.0, 1.0, 15.0,
                  70.0, 1218.0, 1.0, 15.0,
                  50.0, 1225.0, 1.0, 15.0]
        CCD_p2 = [50.0, 1210.0, 1.0, 15.0,
                  70.0, 1218.0, 1.0, 15.0,
                  50.0, 1225.0, 1.0, 15.0]
        CCD_p3 = [50.0, 1210.0, 1.0, 15.0,
                  70.0, 1218.0, 1.0, 15.0,
                  50.0, 1225.0, 1.0, 15.0]
        CCD_p4 = [50.0, 1210.0, 1.0, 30.0,
                  70.0, 1218.0, 1.0, 30.0,
                  50.0, 1225.0, 1.0, 30.0]
        CCD_p5 = [50.0, 1200.0, 1.0, 30.0,
                  70.0, 1220.0, 1.0, 30.0,
                  40.0, 1235.0, 1.0, 30.0]
        CCD_p6 = [50.0, 1195.0, 1.0, 30.0,
                  70.0, 1218.0, 1.0, 30.0,
                  45.0, 1240.0, 1.0, 30.0]
        CCD_p7 = [55.0, 1195.0, 1.0, 30.0,
                  70.0, 1218.0, 1.0, 30.0,
                  45.0, 1240.0, 1.0, 30.0]
        CCD_p8 = [50.0, 1195.0, 1.0, 30.0,
                  70.0, 1218.0, 1.0, 30.0,
                  50.0, 1240.0, 1.0, 30.0]
        CCD_p9 = [50.0, 1195.0, 1.0, 30.0,
                  70.0, 1218.0, 1.0, 30.0,
                  50.0, 1240.0, 1.0, 30.0]
        CCD_p10= [55.0, 1190.0, 1.0, 30.0,
                  75.0, 1220.0, 1.0, 30.0,
                  50.0, 1242.0, 1.0, 30.0]
        CCD_p = [CCD_p0, CCD_p1, CCD_p2, CCD_p3, CCD_p4, CCD_p5, CCD_p6,
                 CCD_p7, CCD_p8, CCD_p9, CCD_p10]
        i = 0
        while i < 11:
            ZoomFit(Pixel, Amp[i], title +
                      str(Amps[i]) + "A Magnetstrom", xlabel1, ylabel, "red",
                      CCD_p[i])
            i += 1
            
    if CCD_ZoomFit_Winkel_plotting == 1:
        CCD_p0 = [40.0, -1.06, 1.0, 10.0,
                  50.0, -1.04, 1.0, 10.0,
                  40.0, -1.02, 1.0, 10.0]
        CCD_p1 = [50.0, -1.08, 1.0, 15.0,
                  60.0, -1.05, 1.0, 15.0,
                  50.0, -1.03, 1.0, 15.0]
        CCD_p2 = [40.0, -1.20, 1.0, 15.0,
                  60.0, -1.00, 1.0, 15.0,
                  50.0, -0.80, 1.0, 15.0]
        CCD_p3 = [50.0, -1.08, 1.0, 15.0,
                  70.0, -1.05, 1.0, 15.0,
                  50.0, -1.02, 1.0, 15.0]
        CCD_p4 = [50.0, -1.08, 1.0, 30.0,
                  70.0, -1.05, 1.0, 30.0,
                  50.0, -1.02, 1.0, 30.0]
        CCD_p5 = [50.0, -1.10, 1.0, 30.0,
                  70.0, -1.05, 1.0, 30.0,
                  40.0, -1.00, 1.0, 30.0]
        CCD_p6 = [50.0, -1.10, 1.0, 30.0,
                  70.0, -1.05, 1.0, 30.0,
                  45.0, -1.00, 1.0, 30.0]
        CCD_p7 = [55.0, -1.10, 1.0, 30.0,
                  70.0, -1.05, 1.0, 30.0,
                  45.0, -1.00, 1.0, 30.0]
        CCD_p8 = [50.0, -1.10, 1.0, 30.0,
                  70.0, -1.05, 1.0, 30.0,
                  50.0, -1.00, 1.0, 30.0]
        CCD_p9 = [50.0, -1.10, 1.0, 30.0,
                  70.0, -1.05, 1.0, 30.0,
                  50.0, -1.00, 1.0, 30.0]
        CCD_p10= [55.0, -1.10, 1.0, 30.0,
                  75.0, -1.05, 1.0, 30.0,
                  50.0, -1.00, 1.0, 30.0]
        CCD_p = [CCD_p0, CCD_p1, CCD_p2, CCD_p3, CCD_p4, CCD_p5, CCD_p6,
                 CCD_p7, CCD_p8, CCD_p9, CCD_p10]
        i = 0
        while i < 11:
            ZoomFit(Winkel, Amp[i], title +
                      str(Amps[i]) + "A Magnetstrom", xlabel2, ylabel,"red",
                      CCD_p[i])
            i += 1



"""============================================================================
MAIN --- running procedures
===============================================================================
"""
# What to do?       0 = Do Not Do It        1 = Do It
CCD_Pixel_plotting = 0
CCD_Winkel_plotting = 0
CCD_ZoomFit_Pixel_plotting = 0
CCD_ZoomFit_Winkel_plotting = 1

FH_SingleRAW_plotting = 0
FH_Vergleiche_plotting = 0

MF_plotting = 0



if CCD_Pixel_plotting == 1 or CCD_Winkel_plotting == 1:
    CCD("Versuch401 - Fabry-Perot-Etalon --- ", "Pixel", "Winkel",
        "Intensitaet")

if CCD_ZoomFit_Pixel_plotting == 1 or CCD_ZoomFit_Winkel_plotting == 1:
    CCD_ZoomFit(1175, 1255, 0, 80, "Versuch401 - FPE Ausschnitt --- ",
                "Pixel", "Winkel", "Intensitaet", "Messwerte")

if FH_SingleRAW_plotting == 1 or FH_Vergleiche_plotting == 1:
    FranckHertz("Versuch401 - Franck-Hertz --- ", "Beschl. Spannung",
                  "Anodenstrom")

if MF_plotting == 1:
    Magnetfeld_Kalibrierung("Versuch401 - Kalibrierung der Magnetfeldes",
                            "Spulenstrom", "Magnetfeld")




#CCD_p0 = [50.0, 830.0, 1.0, 30.0,
                  #70.0, 845.0, 1.0, 30.0,
                  #50.0, 855.0, 1.0, 30.0]
        #CCD_p1 = [50.0, 830.0, 1.0, 30.0,
                  #70.0, 845.0, 1.0, 30.0,
                  #50.0, 855.0, 1.0, 30.0]
        #CCD_p2 = [50.0, 830.0, 1.0, 30.0,
                  #70.0, 845.0, 1.0, 30.0,
                  #50.0, 855.0, 1.0, 30.0]
        #CCD_p3 = [50.0, 830.0, 1.0, 30.0,
                  #70.0, 845.0, 1.0, 30.0,
                  #50.0, 855.0, 1.0, 30.0]
        #CCD_p4 = [50.0, 830.0, 1.0, 30.0,
                  #70.0, 845.0, 1.0, 30.0,
                  #50.0, 855.0, 1.0, 30.0]
        #CCD_p5 = [50.0, 830.0, 1.0, 30.0,
                  #70.0, 845.0, 1.0, 30.0,
                  #50.0, 855.0, 1.0, 30.0]
        #CCD_p6 = [50.0, 825.0, 1.0, 30.0,
                  #70.0, 845.0, 1.0, 30.0,
                  #50.0, 865.0, 1.0, 30.0]
        #CCD_p7 = [50.0, 820.0, 1.0, 30.0,
                  #70.0, 845.0, 1.0, 30.0,
                  #50.0, 865.0, 1.0, 30.0]
        #CCD_p8 = [50.0, 820.0, 1.0, 30.0,
                  #70.0, 845.0, 1.0, 30.0,
                  #50.0, 865.0, 1.0, 30.0]
        #CCD_p9 = [50.0, 820.0, 1.0, 30.0,
                  #70.0, 845.0, 1.0, 30.0,
                  #50.0, 865.0, 1.0, 30.0]
        #CCD_p10= [50.0, 820.0, 1.0, 30.0,
                  #70.0, 845.0, 1.0, 30.0,
                  #50.0, 865.0, 1.0, 30.0]





