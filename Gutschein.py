from Steuern import Steuern
from Kontenerstellung import Konto

class Gutschein(Konto):

    def gegeben(self, Gesamtbrutto):
        # Warenverkauf an den Kunden Müller
        # Gesnet = Steuern.getbefore20(Gesamtbrutto)
        # Ustges = Gesamtbrutto - Gesnet
        # print("2 KFD ", Gesamtbrutto, "    4 Erlöse ", Gesnet)
        # print("                             3 Ust", Ustges)
        #
        # Erlöse.einzahlen(Gesnet)
        # Ust.einzahlen(Ustges)
        # Erlöse.buchen(KDF, Gesnet)
        # Ust.buchen(KDF, Ustges)
        #
        # # Zahlung der AR mit Scheck
        # print("2 erhaltener Scheck", Gesamtbrutto, "2 KFD", Gesamtbrutto)
        # erhaltenerScheck.buchen(KDF, Gesamtbrutto)
        #
        # # Einreichung des Schecks bei der Bank
        # print("2 schwebende Geldbewegung", Gesamtbrutto, "2 erhaltener Scheck", Gesamtbrutto)
        # erhaltenerScheck.buchen(schwebendeGeldbewegung, Gesamtbrutto)
        #
        # # Der Scheck wird auf dem Konto gutgeschrieben
        # print("2 Bank", Gesamtbrutto, "2 schwebende Geldbewegung", Gesamtbrutto)
        # schwebendeGeldbewegung.buchen(Bank, Gesamtbrutto)

        # Beispiel: Scheck.gegeben(7200)

    def erhalten(self, Gesamtbrutto):
        # Wareneinkauf
        # Gesnet = Steuern.getbefore20(Gesamtbrutto)
        # Vstges = Gesamtbrutto - Gesnet
        # print("5 HW-Verbrauch", Gesnet, "3 gegebener Scheck ", Gesamtbrutto)
        # print("2 Vst", Vstges)
        #
        # gegebenerScheck.einzahlen(Gesamtbrutto)
        # gegebenerScheck.buchen(HWVerbrauch, Gesnet)
        # gegebenerScheck.buchen(Vst, Vstges)
        #
        # # Zahlung der AR mit Scheck
        # print("3 gegebener Scheck", Gesamtbrutto, "2 Bank", Gesamtbrutto)
        # Bank.buchen(gegebenerScheck, Gesamtbrutto)
        #
        # # Einreichung des Schecks bei der Bank
        # print("2 schwebende Geldbewegung", Gesamtbrutto, "2 erhaltener Scheck", Gesamtbrutto)
        # erhaltenerScheck.buchen(schwebendeGeldbewegung, Gesamtbrutto)
        #
        # # Der Scheck wird auf dem Konto gutgeschrieben
        # print("2 Bank", Gesamtbrutto, "2 schwebende Geldbewegung", Gesamtbrutto)
        # schwebendeGeldbewegung.buchen(Bank, Gesamtbrutto)

        # Beispiel: Scheck.erhalten(7200)



erhaltenerGutschein = Konto("2341 Maschinen")
gegebenerGutschein= Konto("3341 Maschinen")
schwebendeGeldbewegung = Konto("2230 schwebendeGeldbewegung")


Maschinen = Konto("0100 Maschinen")
Bank = Konto("2000 Bank")
Ust = Konto("3500 Ust")
Vst = Konto("2500 Vst")
KDF = Konto("210 KDF")
LVB = Konto("310 LVB")
HWVerbrauch = Konto("5700 HWVerbrauch")
Erloese = Konto("4000 Erloese")

print(Bank.alles())
print(Vst.alles())
print(LVB.alles())