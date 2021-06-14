from Steuern import Steuern
from Kontenerstellung import Konto



class Scheck(Konto):




    def gegeben(self, Gesamtbrutto):

        # Warenverkauf an den Kunden Müller
        Gesnet = Steuern.getbefore20(Gesamtbrutto)
        Ustges = Gesamtbrutto - Gesnet
        print("2 KFD ", Gesamtbrutto, "    4 Erloese ", Gesnet)
        print("                             3 Ust", Ustges, '\n')

        Erloese.einzahlen(Gesnet)
        Ust.einzahlen(Ustges)
        Erloese.buchen(KDF, Gesnet)
        Ust.buchen(KDF, Ustges)


        # Zahlung der AR mit Scheck
        print("2 erhaltener Scheck", Gesamtbrutto, "2 KFD", Gesamtbrutto, '\n')
        KDF.buchen(erhaltenerScheck, Gesamtbrutto)

        # Einreichung des Schecks bei der Bank
        print("2 schwebende Geldbewegung", Gesamtbrutto, "2 erhaltener Scheck", Gesamtbrutto, '\n')
        erhaltenerScheck.buchen(schwebendeGeldbewegung, Gesamtbrutto)


        # Der Scheck wird auf dem Konto gutgeschrieben
        print("2 Bank", Gesamtbrutto, "2 schwebende Geldbewegung", Gesamtbrutto, '\n')
        schwebendeGeldbewegung.buchen(Bank, Gesamtbrutto)

        #Beispiel: Scheck.gegeben(7200)

    def erhalten(self, Gesamtbrutto):

        # Wareneinkauf
        Gesnet = Steuern.getbefore20(Gesamtbrutto)
        Vstges = Gesamtbrutto - Gesnet
        print("5 HW-Verbrauch", Gesnet, "3 gegebener Scheck ", Gesamtbrutto)
        print("2 Vst", Vstges)

        gegebenerScheck.einzahlen(Gesamtbrutto)
        gegebenerScheck.buchen(HWVerbrauch, Gesnet)
        gegebenerScheck.buchen(Vst, Vstges)


        # Zahlung der AR mit Scheck
        print("3 gegebener Scheck", Gesamtbrutto, "2 Bank", Gesamtbrutto)
        Bank.buchen(gegebenerScheck, Gesamtbrutto)

        # Einreichung des Schecks bei der Bank
        print("2 schwebende Geldbewegung", Gesamtbrutto, "2 erhaltener Scheck", Gesamtbrutto)
        erhaltenerScheck.buchen(schwebendeGeldbewegung, Gesamtbrutto)

        # Der Scheck wird auf dem Konto gutgeschrieben
        print("2 Bank", Gesamtbrutto, "2 schwebende Geldbewegung", Gesamtbrutto)
        schwebendeGeldbewegung.buchen(Bank, Gesamtbrutto)

        #Beispiel: Scheck.erhalten(7200)










erhaltenerScheck = Konto("2340 Maschinen")
gegebenerScheck = Konto("3340 Maschinen")
schwebendeGeldbewegung = Konto("2230 Maschinen")
Maschinen = Konto("0100 Maschinen")
Bank = Konto("2000 Bank")
Ust = Konto("3500 Ust")
Vst = Konto("2500 Vst")
KDF = Konto("210 KDF")
LVB = Konto("310 LVB")
HWVerbrauch = Konto("5700 HWVerbrauch")
Erloese = Konto("4000 Erloese")

sch = Scheck.gegeben(LVB, 7200)



# list=[]
#
# list.append(Konto("2340 Maschinen"))
# list.append(gegebenerScheck)
# list.append(schwebendeGeldbewegung)
# list.append(Maschinen)
#
# for obj in list:
#     print(obj)



print(Bank.alles())
print(Vst.alles())
print(LVB.alles())

# print(dir(sch))
# print(vars(sch))



