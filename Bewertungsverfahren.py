

class Bewertung():

    def Verfahren(Verfahren, Menge, Preis, Endbestand, Zukaufm1, Zukaufp1, Zukaufm2, Zukaufp2, Klasse, Verbrauch1, Verbrauch2, Tagespreis):

        if Verfahren == 'Identitäts':

            Anfangsbestand = Menge * Preis
            Zukauf1 = Zukaufm1 * Zukaufp1
            Zukauf2 = Zukaufm2 * Zukaufp2

            if Verbrauch1 == 0:
                Verbrauch1 = Anfangsbestand + Zukauf1 + Zukauf2 - Endbestand

            Sollendbestand = Anfangsbestand + Zukauf1 + Zukauf2 - Verbrauch1 - Verbrauch2

            if Verbrauch1 is not 0:
                Schadensfall = Sollendbestand - Endbestand
                if Schadensfall is not 0 and Klasse == 1:
                    # print("5 HW-Einsatz ", Verbrauch1, "                     1 HW ", Verbrauch1)
                    print("5 Schadensfall ", Schadensfall, "                   1 HW ", Schadensfall)

                Diff = Zukauf1 - Verbrauch1

                if Schadensfall is not 0 and Klasse == 5 and Zukauf1 > Verbrauch1:
                    print("1 HW ", Diff, "                     5 HW-Einsatz ", Diff)
                    print("5 Schadensfall ", Schadensfall, "                   1 HW ", Schadensfall)

            if Anfangsbestand > Endbestand and Klasse == 1:
                print("5 HW-Einsatz ", Verbrauch1, "                     1 HW ", Verbrauch1)

            if Anfangsbestand > Endbestand and Klasse == 5:
                print("5 HW-Einsatz ", Verbrauch1, "                     1 HW ", Verbrauch1)

            Bilanzansatz =

        if Verfahren == 'FIFO':

        if Verfahren == 'glDurchschnitt':
        if Verfahren == 'GewDurchschnitt':





