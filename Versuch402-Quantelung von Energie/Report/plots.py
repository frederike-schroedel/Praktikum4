import numpy as np
import matplotlib.pyplot as plt


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
    


Versuch402_1_planck()