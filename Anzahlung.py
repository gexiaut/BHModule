from Steuern import Steuern


class Anzahlung():

    def Verkauf(Anzbrutto, Gesamtbrutto):


        # Bank Buchung Anzahlung
        print("2Bank ", Anzbrutto, "an 2KFD", Anzbrutto)
        Anznet = Steuern.getbefore20(Anzbrutto)
        Ustanz = Anzbrutto - Anznet

        # interims Konto/Buchung
        print("2IKerhalteneAnzahlung ", Anzbrutto, "an 3erhalteneAnzahlung20", Anznet)
        print("                                         3Ust", Ustanz)
        Gesnet = Steuern.getbefore20(Gesamtbrutto)
        Ustges = Gesamtbrutto - Gesnet

        # AR voll
        print("2KDF ", Gesamtbrutto, "an 3KFD", Anznet)
        print("                                         3Ust", Ustges)
        # interims Konto/Buchung revertieren
        print("3erhalteneAnzahlung20", Anznet, "an 2IKerhalteneAnzahlung ", Anzbrutto)
        print("3Ust", Ustanz)
        Rest = Gesamtbrutto - Anzbrutto

        # Bank Buchung Rest
        print(" 2Bank ", Rest, "an 2KFD", Rest)

        # Beispiel: Anzahlung.Verkauf(12486, 49944)

    def Kauf(Anzbrutto, Gesamtbrutto):
        # Bank Buchung Anzahlung
        print("3LVB ", Anzbrutto, "an 2Bank", Anzbrutto)
        Anznet = Steuern.getbefore20(Anzbrutto)
        Vstanz = Anzbrutto - Anznet
        # interims Konto/Buchung
        print("1geleisteteAnzahlung ", Anznet, "an 3IK geleistete Anzahlung", Anzbrutto)
        print("2Vst", Vstanz)
        Gesnet = Steuern.getbefore20(Gesamtbrutto)
        Vstges = Gesamtbrutto - Gesnet
        # AR voll
        print("2KDF ", Gesamtbrutto, "an 3KFD", Anznet)
        print("                                         3Ust", Vstges)
        # interims Konto/Buchung revertieren
        print("3IK geleistete Anzahlung", Anznet, "an 1geleisteteAnzahlung ", Anzbrutto)
        print("                                     2Vst", Vstanz)
        Rest = Gesamtbrutto - Anzbrutto
        # Bank Buchung Rest
        print("3LVB ", Rest, "an 2Bank", Rest)

        # Beispiel: Anzahlung.Kauf(12486, 49944)