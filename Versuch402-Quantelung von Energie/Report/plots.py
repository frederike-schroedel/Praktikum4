#-*- coding: utf-8 -*-
import numpy as np
import scipy.optimize as op
import matplotlib.pyplot as plt


"""============================================================================
save a plot under given filename as .pdf as well as .png
===============================================================================
"""
def write_file(filename):
    print "Writing: ", filename
    
    # show small side margins
    plt.margins(0.05, 0.05)
    
    plt.savefig("Figures/" + filename + ".pdf")
    plt.savefig("Figures/" + filename + ".png")


"""============================================================================
"""

def gerade(x, m, b):
    y = m*x + b
    return y


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
    
    p0 = [1.0, 1.0]
    
    first1 = 0
    last1 = -1
    x1 = U_Anode_mV_1[first1:last1]
    y1 = wurzel_1[first1:last1]
    f1, varianz_f1 = op.curve_fit(gerade, x1, y1, p0)
    df1 = np.sqrt(varianz_f1.diagonal())
    
    fit_f1 = np.poly1d(f1)
    
    first2 = 0
    last2 = -4
    x2 = U_Anode_mV_2[first2:last2]
    y2 = wurzel_2[first2:last2]
    f2, varianz_f2 = op.curve_fit(gerade, x2, y2, p0)
    df2 = np.sqrt(varianz_f2.diagonal())
    
    fit_f2 = np.poly1d(f2)
    
    first3 = 0
    last3 = -3
    x3 = U_Anode_mV_3[first3:last3]
    y3 = wurzel_3[first3:last3]
    f3, varianz_f3 = op.curve_fit(gerade, x3, y3, p0)
    df3 = np.sqrt(varianz_f3.diagonal())
    
    fit_f3 = np.poly1d(f3)
    
    # plot y against x
    plt.errorbar(U_Anode_mV_1, wurzel_1, err_wurzel_1, label="Erste Messung",
                 color="red", marker=".", linestyle="none")
    plt.plot(U_Anode_mV_1, fit_f1(U_Anode_mV_1), 
             label=u"f1(x)=(%.2e±%.2e)x+(%.2e±%.2e)" % (f1[0], df1[0],
                                                       f1[1], df1[1]),
             color="red")
   
    plt.errorbar(U_Anode_mV_2, wurzel_2, err_wurzel_2, label="Zweite Messung",
                 color="blue", marker=".", linestyle="none")
    plt.plot(U_Anode_mV_2, fit_f2(U_Anode_mV_2),
             label=u"f2(x)=(%.2e±%.2e)x+(%.2e±%.2e)" % (f2[0], df2[0],
                                                       f2[1], df2[1]),
             color="blue")
    
    plt.errorbar(U_Anode_mV_3, wurzel_3, err_wurzel_3,
                 label="Dritte Messung", color="green", marker=".",
                 linestyle="none")
    plt.plot(U_Anode_mV_3[:-1], fit_f3(U_Anode_mV_3[:-1]),
             label=u"f3(x)=(%.2e±%.2e)x+(%.2e±%.2e)" % (f3[0], df3[0],
                                                       f3[1], df3[1]),
             color="green")
    
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
    return f1, df1, f2, df2, f3, df3


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
    p0 = [1.0, 1.0]
    
    first1 = 0
    last1 = -1
    x1 = U_Anode_mV_1[first1:last1]
    y1 = wurzel_1[first1:last1]
    f1, varianz_f1 = op.curve_fit(gerade, x1, y1, p0)
    df1 = np.sqrt(varianz_f1.diagonal())
    
    fit_f1 = np.poly1d(f1)
    
    first2 = 0
    last2 = -2
    x2 = U_Anode_mV_2[first2:last2]
    y2 = wurzel_2[first2:last2]
    f2, varianz_f2 = op.curve_fit(gerade, x2, y2, p0)
    df2 = np.sqrt(varianz_f2.diagonal())
    
    fit_f2 = np.poly1d(f2)
    
    # plot y against x
    plt.errorbar(U_Anode_mV_1, wurzel_1, err_wurzel_1, label="Erste Messung",
                 color="red", marker=".", linestyle="none")
    plt.plot(U_Anode_mV_1, fit_f1(U_Anode_mV_1), 
             label=u"f1(x)=(%.2e±%.2e)x+(%.2e±%.2e)" % (f1[0], df1[0],
                                                       f1[1], df1[1]),
             color="red")
   
    plt.errorbar(U_Anode_mV_2, wurzel_2, err_wurzel_2, label="Zweite Messung",
                 color="blue", marker=".", linestyle="none")
    plt.plot(U_Anode_mV_2[:-1], fit_f2(U_Anode_mV_2[:-1]),
             label=u"f2(x)=(%.2e±%.2e)x+(%.2e±%.2e)" % (f2[0], df2[0],
                                                       f2[1], df2[1]),
             color="blue")
    
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
    return f1, df1, f2, df2


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
    p0 = [1.0, 1.0]
    
    first1 = 7
    last1 = -2
    x1 = U_Anode_mV_1[first1:last1]
    y1 = wurzel_1[first1:last1]
    f1, varianz_f1 = op.curve_fit(gerade, x1, y1, p0)
    df1 = np.sqrt(varianz_f1.diagonal())
    
    fit_f1 = np.poly1d(f1)
    
    first2 = 0
    last2 = -1
    x2 = U_Anode_mV_2[first2:last2]
    y2 = wurzel_2[first2:last2]
    f2, varianz_f2 = op.curve_fit(gerade, x2, y2, p0)
    df2 = np.sqrt(varianz_f2.diagonal())
    
    fit_f2 = np.poly1d(f2)
    
    # plot y against x
    plt.errorbar(U_Anode_mV_1, wurzel_1, err_wurzel_1, label="Erste Messung",
                 color="red", marker=".", linestyle="none")
    plt.plot(U_Anode_mV_1, fit_f1(U_Anode_mV_1), 
             label=u"f1(x)=(%.2e±%.2e)x+(%.2e±%.2e)" % (f1[0], df1[0],
                                                       f1[1], df1[1]),
             color="red")
   
    plt.errorbar(U_Anode_mV_2, wurzel_2, err_wurzel_2, label="Zweite Messung",
                 color="blue", marker=".", linestyle="none")
    plt.plot(U_Anode_mV_2, fit_f2(U_Anode_mV_2),
             label=u"f1(x)=(%.2e±%.2e)x+(%.2e±%.2e)" % (f2[0], df2[0],
                                                       f2[1], df2[1]),
             color="blue")
    
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
    return f1, df1, f2, df2


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
    p0 = [1.0, 1.0]
    
    first1 = 0
    last1 = -8
    x1 = U_Anode_mV_1[first1:last1]
    y1 = wurzel_1[first1:last1]
    f1, varianz_f1 = op.curve_fit(gerade, x1, y1, p0)
    df1 = np.sqrt(varianz_f1.diagonal())
    
    fit_f1 = np.poly1d(f1)
    
    first2 = 0
    last2 = -4
    x2 = U_Anode_mV_2[first2:last2]
    y2 = wurzel_2[first2:last2]
    f2, varianz_f2 = op.curve_fit(gerade, x2, y2, p0)
    df2 = np.sqrt(varianz_f2.diagonal())
    
    fit_f2 = np.poly1d(f2)
    
    # plot y against x
    plt.errorbar(U_Anode_mV_1, wurzel_1, err_wurzel_1, label="Erste Messung",
                 color="red", marker=".", linestyle="none")
    plt.plot(U_Anode_mV_1, fit_f1(U_Anode_mV_1), 
             label=u"f1(x)=(%.2e±%.2e)x+(%.2e±%.2e)" % (f1[0], df1[0],
                                                       f1[1], df1[1]),
             color="red")
   
    plt.errorbar(U_Anode_mV_2, wurzel_2, err_wurzel_2, label="Zweite Messung",
                 color="blue", marker=".", linestyle="none")
    plt.plot(U_Anode_mV_2, fit_f2(U_Anode_mV_2),
             label=u"f1(x)=(%.2e±%.2e)x+(%.2e±%.2e)" % (f2[0], df2[0],
                                                       f2[1], df2[1]),
             color="blue")
    
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
    return f1, df1, f2, df2


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
    p0 = [1.0, 1.0]
    
    first1 = 0
    last1 = -12
    x1 = U_Anode_mV_1[first1:last1]
    y1 = wurzel_1[first1:last1]
    f1, varianz_f1 = op.curve_fit(gerade, x1, y1, p0)
    df1 = np.sqrt(varianz_f1.diagonal())
    
    fit_f1 = np.poly1d(f1)
    
    first2 = 0
    last2 = -5
    x2 = U_Anode_mV_2[first2:last2]
    y2 = wurzel_2[first2:last2]
    f2, varianz_f2 = op.curve_fit(gerade, x2, y2, p0)
    df2 = np.sqrt(varianz_f2.diagonal())
    
    fit_f2 = np.poly1d(f2)
    
    # plot y against x 
    plt.errorbar(U_Anode_mV_1, wurzel_1, err_wurzel_1, label="Erste Messung",
                 color="red", marker=".", linestyle="none")
    plt.plot(U_Anode_mV_1, fit_f1(U_Anode_mV_1), 
             label=u"f1(x)=(%.2e±%.2e)x+(%.2e±%.2e)" % (f1[0], df1[0],
                                                       f1[1], df1[1]),
             color="red")
   
    plt.errorbar(U_Anode_mV_2[:-1], wurzel_2[:-1], err_wurzel_2[:-1],
                 label="Zweite Messung", color="blue", marker=".",
                 linestyle="none")
    plt.plot(U_Anode_mV_2[:-2], fit_f2(U_Anode_mV_2[:-2]),
             label=u"f2(x)=(%.2e±%.2e)x+(%.2e±%.2e)" % (f2[0], df2[0],
                                                       f2[1], df2[1]),
             color="blue")
    
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
    return f1, df1, f2, df2


def Versuch402_1_alle():
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
    
    plt.figure(20)
    
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
    plt.title("Versuch 402-1: Alle Messungen")
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
    write_file("Versuch402_1_alle")



def Versuch402_1_planck():
    """
    Bestimme h aus den Grenzspannungen
    """
    f1_365, df1_365, f2_365, df2_365, f3_365, df3_365 = Versuch402_1_365()
    f1_405, df1_405, f2_405, df2_405 = Versuch402_1_405()
    f1_436, df1_436, f2_436, df2_436 = Versuch402_1_436()
    f1_546, df1_546, f2_546, df2_546 = Versuch402_1_546()
    f1_578, df1_578, f2_578, df2_578 = Versuch402_1_578()
    
    #print f1_365, f1_405, f1_436, f1_546, f1_578
    #print f2_365, f2_405, f2_436, f2_546, f2_578
    #print f3_365
    
    # Berechnung der Grenzspannungen
    U_Grenz = [0] * 5
    dU_Grenz = [0] * 5
    U_Grenz[0] = ((-f1_365[1]/f1_365[0]) + (-f2_365[1]/f2_365[0])  + 
                  (-f3_365[1]/f3_365[0])) /3 /1000
    dU_Grenz1 = np.sqrt((df1_365[0]*f1_365[1]/f1_365[0]**2)**2 +
                        (df1_365[1]/f1_365[0])**2)
    dU_Grenz2 = np.sqrt((df2_365[0]*f2_365[1]/f2_365[0]**2)**2 +
                        (df2_365[1]/f2_365[0])**2)
    dU_Grenz3 = np.sqrt((df3_365[0]*f3_365[1]/f3_365[0]**2)**2 +
                        (df3_365[1]/f3_365[0])**2)
    dU_Grenz[0] = np.sqrt((dU_Grenz1**2 + dU_Grenz2**2 + dU_Grenz3**2) /3)/1000
    
    U_Grenz[1] = ((-f1_405[1]/f1_405[0]) + (-f2_405[1]/f2_405[0])) /2 / 1000
    dU_Grenz1 = np.sqrt((df1_405[0]*f1_405[1]/f1_405[0]**2)**2 +
                        (df1_405[1]/f1_405[0])**2)
    dU_Grenz2 = np.sqrt((df2_405[0]*f2_405[1]/f2_405[0]**2)**2 +
                        (df2_405[1]/f2_405[0])**2)
    dU_Grenz[1] = np.sqrt((dU_Grenz1**2 + dU_Grenz2**2) /2) /1000

    U_Grenz[2] = ((-f1_436[1]/f1_436[0]) + (-f2_436[1]/f2_436[0])) /2 / 1000
    dU_Grenz1 = np.sqrt((df1_436[0]*f1_436[1]/f1_436[0]**2)**2 +
                        (df1_436[1]/f1_436[0])**2)
    dU_Grenz2 = np.sqrt((df2_436[0]*f2_436[1]/f2_436[0]**2)**2 +
                        (df2_436[1]/f2_436[0])**2)
    dU_Grenz[2] = np.sqrt((dU_Grenz1**2 + dU_Grenz2**2) /2) /1000

    U_Grenz[3] = ((-f1_546[1]/f1_546[0]) + (-f2_546[1]/f2_546[0])) /2 / 1000
    dU_Grenz1 = np.sqrt((df1_546[0]*f1_546[1]/f1_546[0]**2)**2 +
                        (df1_546[1]/f1_546[0])**2)
    dU_Grenz2 = np.sqrt((df2_546[0]*f2_546[1]/f2_546[0]**2)**2 +
                        (df2_546[1]/f2_546[0])**2)
    dU_Grenz[3] = np.sqrt((dU_Grenz1**2 + dU_Grenz2**2) /2) /1000

    U_Grenz[4] = ((-f1_578[1]/f1_578[0]) + (-f2_578[1]/f2_578[0])) /2 / 1000
    dU_Grenz1 = np.sqrt((df1_578[0]*f1_578[1]/f1_578[0]**2)**2 +
                        (df1_578[1]/f1_578[0])**2)
    dU_Grenz2 = np.sqrt((df2_578[0]*f2_578[1]/f2_578[0]**2)**2 +
                        (df2_578[1]/f2_578[0])**2)
    dU_Grenz[4] = np.sqrt((dU_Grenz1**2 + dU_Grenz2**2) /2) /1000

    #print "\nU_Grenz: ", U_Grenz
    #print "\ndU_Grenz: ", dU_Grenz
    
    # Konstanten
    c = 300000000.0
    e = 1.602e-19
    h_LD = 6.1e-34
    h_Lit = 6.62e-34
    
    # Berechnung des Graphen
    Wvlngth = np.array([365, 405, 436, 546, 578])
    #print "\nWvlngth: ", Wvlngth
    Freq = np.array([0] * 5)
    i = 0
    while i < 5:
        Freq[i] = c/(1e-9*Wvlngth[i])
        i += 1
    #print "\nFrequenz: ", Freq
    
    # plotten des Graphen
    plt.figure(6)
    
    # fitting functions
    p0 = [0.1, 1.0]
    
    f, varianz_f = op.curve_fit(gerade, Freq, U_Grenz, p0=p0)
    df = np.sqrt(varianz_f.diagonal())
    
    fit_f = np.poly1d(f)
    
    # plot y against x 
    plt.errorbar(Freq, U_Grenz, dU_Grenz, label="Grenzspannungen", fmt=".")
    plt.plot(Freq, fit_f(Freq), label=u"f(x)=(%.2e±%.2e)x+(%.2e±%.2e)" %
             (f[0], df[0], f[1], df[1]))
    
    # Berechnung von h
    h = e * f[0]
    dh = e * df[0]
    print h, dh
    
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



"""============================================================================
"""

def gauss_fkt_2(x, *p0):
    a1, p1, sigma1, y1, a2, p2, sigma2, y2 = p0
    f1 = a1/(sigma1*np.sqrt(np.pi/2.0)) * np.exp(-2.0*((x-p1)/sigma1)**2.0)+y1
    f2 = a2/(sigma2*np.sqrt(np.pi/2.0)) * np.exp(-2.0*((x-p2)/sigma2)**2.0)+y2
    return f1 +f2


def plot_gaussian_fit_eigen(i, x, y, ylabel, p0): # ich
    plt.figure(i)
    
    # gauss fit
    parameter, varianz = op.curve_fit(gauss_fkt_2, x, y, p0=p0)
    
    fitted_x = np.linspace(np.min(x), np.max(x), 1000)
    fitted_y = gauss_fkt_2(fitted_x, *parameter)
    
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
    pixel = data[:, 0]
    x = data[:, 1]
    gruen1 = data[:, 2]
    rot1 = data[:, 3]
    rot2 = data[:, 4]
    tuerkis = data[:, 5]
    violet = data[:, 6]
    violetX2 = data[:, 7]
    
    # Martins Algorithmus
    first = 970
    last = 1130
    p0 = [40., 1050.0, 1.0, 16.0, 37., 1060.0, 1.0, 16.0]
    plot_gaussian_fit_eigen(7, pixel[first:last], gruen1[first:last],
                       "Gruene Linie", p0)
    first = 1000
    last = 1040
    p0 = [35., 1012.0, 1.0, 20.0, 100., 1024.0, 1.0, 20.0]
    plot_gaussian_fit_eigen(8, pixel[first:last], rot1[first:last],
                       "erste Rote Linie", p0)
    first = 1130
    last = 1240
    p0 = [18., 1180.0, 1.0, 15.0, 17., 1205.0, 1.0, 15.0]
    plot_gaussian_fit_eigen(9, pixel[first:last], rot2[first:last],
                       "zweite Rote Linie", p0)
    first = 1280
    last = 1330
    p0 = [18., 1280.0, 1.0, 13.0, 30., 1300.0, 1.0, 13.0]
    plot_gaussian_fit_eigen(10, pixel[first:last], tuerkis[first:last],
                       "Tuerkise Linie", p0)
    first = 1235
    last = 1275
    p0 = [18., 1250.0, 1.0, 13.0, 16.5, 1258.0, 1.0, 13.0]
    plot_gaussian_fit_eigen(11, pixel[first:last], violet[first:last],
                       "Violette Linie", p0)
    first = 1000
    last = 1280
    p0 = [18., 1100.0, 1.0, 14.0, 16.5, 1225.0, 1.0, 14.0]
    plot_gaussian_fit_eigen(12, pixel[first:last], violetX2[first:last],
                      "Violette Doppelinie", p0)
    


"""============================================================================
"""

#Versuch402_1_alle()

Versuch402_1_planck()
#Versuch402_2_cam()













