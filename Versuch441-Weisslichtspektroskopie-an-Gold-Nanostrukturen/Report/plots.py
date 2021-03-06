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

def set_legend(fsize, msize, opac, location):
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
def gerade(x, m, n):
    f = m*x + n
    return f

def parabola(x, a, b, c):
    f = a*x**2 + b*x + c
    return f

def oneoverrsq(x, a, b):
    f = a/(x**2) + b
    return f

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
    
    minima = []
    dminima = []
    
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
        
        minima.append(f[0])
        dminima.append(df[0])
        
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
    
    return minima, dminima


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
    
    ll = [r"Dark spectrum $0^\circ$", r"Dark spectrum $90^\circ$"]
    plot_nSpecs(2, ybottom, ytop, Wavelen, Intens, r"Dark spectrum " +
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
    
    p = 0
    polar = "null"
    t = "Reference spectrums for "
    if A_OnOff == 1:
        c = "A"
        Intens, ll = get_Ref_Ints(4, c, polar)
        plot_nSpecs(2, ybottom, ytop, Wavelen, Intens,
                    t + c + " - Pol: " + str(p) + r"$^{\circ}$",
                    xl, xu, yl, yu, ll,
                    ["Red", "Green"], fn + c + "Pol" +str(p),
                    lsizef, lsizem, lop, lloc)
    if B_OnOff == 1:
        c = "B"
        Intens, ll = get_Ref_Ints(8, c, polar)
        plot_nSpecs(4, ybottom, ytop, Wavelen, Intens,
                    t + c + " - Pol: " + str(p) + r"$^{\circ}$",
                    xl, xu, yl, yu, ll,
                    ["Red", "Green", "Blue", "Cyan"],
                    fn + c + "Pol" +str(p), lsizef, lsizem, lop, lloc)
    if C_OnOff == 1:
        c = "C"
        Intens, ll = get_Ref_Ints(8, c, polar)
        plot_nSpecs(4, ybottom, ytop, Wavelen, Intens,
                    t + c + " - Pol: " + str(p) + r"$^{\circ}$",
                    xl, xu, yl, yu, ll,
                    ["Red", "Green", "Blue", "Cyan"],
                    fn + c + "Pol" +str(p), lsizef, lsizem, lop, lloc)
    if D_OnOff == 1:
        c = "D"
        Intens, ll = get_Ref_Ints(4, c, polar)
        plot_nSpecs(2, ybottom, ytop, Wavelen, Intens,
                    t + c + " - Pol: " + str(p) + r"$^{\circ}$",
                    xl, xu, yl, yu, ll,
                    ["Red", "Green"], fn + c + "Pol" +str(p),
                    lsizef, lsizem, lop, lloc)
    if E_OnOff == 1:
        c = "E"
        Intens, ll = get_Ref_Ints(8, c, polar)
        plot_nSpecs(4, ybottom, ytop, Wavelen, Intens,
                    t + c + " - Pol: " + str(p) + r"$^{\circ}$",
                    xl, xu, yl, yu, ll,
                    ["Red", "Green", "Blue", "Cyan"],
                    fn + c + "Pol" +str(p), lsizef, lsizem, lop, lloc)
    
    p = 90
    polar = "90"
    t = "Reference spectrums for "
    if A_OnOff == 1:
        c = "A"
        Intens, ll = get_Ref_Ints(4, c, polar)
        plot_nSpecs(2, ybottom, ytop, Wavelen, Intens,
                    t + c + " - Pol: " + str(p) + r"$^{\circ}$",
                    xl, xu, yl, yu, ll,
                    ["Red", "Green"], fn + c + "Pol" +str(p),
                    lsizef, lsizem, lop, lloc)
    if B_OnOff == 1:
        c = "B"
        Intens, ll = get_Ref_Ints(8, c, polar)
        plot_nSpecs(4, ybottom, ytop, Wavelen, Intens,
                    t + c + " - Pol: " + str(p) + r"$^{\circ}$",
                    xl, xu, yl, yu, ll,
                    ["Red", "Green", "Blue", "Cyan"],
                    fn + c + "Pol" +str(p), lsizef, lsizem, lop, lloc)
    if C_OnOff == 1:
        c = "C"
        Intens, ll = get_Ref_Ints(8, c, polar)
        plot_nSpecs(4, ybottom, ytop, Wavelen, Intens,
                    t + c + " - Pol: " + str(p) + r"$^{\circ}$",
                    xl, xu, yl, yu, ll,
                    ["Red", "Green", "Blue", "Cyan"],
                    fn + c + "Pol" +str(p), lsizef, lsizem, lop, lloc)
    if D_OnOff == 1:
        c = "D"
        Intens, ll = get_Ref_Ints(4, c, polar)
        plot_nSpecs(2, ybottom, ytop, Wavelen, Intens,
                    t + c + " - Pol: " + str(p) + r"$^{\circ}$",
                    xl, xu, yl, yu, ll,
                    ["Red", "Green"], fn + c + "Pol" +str(p),
                    lsizef, lsizem, lop, lloc)
    if E_OnOff == 1:
        c = "E"
        Intens, ll = get_Ref_Ints(8, c, polar)
        plot_nSpecs(4, ybottom, ytop, Wavelen, Intens,
                    t + c + " - Pol: " + str(p) + r"$^{\circ}$",
                    xl, xu, yl, yu, ll,
                    ["Red", "Green", "Blue", "Cyan"],
                    fn + c + "Pol" +str(p), lsizef, lsizem, lop, lloc)

def TransSpecRAW(xl, xu, yl, yu, fn):
    ytop = 100
    ybottom = 50
    lsizef = 12
    lsizem = 10
    lop = 0.5
    lloc = 3
    
    p = 0
    polar = "null"
    t = "Transmission spectrums for "
    if A_OnOff == 1:
        c = "A"
        Intens, ll = get_Trans_Ints(4, c, polar)
        plot_nSpecs(4, ybottom, ytop, Wavelen, Intens,
                    t + c + " - Pol: " + str(p) + r"$^{\circ}$",
                    xl, xu, yl, yu, ll,
                    ["Red", "Green", "Blue", "Cyan"],
                    fn + c + "Pol" +str(p), lsizef, lsizem, lop, lloc)
    if B_OnOff == 1:
        c = "B"
        Intens, ll = get_Trans_Ints(9, c, polar)
        plot_nSpecs(9, ybottom, ytop, Wavelen, Intens,
                    t + c + " - Pol: " + str(p) + r"$^{\circ}$",
                    xl, xu, yl, yu, ll,
                    ["Red", "Green", "Blue", "Cyan", "Orange", "Lime",
                        "Magenta", "Brown", "Violet"],
                    fn + c + "Pol" +str(p), lsizef, lsizem, lop, lloc)
    if C_OnOff == 1:
        c = "C"
        Intens, ll = get_Trans_Ints(9, c, polar)
        plot_nSpecs(9, ybottom, ytop, Wavelen, Intens,
                    t + c + " - Pol: " + str(p) + r"$^{\circ}$",
                    xl, xu, yl, yu, ll,
                    ["Red", "Green", "Blue", "Cyan", "Orange", "Lime",
                        "Magenta", "Brown", "Violet"],
                    fn + c + "Pol" +str(p), lsizef, lsizem, lop, lloc)
    if D_OnOff == 1:
        c = "D"
        Intens, ll = get_Trans_Ints(5, c, polar)
        plot_nSpecs(5, ybottom, ytop, Wavelen, Intens,
                    t + c + " - Pol: " + str(p) + r"$^{\circ}$",
                    xl, xu, yl, yu, ll,
                    ["Red", "Green", "Blue", "Cyan", "Orange"],
                    fn + c + "Pol" +str(p), lsizef, lsizem, lop, lloc)
    if E_OnOff == 1:
        c = "E"
        Intens, ll = get_Trans_Ints(8, c, polar)
        plot_nSpecs(8, ybottom, ytop, Wavelen, Intens,
                    t + c + " - Pol: " + str(p) + r"$^{\circ}$",
                    xl, xu, yl, yu, ll,
                    ["Red", "Green", "Blue", "Cyan", "Orange", "Lime",
                        "Magenta", "Brown"],
                    fn + c + "Pol" +str(p), lsizef, lsizem, lop, lloc)

    p = 90
    polar = "90"
    t = "Transmission spectrums for "
    if A_OnOff == 1:
        c = "A"
        Intens, ll = get_Trans_Ints(4, c, polar)
        plot_nSpecs(4, ybottom, ytop, Wavelen, Intens,
                    t + c + " - Pol: " + str(p) + r"$^{\circ}$",
                    xl, xu, yl, yu, ll,
                    ["Red", "Green", "Blue", "Cyan"],
                    fn + c + "Pol" +str(p), lsizef, lsizem, lop, lloc)
    if B_OnOff == 1:
        c = "B"
        Intens, ll = get_Trans_Ints(9, c, polar)
        plot_nSpecs(9, ybottom, ytop, Wavelen, Intens,
                    t + c + " - Pol: " + str(p) + r"$^{\circ}$",
                    xl, xu, yl, yu, ll,
                    ["Red", "Green", "Blue", "Cyan", "Orange", "Lime",
                        "Magenta", "Brown", "Violet"],
                    fn + c + "Pol" +str(p), lsizef, lsizem, lop, lloc)
    if C_OnOff == 1:
        c = "C"
        Intens, ll = get_Trans_Ints(9, c, polar)
        plot_nSpecs(9, ybottom, ytop, Wavelen, Intens,
                    t + c + " - Pol: " + str(p) + r"$^{\circ}$",
                    xl, xu, yl, yu, ll,
                    ["Red", "Green", "Blue", "Cyan", "Orange", "Lime",
                        "Magenta", "Brown", "Violet"],
                    fn + c + "Pol" +str(p), lsizef, lsizem, lop, lloc)
    if D_OnOff == 1:
        c = "D"
        Intens, ll = get_Trans_Ints(5, c, polar)
        plot_nSpecs(5, ybottom, ytop, Wavelen, Intens,
                    t + c + " - Pol: " + str(p) + r"$^{\circ}$",
                    xl, xu, yl, yu, ll,
                    ["Red", "Green", "Blue", "Cyan", "Orange"],
                    fn + c + "Pol" +str(p), lsizef, lsizem, lop, lloc)
    if E_OnOff == 1:
        c = "E"
        Intens, ll = get_Trans_Ints(8, c, polar)
        plot_nSpecs(8, ybottom, ytop, Wavelen, Intens,
                    t + c + " - Pol: " + str(p) + r"$^{\circ}$",
                    xl, xu, yl, yu, ll,
                    ["Red", "Green", "Blue", "Cyan", "Orange", "Lime",
                        "Magenta", "Brown"],
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
    
    t = "Transmission spectrums for "
    if A_OnOff == 1:
        c = "A"
        lloc = 3
        diameter = [140.0, 170.0, 200.0, 230.0]
        
        p = 0
        polar = "null"
        first = 350
        last = 550
        p0 = [800.0, 80.0, 20.0]
        Intens, ll = get_Trans_Ints(4, c, polar)
        mA0, dmA0 = plot_nSpecsFIT(0, 4, ybottom, ytop, first, last, Wavelen,
                                   Intens,
                                   t + c + " - Pol: " + str(p) + r"$^{\circ}$",
                                   xl, xu, yl, yu, ll, p0,
                                   ["Red", "Green", "Blue", "Cyan"],
                                   fn + c + "Pol" +str(p), lsizef, lsizem, lop,
                                   lloc)
        p = 90
        polar = "90"
        first = 300
        last = 650
        p0 = [800.0, 1.0, 20.0]
        Intens, ll = get_Trans_Ints(4, c, polar)
        mA90, dmA90 = plot_nSpecsFIT(0, 4, ybottom, ytop, first, last, Wavelen,
                                     Intens,
                                     t+c + " - Pol: " + str(p) + r"$^{\circ}$",
                                     xl, xu, yl, yu, ll, p0,
                                     ["Red", "Green", "Blue", "Cyan"],
                                     fn + c + "Pol" +str(p), lsizef, lsizem,
                                     lop, lloc)
        plt.figure()
        
        plt.errorbar(diameter, mA0, dmA0, fmt=".", color="red",
                     label=r"Pol: $0^{\circ}$")
        plt.errorbar(diameter, mA90, dmA90, fmt=".", color="green",
                     label=r"Pol: $90^{\circ}$")
        
        diameter = np.array(diameter)
        mA0 = np.array(mA0)
        mA90 = np.array(mA90)
        f, varianz = op.curve_fit(gerade, diameter, mA0, maxfev=100000)
        df = np.sqrt(np.sqrt(varianz.diagonal()**2))
        
        fitted_x = np.linspace(np.min(diameter), np.max(diameter), 1000)
        fitted_y = gerade(fitted_x, *f)
        
        plt.plot(fitted_x, fitted_y, "--", color="red", label="y = m*x + n\n"+
                 u"m: (%.2e±%.2e)" % (f[0], df[0]) +
                 u"   n: (%.2e±%.2e)" % (f[1], df[1]))
        
        f, varianz = op.curve_fit(gerade, diameter, mA90, maxfev=100000)
        df = np.sqrt(np.sqrt(varianz.diagonal()**2))
        
        fitted_x = np.linspace(np.min(diameter), np.max(diameter), 1000)
        fitted_y = gerade(fitted_x, *f)
        
        plt.plot(fitted_x, fitted_y, "--", color="green",
                 label="y = m*x + n\n"+
                 u"m: (%.2e±%.2e)" % (f[0], df[0]) +
                 u"   n: (%.2e±%.2e)" % (f[1], df[1]))
        
        # set axis labels
        plt.title("Position of transmission minima for COLOUM: " + c)
        plt.xlabel("Disk Diameter /nm")
        plt.ylabel("Wavelength /nm")
        
        #plt.ylim(400, 1200)
        
        # place a Legend in the plot
        set_legend(lsizef, 3, lop, 4)
        
        # display grid
        plt.grid(True)
        
        # save the plot in file
        write_file("MinimaPos" + c)
        plt.close()
        
    if B_OnOff == 1:
        c = "B"
        lloc = 2
        diameter = [250.0, 275.0, 300.0, 325.0, 350.0, 375.0, 400.0, 425.0,
                    450.0]
        
        p = 0
        polar = "null"
        first = 450
        last = 600
        p0 = [900.0, 60.0, 40.0]
        Intens, ll = get_Trans_Ints(9, c, polar)
        mB0, dmB0 = plot_nSpecsFIT(0, 9, ybottom, ytop, first, last, Wavelen,
                                   Intens,
                                   t + c + " - Pol: " + str(p) + r"$^{\circ}$",
                                   xl, xu, yl, yu, ll, p0,
                                   ["Red", "Green", "Blue", "Cyan", "Orange",
                                    "Lime", "Magenta", "Brown", "Violet"],
                                   fn + c + "Pol" +str(p), lsizef, lsizem, lop,
                                   lloc)
        p = 90
        polar = "90"
        first = 380
        last = 550
        p0 = [900.0, 60.0, 40.0]
        Intens, ll = get_Trans_Ints(9, c, polar)
        mB90, dmB90 = plot_nSpecsFIT(0, 9, ybottom, ytop, first, last, Wavelen,
                                     Intens,
                                     t+c + " - Pol: " + str(p) + r"$^{\circ}$",
                                     xl, xu, yl, yu, ll, p0,
                                     ["Red", "Green", "Blue", "Cyan", "Orange",
                                      "Lime", "Magenta", "Brown", "Violet"],
                                     fn + c + "Pol" +str(p), lsizef, lsizem,
                                     lop, lloc)
        plt.figure()
        
        plt.errorbar(diameter, mB0, dmB0, fmt=".", color="red",
                     label=r"Pol: $0^{\circ}$")
        plt.errorbar(diameter, mB90, dmB90, fmt=".", color="green",
                     label=r"Pol: $90^{\circ}$")
        
        diameter = np.array(diameter)
        mB0 = np.array(mB0)
        mB90 = np.array(mB90)
        
        f, varianz = op.curve_fit(oneoverrsq, diameter, mB0, maxfev=100000)
        df = np.sqrt(np.sqrt(varianz.diagonal()**2))
        
        fitted_x = np.linspace(np.min(diameter), np.max(diameter), 1000)
        fitted_y = oneoverrsq(fitted_x, *f)
        
        plt.plot(fitted_x, fitted_y, "--", color="red",
                 label="y = a/x**2 + b\n"+
                 u"a: (%.2e±%.2e)" % (f[0], df[0]) +
                 u"   b: (%.2e±%.2e)" % (f[1], df[1]))
        
        f, varianz = op.curve_fit(oneoverrsq, diameter[1:], mB0[1:],
                                  maxfev=100000)
        df = np.sqrt(np.sqrt(varianz.diagonal()**2))
        
        fitted_x = np.linspace(np.min(diameter), np.max(diameter), 1000)
        fitted_y = oneoverrsq(fitted_x, *f)
        
        plt.plot(fitted_x, fitted_y, "-.", color="red",
                 label="y = a/x**2 + b  (without the first data point)\n"+
                 u"a: (%.2e±%.2e)" % (f[0], df[0]) +
                 u"   b: (%.2e±%.2e)" % (f[1], df[1]))
        
        f, varianz = op.curve_fit(oneoverrsq, diameter, mB90, maxfev=100000)
        df = np.sqrt(np.sqrt(varianz.diagonal()**2))
        
        fitted_x = np.linspace(np.min(diameter), np.max(diameter), 1000)
        fitted_y = oneoverrsq(fitted_x, *f)
        
        plt.plot(fitted_x, fitted_y, "--", color="green", label="y = a/x**2 + b\n"+
                 u"a: (%.2e±%.2e)" % (f[0], df[0]) +
                 u"   b: (%.2e±%.2e)" % (f[1], df[1]))
        
        # set axis labels
        plt.title("Position of transmission minima for COLOUM: " + c)
        plt.xlabel("Mid-to-Mid Distance /nm")
        plt.ylabel("Wavelength /nm")
        
        #plt.ylim(400, 1200)
        
        # place a Legend in the plot
        set_legend(lsizef, 3, lop, 4)
        
        # display grid
        plt.grid(True)
        
        # save the plot in file
        write_file("MinimaPos" + c)
        plt.close()
        
    if C_OnOff == 1:
        c = "C"
        lloc = 3
        diameter = [300.0, 325.0, 350.0, 375.0, 400.0, 425.0, 450.0, 475.0,
                    500.0]
        
        p = 0
        polar = "null"
        first = 400
        last = 600
        p0 = [800.0, 80.0, 20.0]
        Intens, ll = get_Trans_Ints(9, c, polar)
        mC0, dmC0 = plot_nSpecsFIT(0, 9, ybottom, ytop, first, last, Wavelen,
                                   Intens,
                                   t + c + " - Pol: " + str(p) + r"$^{\circ}$",
                                   xl, xu, yl, yu, ll, p0,
                                   ["Red", "Green", "Blue", "Cyan", "Orange",
                                    "Lime", "Magenta", "Brown", "Violet"],
                                   fn + c + "Pol" +str(p), lsizef, lsizem, lop,
                                   lloc)
        p = 90
        polar = "90"
        first = 400
        last = 600
        p0 = [800.0, 80.0, 20.0]
        Intens, ll = get_Trans_Ints(9, c, polar)
        mC90, dmC90 = plot_nSpecsFIT(0, 9, ybottom, ytop, first, last, Wavelen,
                                     Intens,
                                     t+c + " - Pol: " + str(p) + r"$^{\circ}$",
                                     xl, xu, yl, yu, ll, p0,
                                     ["Red", "Green", "Blue", "Cyan", "Orange",
                                      "Lime", "Magenta", "Brown", "Violet"],
                                     fn + c + "Pol" +str(p), lsizef, lsizem,
                                     lop, lloc)
        plt.figure()
        
        plt.errorbar(diameter, mC0, dmC0, fmt=".", color="red",
                     label=r"Pol: $0^{\circ}$")
        plt.errorbar(diameter, mC90, dmC90, fmt=".", color="green",
                     label=r"Pol: $90^{\circ}$")
        
        diameter = np.array(diameter)
        mC0 = np.array(mC0)
        mC90 = np.array(mC90)
        
        f, varianz = op.curve_fit(parabola, diameter, mC0, maxfev=100000)
        df = np.sqrt(np.sqrt(varianz.diagonal()**2))
        
        fitted_x = np.linspace(np.min(diameter), np.max(diameter), 1000)
        fitted_y = parabola(fitted_x, *f)
        
        plt.plot(fitted_x, fitted_y, "--", color="red",
                 label="y = a*x**2 + b*x + c\n"+
                 u"a: (%.2e±%.2e)" % (f[0], df[0]) +
                 u"   b: (%.2e±%.2e)" % (f[1], df[1]) +
                 u"   c: (%.2e±%.2e)" % (f[2], df[2]))
        
        f, varianz = op.curve_fit(parabola, diameter, mC90, maxfev=100000)
        df = np.sqrt(np.sqrt(varianz.diagonal()**2))
        
        fitted_x = np.linspace(np.min(diameter), np.max(diameter), 1000)
        fitted_y = parabola(fitted_x, *f)
        
        plt.plot(fitted_x, fitted_y, "--", color="green",
                 label="y = a*x**2 + b*x + c\n"+
                 u"a: (%.2e±%.2e)" % (f[0], df[0]) +
                 u"   b: (%.2e±%.2e)" % (f[1], df[1]) +
                 u"   c: (%.2e±%.2e)" % (f[2], df[2]))
        
        # set axis labels
        plt.title("Position of transmission minima for COLOUM: " + c)
        plt.xlabel("Period /nm")
        plt.ylabel("Wavelength /nm")
        
        #plt.ylim(400, 1200)
        
        # place a Legend in the plot
        set_legend(lsizef, 3, lop, 2)
        
        # display grid
        plt.grid(True)
        
        # save the plot in file
        write_file("MinimaPos" + c)
        plt.close()
        
    if D_OnOff == 1:
        c = "D"
        lloc = 3
        diameter = [150.0, 160.0, 170.0, 180.0, 190.0]
        
        p = 0
        polar = "null"
        first = 300
        last = 550
        p0 = [800.0, 100.0, 20.0]
        Intens, ll = get_Trans_Ints(5, c, polar)
        mD0, dmD0 = plot_nSpecsFIT(0, 5, ybottom, ytop, first, last, Wavelen,
                                   Intens,
                                   t + c + " - Pol: " + str(p) + r"$^{\circ}$",
                                   xl, xu, yl, yu, ll, p0,
                                   ["Red", "Green", "Blue", "Cyan", "Orange"],
                                   fn + c + "Pol" +str(p), lsizef, lsizem, lop,
                                   lloc)
        p = 90
        polar = "90"
        first = 300
        last = 500
        p0 = [800.0, 100.0, 20.0]
        Intens, ll = get_Trans_Ints(5, c, polar)
        mD90, dmD90 = plot_nSpecsFIT(0, 5, ybottom, ytop, first, last, Wavelen,
                                     Intens, 
                                     t+c + " - Pol: " + str(p) + r"$^{\circ}$",
                                     xl, xu, yl, yu, ll, p0,
                                     ["Red", "Green", "Blue", "Cyan","Orange"],
                                     fn + c + "Pol" +str(p), lsizef, lsizem,
                                     lop, lloc)
        plt.figure()
        
        plt.errorbar(diameter, mD0, dmD0, fmt=".", color="red",
                     label=r"Pol: $0^{\circ}$")
        plt.errorbar(diameter, mD90, dmD90, fmt=".", color="green",
                     label=r"Pol: $90^{\circ}$")
        
        mD90 = [mD90[0], mD90[1], mD90[3], mD90[4]]
        
        diameter = np.array(diameter)
        mD0 = np.array(mD0)
        mD90 = np.array(mD90)
        
        f, varianz = op.curve_fit(gerade, diameter[1:], mD0[1:], maxfev=100000)
        df = np.sqrt(np.sqrt(varianz.diagonal()**2))
        
        fitted_x = np.linspace(np.min(diameter), np.max(diameter), 1000)
        fitted_y = gerade(fitted_x, *f)
        
        plt.plot(fitted_x, fitted_y, "--", color="red", label="y = m*x + n\n"+
                 u"m: (%.2e±%.2e)" % (f[0], df[0]) +
                 u"   n: (%.2e±%.2e)" % (f[1], df[1]))
        
        diameter = [diameter[0], diameter[1], diameter[3], diameter[4]]
        diameter = np.array(diameter)
        
        f, varianz = op.curve_fit(gerade, diameter, mD90, maxfev=100000)
        df = np.sqrt(np.sqrt(varianz.diagonal()**2))
        
        fitted_x = np.linspace(np.min(diameter), np.max(diameter), 1000)
        fitted_y = gerade(fitted_x, *f)
        
        plt.plot(fitted_x, fitted_y, "--", color="green",
                 label="y = m*x + n\n"+
                 u"m: (%.2e±%.2e)" % (f[0], df[0]) +
                 u"   n: (%.2e±%.2e)" % (f[1], df[1]))
        
        # set axis labels
        plt.title("Position of transmission minima for COLOUM: " + c)
        plt.xlabel("Mid-Disk-to-Mid-Disk Distance /nm")
        plt.ylabel("Wavelength /nm")
        
        #plt.ylim(400, 1200)
        
        # place a Legend in the plot
        set_legend(lsizef, 3, lop, 4)
        
        # display grid
        plt.grid(True)
        
        # save the plot in file
        write_file("MinimaPos" + c)
        plt.close()
        
    if E_OnOff == 1:
        c = "E"
        lloc = 3
        diameter = [100.0, 120.0, 140.0, 160.0, 180.0, 200.0, 220.0, 240.0]
        
        p = 0
        polar = "null"
        first = 350
        last = 650
        p0 = [900.0, 100.0, 20.0]
        Intens, ll = get_Trans_Ints(8, c, polar)
        mE0, dmE0 = plot_nSpecsFIT(0, 8, ybottom, ytop, first, last, Wavelen,
                                   Intens,
                                   t + c + " - Pol: " + str(p) + r"$^{\circ}$",
                                   xl, xu, yl, yu, ll, p0,
                                   ["Red", "Green", "Blue", "Cyan", "Orange",
                                    "Lime", "Magenta", "Brown"],
                                   fn + c + "Pol" +str(p), lsizef, lsizem, lop,
                                   lloc)
        p = 90
        polar = "90"
        first = 230
        last = 400
        p0 = [800.0, 80.0, 20.0]
        Intens, ll = get_Trans_Ints(8, c, polar)
        mE90, dmE90 = plot_nSpecsFIT(0, 8, ybottom, ytop, first, last, Wavelen,
                                     Intens,
                                     t+c + " - Pol: " + str(p) + r"$^{\circ}$",
                                     xl, xu, yl, yu, ll, p0,
                                     ["Red", "Green", "Blue", "Cyan", "Orange",
                                      "Lime", "Magenta", "Brown"],
                                     fn + c + "Pol" +str(p), lsizef, lsizem,
                                     lop, lloc)
        plt.figure()
        
        mE0 = [mE0[0], mE0[1], mE0[2], mE0[3], mE0[4], mE0[5], mE0[7]]
        dmE0 = [dmE0[0], dmE0[1], dmE0[2], dmE0[3], dmE0[4], dmE0[5], dmE0[7]]
        diameter = [diameter[0], diameter[1], diameter[2], diameter[3],
                    diameter[4], diameter[5], diameter[7]]
        
        plt.errorbar(diameter, mE0, dmE0, fmt=".", color="red",
                     label=r"Pol: $0^{\circ}$")
        diameter = [100.0, 120.0, 140.0, 160.0, 180.0, 200.0, 220.0, 240.0]
        plt.errorbar(diameter, mE90, dmE90, fmt=".", color="green",
                     label=r"Pol: $90^{\circ}$")
        
        diameter = [diameter[0], diameter[1], diameter[2], diameter[3],
                    diameter[4],  diameter[5],  diameter[7]]
        diameter = np.array(diameter)
        mE0 = np.array(mE0)
        mE90 = np.array(mE90)
        
        f, varianz = op.curve_fit(gerade, diameter, mE0, maxfev=100000)
        df = np.sqrt(np.sqrt(varianz.diagonal()**2))
        
        fitted_x = np.linspace(np.min(diameter), np.max(diameter), 1000)
        fitted_y = gerade(fitted_x, *f)
        
        plt.plot(fitted_x, fitted_y, "--", color="red",
                 label="y = m*x + n\n"+
                 u"m: (%.2e±%.2e)" % (f[0], df[0]) +
                 u"   n: (%.2e±%.2e)" % (f[1], df[1]))
        
        diameter = [100.0, 120.0, 140.0, 160.0, 180.0, 200.0, 220.0, 240.0]
        diameter = np.array(diameter)
        f, varianz = op.curve_fit(gerade, diameter, mE90, maxfev=100000)
        df = np.sqrt(np.sqrt(varianz.diagonal()**2))
        
        fitted_x = np.linspace(np.min(diameter), np.max(diameter), 1000)
        fitted_y = gerade(fitted_x, *f)
        
        plt.plot(fitted_x, fitted_y, "--", color="green",
                 label="y = m*x + n\n"+
                 u"m: (%.2e±%.2e)" % (f[0], df[0]) +
                 u"   n: (%.2e±%.2e)" % (f[1], df[1]))
        
        # set axis labels
        plt.title("Position of transmission minima for COLOUM: " + c)
        plt.xlabel(r"$\delta_y$ Diameter /nm")
        plt.ylabel("Wavelength /nm")
        
        #plt.ylim(650, 1300)
        
        # place a Legend in the plot
        set_legend(lsizef, 3, lop, 2)
        
        # display grid
        plt.grid(True)
        
        # save the plot in file
        write_file("MinimaPos" + c)
        plt.close()
        


"""============================================================================
MAIN --- running procedures
===============================================================================
"""
# What to do?       0 = Do Not Do It        1 = Do It
savefig_pdf = 0
savefig_png = 1
msize = 2

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


