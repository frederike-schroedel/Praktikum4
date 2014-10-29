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
    U_Anode_mV_1 = data1[4:, 0]
    err_U_Anode_mV_1 = data1[4:, 1]
    U_Mess_mV_1 = data1[4:, 2]
    err_U_Mess_mV_1 = data1[4:, 3]
    I_Anode_pA_1 = data1[4:, 4]
    err_I_Anode_pA_1 = data1[4:, 5]
    wurzel_1 = data1[4:, 6]
    err_wurzel_1 = data1[4:, 7]
   
    
    """========================================================================
    Wellenlaenge: 365nm
    Messung:     2
    Verstaerkung: 1V = 1E-9A
    I_0:         44.667pA
    ===========================================================================
    """
    data2 = np.loadtxt('Data/Versuch402-1_365nm_2.txt')
    U_Anode_mV_2 = data2[4:, 0]
    err_U_Anode_mV_2 = data2[4:, 1]
    U_Mess_mV_2 = data2[4:, 2]
    err_U_Mess_mV_2 = data2[4:, 3]
    I_Anode_pA_2 = data2[4:, 4]
    err_I_Anode_pA_2 = data2[4:, 5]
    wurzel_2 = data2[4:, 6]
    err_wurzel_2 = data2[4:, 7]
    
    
    """========================================================================
    Wellenlaenge: 365nm
    Messung:     3
    Verstaerkung: 1V = 1E-8A
    I_0:         446.667pA
    ===========================================================================
    """
    data3 = np.loadtxt('Data/Versuch402-1_365nm_3.txt')
    U_Anode_mV_3 = data3[4:, 0]
    err_U_Anode_mV_3 = data3[4:, 1]
    U_Mess_mV_3 = data3[4:, 2]
    err_U_Mess_mV_3 = data3[4:, 3]
    I_Anode_pA_3 = data3[4:, 4]
    err_I_Anode_pA_3 = data3[4:, 5]
    wurzel_3 = data3[4:, 6]
    err_wurzel_3 = data3[4:, 7]
    
    plt.figure(1)
    
    # fitting functions
    first1 = 0
    last1 = -1
    f1 = np.polyfit(U_Anode_mV_1[first1:last1], wurzel_1[first1:last1], 1)
    fit_f1 = np.poly1d(f1)
    
    first2 = 0
    last2 = -6
    f2 = np.polyfit(U_Anode_mV_2[first2:last2], wurzel_2[first2:last2], 1)
    fit_f2 = np.poly1d(f2)
    
    first3 = 0
    last3 = -6
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


def Versuch402_1_405():
    """========================================================================
    Wellenlaenge: 405nm
    Messung:     1
    Verstaerkung: 1V = 1E-10A
    I_0:         0.733pA
    ===========================================================================
    """
    data1 = np.loadtxt('Data/Versuch402-1_405nm_1.txt')
    U_Anode_mV_1 = data1[4:, 0]
    err_U_Anode_mV_1 = data1[4:, 1]
    U_Mess_mV_1 = data1[4:, 2]
    err_U_Mess_mV_1 = data1[4:, 3]
    I_Anode_pA_1 = data1[4:, 4]
    err_I_Anode_pA_1 = data1[4:, 5]
    wurzel_1 = data1[4:, 6]
    err_wurzel_1 = data1[4:, 7]
   
    
    """========================================================================
    Wellenlaenge: 405nm
    Messung:     2
    Verstaerkung: 1V = 1E-9A
    I_0:         46pA
    ===========================================================================
    """
    data2 = np.loadtxt('Data/Versuch402-1_405nm_2.txt')
    U_Anode_mV_2 = data2[4:, 0]
    err_U_Anode_mV_2 = data2[4:, 1]
    U_Mess_mV_2 = data2[4:, 2]
    err_U_Mess_mV_2 = data2[4:, 3]
    I_Anode_pA_2 = data2[4:, 4]
    err_I_Anode_pA_2 = data2[4:, 5]
    wurzel_2 = data2[4:, 6]
    err_wurzel_2 = data2[4:, 7]
    
    plt.figure(2)
    
    # fitting functions
    first1 = 0
    last1 = -3
    f1 = np.polyfit(U_Anode_mV_1[first1:last1], wurzel_1[first1:last1], 1)
    fit_f1 = np.poly1d(f1)
    
    first2 = 0
    last2 = -7
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


def Versuch402_1_436():
    """========================================================================
    Wellenlaenge: 436nm
    Messung:     1
    Verstaerkung: 1V = 1E-9A
    I_0:         40.95pA
    ===========================================================================
    """
    data1 = np.loadtxt('Data/Versuch402-1_436nm_1.txt')
    U_Anode_mV_1 = data1[4:, 0]
    err_U_Anode_mV_1 = data1[4:, 1]
    U_Mess_mV_1 = data1[4:, 2]
    err_U_Mess_mV_1 = data1[4:, 3]
    I_Anode_pA_1 = data1[4:, 4]
    err_I_Anode_pA_1 = data1[4:, 5]
    wurzel_1 = data1[4:, 6]
    err_wurzel_1 = data1[4:, 7]
   
    
    """========================================================================
    Wellenlaenge: 436nm
    Messung:     2
    Verstaerkung: 1V = 1E-9A
    I_0:         47pA
    ===========================================================================
    """
    data2 = np.loadtxt('Data/Versuch402-1_436nm_2.txt')
    U_Anode_mV_2 = data2[4:, 0]
    err_U_Anode_mV_2 = data2[4:, 1]
    U_Mess_mV_2 = data2[4:, 2]
    err_U_Mess_mV_2 = data2[4:, 3]
    I_Anode_pA_2 = data2[4:, 4]
    err_I_Anode_pA_2 = data2[4:, 5]
    wurzel_2 = data2[4:, 6]
    err_wurzel_2 = data2[4:, 7]
    
    plt.figure(3)
    
    # fitting functions
    first1 = 0
    last1 = -3
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


def Versuch402_1_546():
    """========================================================================
    Wellenlaenge: 546nm
    Messung:     1
    Verstaerkung: 1V = 1E-10A
    I_0:         2.83pA
    ===========================================================================
    """
    data1 = np.loadtxt('Data/Versuch402-1_546nm_1.txt')
    U_Anode_mV_1 = data1[4:, 0]
    err_U_Anode_mV_1 = data1[4:, 1]
    U_Mess_mV_1 = data1[4:, 2]
    err_U_Mess_mV_1 = data1[4:, 3]
    I_Anode_pA_1 = data1[4:, 4]
    err_I_Anode_pA_1 = data1[4:, 5]
    wurzel_1 = data1[4:, 6]
    err_wurzel_1 = data1[4:, 7]
   
    
    """========================================================================
    Wellenlaenge: 546nm
    Messung:     2
    Verstaerkung: 1V = 1E-9A
    I_0:         46.75pA
    ===========================================================================
    """
    data2 = np.loadtxt('Data/Versuch402-1_546nm_2.txt')
    U_Anode_mV_2 = data2[4:, 0]
    err_U_Anode_mV_2 = data2[4:, 1]
    U_Mess_mV_2 = data2[4:, 2]
    err_U_Mess_mV_2 = data2[4:, 3]
    I_Anode_pA_2 = data2[4:, 4]
    err_I_Anode_pA_2 = data2[4:, 5]
    wurzel_2 = data2[4:, 6]
    err_wurzel_2 = data2[4:, 7]
    
    plt.figure(4)
    
    # fitting functions
    first1 = 3
    last1 = -4
    f1 = np.polyfit(U_Anode_mV_1[first1:last1], wurzel_1[first1:last1], 1)
    fit_f1 = np.poly1d(f1)
    
    first2 = 0
    last2 = -1
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


def Versuch402_1_578():
    """========================================================================
    Wellenlaenge: 578nm
    Messung:     1
    Verstaerkung: 1V = 1E-10A
    I_0:         3.386pA
    ===========================================================================
    """
    data1 = np.loadtxt('Data/Versuch402-1_578nm_1.txt')
    U_Anode_mV_1 = data1[4:, 0]
    err_U_Anode_mV_1 = data1[4:, 1]
    U_Mess_mV_1 = data1[4:, 2]
    err_U_Mess_mV_1 = data1[4:, 3]
    I_Anode_pA_1 = data1[4:, 4]
    err_I_Anode_pA_1 = data1[4:, 5]
    wurzel_1 = data1[4:, 6]
    err_wurzel_1 = data1[4:, 7]
   
    
    """========================================================================
    Wellenlaenge: 578nm
    Messung:     2
    Verstaerkung: 1V = 1E-9A
    I_0:         47.2667pA
    ===========================================================================
    """
    data2 = np.loadtxt('Data/Versuch402-1_578nm_2.txt')
    U_Anode_mV_2 = data2[4:, 0]
    err_U_Anode_mV_2 = data2[4:, 1]
    U_Mess_mV_2 = data2[4:, 2]
    err_U_Mess_mV_2 = data2[4:, 3]
    I_Anode_pA_2 = data2[4:, 4]
    err_I_Anode_pA_2 = data2[4:, 5]
    wurzel_2 = data2[4:, 6]
    err_wurzel_2 = data2[4:, 7]
    
    plt.figure(5)
    
    # fitting functions
    first1 = 4
    last1 = -4
    f1 = np.polyfit(U_Anode_mV_1[first1:last1], wurzel_1[first1:last1], 1)
    fit_f1 = np.poly1d(f1)
    
    first2 = 0
    last2 = -3
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








Versuch402_1_365()
Versuch402_1_405()
Versuch402_1_436()
Versuch402_1_546()
Versuch402_1_578()
