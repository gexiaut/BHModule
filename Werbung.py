from Steuern import Steuern


class Werbung():

    def Material( Gesamtbrutto):

        # Werbungkauf
        Gesnet = Steuern.getbefore20(Gesamtbrutto)
        Vstges = Gesamtbrutto - Gesnet
        print("7 Werbeaufwand", Gesamtbrutto, "    3 LVB ", Gesnet)
        print(" 2 Vst", Vstges)

        # Zahlung mittels Scheck
        print("3 LVB", Gesamtbrutto, "3 gegebener Scheck", Gesamtbrutto)

        return Gesamtbrutto

        #Beispiel: Werbung.Material(7200)

    def Bewirtung(Speisen, Getränke):

        Getränkenet = Steuern.getbefore20(Getränke)
        Speisennet = Steuern.getbefore10(Speisen)
        Gesamtbrutto = Speisen + Getränke
        Netges = Speisennet + Getränkenet
        abzugsfähig = Netges / 2
        nabzugsfähig = Netges / 2
        Vstges = Gesamtbrutto - Netges

        # print(" 2 Speisennet", Getränkenet)
        # print(" 2 Speisennet", Speisennet)

        print("7 Bewirtung abzugsfähig", abzugsfähig, "         2 Kassa ", Gesamtbrutto)
        print("7 Bewirtung n. Abzugsfähig", nabzugsfähig)
        print("2 Vst", Vstges)

        #Beispiel: Werbung.Bewirtung(110, 60)

    def Blumen(Gesamtbrutto):

        Netges = Steuern.getbeforex(Gesamtbrutto, 13)
        Vstges = Gesamtbrutto - Netges

        # print(" 2 Speisennet", Getränkenet)
        # print(" 2 Speisennet", Speisennet)

        print("7 Werbeaufwand", Netges, "    2 Kassa ", Gesamtbrutto)
        print("2 Vst", Vstges)

        #Beispiel: Werbung.Blumen(67.80)







