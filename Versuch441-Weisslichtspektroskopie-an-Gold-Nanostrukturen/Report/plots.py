#-*- coding: utf-8 -*-
import numpy as np
import scipy.optimize as op
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches


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

def set_legend(fsize, msize, opac, location, ):
    leg = plt.legend(prop={'size':fsize}, loc = location, numpoints=1,
                     markerscale=msize, fancybox=True)
    leg.get_frame().set_alpha(opac)

def set_log_axis(x, y):
    if x == True:
        plt.xscale('log')
    if y == True:
        plt.yscale('log')

def get_Ref_Ints(n, Char, pol):
    Intens = []
    l = []
    i = 1
    while i < n:
        l.append("R: " + Char + str(i))
        data = np.loadtxt('Data/' +pol+ '/' + Char + '_Ref' + str(i) + '.txt',
                            skiprows=15, usecols=[1], comments=">")
        Intens.append(data)
        i += 2
    return Intens, l

def get_Trans_Ints(n, Char, pol):
    Intens = []
    l = []
    i = 1
    while i < n+1:
        l.append("T: " + Char + str(i))
        data = np.loadtxt('Data/' +pol+ '/' +Char+ '_Trans' +str(i)+ '.txt',
                            skiprows=17, usecols=[1], comments=">")
        Intens.append(data)
        i += 1
    return Intens, l

"""============================================================================
Useful functions for plotting and fitting
===============================================================================
"""
def gaussian_neg(x, *p0):
    m, sigmam, a = p0
    f = 100-a*np.exp(-0.5*((x-m)/sigmam)**2)
    return f

def gaussian_neg_off(x, *p0):
    m, sigmam, a, off = p0
    f1 = (100-np.sqrt(off**2))
    f2 = -a*np.exp(-0.5*((x-m)/sigmam)**2)
    return f1 + f2

def gaussian_neg_off2(x, *p0):
    m, sigmam, n, sigman, a, b, off = p0
    f1 = (100-np.sqrt(off**2))
    f2 = -a*np.exp(-0.5*((x-m)/sigmam)**2)
    f3 = -b*np.exp(-0.5*((x-n)/sigman)**2)
    return f1 + f2 + f3

def plot_nSpecs(n, lower, upper, x, y, title, xlabel, xunit, ylabel, yunit, llab, plotcolor, name, lsizef, lsizem, lop, lloc):
    plt.figure()
    
    # plot y against x 
    j = 0
    while j < n:
        plt.plot(x, y[j], ".", markersize=msize, label=llab[j],
                 color=plotcolor[j])
        j += 1
    
    # set axis labels
    plt.title(title)
    plt.xlabel(xlabel + " " + xunit)
    plt.ylabel(ylabel + " " + yunit)
    
    plt.ylim([lower,upper])
    
    # place a Legend in the plot
    set_legend(lsizef, lsizem, lop, lloc)
    
    # display grid
    plt.grid(True)
    
    # save the plot in file
    write_file(name)
    plt.close()

def plot_nSpecsFIT(start, n, lower, upper, bottom, top, x, y, title, xlabel, xunit, ylabel, yunit, llab, p0, plotcolor, name, lsizef, lsizem, lop, lloc):
    plt.figure()
    
    # plot y against x 
    j = start
    while j < n:
        plt.plot(x, y[j], ".", markersize=msize, color=plotcolor[j])
        
        xcut = x[bottom:top]
        ycut = y[j][bottom:top]
        f, varianz = op.curve_fit(gaussian_neg, xcut, ycut, p0=p0,
                                  maxfev=100000)
        df = np.sqrt(np.sqrt(varianz.diagonal()**2))
        
        fitted_x = np.linspace(np.min(xcut), np.max(xcut), 1000)
        fitted_y = gaussian_neg(fitted_x, *f)
        
        plt.plot(fitted_x, fitted_y, color=plotcolor[j], label= llab[j] +
                 u" Peak: (%.1e±%.1e)" % (f[0], df[0]) +
                 u"  FHMW: (%.1e±%.1e)" % (f[1], df[1]) +
                 u"  Ampl.: (%.1e±%.1e)" % (f[2], df[2]))
        
        j += 1
        if j == 5:
            break
    
    # set axis labels
    plt.title(title)
    plt.xlabel(xlabel + " " + xunit)
    plt.ylabel(ylabel + " " + yunit)
    
    plt.ylim([lower,upper])
    
    # place a Legend in the plot
    set_legend(lsizef, lsizem, lop, lloc)
    
    # display grid
    plt.grid(True)
    
    # save the plot in file
    write_file(name + "_" + str(start+1) + "to" + str(j))
    plt.close()
    
    if j == 5 and n > 5:
        plot_nSpecsFIT(j, n, lower, upper, bottom, top, x, y, title, xlabel,
                       xunit, ylabel, yunit, llab, p0, plotcolor, name, lsizef,
                       lsizem, lop, lloc)


"""============================================================================
Plotting RAW data
===============================================================================
"""
def DarkSpec(xl, xu, yl, yu, fn):
    ytop = 230
    ybottom = 210
    lsizef = 12
    lsizem = 10
    lop = 0.5
    lloc = 1
    Intens = []
    data = np.loadtxt('Data/null/A_Dark1.txt', skiprows=15, usecols=[1],
                       comments=">")
    Intens.append(data)
    data = np.loadtxt('Data/90/A_Dark1.txt', skiprows=15, usecols=[1],
                       comments=">")
    Intens.append(data)
    Intens = np.array(Intens)
    
    ll = [r"Darkspectrum $0^\circ$", r"Darkspectrum $90^\circ$"]
    plot_nSpecs(2, ybottom, ytop, Wavelen, Intens, r"Darkspectrum " +
                "(before taking Meassurements)",
                xl, xu, yl, yu, ll,
                ["Red", "Green"], fn, lsizef, lsizem, lop, lloc)

def RefSpec(xl, xu, yl, yu, fn):
    ytop = 4000
    ybottom = 0
    lsizef = 12
    lsizem = 10
    lop = 0.5
    lloc = 1
    
    if P0 == 1:
        p = 0
        polar = "null"
        t = "Referencespectrums for "
        if A_OnOff == 1:
            c = "A"
            Intens, ll = get_Ref_Ints(4, c, polar)
            plot_nSpecs(2, ybottom, ytop, Wavelen, Intens, t + c,
                xl, xu, yl, yu, ll,
                ["Red", "Green"], fn + c + "Pol" +str(p),
                lsizef, lsizem, lop, lloc)
        if B_OnOff == 1:
            c = "B"
            Intens, ll = get_Ref_Ints(8, c, polar)
            plot_nSpecs(4, ybottom, ytop, Wavelen, Intens, t + c,
                xl, xu, yl, yu, ll,
                ["Red", "Green", "Blue", "Cyan"], fn + c + "Pol" +str(p),
                lsizef, lsizem, lop, lloc)
        if C_OnOff == 1:
            c = "C"
            Intens, ll = get_Ref_Ints(8, c, polar)
            plot_nSpecs(4, ybottom, ytop, Wavelen, Intens, t + c,
                xl, xu, yl, yu, ll,
                ["Red", "Green", "Blue", "Cyan"], fn + c + "Pol" +str(p),
                lsizef, lsizem, lop, lloc)
        if D_OnOff == 1:
            c = "D"
            Intens, ll = get_Ref_Ints(4, c, polar)
            plot_nSpecs(2, ybottom, ytop, Wavelen, Intens, t + c,
                xl, xu, yl, yu, ll,
                ["Red", "Green"], fn + c + "Pol" +str(p),
                lsizef, lsizem, lop, lloc)
        if E_OnOff == 1:
            c = "E"
            Intens, ll = get_Ref_Ints(8, c, polar)
            plot_nSpecs(4, ybottom, ytop, Wavelen, Intens, t + c,
                xl, xu, yl, yu, ll,
                ["Red", "Green", "Blue", "Cyan"], fn + c + "Pol" +str(p),
                lsizef, lsizem, lop, lloc)
    
    if P90 == 1:
        p = 90
        polar = "90"
        t = "Referencespectrums for "
        if A_OnOff == 1:
            c = "A"
            Intens, ll = get_Ref_Ints(4, c, polar)
            plot_nSpecs(2, ybottom, ytop, Wavelen, Intens, t + c,
                xl, xu, yl, yu, ll,
                ["Red", "Green"], fn + c + "Pol" +str(p),
                lsizef, lsizem, lop, lloc)
        if B_OnOff == 1:
            c = "B"
            Intens, ll = get_Ref_Ints(8, c, polar)
            plot_nSpecs(4, ybottom, ytop, Wavelen, Intens, t + c,
                xl, xu, yl, yu, ll,
                ["Red", "Green", "Blue", "Cyan"], fn + c + "Pol" +str(p),
                lsizef, lsizem, lop, lloc)
        if C_OnOff == 1:
            c = "C"
            Intens, ll = get_Ref_Ints(8, c, polar)
            plot_nSpecs(4, ybottom, ytop, Wavelen, Intens, t + c,
                xl, xu, yl, yu, ll,
                ["Red", "Green", "Blue", "Cyan"], fn + c + "Pol" +str(p),
                lsizef, lsizem, lop, lloc)
        if D_OnOff == 1:
            c = "D"
            Intens, ll = get_Ref_Ints(4, c, polar)
            plot_nSpecs(2, ybottom, ytop, Wavelen, Intens, t + c,
                xl, xu, yl, yu, ll,
                ["Red", "Green"], fn + c + "Pol" +str(p),
                lsizef, lsizem, lop, lloc)
        if E_OnOff == 1:
            c = "E"
            Intens, ll = get_Ref_Ints(8, c, polar)
            plot_nSpecs(4, ybottom, ytop, Wavelen, Intens, t + c,
                xl, xu, yl, yu, ll,
                ["Red", "Green", "Blue", "Cyan"], fn + c + "Pol" +str(p),
                lsizef, lsizem, lop, lloc)

def TransSpecRAW(xl, xu, yl, yu, fn):
    ytop = 100
    ybottom = 50
    lsizef = 12
    lsizem = 10
    lop = 0.5
    lloc = 3
    
    if P0 == 1:
        p = 0
        polar = "null"
        t = "Transmissionspectrums for "
        if A_OnOff == 1:
            c = "A"
            Intens, ll = get_Trans_Ints(4, c, polar)
            plot_nSpecs(4, ybottom, ytop, Wavelen, Intens, t + c,
                xl, xu, yl, yu, ll,
                ["Red", "Green", "Blue", "Cyan"],
                fn + c + "Pol" +str(p), lsizef, lsizem, lop, lloc)
        if B_OnOff == 1:
            c = "B"
            Intens, ll = get_Trans_Ints(9, c, polar)
            plot_nSpecs(9, ybottom, ytop, Wavelen, Intens, t + c,
                xl, xu, yl, yu, ll,
                ["Red", "Green", "Blue", "Cyan", "Orange", "Lime", "Magenta",
                 "Brown", "Violet"],
                fn + c + "Pol" +str(p), lsizef, lsizem, lop, lloc)
        if C_OnOff == 1:
            c = "C"
            Intens, ll = get_Trans_Ints(9, c, polar)
            plot_nSpecs(9, ybottom, ytop, Wavelen, Intens, t + c,
                xl, xu, yl, yu, ll,
                ["Red", "Green", "Blue", "Cyan", "Orange", "Lime", "Magenta",
                 "Brown", "Violet"],
                fn + c + "Pol" +str(p), lsizef, lsizem, lop, lloc)
        if D_OnOff == 1:
            c = "D"
            Intens, ll = get_Trans_Ints(5, c, polar)
            plot_nSpecs(5, ybottom, ytop, Wavelen, Intens, t + c,
                xl, xu, yl, yu, ll,
                ["Red", "Green", "Blue", "Cyan", "Orange"],
                fn + c + "Pol" +str(p), lsizef, lsizem, lop, lloc)
        if E_OnOff == 1:
            c = "E"
            Intens, ll = get_Trans_Ints(8, c, polar)
            plot_nSpecs(8, ybottom, ytop, Wavelen, Intens, t + c,
                xl, xu, yl, yu, ll,
                ["Red", "Green", "Blue", "Cyan", "Orange", "Lime", "Magenta",
                 "Brown"],
                fn + c + "Pol" +str(p), lsizef, lsizem, lop, lloc)
    
    if P90 == 1:
        p = 90
        polar = "90"
        t = "Transmissionspectrums for "
        if A_OnOff == 1:
            c = "A"
            Intens, ll = get_Trans_Ints(4, c, polar)
            plot_nSpecs(4, ybottom, ytop, Wavelen, Intens, t + c,
                xl, xu, yl, yu, ll,
                ["Red", "Green", "Blue", "Cyan"],
                fn + c + "Pol" +str(p), lsizef, lsizem, lop, lloc)
        if B_OnOff == 1:
            c = "B"
            Intens, ll = get_Trans_Ints(9, c, polar)
            plot_nSpecs(9, ybottom, ytop, Wavelen, Intens, t + c,
                xl, xu, yl, yu, ll,
                ["Red", "Green", "Blue", "Cyan", "Orange", "Lime", "Magenta",
                 "Brown", "Violet"],
                fn + c + "Pol" +str(p), lsizef, lsizem, lop, lloc)
        if C_OnOff == 1:
            c = "C"
            Intens, ll = get_Trans_Ints(9, c, polar)
            plot_nSpecs(9, ybottom, ytop, Wavelen, Intens, t + c,
                xl, xu, yl, yu, ll,
                ["Red", "Green", "Blue", "Cyan", "Orange", "Lime", "Magenta",
                 "Brown", "Violet"],
                fn + c + "Pol" +str(p), lsizef, lsizem, lop, lloc)
        if D_OnOff == 1:
            c = "D"
            Intens, ll = get_Trans_Ints(5, c, polar)
            plot_nSpecs(5, ybottom, ytop, Wavelen, Intens, t + c,
                xl, xu, yl, yu, ll,
                ["Red", "Green", "Blue", "Cyan", "Orange"],
                fn + c + "Pol" +str(p), lsizef, lsizem, lop, lloc)
        if E_OnOff == 1:
            c = "E"
            Intens, ll = get_Trans_Ints(8, c, polar)
            plot_nSpecs(8, ybottom, ytop, Wavelen, Intens, t + c,
                xl, xu, yl, yu, ll,
                ["Red", "Green", "Blue", "Cyan", "Orange", "Lime", "Magenta",
                 "Brown"],
                fn + c + "Pol" +str(p), lsizef, lsizem, lop, lloc)



"""============================================================================
Fitting functions, analysing data and calculating stuff
===============================================================================
"""
def TransSpecFIT(xl, xu, yl, yu, fn):
    ytop = 100
    ybottom = 50
    lsizef = 9
    lsizem = 10
    lop = 0.5
    lloc = 3
    if P0 == 1:
        p = 0
        polar = "null"
        t = "Transmissionspectrums for "
        if A_OnOff == 1:
            c = "A"
            first = 350
            last = 550
            p0 = [800.0, 80.0, 20.0]
            Intens, ll = get_Trans_Ints(4, c, polar)
            plot_nSpecsFIT(0, 4, ybottom, ytop, first, last, Wavelen, Intens,
                           t + c, xl, xu, yl, yu, ll, p0,
                           ["Red", "Green", "Blue", "Cyan"],
                           fn + c + "Pol" +str(p), lsizef, lsizem, lop, lloc)
        if B_OnOff == 1:
            c = "B"
            first = 450
            last = 600
            p0 = [900.0, 60.0, 40.0]
            Intens, ll = get_Trans_Ints(9, c, polar)
            plot_nSpecsFIT(0, 9, ybottom, ytop, first, last, Wavelen, Intens,
                           t + c, xl, xu, yl, yu, ll, p0,
                           ["Red", "Green", "Blue", "Cyan", "Orange", "Lime",
                            "Magenta", "Brown", "Violet"],
                           fn + c + "Pol" +str(p), lsizef, lsizem, lop, lloc)
        if C_OnOff == 1:
            c = "C"
            first = 400
            last = 600
            p0 = [800.0, 80.0, 20.0]
            Intens, ll = get_Trans_Ints(9, c, polar)
            plot_nSpecsFIT(0, 9, ybottom, ytop, first, last, Wavelen, Intens,
                           t + c, xl, xu, yl, yu, ll, p0,
                           ["Red", "Green", "Blue", "Cyan", "Orange", "Lime",
                            "Magenta", "Brown", "Violet"],
                           fn + c + "Pol" +str(p), lsizef, lsizem, lop, lloc)
        if D_OnOff == 1:
            c = "D"
            first = 300
            last = 550
            p0 = [800.0, 100.0, 20.0]
            Intens, ll = get_Trans_Ints(5, c, polar)
            plot_nSpecsFIT(0, 5, ybottom, ytop, first, last, Wavelen, Intens,
                           t + c, xl, xu, yl, yu, ll, p0,
                           ["Red", "Green", "Blue", "Cyan", "Orange"],
                           fn + c + "Pol" +str(p), lsizef, lsizem, lop, lloc)
        if E_OnOff == 1:
            c = "E"
            first = 350
            last = 650
            p0 = [900.0, 100.0, 20.0]
            Intens, ll = get_Trans_Ints(8, c, polar)
            plot_nSpecsFIT(0, 8, ybottom, ytop, first, last, Wavelen, Intens,
                           t + c, xl, xu, yl, yu, ll, p0,
                           ["Red", "Green", "Blue", "Cyan", "Orange", "Lime",
                            "Magenta", "Brown"],
                           fn + c + "Pol" +str(p), lsizef, lsizem, lop, lloc)
    
    if P90 == 1:
        p = 90
        polar = "90"
        t = "Transmissionspectrums for "
        if A_OnOff == 1:
            c = "A"
            first = 300
            last = 650
            p0 = [800.0, 1.0, 20.0]
            Intens, ll = get_Trans_Ints(4, c, polar)
            plot_nSpecsFIT(0, 4, ybottom, ytop, first, last, Wavelen, Intens,
                           t + c, xl, xu, yl, yu, ll, p0,
                           ["Red", "Green", "Blue", "Cyan"],
                           fn + c + "Pol" +str(p), lsizef, lsizem, lop, lloc)
        if B_OnOff == 1:
            c = "B"
            first = 380
            last = 550
            p0 = [900.0, 60.0, 40.0]
            Intens, ll = get_Trans_Ints(9, c, polar)
            plot_nSpecsFIT(0, 9, ybottom, ytop, first, last, Wavelen, Intens,
                           t + c, xl, xu, yl, yu, ll, p0,
                           ["Red", "Green", "Blue", "Cyan", "Orange", "Lime",
                            "Magenta", "Brown", "Violet"],
                           fn + c + "Pol" +str(p), lsizef, lsizem, lop, lloc)
        if C_OnOff == 1:
            c = "C"
            first = 400
            last = 600
            p0 = [800.0, 80.0, 20.0]
            Intens, ll = get_Trans_Ints(9, c, polar)
            plot_nSpecsFIT(0, 9, ybottom, ytop, first, last, Wavelen, Intens,
                           t + c, xl, xu, yl, yu, ll, p0,
                           ["Red", "Green", "Blue", "Cyan", "Orange", "Lime",
                            "Magenta", "Brown", "Violet"],
                           fn + c + "Pol" +str(p), lsizef, lsizem, lop, lloc)
        if D_OnOff == 1:
            c = "D"
            first = 300
            last = 500
            p0 = [800.0, 100.0, 20.0]
            Intens, ll = get_Trans_Ints(5, c, polar)
            plot_nSpecsFIT(0, 5, ybottom, ytop, first, last, Wavelen, Intens,
                           t + c, xl, xu, yl, yu, ll, p0,
                           ["Red", "Green", "Blue", "Cyan", "Orange"],
                           fn + c + "Pol" +str(p), lsizef, lsizem, lop, lloc)
        if E_OnOff == 1:
            c = "E"
            first = 230
            last = 400
            p0 = [800.0, 80.0, 20.0]
            Intens, ll = get_Trans_Ints(8, c, polar)
            plot_nSpecsFIT(0, 8, ybottom, ytop, first, last, Wavelen, Intens,
                           t + c, xl, xu, yl, yu, ll, p0,
                           ["Red", "Green", "Blue", "Cyan", "Orange", "Lime",
                            "Magenta", "Brown"],
                           fn + c + "Pol" +str(p), lsizef, lsizem, lop, lloc)



"""============================================================================
MAIN --- running procedures
===============================================================================
"""
# What to do?       0 = Do Not Do It        1 = Do It
savefig_pdf = 0
savefig_png = 1
msize = 2

P0 = 1
P90 = 1
A_OnOff = 1
B_OnOff = 1
C_OnOff = 1
D_OnOff = 1
E_OnOff = 1

# RAW DATA
Darkspectrum_OnOff = 1
Referencespectrums_OnOff = 1
TransmissionspectrumsRAW_OnOff = 1

# FITTINGS
TransmissionspectrumsFIT_OnOff = 1


# ALL OF THEM
everything = 0

Wavelen= np.loadtxt('Data/null/A_Dark1.txt', skiprows=15, usecols=[0],
                    comments=">")

if everything == 1:
    P0 = 1
    P90 = 1

if Darkspectrum_OnOff == 1:
    DarkSpec("Wavelength", " /nm", "rel. Intensity", " /%", "Darkspec")

if Referencespectrums_OnOff == 1:
    RefSpec("Wavelength", " /nm", "rel. Intensity", " /%", "Refspec_")

if TransmissionspectrumsRAW_OnOff == 1:
    TransSpecRAW("Wavelength", " /nm", "rel. Intensity", " /%", "TransspecRAW_")

if TransmissionspectrumsFIT_OnOff == 1:
    TransSpecFIT("Wavelength", " /nm", "rel. Intensity", " /%",
                 "TransspecFIT_")


