from Steuern import Steuern

class Skonto():

    #Bsp: Skonto.opwz(16200, 0.02)
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
        Vorsteuer = Steuern.getbefore20(brutto)
        naskonto = brutto * (skontoprozent - Steuern.getbefore20(skontoprozent))
        print("Die Zahlung lautet 5HW Verbrauch ", brutto - Vorsteuer - naskonto, "an 3LVB ", brutto)
        print("                   8naSko        ", naskonto)
        print("                   2Vst          ", Vorsteuer)

        bank = brutto - naskonto - naskonto/5

        print("Der Buchungsssatz lautet 3 LVB", brutto, " an 2Bank:", bank, "5Skonto", naskonto, "Vst:", naskonto/5)

        return naskonto
    #naskonto = nicht abgezogener Skonto
    #python Sk


Skonto.opwz(16200, 0.02)