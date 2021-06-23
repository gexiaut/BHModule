

class LöhneGehälter():

    def Vorschüsse(self, Vorschüsse):


        Vorschüsse = 9750

        # BK  Vorschüsse
        SummeGehälter = 10500
        SummeLöhne = 30000
        Brutto = SummeGehälter + SummeLöhne
        SVDN = 7125
        Lohnsteuer = 6525
        Gesamtnettobetrag = Brutto - SVDN - Lohnsteuer
        VBMA = Gesamtnettobetrag - Vorschüsse
        DB = 1485
        DZ = 132
        Kommunalsteuer = 990
        SVDGA = 8471.25
        BMVK = 344.25
        VBGKK = SVDN + SVDGA + BMVK
        VBFA = 12300 + DZ + DB + Lohnsteuer

        print("2 Vorschüsse", Vorschüsse, "         2 Bank ", Vorschüsse, '\n')
        # BU
        print("6 Gehälter", SummeGehälter, "          3 VB GKK ", SVDN)
        print("6 Löhne", SummeLöhne, "             3 VB FA ", Lohnsteuer)
        print("                           3 VB MA ", VBMA)
        print("                           2 Vorschüsse ", Vorschüsse, '\n')

        print("6 DB", DB, "                     3 VB FA ", DB)
        print("6 DZ ", DZ, "                     3 VB FA ", DZ)
        print("6 Kommunalsteuer", Kommunalsteuer, "          3 VB Gemeinde ", Kommunalsteuer)
        print("6 SVDGA", SVDGA, "               3 VB GKK ", SVDGA)
        print("6 BMVK ", BMVK, "                3 VB GKK ", BMVK, '\n')

        # BK  Sammelüberweisung an die Mitarbeiter
        print("3 VB MA ", VBMA, "                2 Bank ", VBMA, '\n')

        # BK  Überweisung an die Gebietskrankenkasse
        print("3 VB GKK", VBGKK, "              2 Bank ", VBGKK, '\n')

        # BK  Überweisung an die Gebietskrankenkasse
        print("3 VB FA", VBFA, "                 2 Bank ", VBFA, '\n')

        # BK  Überweisung an die Gebietskrankenkasse
        print("3 VB Gemeinde", Kommunalsteuer, "             2 Bank ", Kommunalsteuer, '\n')

        #Beispiel: LöhneGehälter.Vorschüsse(9750)


