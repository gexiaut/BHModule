

class Bewertungverfahren():

    def Identitäts(self, Menge, Preis, Endbestand, Zukaufm1, Zukaufp1, Zukaufm2, Zukaufp2, Klasse, Verbrauch1, Verbrauch2, Tagespreis):

        Anfangsbestand = Menge * Preis
        Zukauf1 = Zukaufm1 * Zukaufp1
        Zukauf2 = Zukaufm2 * Zukaufp2
        zwm = Menge + Zukaufm1 + Zukaufm2
        zwg = Menge * Preis + Zukaufm1 * Zukaufp1 + Zukaufm2 * Zukaufp2

        Sollendbestand = Anfangsbestand + Zukauf1 + Zukauf2 - Verbrauch1 - Verbrauch2
        Schadensfall = zwm - Zukaufm1 - Verbrauch2 - Endbestand
        # if Verbrauch1 == 0:
        #     Verbrauch1 = Anfangsbestand + Zukauf1 + Zukauf2 - Endbestand
        #
        # if Verbrauch1 is not 0:
        #     Schadensfall = Sollendbestand - Endbestand
        #     if Schadensfall is not 0 and Klasse == 1:
        #         # print("5 HW-Einsatz ", Verbrauch1, "                     1 HW ", Verbrauch1)
        #         print("5 Schadensfall ", Schadensfall, "                   1 HW ", Schadensfall)
        #
        #     Diff = Zukauf1 - Verbrauch1
        #
        #     if Schadensfall is not 0 and Klasse == 5 and Zukauf1 > Verbrauch1:
        #         print("1 HW ", Diff, "                     5 HW-Einsatz ", Diff)
        #         print("5 Schadensfall ", Schadensfall, "                   1 HW ", Schadensfall)
        # if Anfangsbestand > Endbestand and Klasse == 1:
        #     print("5 HW-Einsatz ", Verbrauch1, "                     1 HW ", Verbrauch1)
        # if Anfangsbestand > Endbestand and Klasse == 5:
        #     print("5 HW-Einsatz ", Verbrauch1, "                     1 HW ", Verbrauch1)

        print("Text                 Menge       Preis        Diff       GES")
        print("Anfangsbestand     ", Menge, "     ", Preis, "           -        ", Anfangsbestand)
        print("+ 1. Zukauf      ", Zukaufm1, "     ", Zukaufp1, "           -        ", Zukauf1)
        print("+ 2. Zukauf      ", Zukaufm2, "     ", Zukaufp2, "           -        ", Zukauf2)


        EBAB = 300 * Preis # (Menge - Verbrauch1) * Preis
        EBzk1 = 500 * Zukaufp1 # (Zukaufm1 - Verbrauch1) * Zukaufp1
        EBzk2 = 400 * Zukaufp2 # (Zukaufm2 - Verbrauch2) * Zukaufp2

        Abfassung1 = Verbrauch1 * Preis + (Zukaufm1 - Verbrauch1) * Zukaufp1
        Abfassung2 = Verbrauch2 * Zukaufp2
        SOLLEBid = zwg - Abfassung1 - Abfassung2
        ISTEBid = EBAB + EBzk1 + EBzk2
        Schadensfallid = SOLLEBid - ISTEBid

        print(zwm, zwg)

        print("-1.Abfassung       ", zwm - Zukaufm1, "     ", Abfassung1 )
        print("-2.Abfassung       ", Verbrauch2, "     ", Abfassung2 )
        print("Soll-EB        ", zwm - Zukaufm1 - Verbrauch2, "     ", "  (200 kg 20 AB) (100 kg 28 2. Zk)   ", SOLLEBid)
        print("-Ist-EB       ", Endbestand, "     ", "  (200 kg 20 AB) (100 kg 28 2. Zk)   ", ISTEBid)
        print("Schadensfall ", Schadensfall, "     ", "  (200 kg 20 AB) (100 kg 28 2. Zk)   ", Schadensfallid, '\n')

        Abwertung = 400 * (Zukaufp2 - Tagespreis)
        Bilanzansatz = ISTEBid - Abwertung
        HWEinsatz = Abfassung1 + Abfassung2
        Einsatz = 25625

        print("Abwertung  ", "Abwertung  "   , Abwertung  )
        print("Bilanzansatz     ", "Abwertung  " , Bilanzansatz, '\n')

        print("Zukauf in 1       ", "5 HW-Einsatz   ",  HWEinsatz, "  1 HW   ", HWEinsatz)
        print("              ", "5 Schadensfall   ",  Schadensfallid, "  1 HW   ", Schadensfallid)
        print("              ", "5 Abschreibung   ",  Abwertung, "  1 HW   ", Abwertung, '\n')

        print("Zukauf in 5       ", " 1 HW    ", Einsatz, "  5 HW-Einsatz   ", Einsatz)
        print("              ", "5 Schadensfall   ", Schadensfallid, "  1 HW   ", Schadensfallid)
        print("              ", "5 Abschreibung   ", Abwertung, "  1 HW   ", Abwertung, '\n')

    def FIFO(self, Menge, Preis, Endbestand, Zukaufm1, Zukaufp1, Zukaufm2, Zukaufp2, Klasse, Verbrauch1, Tagespreis):

        Anfangsbestand = Menge * Preis
        Zukauf1 = Zukaufm1 * Zukaufp1
        Zukauf2 = Zukaufm2 * Zukaufp2
        zwm = Menge + Zukaufm1 + Zukaufm2
        zwg = Menge * Preis + Zukaufm1 * Zukaufp1 + Zukaufm2 * Zukaufp2

        Sollendbestand = Anfangsbestand + Zukauf1 + Zukauf2 - Verbrauch1
        Schadensfall = zwm - Zukaufm1 - Endbestand


        print("Text                 Menge       Preis        Diff       GES")
        print("Anfangsbestand     ", Menge, "     ", Preis, "           -        ", Anfangsbestand)
        print("+ 1. Zukauf      ", Zukaufm1, "     ", Zukaufp1, "           -        ", Zukauf1)
        print("+ 2. Zukauf      ", Zukaufm2, "     ", Zukaufp2, "           -        ", Zukauf2)


        # print(zwm, zwg)

        if Verbrauch1 > Menge + Zukaufm1 and Verbrauch1 < zwm :
            zwischenmenge = Menge + Zukaufm1 + (zwm - Verbrauch1)
            zwischengeld = Anfangsbestand + Zukauf1
            gesgeld = zwischengeld + ((Menge + Zukaufm1 - Verbrauch1 + Zukaufm2) * Zukaufp2)

        # print(zwischenmenge, zwischengeld, gesgeld)


        Abfassung1 = gesgeld
        SOLLEBid = zwg - Abfassung1
        ISTEBid = Endbestand * Zukaufp2
        Schadensfallid = (zwm - Verbrauch1 - Endbestand) * Zukaufp2

        print("- Abfassungen      ", Verbrauch1, "     ", Abfassung1)
        print("Soll-EB        ", zwm - Verbrauch1, "     ", "    ",
              SOLLEBid)
        print("-Ist-EB       ", Endbestand, "     ", "     ", ISTEBid)
        print("Schadensfall ", zwm - Verbrauch1 - Endbestand, "     " , SOLLEBid - ISTEBid , '\n')

        Abwertung = Endbestand * (Zukaufp2 - Tagespreis)
        Bilanzansatz = ISTEBid - Abwertung
        HWEinsatz = Abfassung1
        Einsatz = 22000

        print("Abwertung  ", Abwertung)
        print("Bilanzansatz     ", "Abwertung  ", Bilanzansatz, '\n')

        print("Zukauf in 1       ", "5 HW-Einsatz   ", HWEinsatz, "  1 HW   ", HWEinsatz)
        print("              ", "5 Schadensfall   ", Schadensfallid, "  1 HW   ", Schadensfallid)
        print("              ", "5 Abschreibung   ", Abwertung, "  1 HW   ", Abwertung, '\n')

        print("Zukauf in 5       ", " 1 HW    ", Einsatz, "  5 HW-Einsatz   ", Einsatz)
        print("              ", "5 Schadensfall   ", Schadensfallid, "  1 HW   ", Schadensfallid)
        print("              ", "5 Abschreibung   ", Abwertung, "  1 HW   ", Abwertung, '\n')

    def glDurchschnitt(self, Menge, Preis, Endbestand, Zukaufm1, Zukaufp1, Zukaufm2, Zukaufp2, zkzp1, abzp1, zkzp2, abzp2,  Klasse, Verbrauch1, Verbrauch2, Tagespreis):
        Anfangsbestand = Menge * Preis
        Zukauf1 = Zukaufm1 * Zukaufp1

        zwm = Menge + Zukaufm1
        zwp = ((Anfangsbestand + Zukauf1 )/ zwm)

        print(zwp)

        Zukauf2 = Zukaufm2 * Zukaufp2
        zwg = Menge * Preis + Zukaufm1 * Zukaufp1 + Zukaufm2 * Zukaufp2
        ges = 0
        Abfassung1 = Verbrauch1 * Preis
        Abfassung2 = Verbrauch2 * Zukaufp2

        Sollendbestand = Anfangsbestand + Zukauf1 + Zukauf2 - Verbrauch1 - Verbrauch2


        print(zkzp1, abzp1, zkzp2, abzp2)

        abfs2w = (((zwm - Verbrauch1) * zwp) + Zukauf2) / (zwm - Verbrauch1 + Zukaufm2)

        if zkzp1 < abzp1:
            zw = Anfangsbestand + Zukauf1 - Abfassung1
            print(zw)
            if abzp1 < zkzp2:
                zw1 = zw + Zukauf2
                print(zw1)
                if zkzp2 < abzp2:
                    ges = zw1 - Abfassung2
        kk = zwm - Verbrauch1 + Zukaufm2
        Schadensfall = kk - Verbrauch2 - Endbestand

        print("Text                 Menge       Preis       GES")
        print("Anfangsbestand     ", Menge, "        ", Preis, "      ", Anfangsbestand)
        print("+ 1. Zukauf", zkzp1, "    ", Zukaufm1, "       ", Zukaufp1, "     ", Zukauf1)
        print("                     ", zwm, "     ", zwp, "     ", Anfangsbestand + Zukauf1)
        print("-1.Abfassung", abzp1, "    ", Verbrauch1, "     ", zwp, "     ", Verbrauch1 * zwp)
        print("                     ", zwm - Verbrauch1, "     ", zwp, "     ", (zwm - Verbrauch1) * zwp)
        print("+ 2. Zukauf ", zkzp2, "     ", Zukaufm2, "     ", Zukaufp2, "      ", Zukauf2)
        print("                     ", zwm - Verbrauch1 + Zukaufm2, "     ", abfs2w, "     ", (zwm - Verbrauch1 + Zukaufm2) * abfs2w)
        print("-2.Abfassung ", abzp2, "    ", Verbrauch2, "              ", Verbrauch2 * abfs2w)
        print("Soll-EB             ", kk - Verbrauch2, "     ", (zwm - Verbrauch1 + Zukaufm2) * abfs2w - (Verbrauch2 * abfs2w) )
        print("-Ist-EB          ", Endbestand, "     ", Endbestand * abfs2w)
        print("Schadensfall     ", Schadensfall, "     ", Schadensfall * abfs2w,  '\n')



        Abwertung = Endbestand * (abfs2w - Tagespreis)
        Bilanzansatz = Endbestand * Tagespreis
        HWEinsatz = Abfassung1 + Abfassung2
        Einsatz = 20500

        print("Abwertung        ", Abwertung)
        print("Bilanzansatz     ", Bilanzansatz, '\n')

        print("Zukauf in 1       ", "5 HW-Einsatz   ", HWEinsatz, "  1 HW   ", HWEinsatz)
        print("              ", "5 Schadensfall   ", Schadensfall * abfs2w, "  1 HW   ", Schadensfall * abfs2w)
        print("              ", "5 Abschreibung   ", Abwertung, "  1 HW   ", Abwertung, '\n')

        print("Zukauf in 5       ", " 1 HW    ", Einsatz, "  5 HW-Einsatz   ", Einsatz)
        print("              ", "5 Schadensfall   ", Schadensfall * abfs2w, "  1 HW   ", Schadensfall * abfs2w)
        print("              ", "5 Abschreibung   ", Abwertung, "  1 HW   ", Abwertung, '\n')

    def GewDurchschnitt(self, Menge, Preis, Endbestand, Zukaufm1, Zukaufp1, Zukaufm2, Zukaufp2, Klasse, Verbrauch1, Verbrauch2, Tagespreis):
        pass

# Bewertungverfahren.Identitäts(1, 1000, 20, 1200, 4000, 25, 3000, 28, 1, 500, 2500, 26)


# Bewertungverfahren.FIFO(1, 1000, 20, 1200, 4000, 25, 3000, 28,  1, 6500, 26)


# Bewertungverfahren.glDurchschnitt(1, 1000, 20, 1200, 4000, 25, 3000, 28, 110, 524, 620, 730, 1, 4000, 2500, 26)

# gewD fehlt und Zukauf stimmt noch nicht
