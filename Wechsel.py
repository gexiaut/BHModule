from Steuern import Steuern
from Kontenerstellung import Konto

class Wechsel(Konto):

    def Forderung(self, Gesamtbrutto, Verzugszinsertrag, Diskontzinsaufwand, SpesendesGeldverkehrs):
        # Warenverkauf an den Kunden Müller
        Gesnet = Steuern.getbefore20(Gesamtbrutto)
        Ustges = Gesamtbrutto - Gesnet
        print("2 KFD ", Gesamtbrutto, "    4 Erloese ", Gesnet)
        print("                             3 Ust", Ustges, '\n')

        Erloese.einzahlen(Gesnet)
        Ust.einzahlen(Ustges)
        Erloese.buchen(KDF, Gesnet)
        Ust.buchen(KDF, Ustges)

        # Zahlung der AR mit Wechsel
        print("2 Wechselforderung", Gesamtbrutto + Verzugszinsertrag, "2 KDF", Gesamtbrutto)
        print("                                             8 Verzugszinsertrag", Verzugszinsertrag, '\n')

        Ve.einzahlen(Verzugszinsertrag)
        KDF.buchen(Wf, Gesamtbrutto)
        Ve.buchen(Wf, Verzugszinsertrag)

        # Einreichung des Wechsels bei der Bank
        print("2 schwebende Geldbewegung", Gesamtbrutto, "2 Wechselforderung", Gesamtbrutto + Verzugszinsertrag, '\n')
        Wf.buchen(schwebendeGeld, Gesamtbrutto + Verzugszinsertrag)

        # Der Wechsels wird auf dem Konto gutgeschrieben
        print("2 Bank", Gesamtbrutto + Verzugszinsertrag - Diskontzinsaufwand - SpesendesGeldverkehrs, "2 schwebende Geldbewegung", Gesamtbrutto + Verzugszinsertrag)
        print("8 Diskontzinsaufwand", Diskontzinsaufwand)
        print("7 SpesendesGeldverkehrs", SpesendesGeldverkehrs, '\n')

        schwebendeGeld.buchen(Bank, Gesamtbrutto + Verzugszinsertrag - Diskontzinsaufwand - SpesendesGeldverkehrs)
        schwebendeGeld.buchen(Daufwand, Diskontzinsaufwand)
        schwebendeGeld.buchen(SpesenGeldverkehrs, SpesendesGeldverkehrs)

        Ustspe = Steuern.getafter20(SpesendesGeldverkehrs)
        Dif = Ustspe - SpesendesGeldverkehrs

        print("2 KDF ", Diskontzinsaufwand + SpesendesGeldverkehrs + Dif, "    8 Diskontzinsaufwand", Diskontzinsaufwand)
        print("                            4 weiterverrechneteSpesen", SpesendesGeldverkehrs)
        print("                            3 Ust", Dif, '\n')

        wSpesen.einzahlen(SpesendesGeldverkehrs)
        Ust.einzahlen(Dif)

        Daufwand.buchen(KDF, Diskontzinsaufwand)
        wSpesen.buchen(KDF, SpesendesGeldverkehrs)
        Ust.buchen(KDF, Dif)


        # Verrechnung der Diskontspesen
        print("2 Bank", Gesamtbrutto + Verzugszinsertrag, "2 KDF", Gesamtbrutto, '\n')
        KDF.buchen(Bank, Diskontzinsaufwand + SpesendesGeldverkehrs + Dif)



        # Beispiel: Scheck.gegeben(3600)

    def Schuld(self, Gesamtbrutto):
        # Wareneinkauf
        Gesnet = Steuern.getbefore20(Gesamtbrutto)
        Vstges = Gesamtbrutto - Gesnet
        print("5 HW-Verbrauch", Gesnet, "3 LVB ", Gesamtbrutto)
        print("2 Vst", Vstges, '\n')

        # Zahlung der ER mit Wechsel
        print("3 LVB", Gesamtbrutto, "3 Schuldwechsel ", Gesamtbrutto, '\n')

        # Einreichung des Wechsels bei der Bank
        print("3 Schuldwechsel ", Gesamtbrutto, "2 Bank", Gesamtbrutto, '\n')

        Bank.einzahlen(Gesamtbrutto)
        Bank.buchen(Sw, Gesamtbrutto)

        Sw.buchen(LVB, Gesamtbrutto)

        LVB.buchen(HWVerbrauch, Gesnet)
        LVB.buchen(Vst, Vstges)


        # Beispiel: Scheck.erhalten(7200)



Wf = Konto("2444 Wechselforderung")
Sw = Konto("3444 Schuldwechsel")
wSpesen = Konto("4444 weiterverrechneteSpesen")
Ve = Konto("8444 Verzugszinsertrag")
Daufwand = Konto("8333 Diskontzinsaufwand")
SpesenGeldverkehrs = Konto("7444 SpesendesGeldverkehrs")
schwebendeGeld = Konto("2230 schwebendeGeldbewegung")


Maschinen = Konto("0100 Maschinen")
Bank = Konto("2000 Bank")
Ust = Konto("3500 Ust")
Vst = Konto("2500 Vst")
KDF = Konto("210 KDF")
LVB = Konto("310 LVB")
HWVerbrauch = Konto("5700 HWVerbrauch")
Erloese = Konto("4000 Erloese")


wech = Wechsel.Forderung(KDF, 36000, 1400, 620, 100)


# Forderung

print(Bank.alles())
print(Vst.alles())
print(LVB.alles())
print(HWVerbrauch.alles())
print(Daufwand.alles())
print(Wf.alles())
print(Erloese.alles())
print(schwebendeGeld.alles())
print(SpesenGeldverkehrs.alles())
print(Ve.alles())
print(Ust.alles())
print(KDF.alles())
# Schuld

# print(Bank.alles())
# print(Vst.alles())
# print(LVB.alles())
# print(HWVerbrauch.alles())

# wech = Wechsel.Forderung(KDF, 54000)