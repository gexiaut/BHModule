from Steuern import Steuern
from Kontenerstellung import Konto

class Werbung():

    def Material(self, Gesamtbrutto):

        # Werbungkauf
        Gesnet = Steuern.getbefore20(Gesamtbrutto)
        Vstges = Gesamtbrutto - Gesnet
        print("7 Werbeaufwand", Gesnet, "    3 LVB ", Gesamtbrutto)
        print("2 Vst", Vstges, '\n')

        LVB.einzahlen(Gesamtbrutto)
        LVB.buchen(Werbeaufwand, Gesnet)
        LVB.buchen(Vst, Vstges)

        # Zahlungsmittel extra

        # Zahlung mittels Scheck
        # print("3 LVB", Gesamtbrutto, "3 gegebener Scheck", Gesamtbrutto)
        #
        # gegebenerScheck.buchen(LVB, Vstges)

        return Gesamtbrutto

        #Beispiel: Werbung.Material(7200)

    def Bewirtung(self, Speisen, Getränke):

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
        print("2 Vst", Vstges, '\n')

        Kassa.einzahlen(Gesamtbrutto)
        Kassa.buchen(Bewirtungabzugsfähig, abzugsfähig)
        Kassa.buchen(Bewirtungnabzugsfähig, nabzugsfähig)
        Kassa.buchen(Vst, Vstges)

        #Beispiel: Werbung.Bewirtung(110, 60)

    def Blumen(self, Gesamtbrutto):

        Netges = Steuern.getbeforex(Gesamtbrutto, 13)
        Vstges = Gesamtbrutto - Netges

        # print(" 2 Speisennet", Getränkenet)
        # print(" 2 Speisennet", Speisennet)

        print("7 Werbeaufwand", Netges, "    2 Kassa ", Gesamtbrutto)
        print("2 Vst", Vstges, '\n')
        Kassa.einzahlen(Gesamtbrutto)
        Kassa.buchen(Werbeaufwand, Netges)
        Kassa.buchen(Vst, Vstges)
        #Beispiel: Werbung.Blumen(67.80)


freiwilligerSozialaufwand = Konto("6333 freiwilligerSozialaufwand")
Werbeaufwand = Konto("7321 Werbeaufwand")
Bewirtungabzugsfähig = Konto("7333 Bewirtungabzugsfähig")
Bewirtungnabzugsfähig = Konto("7222 Bewirtungnabzugsfähig")



Kassa = Konto("2200 Kassa")
Maschinen = Konto("0100 Maschinen")
KDF = Konto("210 KDF")
KD3 = Konto("3103 KD3")
LVB = Konto("310 LVB")
Bank = Konto("2000 Bank")
Ust = Konto("3500 Ust")
Vst = Konto("2500 Vst")
Erloese = Konto("4000 Erloese")

# Vererbung fehlt


# Werbung.Material(LVB, 4800)
# print(Werbeaufwand.alles())
# print(Vst.alles())
# print(LVB.alles())

# Werbung.Bewirtung(LVB, 110, 60)
# print(Kassa.alles())
# print(Bewirtungabzugsfähig.alles())
# print(Bewirtungnabzugsfähig.alles())
# print(Vst.alles())


# Werbung.Blumen(LVB, 67.8)
# print(Werbeaufwand.alles())
# print(Vst.alles())
# print(Kassa.alles())