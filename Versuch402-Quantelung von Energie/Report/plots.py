import numpy as np
import scipy.optimize as op
import matplotlib.pyplot as plt
import Gnuplot


"""============================================================================
save a plot under given filename as .pdf as well as .png
===============================================================================
"""
def write_file(filename):
  print "Writing: ", filename
  plt.savefig("Figures/" + filename + ".pdf")
  plt.savefig("Figures/" + filename + ".png")



def Versuch402_1_365():
    """========================================================================
    Wellenlaenge: 365nm
    Messung:     1
    Verstaerkung: 1V = 1E-10A
    I_0:         -3.82pA
    ===========================================================================
    """
    data1 = np.loadtxt('Data/Versuch402-1_365nm_1.txt')
    U_Anode_mV_1 = data1[:, 0]
    err_U_Anode_mV_1 = data1[:, 1]
    U_Mess_mV_1 = data1[:, 2]
    err_U_Mess_mV_1 = data1[:, 3]
    I_Anode_pA_1 = data1[:, 4]
    err_I_Anode_pA_1 = data1[:, 5]
    wurzel_1 = data1[:, 6]
    err_wurzel_1 = data1[:, 7]
   
    
    """========================================================================
    Wellenlaenge: 365nm
    Messung:     2
    Verstaerkung: 1V = 1E-9A
    I_0:         44.667pA
    ===========================================================================
    """
    data2 = np.loadtxt('Data/Versuch402-1_365nm_2.txt')
    U_Anode_mV_2 = data2[:, 0]
    err_U_Anode_mV_2 = data2[:, 1]
    U_Mess_mV_2 = data2[:, 2]
    err_U_Mess_mV_2 = data2[:, 3]
    I_Anode_pA_2 = data2[:, 4]
    err_I_Anode_pA_2 = data2[:, 5]
    wurzel_2 = data2[:, 6]
    err_wurzel_2 = data2[:, 7]
    
    
    """========================================================================
    Wellenlaenge: 365nm
    Messung:     3
    Verstaerkung: 1V = 1E-8A
    I_0:         446.667pA
    ===========================================================================
    """
    data3 = np.loadtxt('Data/Versuch402-1_365nm_3.txt')
    U_Anode_mV_3 = data3[:, 0]
    err_U_Anode_mV_3 = data3[:, 1]
    U_Mess_mV_3 = data3[:, 2]
    err_U_Mess_mV_3 = data3[:, 3]
    I_Anode_pA_3 = data3[:, 4]
    err_I_Anode_pA_3 = data3[:, 5]
    wurzel_3 = data3[:, 6]
    err_wurzel_3 = data3[:, 7]
    
    plt.figure(1)
    
    # fitting functions
    first1 = 0
    last1 = -1
    f1 = np.polyfit(U_Anode_mV_1[first1:last1], wurzel_1[first1:last1], 1)
    fit_f1 = np.poly1d(f1)
    
    first2 = 0
    last2 = -4
    f2 = np.polyfit(U_Anode_mV_2[first2:last2], wurzel_2[first2:last2], 1)
    fit_f2 = np.poly1d(f2)
    
    first3 = 0
    last3 = -3
    f3 = np.polyfit(U_Anode_mV_3[first3:last3], wurzel_3[first3:last3], 1)
    fit_f3 = np.poly1d(f3)
    
    # plot y against x
    plt.errorbar(U_Anode_mV_1, wurzel_1, err_wurzel_1, label="Erste Messung",
                 fmt=".")
    plt.plot(U_Anode_mV_1, fit_f1(U_Anode_mV_1), 
             label="f1(x)=(%.4f)x+(%.4f)" % (f1[0], f1[1]))
   
    plt.errorbar(U_Anode_mV_2, wurzel_2, err_wurzel_2, label="Zweite Messung",
                 fmt=".")
    plt.plot(U_Anode_mV_2, fit_f2(U_Anode_mV_2),
             label="f2(x)=(%.4f)x+(%.4f)" % (f2[0], f2[1]))
    
    plt.errorbar(U_Anode_mV_3, wurzel_3, err_wurzel_3,
                 label="Dritte Messung", fmt=".")
    plt.plot(U_Anode_mV_3[:-1], fit_f3(U_Anode_mV_3[:-1]),
             label="f3(x)=(%.4f)x+(%.4f)" % (f3[0], f3[1]))
    
    # set axis labels
    plt.title("Versuch 402-1: 365nm")
    plt.xlabel("Anodenspannung [mV]")
    plt.ylabel("Wurzel des Anodestroms [pA]")
    
    # place a Legend in the plot
    plt.legend(prop={'size':9})
    #plt.legend(bbox_to_anchor=(0., 0.97, 1., .102), loc=3, ncol=2,
                #mode="expand", borderaxespad=0.)
    
    # display grid
    plt.grid(True)
    
    # save the plot in file
    #filename=x_label + "_" + y_label
    #filename=filename.replace(" ", "")
    write_file("Versuch402_1_365")
    return f1, f2, f3


def Versuch402_1_405():
    """========================================================================
    Wellenlaenge: 405nm
    Messung:     1
    Verstaerkung: 1V = 1E-10A
    I_0:         0.733pA
    ===========================================================================
    """
    data1 = np.loadtxt('Data/Versuch402-1_405nm_1.txt')
    U_Anode_mV_1 = data1[:, 0]
    err_U_Anode_mV_1 = data1[:, 1]
    U_Mess_mV_1 = data1[:, 2]
    err_U_Mess_mV_1 = data1[:, 3]
    I_Anode_pA_1 = data1[:, 4]
    err_I_Anode_pA_1 = data1[:, 5]
    wurzel_1 = data1[:, 6]
    err_wurzel_1 = data1[:, 7]
   
    
    """========================================================================
    Wellenlaenge: 405nm
    Messung:     2
    Verstaerkung: 1V = 1E-9A
    I_0:         46pA
    ===========================================================================
    """
    data2 = np.loadtxt('Data/Versuch402-1_405nm_2.txt')
    U_Anode_mV_2 = data2[:, 0]
    err_U_Anode_mV_2 = data2[:, 1]
    U_Mess_mV_2 = data2[:, 2]
    err_U_Mess_mV_2 = data2[:, 3]
    I_Anode_pA_2 = data2[:, 4]
    err_I_Anode_pA_2 = data2[:, 5]
    wurzel_2 = data2[:, 6]
    err_wurzel_2 = data2[:, 7]
    
    plt.figure(2)
    
    # fitting functions
    first1 = 0
    last1 = -1
    f1 = np.polyfit(U_Anode_mV_1[first1:], wurzel_1[first1:], 1)
    fit_f1 = np.poly1d(f1)
    
    first2 = 0
    last2 = -2
    f2 = np.polyfit(U_Anode_mV_2[first2:last2], wurzel_2[first2:last2], 1)
    fit_f2 = np.poly1d(f2)
    
    # plot y against x
    plt.errorbar(U_Anode_mV_1, wurzel_1, err_wurzel_1, label="Erste Messung",
                 fmt=".")
    plt.plot(U_Anode_mV_1, fit_f1(U_Anode_mV_1), 
             label="f1(x)=(%.4f)x+(%.4f)" % (f1[0], f1[1]))
   
    plt.errorbar(U_Anode_mV_2, wurzel_2, err_wurzel_2, label="Zweite Messung",
                 fmt=".")
    plt.plot(U_Anode_mV_2[:-2], fit_f2(U_Anode_mV_2[:-2]),
             label="f2(x)=(%.4f)x+(%.4f)" % (f2[0], f2[1]))
    
    # set axis labels
    plt.title("Versuch 402-1: 405nm")
    plt.xlabel("Anodenspannung [mV]")
    plt.ylabel("Wurzel des Anodestroms [pA]")
    
    # place a Legend in the plot
    plt.legend(prop={'size':9})
    #plt.legend(bbox_to_anchor=(0., 0.97, 1., .102), loc=3, ncol=2,
                #mode="expand", borderaxespad=0.)
    
    # display grid
    plt.grid(True)
    
    # save the plot in file
    #filename=x_label + "_" + y_label
    #filename=filename.replace(" ", "")
    write_file("Versuch402_1_405")
    return f1, f2


def Versuch402_1_436():
    """========================================================================
    Wellenlaenge: 436nm
    Messung:     1
    Verstaerkung: 1V = 1E-9A
    I_0:         40.95pA
    ===========================================================================
    """
    data1 = np.loadtxt('Data/Versuch402-1_436nm_1.txt')
    U_Anode_mV_1 = data1[:, 0]
    err_U_Anode_mV_1 = data1[:, 1]
    U_Mess_mV_1 = data1[:, 2]
    err_U_Mess_mV_1 = data1[:, 3]
    I_Anode_pA_1 = data1[:, 4]
    err_I_Anode_pA_1 = data1[:, 5]
    wurzel_1 = data1[:, 6]
    err_wurzel_1 = data1[:, 7]
   
    
    """========================================================================
    Wellenlaenge: 436nm
    Messung:     2
    Verstaerkung: 1V = 1E-9A
    I_0:         47pA
    ===========================================================================
    """
    data2 = np.loadtxt('Data/Versuch402-1_436nm_2.txt')
    U_Anode_mV_2 = data2[:, 0]
    err_U_Anode_mV_2 = data2[:, 1]
    U_Mess_mV_2 = data2[:, 2]
    err_U_Mess_mV_2 = data2[:, 3]
    I_Anode_pA_2 = data2[:, 4]
    err_I_Anode_pA_2 = data2[:, 5]
    wurzel_2 = data2[:, 6]
    err_wurzel_2 = data2[:, 7]
    
    plt.figure(3)
    
    # fitting functions
    first1 = 7
    last1 = -2
    f1 = np.polyfit(U_Anode_mV_1[first1:last1], wurzel_1[first1:last1], 1)
    fit_f1 = np.poly1d(f1)
    
    first2 = 0
    last2 = -1
    f2 = np.polyfit(U_Anode_mV_2[first2:last2], wurzel_2[first2:last2], 1)
    fit_f2 = np.poly1d(f2)
    
    # plot y against x
    plt.errorbar(U_Anode_mV_1, wurzel_1, err_wurzel_1, label="Erste Messung",
                 fmt=".")
    plt.plot(U_Anode_mV_1, fit_f1(U_Anode_mV_1), 
             label="f1(x)=(%.4f)x+(%.4f)" % (f1[0], f1[1]))
   
    plt.errorbar(U_Anode_mV_2, wurzel_2, err_wurzel_2, label="Zweite Messung",
                 fmt=".")
    plt.plot(U_Anode_mV_2, fit_f2(U_Anode_mV_2),
             label="f2(x)=(%.4f)x+(%.4f)" % (f2[0], f2[1]))
    
    # set axis labels
    plt.title("Versuch 402-1: 436nm")
    plt.xlabel("Anodenspannung [mV]")
    plt.ylabel("Wurzel des Anodestroms [pA]")
    
    # place a Legend in the plot
    plt.legend(prop={'size':9})
    #plt.legend(bbox_to_anchor=(0., 0.97, 1., .102), loc=3, ncol=2,
                #mode="expand", borderaxespad=0.)
    
    # display grid
    plt.grid(True)
    
    # save the plot in file
    #filename=x_label + "_" + y_label
    #filename=filename.replace(" ", "")
    write_file("Versuch402_1_436")
    return f1, f2


def Versuch402_1_546():
    """========================================================================
    Wellenlaenge: 546nm
    Messung:     1
    Verstaerkung: 1V = 1E-10A
    I_0:         2.83pA
    ===========================================================================
    """
    data1 = np.loadtxt('Data/Versuch402-1_546nm_1.txt')
    U_Anode_mV_1 = data1[:, 0]
    err_U_Anode_mV_1 = data1[:, 1]
    U_Mess_mV_1 = data1[:, 2]
    err_U_Mess_mV_1 = data1[:, 3]
    I_Anode_pA_1 = data1[:, 4]
    err_I_Anode_pA_1 = data1[:, 5]
    wurzel_1 = data1[:, 6]
    err_wurzel_1 = data1[:, 7]
   
    
    """========================================================================
    Wellenlaenge: 546nm
    Messung:     2
    Verstaerkung: 1V = 1E-9A
    I_0:         46.75pA
    ===========================================================================
    """
    data2 = np.loadtxt('Data/Versuch402-1_546nm_2.txt')
    U_Anode_mV_2 = data2[:, 0]
    err_U_Anode_mV_2 = data2[:, 1]
    U_Mess_mV_2 = data2[:, 2]
    err_U_Mess_mV_2 = data2[:, 3]
    I_Anode_pA_2 = data2[:, 4]
    err_I_Anode_pA_2 = data2[:, 5]
    wurzel_2 = data2[:, 6]
    err_wurzel_2 = data2[:, 7]
    
    plt.figure(4)
    
    # fitting functions
    first1 = 0
    last1 = -8
    f1 = np.polyfit(U_Anode_mV_1[first1:last1], wurzel_1[first1:last1], 1)
    fit_f1 = np.poly1d(f1)
    
    first2 = 0
    last2 = -4
    f2 = np.polyfit(U_Anode_mV_2[first2:last2], wurzel_2[first2:last2], 1)
    fit_f2 = np.poly1d(f2)
    
    # plot y against x
    plt.errorbar(U_Anode_mV_1, wurzel_1, err_wurzel_1, label="Erste Messung",
                 fmt=".")
    plt.plot(U_Anode_mV_1[:-1], fit_f1(U_Anode_mV_1[:-1]), 
             label="f1(x)=(%.4f)x+(%.4f)" % (f1[0], f1[1]))
   
    plt.errorbar(U_Anode_mV_2, wurzel_2, err_wurzel_2, label="Zweite Messung",
                 fmt=".")
    plt.plot(U_Anode_mV_2, fit_f2(U_Anode_mV_2),
             label="f2(x)=(%.4f)x+(%.4f)" % (f2[0], f2[1]))
    
    # set axis labels
    plt.title("Versuch 402-1: 546nm")
    plt.xlabel("Anodenspannung [mV]")
    plt.ylabel("Wurzel des Anodestroms [pA]")
    
    # place a Legend in the plot
    plt.legend(prop={'size':9})
    #plt.legend(bbox_to_anchor=(0., 0.97, 1., .102), loc=3, ncol=2,
                #mode="expand", borderaxespad=0.)
    
    # display grid
    plt.grid(True)
    
    # save the plot in file
    #filename=x_label + "_" + y_label
    #filename=filename.replace(" ", "")
    write_file("Versuch402_1_546")
    return f1, f2


def Versuch402_1_578():
    """========================================================================
    Wellenlaenge: 578nm
    Messung:     1
    Verstaerkung: 1V = 1E-10A
    I_0:         3.386pA
    ===========================================================================
    """
    data1 = np.loadtxt('Data/Versuch402-1_578nm_1.txt')
    U_Anode_mV_1 = data1[:, 0]
    err_U_Anode_mV_1 = data1[:, 1]
    U_Mess_mV_1 = data1[:, 2]
    err_U_Mess_mV_1 = data1[:, 3]
    I_Anode_pA_1 = data1[:, 4]
    err_I_Anode_pA_1 = data1[:, 5]
    wurzel_1 = data1[:, 6]
    err_wurzel_1 = data1[:, 7]
   
    
    """========================================================================
    Wellenlaenge: 578nm
    Messung:     2
    Verstaerkung: 1V = 1E-9A
    I_0:         47.2667pA
    ===========================================================================
    """
    data2 = np.loadtxt('Data/Versuch402-1_578nm_2.txt')
    U_Anode_mV_2 = data2[:, 0]
    err_U_Anode_mV_2 = data2[:, 1]
    U_Mess_mV_2 = data2[:, 2]
    err_U_Mess_mV_2 = data2[:, 3]
    I_Anode_pA_2 = data2[:, 4]
    err_I_Anode_pA_2 = data2[:, 5]
    wurzel_2 = data2[:, 6]
    err_wurzel_2 = data2[:, 7]
    
    plt.figure(5)
    
    # fitting functions
    first1 = 0
    last1 = -12
    f1 = np.polyfit(U_Anode_mV_1[first1:last1], wurzel_1[first1:last1], 1)
    fit_f1 = np.poly1d(f1)
    
    first2 = 0
    last2 = -5
    f2 = np.polyfit(U_Anode_mV_2[first2:last2], wurzel_2[first2:last2], 1)
    fit_f2 = np.poly1d(f2)
    
    # plot y against x 
    plt.errorbar(U_Anode_mV_1, wurzel_1, err_wurzel_1, label="Erste Messung",
                 fmt=".")
    plt.plot(U_Anode_mV_1, fit_f1(U_Anode_mV_1), 
             label="f1(x)=(%.4f)x+(%.4f)" % (f1[0], f1[1]))
   
    plt.errorbar(U_Anode_mV_2[:-1], wurzel_2[:-1], err_wurzel_2[:-1],
                 label="Zweite Messung", fmt=".")
    plt.plot(U_Anode_mV_2[:-2], fit_f2(U_Anode_mV_2[:-2]),
             label="f2(x)=(%.4f)x+(%.4f)" % (f2[0], f2[1]))
    
    # set axis labels
    plt.title("Versuch 402-1: 578nm")
    plt.xlabel("Anodenspannung [mV]")
    plt.ylabel("Wurzel des Anodestroms [pA]")
    
    # place a Legend in the plot
    plt.legend(prop={'size':9})
    #plt.legend(bbox_to_anchor=(0., 0.97, 1., .102), loc=3, ncol=2,
                #mode="expand", borderaxespad=0.)
    
    # display grid
    plt.grid(True)
    
    # save the plot in file
    #filename=x_label + "_" + y_label
    #filename=filename.replace(" ", "")
    write_file("Versuch402_1_578")
    return f1, f2


def Versuch402_1_planck():
    """
    Bestimme h aus den Grenzspannungen
    """
    f1_365, f2_365, f3_365 = Versuch402_1_365()
    f1_405, f2_405 = Versuch402_1_405()
    f1_436, f2_436 = Versuch402_1_436()
    f1_546, f2_546 = Versuch402_1_546()
    f1_578, f2_578 = Versuch402_1_578()
    
    #print f1_365, f1_405, f1_436, f1_546, f1_578
    #print f2_365, f2_405, f2_436, f2_546, f2_578
    #print f3_365
    
    # Berechnung der Grenzspannungen
    U_Grenz = [0] * 5
    U_Grenz[0] = ((-f1_365[1]/f1_365[0]) + (-f2_365[1]/f2_365[0])  + 
                  (-f3_365[1]/f3_365[0])) /3 /1000
    U_Grenz[1] = ((-f1_405[1]/f1_405[0]) + (-f2_405[1]/f2_405[0])) /2 / 1000
    U_Grenz[2] = ((-f1_436[1]/f1_436[0]) + (-f2_436[1]/f2_436[0])) /2 / 1000
    U_Grenz[3] = ((-f1_546[1]/f1_546[0]) + (-f2_546[1]/f2_546[0])) /2 / 1000
    U_Grenz[4] = ((-f1_578[1]/f1_578[0]) + (-f2_578[1]/f2_578[0])) /2 / 1000
    print "\nU_Grenz: ", U_Grenz
    
    # Konstanten
    c = 300000000.0
    e = 1.602e-19
    h_LD = 6.1e-34
    h_Lit = 6.62e-34
    
    # Berechnung des Graphen
    Wvlngth = [365, 405, 436, 546, 578]
    #print "\nWvlngth: ", Wvlngth
    Freq = [0] * 5
    i = 0
    while i < 5:
        Freq[i] = c/(1e-9*Wvlngth[i])
        i += 1
    #print "\nFrequenz: ", Freq
    
    # plotten des Graphen
    plt.figure(6)
    
    # fitting functions
    f = np.polyfit(Freq, U_Grenz, 1)
    fit_f = np.poly1d(f)
    
    # plot y against x 
    plt.errorbar(Freq, U_Grenz, label="Grenzspannungen", fmt=".")
    plt.plot(Freq, fit_f(Freq), label="f(x)=(%.4e)x+(%.4e)" % (f[0], f[1]))
    
    # Berechnung von h
    h = e * f[0]
    print h
    
    # set axis labels
    plt.title("Versuch 402-1: Grenzspannungen")
    plt.xlabel("Frequenz [Hz]")
    plt.ylabel("Spannung [V]")
    
    # place a Legend in the plot
    plt.legend(prop={'size':9}, loc=4)
    #plt.legend(bbox_to_anchor=(0., 0.97, 1., .102), loc=3, ncol=2,
                #mode="expand", borderaxespad=0.)
    
    # display grid
    plt.grid(True)
    
    # save the plot in file
    #filename=x_label + "_" + y_label
    #filename=filename.replace(" ", "")
    write_file("Versuch402_1_PlanckschesWirkungsquant")


def normal_distribution(x, integral, mean, sigma):
    return integral / np.sqrt(2*np.pi) / sigma *np.exp(- x**2 / sigma**2)


def plot_gaussian_fit1(i, x, y, ylabel): #martin
    plt.figure(i)
    
    # gauss fit
    popt, pconv = op.curve_fit(normal_distribution, x, y)
    #fehler = np.sqrt(pconv.diagonal())
    
    fitted_x = np.linspace(np.min(x), np.max(x), 1000)
    fitted_y = normal_distribution(fitted_x, *popt)
    
    # Plotte die Originaldaten. Da es Messdaten sind, werden sie nicht mit
    # einer Linie verbunden.
    plt.plot(x, y, ".", label=ylabel)

    # Plotte die Anpassungsfunktion. Diesmal ohne Punkte, aber mit einer Linie.
    plt.plot(fitted_x, fitted_y, label="Fit: ")
    
    # set axis labels
    plt.title("Versuch 402-2: Winkel - " + ylabel)
    plt.xlabel("Pixel")
    plt.ylabel("Intensitaet")
    
    
    # place a Legend in the plot
    plt.legend(prop={'size':9})
    #plt.legend(bbox_to_anchor=(0., 0.97, 1., .102), loc=3, ncol=2,
                #mode="expand", borderaxespad=0.)
    
    # display grid
    plt.grid(True)
    
    # save the plot in file
    filename = "Versuch402_2_" + ylabel
    filename = filename.replace(" ", "")
    write_file(filename)


def gnuplot_gauss(i, x, y, ylabel, first, last, a, p, b, q, y0, y1):
    plt.figure(i)
    filename = "Versuch402_2_" + ylabel + "GNUplot"
    filename = filename.replace(" ", "")
    #Instantiate Gnuplot object
    g = Gnuplot.Gnuplot(persist = 1)
    g('set title "' + ylabel + '"')
    g('set xlabel "Pixel"')
    g('set ylabel "Intensitaet"')
    #set yrange [-10:*]
    g('set fit errorvariables')
    g('set terminal png')
    g('set grid')
    g('set output "Figures/' + filename + '.png"')
    
    
    g('gauss(x) = a / (sigma*sqrt(0.5*3.1415926)) * ' +
      'exp(-2.0*((x-p)/sigma)**2.0) + y0 + b / (sigm * ' +
      'sqrt(0.5*3.1415926)) * exp(-2.0*((x-q)/sigm)**2.0) + y1')
    
    g('a=' + a) # hoehe erster peak
    g('p=' + p) # position erster peak
    g('b=' + b) # hoehe zweiter peak
    g('q=' + q) # position zweiter peak
    g('y0=' + y0)
    g('y1=' + y1)
    
    g('fit ['+ first +':'+ last+'] gauss(x) "Data/402BalmerAlle.txt" using '+
      x +':'+ y +' via a, b, sigm, sigma, p, q, y0, y1')

    g('A1=sigma/p')
    g('A2=sigm/q')

    g('plot ['+ first +':'+ last+'] "Data/402BalmerAlle.txt" using '+
      x +':'+ y +', gauss(x) ')#t sprintf("P1 = %.3f \261 %.3f ; ' + 
      #'FWHM_1 = %.3f \261 %.3f \n P2 = %.3f \261 %.3f", p, p_err, ' +
      #'sigma, sigma_err, q, q_err)')


# Setting up test data
def norm(x, mean, sd):
    norm = []
    for i in range(x.size):
        norm += [1.0/(sd*np.sqrt(2*np.pi))*np.exp(-(x[i] - mean)**2/(2*sd**2))]
    return np.array(norm)


def res(p, y, x):
    m, dm, sd1, sd2 = p
    m1 = m
    m2 = m1 + dm
    y_fit = norm(x, m1, sd1) + norm(x, m2, sd2)
    err = y - y_fit
    return err


def plot_gaussian_fit2(i, x, y_real, ylabel):
    mean1, mean2 = 0, -1
    std1, std2 = 0.5, 1 
    
    
    
    
    # Solving
    m, dm, sd1, sd2 = [0.1, 0.13, 1, 1]
    p = [m, dm, sd1, sd2] # Initial guesses for op.leastsq
    y_init = norm(x, m, sd1) + norm(x, m + dm, sd2) # For final comparison plot

    plsq = op.leastsq(res, p, args = (y_real, x))

    y_est = norm(x, plsq[0][0], plsq[0][2]) + norm(x, plsq[0][0] + plsq[0][1], 
    plsq[0][3])

    plt.plot(x, y_real, ".", label=ylabel)
    plt.plot(x, y_est, 'g', label='Fitted')
    
    # set axis labels
    plt.title("Versuch 402-2: Winkel - " + ylabel)
    plt.xlabel("Pixel")
    plt.ylabel("Intensitaet")
    
    
    # place a Legend in the plot
    plt.legend(prop={'size':9})
    #plt.legend(bbox_to_anchor=(0., 0.97, 1., .102), loc=3, ncol=2,
                #mode="expand", borderaxespad=0.)
    
    # display grid
    plt.grid(True)
    
    # save the plot in file
    filename = "Versuch402_2_" + ylabel
    filename = filename.replace(" ", "")
    write_file(filename)


def shift(var, varshift):
    i=0
    while i < len(var):
        var[i] += varshift
        i += 1
    return var


def reduce_by_min(var):
    i=0
    varmin = min(var)
    while i < len(var):
        var[i] -= varmin
        i += 1
    return var


def Versuch402_2_cam():
    """========================================================================
    
    ===========================================================================
    """
    data = np.loadtxt('Data/402BalmerAlle.txt')
    x = data[:, 0]
    gruen1 = data[:, 1]
    rot1 = data[:, 2]
    rot2 = data[:, 3]
    tuerkis = data[:, 4]
    violet = data[:, 5]
    violetX2 = data[:, 6]
    
    # Martins Algorithmus
    first = 950
    last = 1130
    plot_gaussian_fit1(7, x[first:last], gruen1[first:last],
                       "Gruene Linie")
    first = 1010
    last = 1035
    plot_gaussian_fit1(8, x[first:last], rot1[first:last],
                       "erste Rote Linie")
    first = 0
    last = 2048
    plot_gaussian_fit1(9, x[first:last], rot2[first:last],
                       "zweite Rote Linie")
    first = 0
    last = 2048
    plot_gaussian_fit1(10, x[first:last], tuerkis[first:last],
                       "Tuerkise Linie")
    first = 0
    last = 2048
    plot_gaussian_fit1(11, x[first:last], violet[first:last],
                       "Violette Linie")
    first = 0
    last = 2048
    plot_gaussian_fit1(12, x[first:last], violetX2[first:last],
                      "Violette Doppelinie")
    
    
    # Gnuplot variante
    #first = 950
    #last = 1130
    #gnuplot_gauss(13, str(1), str(2), "Gruene Linie", str(first), str(last),
                  #str(1), str(10), str(2), str(5), str(1), str(1))
    #first = 1010
    #last = 1035
    #gnuplot_gauss(14, str(1), str(3), "erste Rote Linie", str(first), 
                  #str(last), str(1), str(10), str(2), str(5), str(1), str(1))
    #first = 0
    #last = 2048
    #gnuplot_gauss(15, str(1), str(4), "zweite Rote Linie", str(first),
                  #str(last), str(1), str(10), str(2), str(5), str(1), str(1))
    #first = 0
    #last = 2048
    #gnuplot_gauss(16, str(1), str(5), "Tuerkise Linie", str(first), str(last),
                  #str(1), str(10), str(2), str(5), str(1), str(1))
    #first = 0
    #last = 2048
    #gnuplot_gauss(17, str(1), str(6), "Violette Linie", str(first), str(last),
                  #str(1), str(10), str(2), str(5), str(1), str(1))
    #first = 0
    #last = 2048
    #gnuplot_gauss(18, str(1), str(7), "Violette Doppelinie", str(first),
                  #str(last), str(1), str(10), str(2), str(5), str(1), str(1))
    
    
    # Internet variante
    #first = 1005
    #last = 1045
    #plot_gaussian_fit2(7, shift(x[first:last], 0.1), rot1[first:last],
                       #"erste Rote Linie")
    



#Versuch402_1_planck()
Versuch402_2_cam()


