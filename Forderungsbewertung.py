from Steuern import Steuern


class Forderungsbewertung():


    def EWB(self, Forderung, EQuote, Quote, vquote):

        Forderungnetto = Steuern.getbefore20(Forderung)
        Zuweisung = Forderungnetto * (1-EQuote)
        Abschreibung = Forderung * (1-Quote)
        Netto = Steuern.getbefore20(Abschreibung)

        Abschreibungv = Forderung * vquote
        Nettov = Steuern.getbefore20(Abschreibungv)

        print(Forderungnetto, Zuweisung, Abschreibung, '\n')

        if EQuote is not 0:
            print("7 Zuweisung EWB FD ", Zuweisung, "                   2 EWB FD ", Zuweisung, '\n')

        if Quote < EQuote:
            print("7 Abschreibung FD ", Netto, "                   2 KFD ", Abschreibung)
            print("3 USt ", Abschreibung - Netto)
            print("2 EWB FD ", Zuweisung, "       7 Zuweisung EWB FD ", Zuweisung, '\n')

        if Quote > EQuote:
            print("7 Abschreibung FD ", Netto, "                   2 KFD ", Abschreibung)
            print("3 USt ", Abschreibung - Netto)
            print("2 EWB FD", Zuweisung, "                 7 Zuweisung EWB FD      ", Netto)
            print("                                 4 Erträge Auflösung      ", Zuweisung - Netto, '\n')

        if EQuote is not 0 and Quote == EQuote:
            print("7 Abschreibung FD", Netto, "                 7 Zuweisung EWB FD      ", Abschreibung)
            print("3 USt ", Abschreibung - Netto)

            print("2 EWB FD ", Zuweisung, "       7 Zuweisung EWB FD ", Zuweisung, '\n')

        if EQuote == 0 and vquote == 0:
            print("7 Abschreibung FD ", Netto, "                   2 KFD ", Abschreibung)
            print("3 USt ", Abschreibung - Netto)

        if vquote is not 0:
            print("7 Abschreibung FD ", Nettov, "                   2 KFD ", Abschreibungv)
            print("3 USt ", Abschreibungv - Nettov)

    def PWB(self, Forderung, EQuote, Quote):

        pass

# Forderungsbewertung.EWB(1, 6480, 0.45, 0.45, 0)
# Forderungsbewertung.EWB(1, 5200, 0, 0, 0)
Forderungsbewertung.EWB(1, 10200, 0, 0, 0.3)

# PWB fehlt




