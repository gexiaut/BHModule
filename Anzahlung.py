from Kontenerstellung import Konto
from Steuern import Steuern


class Anzahlung(Konto):


    # def __init__(self, Anzbrutto,
    #              Gesamtbrutto, Anznet, Ustanz, Gesnet, Ustges, Rest, Vstanz, Vstges):
    #     self.Anzbrutto = Anzbrutto
    #     self.Gesamtbrutto = Gesamtbrutto
    #     self.Anznet = Anznet
    #     self.Ustanz = Ustanz
    #     self.Ustanz = Vstanz
    #     self.Gesnet = Gesnet
    #     self.Ustges = Ustges
    #     self.Ustges = Vstges
    #     self.Rest = Rest
    #
    # def all(self, Konto):
    #     Accs.append(Anzahlung(Konto))


    def Verkauf(self, Anzbrutto, Gesamtbrutto):
        # Bank Buchung Anzahlung
        KDF.einzahlen(Anzbrutto)
        KDF.buchen(Bank, Anzbrutto)

        print("2 Bank ", Anzbrutto, "an 2 KFD", Anzbrutto, '\n')
        Anznet = Steuern.getbefore20(Anzbrutto)
        Ustanz = Anzbrutto - Anznet

        # interims Konto/Buchung
        erhalteneAnzahlung20.einzahlen(Anznet)
        Ust.einzahlen(Ustanz)
        erhalteneAnzahlung20.buchen(IKerhalteneAnzahlung2, Anznet)
        Ust.buchen(IKerhalteneAnzahlung2, Ustanz)

        print("2 IKerhalteneAnzahlung ", Anzbrutto, "an 3 erhalteneAnzahlung20", Anznet)
        print("                                         3 Ust", Ustanz, '\n')
        Gesnet = Steuern.getbefore20(Gesamtbrutto)
        Ustges = Gesamtbrutto - Gesnet

        # AR voll

        Erloese.einzahlen(Gesnet)
        Ust.einzahlen(Ustges)
        Erloese.buchen(KDF, Gesnet)
        Ust.buchen(KDF, Ustges)


        print("2 KDF", Gesamtbrutto, "an 4 Erloese 20", Gesnet)
        print("                          3 Ust", Ustges, '\n')

        # interims Konto/Buchung revertieren
        print(IKerhalteneAnzahlung2.alles())

        IKerhalteneAnzahlung2.buchen(erhalteneAnzahlung20, Anznet)
        IKerhalteneAnzahlung2.buchen(Ust, Ustanz)
        erhalteneAnzahlung20.auszahlen(Anznet)
        Ust.auszahlen(Ustanz)

        print("3 erhalteneAnzahlung20", Anznet, "an 2 IKerhalteneAnzahlung ", Anzbrutto)
        print("3 Ust", Ustanz, '\n')
        Rest = Gesamtbrutto - Anzbrutto

        # Bank Buchung Rest
        KDF.buchen(Bank, Rest)
        KDF.auszahlen(Anzbrutto)

        print("2 Bank ", Rest, "an 2 KFD", Rest, '\n')
        # Beispiel: Anzahlung.Verkauf(12486, 49944)

    def Kauf(self, Anzbrutto, Gesamtbrutto):

        # zukauf in klasse bestummen

        # Bank Buchung Anzahlung
        Bank.einzahlen(Gesamtbrutto)
        Bank.buchen(LVB, Anzbrutto)
        print("3 LVB ", Anzbrutto, "an 2 Bank", Anzbrutto, '\n')

        Anznet = Steuern.getbefore20(Anzbrutto)
        Vstanz = Anzbrutto - Anznet

        # interims Konto/Buchung
        IKgeleisteteAnz.einzahlen(Anzbrutto)
        IKgeleisteteAnz.buchen(geleisteteAnz, Anznet)
        IKgeleisteteAnz.buchen(Vst, Vstanz)
        print("1 geleisteteAnzahlung ", Anznet, "an 3 IKgeleistete Anzahlung", Anzbrutto)
        print("2 Vst", Vstanz, '\n')

        Gesnet = Steuern.getbefore20(Gesamtbrutto)
        Vstges = Gesamtbrutto - Gesnet

        # print(IKgeleisteteAnz.alles())
        # ER voll
        LVB.einzahlen(Gesamtbrutto)
        LVB.buchen(Maschinen, Gesnet)
        LVB.buchen(Vst, Vstges)


        print("0 Maschinen ", Gesnet, "an 3 LVB", Gesamtbrutto)
        print("2 Vst", Vstges, '\n')

        # interims Konto/Buchung aufloesen
        geleisteteAnz.buchen(IKgeleisteteAnz, Anznet)
        Vst.buchen(IKgeleisteteAnz, Vstanz)

        print("3 IK geleistete Anzahlung", Anznet, "an 1 geleisteteAnzahlung ", Anzbrutto)
        print("                                        2 Vst", Vstanz, '\n')
        Rest = Gesamtbrutto - Anzbrutto

        # Bank Buchung Rest
        Bank.buchen(LVB, Rest)
        IKgeleisteteAnz.auszahlen(Anzbrutto)
        # LVB.auszahlen(Anzbrutto)
        print("3 LVB ", Rest, "an 2 Bank", Rest, '\n')

        # Beispiel: Anzahlung.Kauf(12486, 49944)




geleisteteAnz = Konto("20001 gA")
erhalteneAnzahlung20 = Konto("30001 eA20")
IKerhalteneAnzahlung2 = Konto("200001 IKeA")
IKgeleisteteAnz = Konto("300001 IKgA")

Maschinen = Konto("0100 Maschinen")
KDF = Konto("210 KDF")
KD3 = Konto("3103 KD3")
LVB = Konto("310 LVB")
Bank = Konto("2000 Bank")
Ust = Konto("3500 Ust")
Vst = Konto("2500 Vst")
Erloese = Konto("4000 Erloese")



ans = Anzahlung.Kauf(Anzahlung, 12000, 60000)



# print(Bank.alles())
# print(geleisteteAnz.alles())
# print(IKgeleisteteAnz.alles())
print(Maschinen.alles())
# print(Vst.alles())


# print(KDF.alles())
# print(Erloese.alles())
# print(Ust.alles())
# print(erhalteneAnzahlung20.alles())
# print(IKerhalteneAnzahlung2.alles())
