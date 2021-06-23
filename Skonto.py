from Steuern import Steuern
from Kontenerstellung import Konto


class Skonto(Konto):

    def praktikermethodeeinkauf(self, Gesamtbrutto, Skontoprozent):
        # ER
        Gesnet = Steuern.getbefore20(Gesamtbrutto)
        print("Die Zahlung lautet 5HW Verbrauch ", Gesnet, "an 3 LVB ", Gesamtbrutto)
        print("                   2Vst          ", Gesamtbrutto - Gesnet, '\n')

        LVB.einzahlen(Gesamtbrutto)
        LVB.buchen(HWVerbrauch, Gesamtbrutto - Gesnet)
        LVB.buchen(Vst, Gesnet)

        # Banküberweisung mit Skonto
        i = Gesamtbrutto * Skontoprozent
        skonto = Steuern.getbefore20(i)
        Vstges = i - skonto
        print("Der Buchungsssatz lautet 3 LVB", Gesamtbrutto, "  an 2 Bank:", Gesamtbrutto - i)
        print("                                                     5 Skonto", skonto)
        print("                                                     2 Vst:", Vstges, '\n')

        Bank.einzahlen(Gesamtbrutto - i)
        Sko.einzahlen(skonto)
        Vst.einzahlen(Vstges)
        Bank.buchen(LVB, Gesamtbrutto - i)
        Sko.buchen(LVB, skonto)
        Vst.buchen(LVB, Vstges)

        # i = Skonto mit Vorsteuer
        return skonto

    # def Praktikermethodeverkauf(self, Gesamtbrutto, Skontoprozent):

    # ER
    # Gesnet = Steuern.getbefore20(Gesamtbrutto)
    # print("Die Zahlung lautet 5HW Verbrauch ", Gesnet, "an 3 LVB ", Gesamtbrutto)
    # print("                   2Vst          ", Gesamtbrutto - Gesnet, '\n')
    #
    # LVB.einzahlen(Gesamtbrutto)
    # LVB.buchen(HWVerbrauch, Gesamtbrutto - Gesnet)
    # LVB.buchen(Vst, Gesnet)
    #
    # # Banküberweisung mit Skonto
    # i = Gesamtbrutto * Skontoprozent
    # skonto = Steuern.getbefore20(i)
    # Vstges = i - skonto
    # print("Der Buchungsssatz lautet 3 LVB", Gesamtbrutto, "  an 2 Bank:", Gesamtbrutto - i)
    # print("                                                     5 Skonto", skonto)
    # print("                                                     2 Vst:", Vstges, '\n')
    #
    # Bank.einzahlen(Gesamtbrutto - i)
    # Sko.einzahlen(skonto)
    # Vst.einzahlen(Vstges)
    # Bank.buchen(LVB, Gesamtbrutto - i)
    # Sko.buchen(LVB, skonto)
    # Vst.buchen(LVB, Vstges)

    # i = Skonto mit Vorsteuer
    # return skonto

    def opwzeinkauf(self, Gesamtbrutto, skontoprozent):
        Netto = Steuern.getbefore20(Gesamtbrutto)
        Rabattmitvst = Gesamtbrutto * skontoprozent
        bank = Gesamtbrutto - Rabattmitvst
        skonto = Steuern.getbefore20(Rabattmitvst)
        Vstges = Rabattmitvst - skonto

        print("5 Wareneinsatz ", Netto - skonto, "      3 LVB", Gesamtbrutto)
        print("8 naLieferantenskonti", skonto)
        print("2 Vst", Gesamtbrutto - Netto, '\n')

        print("3 LVB", Gesamtbrutto, "      2 Bank:", bank)
        print("                             8 naLieferantenskonti", skonto)
        print("                             2 Vst", Vstges, '\n')

        LVB.einzahlen(Gesamtbrutto)

        LVB.buchen(HWVerbrauch, Netto - skonto)
        LVB.buchen(naLieferantenskonti, skonto)
        LVB.buchen(Vst, Gesamtbrutto - Netto)

        Bank.einzahlen(bank)
        Bank.buchen(LVB, Netto - skonto)
        naLieferantenskonti.buchen(LVB, skonto)
        Vst.buchen(LVB, Vstges)

        return skonto
    # naskonto = nicht abgezogener Skonto
    # python Sk

    # Beispiel: Skonto.opwz(16200, 0.02)


Maschinen = Konto("0100 Maschinen")
Bank = Konto("2000 Bank")
Ust = Konto("3500 Ust")
Vst = Konto("2500 Vst")
LVB = Konto("310 LVB")
Erloese = Konto("4000 Erloese")
HWVerbrauch = Konto("5700 HWVerbrauch")

Sko = Konto("5400 Skonto")
naLieferantenskonti = Konto("8300 naLieferantenskonti")
Skontoertrag = Konto("8400 Skontoertrag")






# sko = Skonto.praktikermethodeeinkauf(LVB, 16200, 0.02)
#
# print(Bank.alles())
# print(Vst.alles())
# print(LVB.alles())

# sko = Skonto.opwzeinkauf(LVB, 144, 0.02)
# print(Bank.alles())
# print(Vst.alles())
# print(LVB.alles())
# print(naLieferantenskonti.alles())
# print(HWVerbrauch.alles())
