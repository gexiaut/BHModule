from Steuern import Steuern


class Forderungsbewertung():


    def EWB(Forderung, EQuote, Quote):

        C = Forderung * EQuote
        M = 1-Quote
        K = Forderung * M
        Netto = Steuern.getbefore20(K)


        print("7 Zuweisung EWB FD ", C, "                   2 EWB FD ", C)

        print("7 Zuweisung EWB FD ", Netto, "                   2 EWB FD ", K)
        print("3 USt ", K - Netto)



        if Quote <= EQuote:
            print("2 EWB FD", C, "               7 Zuweisung EWB FD      ", C)

        if Quote > EQuote:
            E = C - Netto
            print("2 EWB FD", C, "                 7 Zuweisung EWB FD      ", Netto)
            print("                                 4 Erträge Auflösung      ", E)

        # Beispiel testen Forderungsbewertung.Bew(6480, 0.45  , 0.45)

    def PWB(Forderung, EQuote, Quote):

        C = Forderung * EQuote
        M = 1-Quote
        K = Forderung * M
        Netto = Steuern.getbefore20(K)


        print("7 Zuweisung EWB FD ", C, "                   2 EWB FD ", C)

        print("7 Zuweisung EWB FD ", Netto, "                   2 EWB FD ", K)
        print("3 USt ", K - Netto)



        if Quote <= EQuote:
            print("2 EWB FD", C, "               7 Zuweisung EWB FD      ", C)

        if Quote > EQuote:
            E = C - Netto
            print("2 EWB FD", C, "                 7 Zuweisung EWB FD      ", Netto)
            print("                                 4 Erträge Auflösung      ", E)

        # Beispiel testen Forderungsbewertung.Bew(6480, 0.45  , 0.45)

Forderungsbewertung.Bew(6480, 0.45, 0.45)




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



