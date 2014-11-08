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
