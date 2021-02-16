from Land import Land
from Steuern import Steuern
from Skonto import Skonto

class Anlagevermögen():


    def Kauf(Bruttogesamt, skontoprozent, Nutzungsdauer):

        Maschine = Steuern.getbefore20(Bruttogesamt)
        VSt = Bruttogesamt - Maschine

        # ER
        print("0 Maschinen", Maschine, "                     3 LVB ", Bruttogesamt)
        print("2 VSt", VSt, '\n')

        # BK Skonto
        if skontoprozent is not 0:
            Rabatt = Skonto.opwz(Bruttogesamt, skontoprozent)

        # Anschaffungswert AW

        Anschaffungswert = Maschine - Rabatt
        print("Anschaffungswert", Anschaffungswert, '\n')

        # BU

        # WertverlusstproJahr = Anschaffungswert * Nutzungsdauer
        WertverlusstproHalbjahr = Anschaffungswert * Nutzungsdauer
        Abschreibung =  WertverlusstproHalbjahr

        print("7 planm. Abschreibung", Abschreibung, "      0 kum. Abschreibung Maschinen ", Abschreibung)


        # Beispiel: Anlagevermögen.Kauf(118800, 0.03, 0.1)

        return Abschreibung

        #direkt/indirekt
    def Verkauf(Bruttogesamt, skontoprozent, Nutzungsdauer):

        Erlöse = Steuern.getbefore20(Bruttogesamt)
        USt = Bruttogesamt - Erlöse

        # ER
        print("2 KFD", Bruttogesamt, "                     4 Erlöse AV 20 % ", Erlöse)
        print("                                        3 USt", USt, '\n')

        # BK Skonto
        if skontoprozent is not 0:

            Rabatt = Skonto.opwz(Bruttogesamt, skontoprozent)

        if skontoprozent == 0:
            Rabatt = 0
        # Anschaffungswert AW

        Anschaffungswert = Erlöse - Rabatt
        print("Anschaffungswert", Anschaffungswert, '\n')

        # BU

        # WertverlusstproJahr = Anschaffungswert * Nutzungsdauer
        WertverlusstproHalbjahr = Anschaffungswert * Nutzungsdauer
        Abschreibung =  WertverlusstproHalbjahr

        print("7 planm. Abschreibung", Abschreibung, "      0 kum. Abschreibung Maschinen ", Abschreibung)




        return Abschreibung

Anlagevermögen.Verkauf(4080, 0, 0.1)