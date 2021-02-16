from Steuern import Steuern

class Skonto():


    def Praktikermethodeeinkauf(brutto, Skontoprozent):

        Vorsteuer = Steuern.getbefore20(brutto)
        print("Die Zahlung lautet 5HW Verbrauch ", brutto - Vorsteuer, "an 3LVB ", brutto)
        print("                   2Vst          ", Vorsteuer)

        i = brutto * Skontoprozent
        Vorsteuer = Steuern.getbefore20(i)
        skonto = i - Vorsteuer
        print("Der Buchungsssatz lautet 3 LVB", brutto, " an 2Bank:", brutto - i, "5Skonto", skonto, "Vst:", Vorsteuer)

    # i = Skonto mit Vorsteuer
        return skonto

    def opwz(brutto, skontoprozent):
        Netto = Steuern.getbefore20(brutto)
        Rabattmitvst = brutto * skontoprozent
        bank = brutto - Rabattmitvst
        Skonto = Steuern.getbefore20(Rabattmitvst)
        Vst = Rabattmitvst - Skonto

        print("3 LVB", brutto, "    2 Bank:", bank)
        print("                     0 Maschinen        ", Skonto)
        print("                     2 Vst          ", Vst, '\n')

        return Skonto
    #naskonto = nicht abgezogener Skonto
    #python Sk


    #Beispiel: Skonto.opwz(16200, 0.02)