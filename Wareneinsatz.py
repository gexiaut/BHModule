

class Waren():


    def Einsatz(Anfangsbestand, Endbestand, Zukauf, Klasse, Verbrauch):

        if Verbrauch == 0:
            Verbrauch = Anfangsbestand + Zukauf - Endbestand


        Sollendbestand = Anfangsbestand + Zukauf - Verbrauch

        if Verbrauch is not 0:
            Schadensfall = Sollendbestand - Endbestand
            if Schadensfall is not 0 and Klasse == 1:
                #print("5 HW-Einsatz ", Verbrauch, "                     1 HW ", Verbrauch)
                print("5 Schadensfall ", Schadensfall, "                   1 HW ", Schadensfall)

            Diff = Zukauf - Verbrauch

            if Schadensfall is not 0 and Klasse == 5 and Zukauf > Verbrauch:
                print("1 HW ", Diff, "                     5 HW-Einsatz ", Diff)
                print("5 Schadensfall ", Schadensfall, "                   1 HW ", Schadensfall)

        if Anfangsbestand > Endbestand and Klasse == 1:
            print("5 HW-Einsatz ", Verbrauch, "                     1 HW ", Verbrauch)

        if Anfangsbestand > Endbestand and Klasse == 5:
            print("5 HW-Einsatz ", Verbrauch - Zukauf, "                     1 HW ", Verbrauch - Zukauf)

        return Verbrauch



    def HWliste(MS, MH, HWS, HWH, MES,MEH,HWES,HWEH,SS,SH,Material,MEndbestand,HW,HEndbestand):

        print("                     SOLL        HABEN")
        print("Material         ", MS, "        ", MH)
        print("Handelswaren     ", HWS, "       ", HWH)
        print("Materialeinsatz     ", MES, "          ", MEH)
        print("Handelswareneinsatz  ", HWES, "     ",HWEH)
        print("Schadensfälle        ", SS, "         ", SH, '\n')


        print("                    Material  Verbrauch lt. Lagerbuchhaltung ", Material)
        print("                                 Endbestand lt. Inventur  ", MEndbestand)
        print("                     HW          Verbrauch lt. Lagerbuchhaltung ", HW)
        print("                                 Endbestand lt. Inventur  ", HEndbestand, '\n')

        SOLLEB = MS - Material
        SS = SOLLEB - MEndbestand



        print("5 Materialeinsatz ", Material, "                     1 Material ", Material)
        print("5 Einsatz ", SS, "                            1 Material ", SS)






# Waren.Einsatz(170680, 177180, 75000, 5, 68300)
# Waren.HWliste(3670000, 0, 350000, 0, 0, 0, 935000, 0, 0, 0, 3400000, 265000, 905000, 375000)


# Beispiel testen



        # if AB > EB and KL == 1:
        #     if ES is not 0:
        #         V = ES
        #         SEB = AB + ZK - V
        #         S = SEB - EB
        #         print("Sollendbestand", SEB, "IstEndbestand", EB, "Schadensfall", S)
        #         print("Der Buchungssatz lautet 5HW Einsatz an 1HW", V)
        #         print("                        5Schadensfall an 1HW", S)
        #     else:
        #         V = AB + ZK - EB
        #         print("Der Verbrauch ist", V)
        #         print("Der Buchungssatz lautet  5HW Einsatz an 1HW", V)
        #
        # elif AB > EB or AB < EB and KL == 5:
        #     if ES is not 0:
        #         V = ES
        #         SEB = AB + ZK - V
        #         S = SEB - EB
        #         print("Sollendbestand", SEB, "IstEndbestand", EB, "Schadensfall", S)
        #         D = V - ZK
        #         if D < 0:
        #             D = D * -1
        #         print("Der Buchungssatz lautet 1HW an 5HW Einsatz", D)
        #         print("                        5Schadensfall an 1HW", S)
        #     else:
        #         V = AB + ZK - EB
        #         print("Der Verbrauch ist", V)
        #         D = V - ZK
        #         print("Der Buchungssatz lautet  5HW Einsatz an 1HW", D)



