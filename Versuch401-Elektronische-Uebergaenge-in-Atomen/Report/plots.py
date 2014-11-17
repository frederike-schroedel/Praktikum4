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
    filename = filename.replace("'", "")
    filename = filename.replace(".", "_")
    filename = filename.replace("---", "-")
    print "Writing: ", filename
    
    # show small side margins
    plt.margins(0.05, 0.05)
    
    if savefig_pdf == 1:
        plt.savefig("Figures/" + filename + ".pdf")
    
    if savefig_png == 1:
        plt.savefig("Figures/" + filename + ".png")

def set_legend(location):
    leg = plt.legend(prop={'size':9}, loc = location, numpoints=1,
                         fancybox=True)
    leg.get_frame().set_alpha(0.7)

def set_log_axis(x, y):
    if x == True:
        plt.xscale('log')
    if y == True:
        plt.yscale('log')

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

def polynom3(x, *p0):
    (a, b, c, d) = p0
    y = a*x**3 + b*x**2 + c*x + d
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

def gauss_fkt_2x3(x, *p0):
    (a1, p1, sigma1, a2, p2, sigma2, a) = p0
    f1 = a1/(sigma1*np.sqrt(np.pi/2.0)) * np.exp(-2.0*((x-p1)/sigma1)**2.0)
    f2 = a2/(sigma2*np.sqrt(np.pi/2.0)) * np.exp(-2.0*((x-p2)/sigma2)**2.0)
    f3 = a*x**3
    return f1 + f2 + f3

def gauss_fkt_3x3(x, *p0):
    (a1, p1, sigma1, a2, p2, sigma2, a3, p3, sigma3, a) = p0
    f1 = a1/(sigma1*np.sqrt(np.pi/2.0)) * np.exp(-2.0*((x-p1)/sigma1)**2.0)
    f2 = a2/(sigma2*np.sqrt(np.pi/2.0)) * np.exp(-2.0*((x-p2)/sigma2)**2.0)
    f3 = a3/(sigma3*np.sqrt(np.pi/2.0)) * np.exp(-2.0*((x-p3)/sigma3)**2.0)
    f4 = a*x**3
    return f1 + f2 + f3 + f4

def gauss_fkt_4x3(x, *p0):
    (a1, p1, sigma1, a2, p2, sigma2, a3, p3, sigma3, a4, p4, sigma4, a) = p0
    f1 = a1/(sigma1*np.sqrt(np.pi/2.0)) * np.exp(-2.0*((x-p1)/sigma1)**2.0)
    f2 = a2/(sigma2*np.sqrt(np.pi/2.0)) * np.exp(-2.0*((x-p2)/sigma2)**2.0)
    f3 = a3/(sigma3*np.sqrt(np.pi/2.0)) * np.exp(-2.0*((x-p3)/sigma3)**2.0)
    f4 = a4/(sigma4*np.sqrt(np.pi/2.0)) * np.exp(-2.0*((x-p4)/sigma4)**2.0)
    f5 = a*x**3
    return f1 + f2 + f3 + f4 +f5

def gauss_fkt_5x3(x, *p0):
    (a1, p1, sigma1, a2, p2, sigma2, a3, p3, sigma3, a4, p4, sigma4, a5, p5,
     sigma5, a) = p0
    f1 = a1/(sigma1*np.sqrt(np.pi/2.0)) * np.exp(-2.0*((x-p1)/sigma1)**2.0)
    f2 = a2/(sigma2*np.sqrt(np.pi/2.0)) * np.exp(-2.0*((x-p2)/sigma2)**2.0)
    f3 = a3/(sigma3*np.sqrt(np.pi/2.0)) * np.exp(-2.0*((x-p3)/sigma3)**2.0)
    f4 = a4/(sigma4*np.sqrt(np.pi/2.0)) * np.exp(-2.0*((x-p4)/sigma4)**2.0)
    f5 = a5/(sigma5*np.sqrt(np.pi/2.0)) * np.exp(-2.0*((x-p5)/sigma5)**2.0)
    f6 = a*x**3
    return f1 + f2 + f3 + f4 +f5 +f6

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

def plot_data(x, y, title, xlabel, xunit, ylabel, yunit, plotcolor):
    plt.figure()
    
    # plot y against x 
    plt.plot(x, y, label=ylabel, color=plotcolor)
    
    # set axis labels
    plt.title(title)
    plt.xlabel(xlabel + " " + xunit)
    plt.ylabel(ylabel + " " + yunit)
    
    # place a Legend in the plot
    set_legend(1)
    
    # display grid
    plt.grid(True)
    
    # save the plot in file
    filename = title + "_" + xlabel + "_" + ylabel
    write_file(filename)
    plt.close()

def plot_data_error(x, y, title, xlabel, xunit, ylabel, yunit, yerror, plotcolor):
    plt.figure()
    
    # plot y against x 
    plt.errorbar(x, y, yerror, color=plotcolor, fmt=".")
    
    # set axis labels
    plt.title(title)
    plt.xlabel(xlabel + " " + xunit)
    plt.ylabel(ylabel + " " + unit)
    
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
def CCD_RAW(title, xlabel1, xunit1, xlabel2, xunit2, ylabel, yunit):
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
                      xlabel1, xunit1, ylabel, yunit, "red")
            i += 1
            
    if CCD_Winkel_plotting == 1:
        i = 0
        while i < 11:
            plot_data(Winkel, Amp[i], title + str(Amps[i]) + "A Magnetstrom",
                      xlabel2, xunit2, ylabel, yunit,"red")
            i += 1

    # plot RAW data Combination
    if CCD_Pixel_combi_plotting == 1:
        plt.figure()
        
        i = 0
        while i < 11:
            plt.plot(Pixel, Amp[i], label="I = %.1f" % (Amps[i]) + "A")
            i += 1
        
        # set axis labels
        plt.title(title + " Kombination")
        plt.xlabel(xlabel1 + " " + xunit1)
        plt.ylabel(ylabel + " " + yunit)
        
        # place a Legend in the plot
        set_legend(1)
        
        # display grid
        plt.grid(True)
        
        # save the plot in file
        filename = title + "Kombination" + "_" + xlabel1 + "_" + ylabel
        write_file(filename)
        plt.close()
        
        plt.figure()
        
        i = 0
        while i < 11:
            plt.plot(Pixel, Amp[i], label="I = %.1f" % (Amps[i]) + "A")
            i += 1
        
        # set axis labels
        plt.title(title + " Kombination Zoom")
        plt.xlabel(xlabel1 + " " + xunit1)
        plt.ylabel(ylabel + " " + yunit)
        
        plt.xlim([630,750])
        
        # place a Legend in the plot
        set_legend(1)
        
        # display grid
        plt.grid(True)
        
        # save the plot in file
        filename = title + "KombinationZoom" + "_" + xlabel1 + "_" + ylabel
        write_file(filename)
        plt.close()
        
        
    if CCD_Winkel_combi_plotting == 1:
        plt.figure()
        
        i = 0
        while i < 11:
            plt.plot(Winkel, Amp[i], label="I = %.1f" % (Amps[i]) + "A")
            i += 1
        
        # set axis labels
        plt.title(title + " Kombination")
        plt.xlabel(xlabel2 + " " + xunit2)
        plt.ylabel(ylabel + " " + yunit)
        
        # place a Legend in the plot
        set_legend(1)
        
        # display grid
        plt.grid(True)
        
        # save the plot in file
        filename = title + "Kombination" + "_" + xlabel2 + "_" + ylabel
        write_file(filename)
        plt.close()
        
        plt.figure()
        
        i = 0
        while i < 11:
            plt.plot(Winkel, Amp[i], label="I = %.1f" % (Amps[i]) + "A")
            i += 1
        
        # set axis labels
        plt.title(title + " Kombination Zoom")
        plt.xlabel(xlabel2 + " " + xunit2)
        plt.ylabel(ylabel + " " + yunit)
        
        plt.xlim([-2,-1.2])
        
        # place a Legend in the plot
        set_legend(1)
        
        # display grid
        plt.grid(True)
        
        # save the plot in file
        filename = title + "KombinationZoom" + "_" + xlabel2 + "_" + ylabel
        write_file(filename)
        plt.close()

def FranckHertz_RAW(title, xlabel, xunit, ylabel, yunit):
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
    FH_T = [data[:, 0], data[:, 1], data[:, 2], data[:, 3], data[:, 4],
            data[:, 5], data[:, 6], data[:, 7], data[:, 8], data[:, 9]]
    
    
    def SingleRAW():
        i = 0
        while i < 10:
            plot_data(FH_B[i], FH_B[i+1], title + str(Brems[i/2]) +
                      "V Bremsspannung", xlabel, xunit, ylabel, yunit, "red")
            i += 2
        i = 0
        while i < 10:
            plot_data(FH_T[i], FH_T[i+1], title + str(Temp[i/2])
                      + "C Temperatur", xlabel, xunit, ylabel, yunit, "red")
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
        plt.xlabel(xlabel + " " + xunit)
        plt.ylabel(ylabel + " " + yunit)
        
        # place a Legend in the plot
        set_legend(2)
        
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
        plt.xlabel(xlabel + " " + xunit)
        plt.ylabel(ylabel + " " + yunit)
        
        # place a Legend in the plot
        set_legend(2)
        
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
        ax2.set_xlabel(xlabel + " " + xunit)
        ax1.set_ylabel(ylabel + " " + yunit)
        ax2.set_ylabel(ylabel + " " + yunit)
        
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

def Magnetfeld_Kalibrierung_RAW(title, xlabel, xunit, ylabel, yunit):
    """========================================================================
    Kalibrierung des Magnetfeldes
    ===========================================================================
    """
    data = np.loadtxt('Data/Magnetfeld_Kalibrierung.csv')
    MF = [data[:, 0], data[:, 1], data[:, 2], data[:, 3]]
    
    plt.figure()
    
    x = np.array(MF[0])
    y = np.array(MF[1])
    p0 = [1.0, 1.0, 1.0, 1.0]
    
    f, varianz = op.curve_fit(polynom3, x, y, p0=p0)
    df = np.sqrt(np.sqrt(varianz.diagonal()**2))
            
    fitted_x = np.linspace(np.min(x), np.max(x), 1000)
    fitted_y = polynom3(fitted_x, *f)
    
    # plot y against x 
    plt.plot(x, y, ".", label="Erste Messung zu" +
             "\nbeginn des Versuches", color="green")
    plt.plot(fitted_x, fitted_y, label=u"Fit: y = a*x**3 + b*x**2 + c*x + d" +
             u"\na : (%.2f±%.2f)" % (f[0], df[0]) +
             u"  b : (%.2f±%.2f)" % (f[1], df[1]) +
             u"\nc : (%.2f±%.2f)" % (f[2], df[2]) +
             u"  d : (%.2f±%.2f)" % (f[3], df[3]), color="green")
    
    x = np.array(MF[2])
    y = np.array(MF[3])
    p0 = [1.0, 1.0, 1.0, 1.0]
    
    f, varianz = op.curve_fit(polynom3, x, y, p0=p0)
    df = np.sqrt(np.sqrt(varianz.diagonal()**2))
            
    fitted_x = np.linspace(np.min(x), np.max(x), 1000)
    fitted_y = polynom3(fitted_x, *f)
    
    # plot y against x 
    plt.plot(x, y, ".", label="Zweite Messung nach" +
             "\nAbschluss des Versuches", color="red")
    plt.plot(fitted_x, fitted_y, label=u"Fit: y = a*x**3 + b*x**2 + c*x + d" +
             u"\na : (%.2f±%.2f)" % (f[0], df[0]) +
             u"  b : (%.2f±%.2f)" % (f[1], df[1]) +
             u"\nc : (%.2f±%.2f)" % (f[2], df[2]) +
             u"  d : (%.2f±%.2f)" % (f[3], df[3]), color="red")
    
    x = np.array((MF[0] + MF[2])/2)
    y = np.array((MF[1] + MF[3])/2)
    p0 = [1.0, 1.0, 1.0, 1.0]
    
    f, varianz = op.curve_fit(polynom3, x, y, p0=p0)
    df = np.sqrt(np.sqrt(varianz.diagonal()**2))
            
    fitted_x = np.linspace(np.min(x), np.max(x), 1000)
    fitted_y = polynom3(fitted_x, *f)
    
    # plot y against x 
    #plt.plot(x, y, ".", label="Mittelwert der Messungen",
             #color="blue")
    plt.plot(fitted_x, fitted_y, label="Mittelwert der Messungen"
             u"\nFit: y = a*x**3 + b*x**2 + c*x + d" +
             u"\na : (%.2f±%.2f)" % (f[0], df[0]) +
             u"  b : (%.2f±%.2f)" % (f[1], df[1]) +
             u"\nc : (%.2f±%.2f)" % (f[2], df[2]) +
             u"  d : (%.2f±%.2f)" % (f[3], df[3]), color="blue")
    
    # set axis labels
    plt.title(title)
    plt.xlabel(xlabel + " " + xunit)
    plt.ylabel(ylabel + " " + yunit)
    
    set_log_axis(False, False)
    
    # place a Legend in the plot
    set_legend(4)
    
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
def CCD_ZoomFit(first, last, bottom, top, title, xlabel1, xunit1, xlabel2, xunit2, ylabel, yunit, ll):
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
    B = []
    dEp = []
    dEn = []
    ddEp = []
    ddEn = []
    
    def ZoomFit(x, y, title, xlabel, xunit, ylabel, yunit, plotcolor, p0):
        plt.figure()
        
        B.append((-0.37*Amps[i]**3+0.57*Amps[i]**2+93.51*Amps[i]-7.16)/1000)
        
        # gauss fit
        f, varianz = op.curve_fit(gauss_fkt_3, x, y, p0=p0, maxfev=1000000)
        df = np.sqrt(np.sqrt(varianz.diagonal()**2))
        
        fitted_x = np.linspace(np.min(x), np.max(x), 1000)
        fitted_y = gauss_fkt_3(fitted_x, *f)
        
        yshift = f[3] + f[7] + f[11]
        dyshift = np.sqrt(df[3]**2 + df[7]**2 + df[11]**2)
        
        dpixel = (np.sqrt((f[1] - f[5])**2) + np.sqrt((f[5] - f[9])**2))/2
        ddpixel = np.sqrt((df[1]/2)**2 + (2*df[5]/2)**2 + (df[9]/2)**2)
        
        alphasp = np.arctan((1024-(f[5]+dpixel)*0.014)/flinse)
        alphasn = np.arctan((1024-(f[5]-dpixel)*0.014)/flinse)
        alphap = np.arctan((1024-(f[5])*0.014)/flinse)
        
        dlprolp = np.sqrt((n**2-np.sin(alphasp)**2)/(n**2-np.sin(alphap)**2))-1
        dlproln = np.sqrt((n**2-np.sin(alphasn)**2)/(n**2-np.sin(alphap)**2))-1
        
        z = 0.1
        ddlproln = dlproln*z
        ddlprolp = dlprolp*z
        
        dEp.append(-h*c*dlprolp/l0)
        dEn.append(-h*c*dlproln/l0)
        ddEp.append(np.sqrt((h*c*ddlprolp/l0)**2))
        ddEn.append(np.sqrt((h*c*ddlproln/l0)**2))
        #print dEn
        #print B
        # Plotte die Originaldaten. Da es Messdaten sind, werden sie nicht mit
        # einer Linie verbunden.
        plt.plot(x, y, ".", label=ll, color=plotcolor)

        # Plotte die Anpassungsfunktion. Diesmal ohne Punkte, aber mit einer Linie.
        plt.plot(fitted_x, fitted_y, label=u"Fit: " + 
                 u"\nPeak 1: (%.2f±%.2f)" % (f[1], df[1]) +
                 u"\nFHMW 1: (%.2f±%.2f)" % (f[2], df[2]) +
                 u"\nPeak 2: (%.2f±%.2f)" % (f[5], df[5]) +
                 u"\nFHMW 2: (%.2f±%.2f)" % (f[6], df[6]) +
                 u"\nPeak 3: (%.2f±%.2f)" % (f[9], df[9]) +
                 u"\nFHMW 3: (%.2f±%.2f)" % (f[10], df[10]))
                 #u"\n    y : (%.2f±%.2f)" % (yshift, dyshift))
        
        # set axis labels
        plt.title(title)
        plt.xlabel(xlabel + " " + xunit)
        plt.ylabel(ylabel + " " + yunit)
        
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
            ZoomFit(Pixel, Amp[i], title + str(Amps[i]) + "A Magnetstrom",
                    xlabel1, xunit1, ylabel, yunit, "red", CCD_p[i])
            i += 1
        plt.figure()
        
        ab = 2
        bis = 8
        b = np.array(B[ab:bis])
        en = np.array(dEn[ab:bis])
        ep = np.array(dEp[ab:bis])
        den = np.array(ddEn[ab:bis])
        dep = np.array(ddEp[ab:bis])
        p0 = [0.01, 0.01]
        
        # plot y against x 
        plt.errorbar(b, en, den, fmt=".", label="sigma -", color="red")
        f, varianz = op.curve_fit(gerade, b, en, p0=p0)
        df = np.sqrt(np.sqrt(varianz.diagonal()**2))
        fitted_x = np.linspace(np.min(b), np.max(b), 1000)
        fitted_y = gerade(fitted_x, *f)
        plt.plot(fitted_x, fitted_y, color="red", label=u"Fit: " + 
                 u"Steigung: (%.2e±%.1e)" % (f[0], df[0]))
        
        plt.errorbar(b, ep, dep, fmt=".", label="sigma +", color="green")
        f, varianz = op.curve_fit(gerade, b, ep, p0=p0)
        df = np.sqrt(np.sqrt(varianz.diagonal()**2))
        fitted_x = np.linspace(np.min(b), np.max(b), 1000)
        fitted_y = gerade(fitted_x, *f)
        plt.plot(fitted_x, fitted_y, color="green", label=u"Fit: " + 
                 u"Steigung: (%.2e±%.1e)" % (f[0], df[0]))
        
        title = "Bohr'sches Magneton"
        xlabel = "Magnetfeld"
        xunit = "[T]"
        ylabel = r"$\Delta$E"
        yunit = "[eV]"
        
        # set axis labels
        plt.title(title)
        plt.xlabel(xlabel + " " + xunit)
        plt.ylabel(ylabel + " " + yunit)
        
        # place a Legend in the plot
        set_legend(5)
        
        plt.gca().get_yaxis().get_major_formatter().set_powerlimits((0, 1))
        
        # display grid
        plt.grid(True)
        
        # save the plot in file
        filename = title + "_" + xlabel + "_" + "dE"
        write_file(filename)
        plt.close()
            
    if CCD_ZoomFit_Winkel_plotting == 1:
        CCD_p0 = [40.0, 0.96, 1.0, 10.0,
                  50.0, 0.96, 1.0, 10.0,
                  40.0, 0.96, 1.0, 10.0]
        CCD_p1 = [50.0, 0.97, 1.0, 10.0,
                  60.0, 0.97, 1.0, 10.0,
                  50.0, 0.97, 1.0, 10.0]
        CCD_p2 = [50.0, 0.97, 1.0, 15.0,
                  60.0, 0.97, 1.0, 15.0,
                  50.0, 0.97, 1.0, 15.0]
        CCD_p3 = [50.0, 1.00, 1.0, 15.0,
                  70.0, 1.00, 1.0, 15.0,
                  50.0, 1.00, 1.0, 15.0]
        CCD_p4 = [50.0, 0.97, 1.0, 15.0,
                  60.0, 0.97, 1.0, 15.0,
                  50.0, 0.97, 1.0, 15.0]
        CCD_p5 = [50.0, 0.86, 1.0, 30.0,
                  60.0, 0.98, 1.0, 30.0,
                  50.0, 1.05, 1.0, 30.0]
        CCD_p6 = [40.0, 1.00, 1.0, 30.0,
                  50.0, 1.00, 1.0, 30.0,
                  50.0, 1.00, 1.0, 30.0]
        CCD_p7 = [50.0, 1.00, 1.0, 30.0,
                  60.0, 1.00, 1.0, 30.0,
                  50.0, 1.00, 1.0, 30.0]
        CCD_p8 = [50.0, 1.00, 1.0, 30.0,
                  60.0, 1.00, 1.0, 30.0,
                  50.0, 1.00, 1.0, 30.0]
        CCD_p9 = [50.0, 1.00, 1.0, 30.0,
                  60.0, 1.00, 1.0, 30.0,
                  50.0, 1.00, 1.0, 30.0]
        CCD_p10= [50.0, 1.05, 0.1, 30.0,
                  75.0, 1.00, 0.1, 30.0,
                  55.0, 1.10, 0.1, 30.0]
        CCD_p = [CCD_p0, CCD_p1, CCD_p2, CCD_p3, CCD_p4, CCD_p5, CCD_p6,
                 CCD_p7, CCD_p8, CCD_p9, CCD_p10]
        i = 0
        while i < 11:
            ZoomFit(Winkel, Amp[i], title + str(Amps[i]) + "A Magnetstrom",
                    xlabel2, xunit2, ylabel, yunit,"red", CCD_p[i])
            i += 1

def FH_Fit(bottom, top, title, xlabel, xunit, ylabel, yunit):
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
    FH_T = [data[:, 0], data[:, 1], data[:, 2], data[:, 3], data[:, 4],
            data[:, 5], data[:, 6], data[:, 7], data[:, 8], data[:, 9]]
    
    def plot_fit(n, x, y, title, xlabel, xunit, ylabel, yunit, plotcolor, p0, ll):
        plt.figure()
        
        # Plotte die Originaldaten. Da es Messdaten sind, werden sie nicht mit
        # einer Linie verbunden.
        plt.plot(x, y, ".", label=ll, color=plotcolor)
        
        # gauss fit
        if n == 2:
            f, varianz = op.curve_fit(gauss_fkt_2x3, x, y, p0=p0)
            df = np.sqrt(np.sqrt(varianz.diagonal()**2))
            
            fitted_x = np.linspace(np.min(x), np.max(x), 1000)
            fitted_y = gauss_fkt_2x3(fitted_x, *f)
            
            A = (f[4] - f[1])
            dA = np.sqrt((df[4])**2 + (df[1])**2)
            B = (f[2] + f[5])/n
            dB = np.sqrt((df[2]/n)**2 + (df[5]/n)**2)
            
            """ Plotte die Anpassungsfunktion. Diesmal ohne Punkte, aber mit
            einer Linie.
            """
            plt.plot(fitted_x, fitted_y, label=u"Fit: " + 
                     u"\nPeak 1: (%.2f±%.2f)" % (f[1], df[1]) +
                     u"  FHMW 1: (%.2f±%.2f)" % (f[2], df[2]) +
                     u"\nPeak 2: (%.2f±%.2f)" % (f[4], df[4]) +
                     u"  FHMW 2: (%.2f±%.2f)" % (f[5], df[5]) +
                     u"\nAbstand (Mittelwert): (%.2f±%.2f)" % (A, dA) +
                     u"\nBreite     (Mittelwert): (%.2f±%.2f)" % (B, dB))
        
        if n == 3:
            f, varianz = op.curve_fit(gauss_fkt_3x3, x, y, p0=p0)
            df = np.sqrt(np.sqrt(varianz.diagonal()**2))
            
            fitted_x = np.linspace(np.min(x), np.max(x), 1000)
            fitted_y = gauss_fkt_3x3(fitted_x, *f)
            
            A = ((f[4] - f[1]) + (f[7] - f[4])) / 2
            dA = np.sqrt((df[1]/2)**2 + (2*df[4]/2)**2 + (df[7]/2)**2)
            B = (f[2] + f[5] + f[8])/n
            dB = np.sqrt((df[2]/n)**2 + (df[5]/n)**2 + (df[8]/n)**2)
            
            """ Plotte die Anpassungsfunktion. Diesmal ohne Punkte, aber mit
            einer Linie.
            """
            plt.plot(fitted_x, fitted_y, label=u"Fit: " + 
                     u"\nPeak 1: (%.2f±%.2f)" % (f[1], df[1]) +
                     u"  FHMW 1: (%.2f±%.2f)" % (f[2], df[2]) +
                     u"\nPeak 2: (%.2f±%.2f)" % (f[4], df[4]) +
                     u"  FHMW 2: (%.2f±%.2f)" % (f[5], df[5]) +
                     u"\nPeak 3: (%.2f±%.2f)" % (f[7], df[7]) +
                     u"  FHMW 3: (%.2f±%.2f)" % (f[8], df[8]) +
                     u"\nAbstand (Mittelwert): (%.2f±%.2f)" % (A, dA) +
                     u"\nBreite     (Mittelwert): (%.2f±%.2f)" % (B, dB))
        
        if n == 4:
            f, varianz = op.curve_fit(gauss_fkt_4x3, x, y, p0=p0)
            df = np.sqrt(np.sqrt(varianz.diagonal()**2))
            
            fitted_x = np.linspace(np.min(x), np.max(x), 1000)
            fitted_y = gauss_fkt_4x3(fitted_x, *f)
            
            A = ((f[4]-f[1]) + (f[7]-f[4]) + (f[10]-f[7])) / 3
            dA = np.sqrt((df[1]/3)**2 + (2*df[4]/3)**2 + (2*df[7]/3)**2 +
                         (df[10]/3)**2)
            B = (f[2] + f[5] + f[8] + f[11])/n
            dB = np.sqrt((df[2]/n)**2 + (df[5]/n)**2 + (df[8]/n)**2 +
                         (df[11]/n)**2)
            
            """ Plotte die Anpassungsfunktion. Diesmal ohne Punkte, aber mit
            einer Linie.
            """
            plt.plot(fitted_x, fitted_y, label=u"Fit: " + 
                     u"\nPeak 1: (%.2f±%.2f)" % (f[1], df[1]) +
                     u"  FHMW 1: (%.2f±%.2f)" % (f[2], df[2]) +
                     u"\nPeak 2: (%.2f±%.2f)" % (f[4], df[4]) +
                     u"  FHMW 2: (%.2f±%.2f)" % (f[5], df[5]) +
                     u"\nPeak 3: (%.2f±%.2f)" % (f[7], df[7]) +
                     u"  FHMW 3: (%.2f±%.2f)" % (f[8], df[8]) +
                     u"\nPeak 4: (%.2f±%.2f)" % (f[10], df[10]) +
                     u"  FHMW 4: (%.2f±%.2f)" % (f[11], df[11]) +
                     u"\nAbstand (Mittelwert): (%.2f±%.2f)" % (A, dA) +
                     u"\nBreite     (Mittelwert): (%.2f±%.2f)" % (B, dB))
        
        if n == 5:
            f, varianz = op.curve_fit(gauss_fkt_5x3, x, y, p0=p0)
            df = np.sqrt(np.sqrt(varianz.diagonal()**2))
            
            fitted_x = np.linspace(np.min(x), np.max(x), 1000)
            fitted_y = gauss_fkt_5x3(fitted_x, *f)
            
            A = ((f[4]-f[1]) + (f[7]-f[4]) + (f[10]-f[7]) +
                       (f[13]-f[10])) / 4
            dA = np.sqrt((df[1]/4)**2 + (2*df[4]/4)**2 + (2*df[7]/4)**2 +
                         (2*df[10]/4)**2 + (df[13]/4)**2)
            B = (f[2] + f[5] + f[8] + f[11] + f[14])/n
            dB = np.sqrt((df[2]/n)**2 + (df[5]/n)**2 + (df[8]/n)**2 +
                         (df[11]/n)**2 + (df[14]/n)**2)
            
            """ Plotte die Anpassungsfunktion. Diesmal ohne Punkte, aber mit
            einer Linie.
            """
            plt.plot(fitted_x, fitted_y, label=u"Fit: " + 
                     u"\nPeak 1: (%.2f±%.2f)" % (f[1], df[1]) +
                     u"  FHMW 1: (%.2f±%.2f)" % (f[2], df[2]) +
                     u"\nPeak 2: (%.2f±%.2f)" % (f[4], df[4]) +
                     u"  FHMW 2: (%.2f±%.2f)" % (f[5], df[5]) +
                     u"\nPeak 3: (%.2f±%.2f)" % (f[7], df[7]) +
                     u"  FHMW 3: (%.2f±%.2f)" % (f[8], df[8]) +
                     u"\nPeak 4: (%.2f±%.2f)" % (f[10], df[10]) +
                     u"  FHMW 4: (%.2f±%.2f)" % (f[11], df[11]) +
                     u"\nPeak 5: (%.2f±%.2f)" % (f[13], df[13]) +
                     u"  FHMW 5: (%.2f±%.2f)" % (f[14], df[14]) +
                     u"\nAbstand (Mittelwert): (%.2f±%.2f)" % (A, dA) +
                     u"\nBreite     (Mittelwert): (%.2f±%.2f)" % (B, dB))
        
        # set axis labels
        plt.title(title)
        plt.xlabel(xlabel + " " + xunit)
        plt.ylabel(ylabel + " " + yunit)
        
        # set axis limits
        #plt.xlim([first,last])
        plt.ylim([bottom,top])
        
        # place a Legend in the plot
        set_legend(2)
        
        # display grid
        plt.grid(True)
        
        # save the plot in file
        filename = title + "_" + xlabel + "_" + ylabel
        write_file(filename)
        plt.close()
    
    if FH_B_Gauss_plotting == 1:
        CCD_p0 = [1.0, 17.0, 1.0,
                  3.0, 22.0, 1.0,
                  5.0, 26.0, 1.0,
                  7.0, 32.0, 1.0,
                  9.0, 37.0, 1.0,
                  0.1]
        CCD_p1 = [1.0, 17.0, 1.0,
                  2.0, 22.0, 1.0,
                  4.0, 26.0, 1.0,
                  6.0, 32.0, 1.0,
                  9.0, 37.0, 1.0,
                  0.1]
        CCD_p2 = [0.8, 17.0, 1.0,
                  1.5, 22.0, 1.0,
                  2.5, 26.0, 1.0,
                  4.0, 32.0, 1.0,
                  5.5, 37.0, 1.0,
                  0.1]
        CCD_p3 = [0.5, 17.0, 1.0,
                  0.9, 22.0, 1.0,
                  1.6, 26.0, 1.0,
                  2.4, 32.0, 1.0,
                  3.5, 37.0, 1.0,
                  0.1]
        CCD_p4 = [1.0, 17.0, 1.0,
                  3.0, 22.0, 1.0,
                  5.0, 26.0, 1.0,
                  7.0, 32.0, 1.0,
                  9.0, 37.0, 1.0,
                  0.1]
        CCD_p = [CCD_p0, CCD_p1, CCD_p2, CCD_p3, CCD_p4]
        npoly = [5.0, 5.0, 5.0, 5.0, 5.0]
        i = 0
        while i < 10:
            plot_fit(npoly[i/2], FH_B[i], FH_B[i+1], title + str(Brems[i/2]) +
                    "V Bremsspannung", xlabel, xunit, ylabel, yunit, "red",
                    CCD_p[i/2], "Bremsspannung: " + str(Brems[i/2]))
            i += 2
    
    if FH_T_Gauss_plotting == 1:
        CCD_p0 = [4.4, 12.0, 1.0,
                  11.0, 17.0, 1.0,
                  0.1]
        CCD_p1 = [1.7, 12.0, 1.0,
                  5.8, 17.0, 1.0,
                  11.0, 22.0, 1.0,
                  0.1]
        CCD_p2 = [3.0, 17.0, 1.0,
                  6.0, 22.0, 1.0,
                  11.0, 27.0, 1.0,
                  0.1]
        CCD_p3 = [1.0, 17.0, 1.0,
                  2.2, 22.0, 1.0,
                  3.8, 27.0, 1.0,
                  5.7, 32.0, 1.0,
                  8.6, 37.0, 1.0,
                  0.1]
        CCD_p4 = [1.2, 17.0, 1.0,
                  2.4, 22.0, 1.0,
                  4.1, 27.0, 1.0,
                  6.0, 32.0, 1.0,
                  9.5, 37.0, 1.0,
                  0.1]
        CCD_p = [CCD_p0, CCD_p1, CCD_p2, CCD_p3, CCD_p4]
        npoly = [2.0, 3.0, 3.0, 5.0, 5.0]
        i = 0
        while i < 10:
            plot_fit(npoly[i/2], FH_T[i], FH_T[i+1], title + str(Temp[i/2]) +
                    "C Temperatur", xlabel, xunit, ylabel, yunit, "red",
                    CCD_p[i/2], "Temperatur: " + str(Temp[i/2]))
            i += 2



"""============================================================================
MAIN --- running procedures
===============================================================================
"""
h = 4.136e-15
c = 3e8
l0 = 643.8e-9
n = 1.457
flinse = 235

# What to do?       0 = Do Not Do It        1 = Do It
savefig_pdf = 0
savefig_png = 1

# RAW DATA
CCD_Pixel_plotting = 0
CCD_Winkel_plotting = 0
CCD_Pixel_combi_plotting = 0
CCD_Winkel_combi_plotting = 0
# FITTINGS
CCD_ZoomFit_Pixel_plotting = 1
CCD_ZoomFit_Winkel_plotting = 0

# RAW DATA
FH_SingleRAW_plotting = 0
FH_Vergleiche_plotting = 0
# FITTINGS
FH_B_Gauss_plotting = 0
FH_T_Gauss_plotting = 0

# RAW DATA
MF_plotting = 0

# ALL OF THEM
everything = 0

if everything == 1:
    CCD_Pixel_plotting = 1
    CCD_Winkel_plotting = 1
    CCD_Pixel_combi_plotting = 1
    CCD_Winkel_combi_plotting = 1
    CCD_ZoomFit_Pixel_plotting = 1
    CCD_ZoomFit_Winkel_plotting = 1
    FH_SingleRAW_plotting = 1
    FH_Vergleiche_plotting = 1
    FH_B_Gauss_plotting = 1
    FH_T_Gauss_plotting = 1
    MF_plotting = 1


def plot():
    if (CCD_Pixel_plotting == 1 or CCD_Winkel_plotting == 1 or
        CCD_Pixel_combi_plotting == 1 or CCD_Winkel_combi_plotting == 1):
        CCD_RAW("Versuch401 - Fabry-Perot-Etalon --- ", "Pixel", "[#]",
                "Winkel", "[rad]", "Intensitaet", "[%]")
#pixel 1175, 1255
#winkel 803, 890
    if CCD_ZoomFit_Pixel_plotting == 1 or CCD_ZoomFit_Winkel_plotting == 1:
        CCD_ZoomFit(1175, 1255, 0, 80, "Versuch401 - FPE Ausschnitt --- ",
                    "Pixel", "[#]", "Winkel", "[rad]", "Intensitaet", "[%]",
                    "Messwerte")

    if FH_SingleRAW_plotting == 1 or FH_Vergleiche_plotting == 1:
        FranckHertz_RAW("Versuch401 - Franck-Hertz --- ",
                        "Beschl. Spannung", "[V]", "Anodenspannung", "[V]")

    if FH_B_Gauss_plotting == 1 or FH_T_Gauss_plotting == 1:
        FH_Fit(0, 12, "Versuch401 - Franck-Hertz --- ",
               "Beschl. Spannung", "[V]", "Anodenspannung", "[V]")

    if MF_plotting == 1:
        Magnetfeld_Kalibrierung_RAW("Versuch401 - Kalibrierung des " +
                                    "Magnetfeldes", "Spulenstrom", "[A]",
                                    "Magnetfeld", "[T]")

plot()




