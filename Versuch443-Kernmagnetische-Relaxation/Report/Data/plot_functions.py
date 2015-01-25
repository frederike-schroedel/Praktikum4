#-*- coding: utf-8 -*-
# Import all neccessary packages
import matplotlib.pyplot as plt
import numpy as np
import scipy.optimize as op
import scipy.signal as sig
import data_handling as dh
import calculations as calc

savefig_pdf = 0
savefig_png = 0

screenlogging = True


# figure settings
dpi = 200
msize_leg = 2
leg_linewidth = 3.0
leg_anchor_x = 1
leg_anchor_y = 0.5

"""============================================================================
save a plot under given filename as .pdf as well as .png
and other useful stuff...
===============================================================================
"""
def write_file(filename):
    filename = filename.replace(" ", "")
    filename = filename.replace(":", "")
    filename = filename.replace(".", "_")
    filename = filename.replace("---", "-")
    
    # show small side margins
    plt.margins(0.05, 0.05)
    
    if screenlogging == True:
        print ("        Writing: ../Figures/%-30s" % filename, end="")
    if savefig_pdf == 1:
        plt.savefig("../Figures/" + filename + ".pdf", dpi=dpi)
    
    if savefig_png == 1:
        plt.savefig("../Figures/" + filename + ".png", dpi=dpi)
    
    if screenlogging == True:
        print (" DONE!")
    
def write_file_leg(filename, leg):
    filename = filename.replace(" ", "")
    filename = filename.replace(":", "")
    filename = filename.replace(".", "_")
    filename = filename.replace("---", "-")
    
    # show small side margins
    plt.margins(0.05, 0.05)
    
    if screenlogging == True:
        print ("        Writing: ../Figures/" + filename)
    if savefig_pdf == 1:
        plt.savefig("../Figures/" + filename + ".pdf", dpi=dpi,
                    bbox_extra_artists=(leg,), bbox_inches="tight")
    
    if savefig_png == 1:
        plt.savefig("../Figures/" + filename + ".png", dpi=dpi,
                    bbox_extra_artists=(leg,), bbox_inches="tight")

def set_legend(fsize, msize, opac, location, outside):
    if outside == False:
        leg = plt.legend(prop={'size':fsize}, loc=location, numpoints=1,
                        markerscale=msize_leg, fancybox=True)
        leg.get_frame().set_alpha(opac)
        for legobj in leg.legendHandles:
            legobj.set_linewidth(leg_linewidth)
        return leg
    else:
        leg = plt.legend(prop={'size':fsize}, loc="center left", numpoints=1,
                        markerscale=msize_leg, fancybox=True,
                        bbox_to_anchor=(leg_anchor_x,leg_anchor_y))
        leg.get_frame().set_alpha(opac)
        for legobj in leg.legendHandles:
            legobj.set_linewidth(leg_linewidth)
        return leg

def set_log_axis(x, y):
    if x == True:
        plt.xscale('log')
    if y == True:
        plt.yscale('log')

plt.rc('text', usetex=True)
plt.rcParams['text.latex.unicode']=True
plt.rcParams['text.latex.preamble'] = [
    r'\usepackage[ngerman]{babel}',
    r'\usepackage[separate-uncertainty  = true,uncertainty-separator =  {\,},output-decimal-marker ={,}, multi-part-units      = brackets,range-units           = brackets,range-phrase          = {\,--\,}]{siunitx}',   # i need upright \micro symbols, but you need...
    r'\sisetup{detect-all}',   # ...this to force siunitx to actually use your fonts
    r'\usepackage{helvet}',    # set the normal font here
    r'\usepackage{sansmath}',  # load up the sansmath so that math -> helvet
    r'\sansmath'               # <- tricky! -- gotta actually tell tex to use!
    ]  


"""============================================================================
Fitting functions
===============================================================================
"""

M0 = 0


def f_saet(x, M0, T1):
    if T1 > 0:
        return M0*(1-np.exp(-x/T1))
    else:
        return 1e5

def f_pol(x, M0, T1):
    f = M0*(1-2*np.exp(-x/T1))
    return f

def f_hahn(x, M0, T2):
    f = M0*np.exp(-(x)/T2)
    return f

def f_fid(x, a, b, c):
    if 1:#(b > 0):
        return (a*np.exp(-(x/b)+c))
    else:
        return 1e5

def f_carr(x, M0, T2):
    f = M0*np.exp(-(x)/T2)
    return f

def f_mg(x, M0, T2):
    f = M0*np.exp(-(x)/T2)
    return f

def f_rabi_a(x, a, b, d):
    if 1:#a < 4.0 and b > 0.4 and d < 2.5:
        return (a*np.sin(b*x))+d
    else:
        return 1e5

def f_rabi_b(x, a, b, d):
    if a < 10.0 and b > 0.4 and d < 2.5:
        return  np.sqrt((a*np.sin(b*x))**2)+d
    else:
        return 1e5

def peak_management(x, y):
    w = np.arange(1,10)
    
    peaks = sig.find_peaks_cwt(y, w,
                               max_distances=w/4,
                               noise_perc=25,
                               min_snr=1,
                               gap_thresh=2)
    
    peaksx = []
    peaksy = []
    
    for i in peaks:
        peaksx.append(x[i])
        peaksy.append(y[i])
    
    #plt.plot(peaksx, peaksy, ".", markersize=2*msize, label="Maxima1",
             #color="black")
    
    peaksx = []
    peaksy = []
    newpeaks = []
    
    i = 0
    while i < len(peaks)-1:
        if (len(peaksx) == 0 and y[peaks[i]] > 1):
            peaksx.append(x[peaks[i]])
            peaksy.append(y[peaks[i]])
            newpeaks.append(peaks[i])
        else:
            if len(peaksx) != 0 and y[peaks[i]] > y[peaks[i+1]] and y[peaks[i]] > 0.25:
                peaksx.append(x[peaks[i]])
                peaksy.append(y[peaks[i]])
                newpeaks.append(peaks[i])
        i += 1
    
    #plt.plot(peaksx, peaksy, ".", markersize=2*msize, label="Maxima1",
             #color="blue")
    
    peaksx = []
    peaksy = []
    
    peaks = newpeaks
    newpeaks = []
    
    i = 0
    while i < len(peaks):
        if i == 1000:
            print ("Emergency stop!!!!")
            break
        if i == len(peaks)-1:
            peaksx.append(x[peaks[i]])
            peaksy.append(y[peaks[i]])
            newpeaks.append(peaks[i])
        else:
            if y[peaks[i]] > y[peaks[i+1]]:
                peaksx.append(x[peaks[i]])
                peaksy.append(y[peaks[i]])
                newpeaks.append(peaks[i])
        i += 1
    
    #plt.plot(peaksx, peaksy, ".", markersize=2*msize, label="Maxima",
             #color="green")
    
    peaks = newpeaks
    dist = []
    
    i = 0
    while i < len(peaksx)-1:
        if i == 1000:
            print ("Emergency stop!!!!")
            break
        dist.append(x[peaks[i+1]]-x[peaks[i]])
        i += 1
    
    Averagex = np.mean(dist)
    
    #print(Averagex)
    
    peaksx = []
    peaksy = []
    
    i = 0
    while i < len(peaks):
        if i == 1000:
            print ("Emergency stop!!!!")
            break
        if i == 0:
            peaksx.append(x[peaks[i]])
            peaksy.append(y[peaks[i]])
        else:
            if x[peaks[i]]-x[peaks[i-1]] < Averagex*1.4:
                peaksx.append(x[peaks[i]])
                peaksy.append(y[peaks[i]])
        i += 1
    
    #plt.plot(peaksx, peaksy, ".", markersize=2*msize, label="Maxima",
             #color="orange")
    
    #print(Averagex)
    
    peaksx = []
    peaksy = []
    
    i = 0
    while i < len(peaks):
        if i == 1000:
            print ("Emergency stop!!!!")
            break
        if i == 0:
            peaksx.append(x[peaks[i]])
            peaksy.append(y[peaks[i]])
        else:
            if x[peaks[i]]-x[peaks[i-1]] > Averagex*0.8:
                peaksx.append(x[peaks[i]])
                peaksy.append(y[peaks[i]])
        i += 1
    
    return peaksx, peaksy

"""============================================================================
create a plot of a single graph 
===============================================================================
"""
def plot_xy(fn, x, xlabel, y, ylabel, label, title, style, fsize, msize, opac, location, xlog, ylog):
    plt.figure()
    
    # plot y against x
    plt.plot(x, y, style, markersize=msize, label=ylabel)
    
    # set axis labels
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(label)
    
    # place a Legend in the plot
    leg = set_legend(fsize, msize, opac, location, False)
    
    # display grid
    plt.grid(True)
    
    set_log_axis(xlog, ylog)
    
    # save the plot in file
    write_file(fn)
    plt.close()

def plot_xy_decay(fn, x, xlabel, y, ylabel, label, title, style, fsize, msize, opac, location, xlog, ylog):
    plt.figure()
    
    # plot y against x
    plt.plot(x, y, style, markersize=msize, label=ylabel)
    
    func = f_fid
    func_form = r"$M(\tau)=M_0\exp{\left(-\frac{\tau}{T_{2}^{*}}+c\right)}$"
    
    xfit = []
    yfit = []
    
    xmin = 1.5
    xmax = 4.5
    
    i = 0
    while i < len(x):
        if i == 1000:
            print ("Emergency Stop!!!!")
            break
        if x[i] > xmin and x[i] < xmax:
            xfit.append(x[i])
            yfit.append(y[i])
        i += 1
    
    xfit = np.array(xfit)
    yfit = np.array(yfit)
    
    #print (xfit.shape)
    #print (yfit.shape)
    
    # Fit functions
    f, varianz = op.curve_fit(func, xfit, yfit, maxfev=1000000)
    df = np.sqrt(np.sqrt(varianz.diagonal()**2))
    
    fitted_x = np.linspace(0, xmin, 1000)
    fitted_y = func(fitted_x, *f)
    plt.plot(fitted_x, fitted_y, "--", color="green")
    
    fitted_x = np.linspace(xmax, 9, 1000)
    fitted_y = func(fitted_x, *f)
    plt.plot(fitted_x, fitted_y, "--", color="green")
    
    fitted_x = np.linspace(xmin, xmax, 1000)
    fitted_y = func(fitted_x, *f)
    plt.plot(fitted_x, fitted_y, "--", color="red",
             label="Angepasste Funktion: \n" + func_form +
             "\n" +
             r"$M_0=\SI{%s(%s)}{\volt}$" % (str(round(f[0],3)),
                                            str(round(df[0],4))[-2:]) +
             "\ \ \ \ " +
             r"$T_2^*=\SI{%s(%s)}{\milli\second}$" % (str(round(f[1],3)),
                                                    str(round(df[1],4))[-2:]) +
             "\n" +
             r"$c=\SI{%s(%s)}{\volt}$" % (str(round(f[2],3)),
                                            str(round(df[2],4))[-2:]))
    
    # set axis labels
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(label)
    
    plt.xlim(-1,10)
    
    # place a Legend in the plot
    leg = set_legend(fsize, msize, opac, location, False)
    
        
    # display grid
    plt.grid(True)
    
    set_log_axis(xlog, ylog)
    
    # save the plot in file
    write_file(fn)
    plt.close()

def plot_xy_maxfit(fn, x, xlabel, y, ylabel, label, title, style, fsize, msize, opac, location, xlog, ylog):
    plt.figure()
    
    # plot y against x
    plt.plot(x, y, style, markersize=msize, label=ylabel)
    
    peaksx, peaksy = peak_management(x, y)
    plt.plot(peaksx, peaksy, ".", markersize=2*msize, label="Maxima",
             color="red")
    
    peaksx = np.array(peaksx[1:])
    peaksy = np.array(peaksy[1:])
    
    if fn[-5:-1] == "Carr":
        func = f_carr
    if fn[-7:-1] == "MG_env":
        func = f_mg
        #if fn[-1] == "1" or fn[-1] == "3":
            #ende = 15
            #peaksx = np.array(peaksx[:ende])
            #peaksy = np.array(peaksy[:ende])
    
    func_form = r"$M(\tau)=M_0\exp{\left(-\frac{\tau}{T_2}\right)}$"
    
    xfit = []
    yfit = []
    
    xmin = 2
    xmax = 50
    
    i = 0
    while i < len(peaksx):
        if i == 1000:
            print ("Emergency Stop!!!!")
            break
        if peaksx[i] > xmin and peaksx[i] < xmax:
            xfit.append(peaksx[i])
            yfit.append(peaksy[i])
        i += 1
    
    xfit = np.array(xfit)
    yfit = np.array(yfit)
    
    # Fit functions
    f, varianz = op.curve_fit(func, xfit, yfit, maxfev=1000000)
    df = np.sqrt(np.sqrt(varianz.diagonal()**2))
    
    fitted_x = np.linspace(0, xmin, 1000)
    fitted_y = func(fitted_x, *f)
    plt.plot(fitted_x, fitted_y, "--", color="green")
    
    fitted_x = np.linspace(xmax, 100, 1000)
    fitted_y = func(fitted_x, *f)
    plt.plot(fitted_x, fitted_y, "--", color="green")
    
    fitted_x = np.linspace(xmin, xmax, 1000)
    fitted_y = func(fitted_x, *f)
    plt.plot(fitted_x, fitted_y, "--", color="red",
             label="Angepasste Funktion: \n" + func_form +
             "\n" + r"$M_0=\SI{%s(%s)}{\volt}$" % (str(round(f[0],3)),
                                              str(round(df[0],4))[-2:]) +
             "\ \ \ \ " + r"$T_2=\SI{%s(%s)}{\milli\second}$" %
             (str(round(f[1],3)), str(round(df[1],4))[-2:]))
    
    # set axis labels
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(label)
    
    plt.xlim(-5,100)
    
    # place a Legend in the plot
    leg = set_legend(fsize, msize, opac, location, False)
    
    # display grid
    plt.grid(True)
    
    set_log_axis(xlog, ylog)
    
    # save the plot in file
    write_file(fn)
    plt.close()

def plot_xy_vlines(fn, x, xlabel, y , ylabel, title, PulseNr, HeFlash, PulseStart, InterpulseStart, style, fsize, msize, opac, location, xlog, ylog):
    plt.figure()
    
    # plot y against x
    plt.plot(x, y, style, markersize=msize, label=ylabel)
    
    lw = 0.7
    
    plt.axvline(x=HeFlash[0],
                linewidth=lw, markersize=msize, color="green",
                label="He-Flash")
    plt.axvline(x=PulseStart[0],
                linewidth=lw, markersize=msize, color="orange",
                label="Start of Pulse")
    plt.axvline(x=InterpulseStart[0],
                linewidth=lw, markersize=msize, color="red",
                label="End of Pulse")
    
    i = 1
    while i < len(PulseNr):
        plt.axvline(x=HeFlash[i],
                    linewidth=lw, markersize=msize, color="green")
        plt.axvline(x=PulseStart[i],
                    linewidth=lw, markersize=msize, color="orange")
        plt.axvline(x=InterpulseStart[i],
                    linewidth=lw, markersize=msize, color="red")
        i += 1
    
    # set axis labels
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    
    # place a Legend in the plot
    leg = set_legend(fsize, msize, opac, location, False)
    
    # display grid
    plt.grid(True)
    
    set_log_axis(xlog, ylog)
    
    # save the plot in file
    write_file(fn)
    plt.close()

def plot_xy_fit(fn, f, df, a, b, x, xlabel, y, ylabel, title, fsize, msize, opac, location, xlog, ylog):
    plt.figure()
    
    # Plotte die Originaldaten. Da es Messdaten sind, werden sie nicht mit
    # einer Linie verbunden.
    plt.plot(x, y, ".", markersize=msize, label=ylabel)
    
    # polytropic fit
    x1 = x[:a+1]
    x2 = x[a:b]
    x3 = x[b-1:]
    
    fitted_ex1 = np.linspace(np.min(x1)-1, np.max(x1), 1000)
    fitted_ey11, fitted_ey12 = polytropic_FIT(fitted_ex1, *f)
    fitted_ey1 = fitted_ey11 + fitted_ey12 
    fitted_ex2 = np.linspace(np.min(x3), np.max(x3)+1, 1000)
    fitted_ey21, fitted_ey22 = polytropic_FIT(fitted_ex2, *f)
    fitted_ey2 = fitted_ey21 + fitted_ey22 
    
    fitted_x2 = np.linspace(np.min(x2), np.max(x2), 1000)
    fitted_y21, fitted_y22 = polytropic_FIT(fitted_x2, *f)
    fitted_y2 = fitted_y21 + fitted_y22 
    
    fitted_fx = np.linspace(np.min(x)-1, np.max(x)+1, 1000)
    fitted_f1y, fitted_f2y = polytropic_FIT(fitted_fx, *f)
    
    #fitted_x = np.logspace(np.min(np.log10(x)), np.max(np.log10(x)), num=1000)
    #fitted_y = func(fitted_x, *f)

    # Plotte die Anpassungsfunktion. Diesmal ohne Punkte, aber mit einer Linie.
    plt.plot(fitted_x2, fitted_y2, "--", color="green",
             label="Fitting Result: f1 + f2")
    
    plt.plot(fitted_fx, fitted_f1y, "-.", color="orange", label="f1:" +
             u"\na1: (%-3.2e±%-3.2e)" % (f[0], df[0]) +
             u"  b1: (%-3.2e±%-3.2e)" % (f[1], df[1]) +
             u"\nm1: (%-3.2e±%-3.2e)" % (f[2], df[2]) +
             u"  n1: (%-3.2e±%-3.2e)" % (f[3], df[3]))
    plt.plot(fitted_fx, fitted_f2y, "-.", color="violet", label="f2:" +
             u"\na2: (%-3.2e±%-3.2e)" % (f[4], df[4]) +
             u"  b2: (%-3.2e±%-3.2e)" % (f[5], df[5]) +
             u"\nm2: (%-3.2e±%-3.2e)" % (f[6], df[6]) +
             u"  n2: (%-3.2e±%-3.2e)" % (f[7], df[7]))
    
    plt.plot(fitted_ex1, fitted_ey1, "--", color="red", label="Extrapolation")
    plt.plot(fitted_ex2, fitted_ey2, "--", color="red")
    
    # set axis labels
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    
    #plt.ylim(1e-8,1e0)
    #plt.xlim(0.844,0.847)
    
    set_log_axis(xlog, ylog)
    
    # place a Legend in the plot
    leg = set_legend(fsize, msize, opac, location, False)
    
    # display grid
    plt.grid(True)
    
    # save the plot in file
    write_file(fn)
    plt.close()
    
    return f, df

def plot_xy_list(*parameters):
    (fn, xlist, xlabel, ylist , ylabel, title, xlow, xhigh, every, style,
     fsize, msize, opac, location, xlog, ylog) = parameters
    plt.figure()
    
    # plot y against x 
    i = 0
    while i < len(xlist):
        if i % every == 0:
            x = xlist[i]
            y = ylist[i]
            plt.plot(x, y, style, label=ylabel + "  i: " + str(i))
        i += 1
    

    # set axis labels
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    
    set_log_axis(xlog, ylog)
    
    plt.xlim([xlow, xhigh])
    
    # place a Legend in the plot
    leg = set_legend(fsize, msize, opac, location, False)

    
    # display grid
    plt.grid(True)
    
    # save the plot in file
    write_file(fn)
    plt.close()

def plot_xy_error(fn, x, xlabel, y , ylabel, yerror, label, title, style, fsize, msize, opac, location, xlog, ylog):
    plt.figure()
    
    plt.errorbar(x, y, yerr=yerror, fmt=style, markersize=msize, label=label)
    
    #global M0
    
    if fn[0:3] == "Sae":
        T = 1
        func = f_saet
        func_form = r"$M(\tau)=M_0\left(1-\exp{\left(-\frac{\tau}{T_1}\right)}\right)$"
    
    if fn[0:3] == "Pol":
        T = 1
        func = f_pol
        #x = x[1:]
        #y = y[1:]
        func_form = r"$M(\tau)=M_0\left(1-2\exp{\left(-\frac{\tau}{T_1}\right)}\right)$"
    
    if fn[0:3] == "Hom":
        T = 2
        func = f_hahn
        func_form = r"$M(\tau)=M_0\exp{\left(-\frac{\tau}{T_2}\right)}$"
    
    # Fit functions
    f, varianz = op.curve_fit(func, x, y, maxfev=1000000)
    df = np.sqrt(np.sqrt(varianz.diagonal()**2))
    
    fitted_x = np.linspace(np.min(x), np.max(x), 1000)
    fitted_y = func(fitted_x, *f)
    plt.plot(fitted_x, fitted_y, "--", color="green",
             label="Angepasste Funktion: \n" + func_form +
             "\n" + r"$M_0=\SI{%s(%s)}{\volt}$" % (str(round(f[0],3)),
                                              str(round(df[0],4))[-2:]) +
             "\n" + r"$T_%s=\SI{%s(%s)}{\milli\second}$" %
             (str(T), str(round(f[1],3)), str(round(df[1],4))[-2:]))
    
    # set axis labels
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    
    #plt.ylim(0,12)
    
    # place a Legend in the plot
    leg = set_legend(fsize, msize, opac, location, True)
    
    # display grid
    plt.grid(True)
    
    set_log_axis(xlog, ylog)
    
    # save the plot in file
    write_file_leg(fn, leg)
    plt.close()

def plot_xy_errorlist(fn, xlist, xlabel, ylist , ylabel, yerrorlist, labels, title, style, fsize, msize, opac, location, xlog, ylog):
    plt.figure()
    
    colors = ["red", "green", "blue", "orange"]
    func = [f_rabi_b, f_rabi_a, f_rabi_b, f_rabi_a]
    func_form = [r"$f(x)=a |\sin{\left(b x\right)}|+d$",
                 r"$f(x)=a \sin{\left(b x\right)}+d$",
                 r"$f(x)=a |\sin{\left(b x\right)}|+d$",
                 r"$f(x)=a \sin{\left(b x\right)}+d$"]
    p0 = [[8.0, 0.5, 0], [1.0, 0.5, 0.2],
          [8.0, 0.5, 0], [1.0, 0.5, 0.2]]
    
    
    i = 0
    while i < len(xlist):
        plt.errorbar(xlist[i], ylist[i], yerr=yerrorlist[i], fmt=style,
                     markersize=msize, label=labels[i], color=colors[i])
        
        # Fit functions
        f, varianz = op.curve_fit(func[i], xlist[i], ylist[i],
                                p0=p0[i], maxfev=1000000)
        df = np.sqrt(np.sqrt(varianz.diagonal()**2))
        
        #print(f)
        
        fitted_x = np.linspace(0, 12, 1000)
        fitted_y = func[i](fitted_x, *f)
        
        plt.plot(fitted_x, fitted_y, ":", color=colors[i],
                 label=func_form[i] +
                 "\n" +
                 r"$a=\SI{%s(%s)}{}$" % (str(round(f[0],3)),
                                         str(round(df[0],4))[-2:]) +
                 "\n" +
                 r"$b=\SI{%s(%s)}{}$" % (str(round(f[1],3)),
                                         str(round(df[1],4))[-2:])+
                 "\n" +
                 r"$d=\SI{%s(%s)}{}$" % (str(round(f[2],3)),
                                         str(round(df[2],4))[-2:]))
        i += 1
    
    # set axis labels
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    
    # place a Legend in the plot
    leg = set_legend(fsize, msize, opac, location, True)
    
    # display grid
    plt.grid(True)
    
    set_log_axis(xlog, ylog)
    
    # save the plot in file
    write_file_leg(fn, leg)
    plt.close()


"""============================================================================
create two graphs in the same plot
===============================================================================
"""
def plot_x2y(fn, x, xlabel, y1 , y1label, y2 , y2label, ylabel, title, style, fsize, msize, opac, location, xlog, ylog):
    plt.figure()
    
    # plot y1 against x
    plt.plot(x, y1, style, label=y1label)
    
    # plot y2 against x
    plt.plot(x, y2, style, label=y2label, color="red")
    
    # set axis labels
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    
    # place a Legend in the plot
    leg = set_legend(fsize, msize, opac, location, False)
    
    # display grid
    plt.grid(True)
    #plt.grid(b=True, which='major', color='b', linestyle='-')
    #plt.grid(b=True, which='minor', color='r', linestyle='--')
    
    set_log_axis(xlog, ylog)
    
    # save the plot in file
    write_file(fn)
    plt.close()

def plot2_xy(fn, x, xlabel, y1, y1label, y2, y2label, title, style, fsize, msize, opac, location, xlog, ylog):
    plt.figure()
    fig, (ax1, ax2) = plt.subplots(2, sharex=True)
    
    ax1.plot(x, y1, style, markersize=msize, color="red", label=y1label)
    ax1.axhline(y=np.mean(y1), ls="--", color="red",
                label="  Average: = %.3f" % np.mean(y1))
    ax1.axhline(y=np.mean(y1)+np.sqrt(np.var(y1)/len(y1)), ls="--",
                color="orange",
                label="  Std. Err.: %.3f" % (np.sqrt(np.var(y1)/len(y1))))
    ax1.axhline(y=np.mean(y1)-np.sqrt(np.var(y1)/len(y1)), ls="--",
                color="orange")
    ax1.axhline(y=np.mean(y1)+np.sqrt(np.var(y1)), ls="--", color="green",
                label="  Std. Dev.: %.3f" % np.sqrt(np.var(y1)))
    ax1.axhline(y=np.mean(y1)-np.sqrt(np.var(y1)), ls="--", color="green")
    ax1.set_ylabel(y1label)
    ax1.set_title(title)
    
    ax2.plot(x, y2, style, markersize=msize, color="red", label=y2label)
    ax2.axhline(y=np.mean(y2), ls="--", color="red",
                label="  Average: = %.3f" % np.mean(y2))
    ax2.axhline(y=np.mean(y2)+np.sqrt(np.var(y2)/len(y2)), ls="--",
                color="orange",
                label="  Std. Err.: %.3f" % (np.sqrt(np.var(y2)/len(y2))))
    ax2.axhline(y=np.mean(y2)-np.sqrt(np.var(y2)/len(y2)), ls="--",
                color="orange")
    ax2.axhline(y=np.mean(y2)+np.sqrt(np.var(y2)), ls="--", color="green",
                label="  Std. Dev.: %.3f" % np.sqrt(np.var(y2)))
    ax2.axhline(y=np.mean(y2)-np.sqrt(np.var(y2)), ls="--", color="green")
    ax2.set_ylabel(y2label)
    ax2.set_xlabel(xlabel)
    
    # fine-tuning
    fig.subplots_adjust(hspace=0)   # move plots closer together
    plt.setp([a.get_xticklabels() for a in fig.axes[:-1]], visible=False)
    
    # place a Legend in the plot
    leg1 = ax1.legend(prop={'size':fsize}, loc = location, numpoints=1,
                      markerscale=msize_leg, fancybox=True)
    leg1.get_frame().set_alpha(opac)
    leg2 = ax2.legend(prop={'size':fsize}, loc = location, numpoints=1,
                      markerscale=msize_leg, fancybox=True)
    leg2.get_frame().set_alpha(opac)
    
    if xlog == True:
        ax1.set_xscale('log')
        ax2.set_xscale('log')
    
    if ylog == True:
        ax1.set_yscale('log')
        ax2.set_yscale('log')
    
    # display grid
    ax1.grid(True)
    ax2.grid(True)
    
    #ax1.set_ylim(0.5*(sum(y1)/len(y1)), 1.5*(sum(y1)/len(y1)))
    #ax2.set_ylim(0.5*(sum(y2)/len(y2)), 1.5*(sum(y2)/len(y2)))
    
    # save the plot in file
    write_file(fn)
    plt.close()

def plot2_xy_list(*parameters):
    (fn, xlist, xlabel, y1list , y1label, y2list , y2label, title, xlow, xhigh,
     every, style, fsize, msize, opac, location, xlog, ylog) = parameters
    plt.figure()
    fig, (ax1, ax2) = plt.subplots(2, sharex=True)
    
    # plot y against x 
    i = 0
    while i < len(xlist):
        if i % every == 0:
            x = xlist[i]
            y1 = y1list[i]
            y2 = y2list[i]
            ax1.plot(x, y1, style, label=y1label + "  i: " + str(i))
            ax2.plot(x, y2, style, label=y2label + "  i: " + str(i))
        i += 1
    

    fig.subplots_adjust(hspace=0)
    
    # set axis labels
    ax1.set_title(title)
    ax2.set_xlabel(xlabel)
    ax1.set_ylabel(y1label)
    ax2.set_ylabel(y2label)
    
    if xlog == True:
        ax1.set_xscale('log')
        ax2.set_xscale('log')
    
    if ylog == True:
        ax1.set_yscale('log')
        ax2.set_yscale('log')
    
    ax1.set_xlim([xlow, xhigh])
    ax2.set_xlim([xlow, xhigh])
    
    # place a Legend in the plot
    leg1 = ax1.legend(prop={'size':9}, loc = 1, numpoints=1,
                        fancybox=True)
    leg1.get_frame().set_alpha(0.5)
    leg2 = ax2.legend(prop={'size':9}, loc = 1, numpoints=1,
                        fancybox=True)
    leg2.get_frame().set_alpha(0.5)
    
    # display grid
    ax1.grid(True)
    ax2.grid(True)
    
    # save the plot in file
    write_file(fn)
    plt.close()



"""============================================================================
create three graphs in the same plot
===============================================================================
"""
def plot_x3y(fn, x, xlabel, y1 , y1label, y2 , y2label, y3 , y3label, ylabel, title, style, fsize, msize, opac, location, xlog, ylog):
    plt.figure()
    
    # plot y1 against x
    plt.plot(x, y1, style, label=y1label)
    
    # plot y2 against x
    plt.plot(x, y2, style, label=y2label)
    
    # plot y3 against x
    plt.plot(x, y3, style, label=y3label)
    
    # set axis labels
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    
    # place a Legend in the plot
    leg = set_legend(fsize, msize, opac, location, False)
    
    # display grid
    #plt.minorticks_on
    plt.grid(True)
    #plt.grid(b=True, which='major', color='b', linestyle='-')
    #plt.grid(b=True, which='minor', color='r', linestyle='--')
    
    set_log_axis(xlog, ylog)
    
    # save the plot in file
    write_file(fn)
    plt.close()

def plot_x3y_averages(fn, x, xlabel, y1 , y1label, y2 , y2label, y3 , y3label, ylabel, title, style, fsize, msize, opac, location, xlog, ylog):
    plt.figure()
    
    l = 0.3
    
    # plot y1 against x
    ave1 = [np.mean(y1), np.sqrt(np.var(y1)/len(y1))]
    ave2 = [np.mean(y2), np.sqrt(np.var(y2)/len(y2))]
    ave3 = [np.mean(y3), np.sqrt(np.var(y3)/len(y3))]
    
    plt.axhline(y=ave1[0], ls="--", lw=1.5, color="blue")
    plt.axhline(y=ave2[0], ls="--", lw=1.5, color="green")
    plt.axhline(y=ave3[0], ls="--", lw=1.5, color="red")
    
    plt.plot(x, y1, style, linewidth=l,
             label=y1label + " -- Offset:\n" + r"$U^{env}_0 = " +
             r"\SI{%s(%s)}{\volt}$" % (str(round(ave1[0],3)),
                                       str(round(ave1[1],4))[-2:]))
    
    # plot y2 against x
    plt.plot(x, y2, style, linewidth=l,
             label=y2label + " -- Offset:\n" + r"$U^{env}_0 = " +
             r"\SI{%s(%s)}{\volt}$" % (str(round(ave2[0],3)),
                                       str(round(ave2[1],4))[-2:]))
    
    # plot y3 against x
    plt.plot(x, y3, style, linewidth=l,
             label=y3label + " -- Offset:\n" + r"$U^{env}_0 = " +
             r"\SI{%s(%s)}{\volt}$" % (str(round(ave3[0],3)),
                                       str(round(ave3[1],4))[-2:]))
    
    # set axis labels
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    
    plt.ylim([-0.05,0.55])
    
    # place a Legend in the plot
    leg = set_legend(fsize, msize, opac, location, True)
    
    # display grid
    #plt.minorticks_on
    plt.grid(True)
    #plt.grid(b=True, which='major', color='b', linestyle='-')
    #plt.grid(b=True, which='minor', color='r', linestyle='--')
    
    set_log_axis(xlog, ylog)
    
    # save the plot in file
    write_file_leg(fn, leg)
    plt.close()
    














