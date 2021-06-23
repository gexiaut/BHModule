from Steuern import Steuern


class Rechnungsabgrenzung():

    # if wann == 'Folgejahr':
    #     print("2 SFD ", ARA, "                   8 Zinserträge", ARA)
    #     print(" 8 Zinsaufwand  ", PRA, "                   3 SVB", PRA)

    # if wann == 'Voraus' or 'Vorhinein':
    #     print("2 ARA ", ARA, "                   7 Mietaufwand ", ARA)
    #     print("4 Mieterträge", PRA, "                   3 PRA ", PRA)
    #     print("8 Zinserträge", PRA, "                   3 PRA ", PRA)


    # if Aufwand
    #     ARA or SVB
    # if Ertrag
    #     PRA or SFD
    # ggf UST rausrechnen


    def ARA(self, Brutto, wann, was, RA):

        # was nicht mehr im Jahr ist

        if RA == 'ARA':
            ARA = wann / 12 * Brutto
            if was == 'Versicherung':
                print("2 ARA ", ARA, "                   7 Versicherung ", ARA)
            if was == 'Mietaufwand':
                print("2 ARA ", ARA, "                   7 Mietaufwand ", ARA)

        # was noch in dem Jahr liegt

        if RA == 'SFD':
            SFD = wann / 12 * Brutto
            if was == 'Zinserträge':
                print("2 SFD ", SFD, "                   8 Zinserträge", SFD)
            if was == 'Miete':
                print("2 SFD ", SFD, "                   4 Mieterträge", SFD)

    def PRA(self, Brutto, wann, was, RA):


        if RA == 'PRA':
            PRA = wann / 12 * Brutto
            if was == 'Mieterträge':
                print("4 Mieterträge", PRA, "                   3 PRA ", PRA)
            if was == 'Zinserträge':
                print("8 Zinserträge ", PRA, "                   3 PRA", PRA)


        if RA == 'SVB':
            SVB = wann / 12 * Brutto
            if was == 'Instandhaltung':
                print("7 Instandhaltung  ", SVB, "                   3 SVB", SVB)
            if was == 'Versicherung':
                print("7 Versicherung  ", SVB, "                   3 SVB", SVB)
            if was == 'Miete':
                print("7 Mieteaufwand  ", SVB, "                   3 SVB", SVB)
            if was == 'Zinsaufwand':
                print(" 8 Zinsaufwand  ", SVB, "                   3 SVB", SVB)
            if was == 'Transporte':
                print("7 Transporte", SVB, "                   3 SVB", SVB)




# Beispiel testen Rechnungsabgrenzung.ARA(6000 , 8, 'Versicherung', 'ARA')

# Rechnungsabgrenzung.ARA(1, 2160 , 10, 'Miete', 'SFD')

Rechnungsabgrenzung.PRA(1, 2640 , 10, 'Miete', 'SVB')

