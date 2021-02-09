class Steuern():

    def getafter20(beforetax):
        tax = beforetax/5
        aftertax = beforetax + tax
        print("Amount after tax:", aftertax)
        print("The tax at 20%:", tax)

        return aftertax

    def getbefore20(aftertax):
        tax = aftertax/6
        beforetax = aftertax - tax
        print("Amount before tax:", beforetax)
        print("The tax at 20%:", tax)

        return beforetax

    def getafter10(beforetax):
        tax = beforetax * 0.1
        aftertax = beforetax + tax
        print("Amount after tax:", aftertax)
        print("The tax at 10%:", tax)

        return aftertax

    def getbefore10(aftertax):
        tax = aftertax * 10/110
        beforetax = aftertax - tax
        print("Amount before tax:", beforetax)
        print("The tax at 20%:", tax)

        return beforetax

    def getafterx(beforetax, x):
        tax = beforetax * x / 100
        aftertax = beforetax + tax
        print("Amount after tax:", aftertax)
        print("The tax", x,"% is:", tax)

        return aftertax

    def getbeforex(aftertax, x):
        tax = aftertax * x / (100 + x)
        beforetax = aftertax - tax
        print("Amount before tax:", beforetax)
        print("The tax", x,"% is:", tax)

        return beforetax

#Steuern.getbefore20(16200)

        # if Vermietung
        # elif Personenbeförderung
        # elif Müllabfuhr
        # elif Bücher, Zeitungen, Zeitschriften, Lebensmittel
        #
        #     Steuersatz = 0,1
        #
        # else
        #     Steuersatz = 0,13

# def e(Einkommen):
#
#     if Einkommen < 11000:
#         lohnsteuersatz = 0
#
#     elif Einkommen > 1100 and Einkommen < 18000:
#         lohnsteuersatz = 0.25
#
#     elif Einkommen > 18000 and Einkommen < 31000:
#         lohnsteuersatz = 0.35
#
#     elif Einkommen > 31000 and Einkommen < 60000:
#         lohnsteuersatz = 0.42
#
#     elif Einkommen > 60000 and Einkommen < 90000:
#         lohnsteuersatz = 0.48
#
#     elif Einkommen > 90000 and Einkommen < 100000:
#         lohnsteuersatz = 0.5
#     else:
#         lohnsteuersatz = 0.55
#
#     print(Einkommen, lohnsteuersatz)


    #print("Die zu zahlende Einkommensteuer ist:", e, "bei einem Lohnsteuersatz von;", Lohnsteuersatz)

    #
    #
    # def Korperschaftsteuer(self,):
    #
    # def Kapitalertragssteuer():



