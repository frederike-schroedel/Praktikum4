#-*- coding: utf-8 -*-
import numpy as np
import scipy.optimize as op
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib import rc
rc('text', usetex=True)

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
                     markerscale=1, fancybox=True)
    leg.get_frame().set_alpha(opac)

def set_log_axis(x, y):
    if x == True:
        plt.xscale('log')
    if y == True:
        plt.yscale('log')


# What to do?       0 = Do Not Do It        1 = Do It
savefig_pdf = 0
savefig_png = 1
fsize = 12
msize = 9
opac = 0.5
location = 5

data = np.loadtxt('Tables/TemperaturInAsResultate.txt', unpack=True)

Temp = data[0]
TempInv = data[1]
sigma = data[2]
Hall = data[3]
Ladungsdichte = data[4]
Beweglichkeit = data[5]

data = np.loadtxt('Tables/TemperaturInAsResultateERRORS.txt', unpack=True)

Temp_err = data[0]
TempInv_err = data[1]
sigma_err = data[2]
Hall_err = data[3]
Ladungsdichte_err = data[4]
Beweglichkeit_err = data[5]



def plot_xy(fn, x, xerror, xlabel, y, yerror, ylabel, title, style, fsize, msize, opac, location, xlog, ylog):
    plt.figure()
    
    plt.rc('text', usetex=True)
    plt.rcParams['text.latex.preamble'] = [
        r'\usepackage{siunitx}',   # i need upright \micro symbols, but you need...
        r'\sisetup{detect-all}',   # ...this to force siunitx to actually use your fonts
        r'\usepackage{helvet}',    # set the normal font here
        r'\usepackage{sansmath}',  # load up the sansmath so that math -> helvet
        r'\sansmath'               # <- tricky! -- gotta actually tell tex to use!
        ]  
    
    # plot y against x
    plt.errorbar(x, y, xerr=xerror, yerr=yerror, fmt=style, markersize=msize, label=ylabel)
    
    # set axis labels
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    
    # place a Legend in the plot
    set_legend(fsize, msize, opac, location)
    
    # display grid
    plt.grid(True)
    
    set_log_axis(xlog, ylog)
    
    # save the plot in file
    write_file(fn)
    plt.close()


#x = Temp + [273.15]*len(Temp)
x = TempInv
xerror = TempInv_err
i = 0
while i < len(sigma_err):
    sigma_err[i]=sigma_err[i]/sigma[i]
    Hall_err[i]=Hall_err[i]/Hall[i]
    Ladungsdichte_err[i]=Ladungsdichte_err[i]/Ladungsdichte[i]
    Beweglichkeit_err[i]=Beweglichkeit_err[i]/Beweglichkeit[i]
    i += 1

plot_xy("Temp_Leitfaehigkeit", x, xerror,
        r"Temperatur $/T^{-1}$", np.log(sigma), sigma_err,
        r"Leitf\"ahigkeit $ln(\sigma_S)$",
        r"Temperaturabh\"angigkeit der Leitf\"ahigkeit",
        ".", fsize, msize, opac, location, False, False)
plot_xy("Temp_Hallkonstante", x, xerror,
        r"Temperatur $/T^{-1}$", np.log(Hall), Hall_err,
        r"Hallkonstante $ln(R_H)$",
        r"Temperaturabh\"angigkeit der Hallkonstanten",
        ".", fsize, msize, opac, location, False, False)
plot_xy("Temp_Ladungsdichte", x, xerror,
        r"Temperatur $/T^{-1}$", np.log(Ladungsdichte), Ladungsdichte_err,
        r"Ladungstr\"agerdichte $ln(p_S)$",
        r"Temperaturabh\"angigkeit der Ladungstr\"agerdichte",
        ".", fsize, msize, opac, location, False, False)
plot_xy("Temp_Beweglichkeit", x, xerror,
        r"Temperatur $/T^{-1}$", np.log(Beweglichkeit), Beweglichkeit_err,
        r"Beweglichkeit $ln(\mu_S)$",
        r"Temperaturabh\"angigkeit der Beweglichkeit",
        ".", fsize, msize, opac, location, False, False)


