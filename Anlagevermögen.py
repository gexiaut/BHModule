from Land import Land
from Steuern import Steuern
from Skonto import Skonto

class Anlagevermögen():

# Nutzungsdsdauer in Halbjahren also 2x

    def Einkauf(self, Bruttogesamt, Skontoprozent, Nutzungsdauer):

        Maschine = Steuern.getbefore20(Bruttogesamt)
        VSt = Bruttogesamt - Maschine

        # ER
        print("0 Maschinen", Maschine, "                     3 LVB ", Bruttogesamt)
        print("2 VSt", VSt, '\n')

        # BK Skonto
        if Skontoprozent is not 0:
            Rabatt = Skonto.praktikermethodeeinkauf(1, Bruttogesamt, Skontoprozent)

        # Anschaffungswert AW

        Anschaffungswert = Maschine - Rabatt
        print("Anschaffungswert", Anschaffungswert, '\n')

        # BU

        # WertverlusstproJahr = Anschaffungswert * Nutzungsdauer
        NDJ = Nutzungsdauer * 2 / 100

        # print(NDJ)

        WertverlusstproHalbjahr = Anschaffungswert * NDJ
        Abschreibung = WertverlusstproHalbjahr

        print("7 planm. Abschreibung", Abschreibung, "      0 kum. Abschreibung Maschinen ", Abschreibung)


        # Beispiel: Anlagevermögen.Kauf(118800, 0.03, 0.1)

        return Abschreibung

        #direkt/indirekt

    def Verkauf(self, Bruttogesamt, Skontoprozent, Nutzungsdauer, Nutzungsdsdauerbisher, Anschaffungswert, BW, Methode):



        Erlöse = Steuern.getbefore20(Bruttogesamt)
        USt = Bruttogesamt - Erlöse

        # ER
        print("2 KFD", Bruttogesamt, "                     4 Erlöse AV 20 % ", Erlöse)
        print("                                  3 USt", USt, '\n')

        # BK Skonto
        if Skontoprozent is not 0:

            Rabatt = Skonto.praktikermethodeeinkauf(Bruttogesamt, Skontoprozent)

        if Skontoprozent == 0:
            Rabatt = 0
        # Anschaffungswert AW

        print("Anschaffungswert", Anschaffungswert, '\n')

        # Bankbuchung

        print("2 Bank", Bruttogesamt, "      2 KFD ", Bruttogesamt, '\n')


        NDJ = Nutzungsdauer * 12    # Monate
        NDJ2 = Nutzungsdsdauerbisher * 12
        diff = NDJ - NDJ2

        NDJ = (Nutzungsdauer - (Nutzungsdauer - Nutzungsdsdauerbisher)) * 1 / diff

        print(NDJ)
        NDJ = 0.0625
        WertverlusstproHalbjahr = Anschaffungswert / Nutzungsdauer
        Abschreibung = WertverlusstproHalbjahr
        NDJbisher = Nutzungsdsdauerbisher * 2


        if Methode == "indirekt":
            print("7 planm. Abschreibung", Abschreibung, "              0 kum. Abschreibung Maschinen ", Abschreibung)
            print("0 kum. Abschreibung Maschinen", NDJbisher * Abschreibung, "     0 Maschinen ", NDJbisher * Abschreibung)
            print("7 Buchwert abg. Anlagen", Anschaffungswert - NDJbisher * Abschreibung, "            0 Maschinen ", Anschaffungswert- NDJbisher * Abschreibung)


        if Methode == "direkt":
            print("7 planm. Abschreibung", Abschreibung, "      0 EDV ", Abschreibung)
            print("7 Buchwert abg. Anlagen", BW - Abschreibung, "      0 EDV ", BW -  Abschreibung)



        return Abschreibung

    def Tauschaltgegenneu (self, Brneu, Bralt, Anschaffungswert, Nutzungsdsdauerbisher, BW,  Nutzungsdauer, wann, Methode ):
        Maschinealt = Steuern.getbefore20(Bralt)
        Maschineneu = Steuern.getbefore20(Brneu)


        print("0 Maschinen", Maschineneu, "               4 Erlöse AV 20 % ", Maschinealt)
        print("2 VSt", Brneu - Maschineneu,"                    3 UST ", Bralt - Maschinealt)
        print("                                  3 LVB", Brneu - Bralt, '\n')

        #print(Maschinealt, Maschineneu)

        print("3 LVB", Brneu - Bralt, "            2 Bank",  Brneu - Bralt, '\n')


        Abschreibungalt = BW - Anschaffungswert / (Nutzungsdauer / 2)
        Abschreibungneu = Maschineneu / (Nutzungsdauer / 2) / wann

        print(Abschreibungalt, Abschreibungneu)

        if Methode == "indirekt":
            print("7 planm. Abschreibung", Abschreibungalt + Abschreibungneu, "     0 kum. Abschreibung Maschinen ", Abschreibungalt + Abschreibungneu)
            # print("0 kum. Abschreibung Maschinen", NDJbisher * Abschreibung, "     0 Maschinen ", NDJbisher * Abschreibung)
            print("7 Buchwert abg. Anlagen", Anschaffungswert / (Nutzungsdauer / 2), "            0 Maschinen ", Anschaffungswert / (Nutzungsdauer / 2))


        if Methode == "direkt":
            print("7 planm. Abschreibung", Abschreibungalt + Abschreibungneu, "      0 Maschinen ", Abschreibungalt + Abschreibungneu)
            print("7 Buchwert abg. Anlagen", Abschreibungalt, "      0 Maschinen ", Abschreibungalt)

        return Abschreibungneu


    # def mehrereMaschinen(self, AW1, AW2, AW3, IB1 , IB2 , IB3 , ND1, ND2, ND3):
    #
    #     xx = 0
    #     xy = 0
    #     xz = 0
    #     ges = xx + xy + xz
    #
    #     print("Text  Maschine X    Maschine Y       Maschine Z ")
    #     print("ND     ", ND1, "     ", ND2, "         ", ND3)
    #     print("Inbetriebnahme     ", IB1, "     ", IB2, "       ", IB3)
    #     print("AW   ", AW1, "     ", AW2, "          ", AW3,'\n')
    #
    #     print("Maschinen    AW      Kum. Abschr   Planmäßige Abschr   Inbetriebnahme/Ausscheiden    Kum Abschreibung beim Auscheiden  RBW")
    #     print("Maschine X     ", xx, "     ", yx, "           -        ", TGVSt, TGAufwand)
    #     print("Maschine Y    ", xy, "     ", yy, "             -      ", NVst, NAufwand)
    #     print("Maschine Z    ", xz, "     ", yz, "             -      ", NVst, NAufwand)
    #     print("Gesamt ", ges, "     ", gesa, "         -       ", gesVSt, gesAufwand, '\n')
    #
    #
    #     pass

# Anlagevermögen.Einkauf(1, 90800, 0.05, 5)
# Import/Export fehlt

# Anlagevermögen.Verkauf(1, 4080, 0, 8, 0, 17800, 4450,  "direkt")

# Anlagevermögen.Tauschaltgegenneu(1, 24600, 4200, 13000, 6, 3900, 10, 1, "indirekt")

# Tausch noch nicht korrekt