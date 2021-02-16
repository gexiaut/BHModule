from Steuern import Steuern


class Scheck():

    def gegeben(Gesamtbrutto):

        # Warenverkauf an den Kunden Müller
        Gesnet = Steuern.getbefore20(Gesamtbrutto)
        Ustges = Gesamtbrutto - Gesnet
        print("2 KFD ", Gesamtbrutto, "    4 Erlöse ", Gesnet)
        print("                3 Ust", Ustges)

        # Zahlung der AR mit Scheck
        print("2 erhaltener Scheck", Gesamtbrutto, "2 KFD", Gesamtbrutto)

        # Einreichung des Schecks bei der Bank
        print("2 schwebende Geldbewegung", Gesamtbrutto, "2 erhaltener Scheck", Gesamtbrutto)

        # Der Scheck wird auf dem Konto gutgeschrieben
        print("2 Bank", Gesamtbrutto, "2 schwebende Geldbewegung", Gesamtbrutto)

        #Beispiel: Scheck.gegeben(7200)

    def erhalten(Gesamtbrutto):

        # Wareneinkauf
        Gesnet = Steuern.getbefore20(Gesamtbrutto)
        Vstges = Gesamtbrutto - Gesnet
        print("5 HW-Verbrauch", Gesnet, "3 gegebener Scheck ", Gesamtbrutto)
        print("2 Vst", Vstges)

        # Zahlung der AR mit Scheck
        print("3 gegebener Scheck", Gesamtbrutto, "2 Bank", Gesamtbrutto)

        # Einreichung des Schecks bei der Bank
        print("2 schwebende Geldbewegung", Gesamtbrutto, "2 erhaltener Scheck", Gesamtbrutto)

        # Der Scheck wird auf dem Konto gutgeschrieben
        print("2 Bank", Gesamtbrutto, "2 schwebende Geldbewegung", Gesamtbrutto)

        #Beispiel: Scheck.erhalten(7200)

