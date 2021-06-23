from Land import Land
from Steuern import Steuern
from Werbung import Werbung

class Reisekosten():


    # if Reisedauer < 3h kein Tagesgeld
    # Nächtigung, Pauschale 15€/Nacht oder Belege
    # Öffis Aufwendungen voll
    # kmges < 15000



    def DienstreiseMitarbeiter(self, Reisedauer, Nächte, Nächtigungsbeleg, Ländercode, Bahnticket, Taxi, km, kmSatz,
                               Tagsatz):


        Tage = Reisedauer / 12

        # Taggeld
        if Tagsatz is not 0:
            Taggeld = Tage * Tagsatz
        else:
            Tagsatz = Land.getdnmoney(1, Ländercode)[0]
            Taggeld = Tage * Tagsatz
        sttg = Steuern.getbefore10(Taggeld)

        # Nächtigung
        if Nächtigungsbeleg is not 0:
            Nächtigung = Nächtigungsbeleg
        else:
            Nachtsatz = Land.getdnmoney(1, Ländercode)[1]
            Nächtigung = Nächte * Nachtsatz
        stng = Steuern.getbefore10(Nächtigungsbeleg)

        # Fahrt
        Fahrt = Bahnticket + Taxi
        stFahrt = Steuern.getbefore10(Fahrt)
        # PKW
        if kmSatz is not 0.42:
            PKW = km * kmSatz
        else:
            PKW = km * 0.42

        TGVSt = Taggeld - sttg
        NGVSt = Nächtigung - stng
        KMVSt = 0
        FahrtVSt = Fahrt - stFahrt
        TGAufwand = Taggeld - TGVSt
        NGAufwand = Nächtigung - NGVSt
        kmAufwand = 0
        # PKW = kmAufwand
        # kmAufwand = PKW
        Fahrtaufwand = stFahrt
        gesa = Taggeld + Nächtigung + Fahrt + PKW
        # gesf = Taggeldf + Nächtigungf + kmf
        gesVSt = TGVSt + NGVSt + KMVSt + FahrtVSt
        gesAufwand = TGAufwand + NGAufwand + kmAufwand + Fahrtaufwand

        # Beispiel:  Reisekosten.DienstreiseMitarbeiter(25, 2, 125, 43, 68, 28, 0, 0, 0)
        print("Text  Auszahlung   Frei       Pflichtig   VSt     Aufwand")
        print("TG     ", Taggeld, "     ", Taggeld, "           -        ", TGVSt, TGAufwand)
        print("NG     ", Nächtigung, "     ", Nächtigung, "             -      ", NGVSt, NGAufwand)
        if PKW == 0:
            print("Fahrt    ", Fahrt, "     ", Fahrt, "            -       ", FahrtVSt, Fahrtaufwand)
        else:
            print("KM     ", PKW, "     ", PKW, "           -       ", KMVSt, kmAufwand)
        print("Gesamt ", gesa, "     ", gesa, "         -       ", gesVSt, gesAufwand, '\n')

        print("7 TG MA      ", TGAufwand, "                3 RK VB MA ", gesAufwand + gesVSt)

        print("7 NG MA      ", NGAufwand)
        if PKW == 0:
            print("7 Fahrtaufwand", Fahrtaufwand)
        else:
            print("7 km Geld MA", kmAufwand)
        print("2 VSt        ", gesVSt, '\n')

    def DienstreiseUnternehmerin(self, Reisedauer, Nächte, Nächtigungsbeleg, Ländercode, Bahnticket, Taxi, gesKM, km, kmSatz,
                                 Tagsatz):

        Tage = Reisedauer / 12

        # Taggeld
        if Tagsatz is not 0:
            Taggeld = Tage * Tagsatz
        else:
            Tagsatz = Land.getdnmoney(1, Ländercode)[0]
            Taggeld = Tage * Tagsatz
        sttg = Steuern.getbefore10(Taggeld)

        # Nächtigung
        if Nächtigungsbeleg is not 0:
            Nächtigung = Nächtigungsbeleg
        else:
            Nachtsatz = Land.getdnmoney(1, Ländercode)[1]
            Nächtigung = Nächte * Nachtsatz
        stng = Steuern.getbefore10(Nächtigungsbeleg)

        # Fahrt
        Fahrt = Bahnticket + Taxi
        stFahrt = Steuern.getbefore10(Fahrt)

        # PKW
        if kmSatz is not 0.42:
            PKW = km * kmSatz

        TGVSt = Taggeld - sttg
        NGVSt = Nächtigung - stng
        KMVSt = 0
        FahrtVSt = Fahrt - stFahrt
        TGAufwand = Taggeld - TGVSt
        NGAufwand = Nächtigung - NGVSt
        kmAufwand = PKW
        Fahrtaufwand = stFahrt
        gesa = Taggeld + Nächtigung + PKW
        # gesf = Taggeldf + Nächtigungf + kmf
        gesVSt = TGVSt + NGVSt + KMVSt
        gesAufwand = TGAufwand + NGAufwand + kmAufwand + Fahrtaufwand

        if gesKM + km < 30000:
            kmAufwand = PKW

        if gesKM + km > 30000:
            PKW = (gesKM + km - 30000) * 0.42
            if gesKM < 30000:
                Diffkm = 30000 - gesKM
                Diff = Diffkm * kmSatz



        # Beispiel:  Reisekosten.DienstreiseMitarbeiter(25, 2, 125, 43, 68, 28, 0, 0, 0)
        print("Text  Auszahlung   Abzug       n.abzug   VSt     Aufwand")
        print("TG     ", Taggeld, "     ", Taggeld, "           -        ", TGVSt, TGAufwand)
        print("NG     ", Nächtigung, "     ", Nächtigung, "             -      ", NGVSt, NGAufwand)
        if PKW == 0:
            print("Fahrt    ", Fahrt, "     ", Fahrt, "            -       ", FahrtVSt, Fahrtaufwand)
        else:
            print("KM     ", PKW + Diff, "     ", Diff, PKW, KMVSt, kmAufwand)
        print("Gesamt ", gesa, "     ", gesa, "         -       ", gesVSt, gesAufwand, '\n')

        print("7 TG MA      ", TGAufwand, "                3 RK VB MA ", gesAufwand + gesVSt)

        print("7 NG MA      ", NGAufwand)
        if PKW == 0:
            print("7 Fahrtaufwand", Fahrtaufwand)
        else:
            print("7 km Geld MA", kmAufwand)
        print("2 VSt        ", gesVSt, '\n')


    def DienstreiseBewritung(self, Reisedauer, Nächte, Nächtigungsbeleg, Ländercode, Bahnticket, Taxi, gesKM, km, kmSatz,
                                 Tagsatz, Speisen, Getränke):

        Tage = Reisedauer / 12
        stng = 0
        # Taggeld
        if Tagsatz is not 0:
            Taggeld = Tage * Tagsatz
        else:
            Tagsatz = Land.getdnmoney(1, Ländercode)[0]
            Taggeld = Tage * Tagsatz
        sttg = Steuern.getbefore10(Taggeld)

        # Nächtigung
        if Nächtigungsbeleg is not 0:
            Nächtigung = Nächtigungsbeleg
            NAufwand = Steuern.getbefore10(Nächtigung)
        else:
            Nachtsatz = Land.getdnmoney(1, Ländercode)[1]
            Nächtigung = Nächte * Nachtsatz
            NAufwand = Steuern.getbefore10(Nächtigung)




        # Fahrt
        Fahrt = Bahnticket + Taxi
        stFahrt = Steuern.getbefore10(Fahrt)

        # PKW
        if kmSatz is not 0.42:
            PKW = km * kmSatz

        TGVSt = Taggeld - sttg
        KMVSt = 0
        FahrtVSt = Fahrt - stFahrt
        TGAufwand = Taggeld - TGVSt
        NVst = Nächtigung - NAufwand
        kmAufwand = PKW
        Fahrtaufwand = stFahrt
        gesa = Taggeld + Nächtigung + PKW
        # gesf = Taggeldf + Nächtigungf + kmf
        gesVSt = TGVSt + NVst + KMVSt
        gesAufwand = TGAufwand + NVst + kmAufwand + Fahrtaufwand
        Diff = 0


        if gesKM + km < 30000:
            kmAufwand = PKW

        if gesKM + km > 30000:
            PKW = (gesKM + km - 30000) * 0.42
            if gesKM < 30000:
                Diffkm = 30000 - gesKM
                Diff = Diffkm * kmSatz






        # Beispiel:  Reisekosten.DienstreiseMitarbeiter(25, 2, 125, 43, 68, 28, 0, 0, 0)
        print("Text  Auszahlung   Abzug       n.abzug   VSt     Aufwand")
        print("TG     ", Taggeld, "     ", Taggeld, "           -        ", TGVSt, TGAufwand)
        print("NG     ", Nächtigung, "     ", Nächtigung, "             -      ", NVst, NAufwand)
        if PKW == 0:
            print("Fahrt    ", Fahrt, "     ", Fahrt, "            -       ", FahrtVSt, Fahrtaufwand)
        else:
            print("KM     ", PKW + Diff, "     ", PKW, "         ", KMVSt, kmAufwand)
        print("Gesamt ", gesa, "     ", gesa, "         -       ", gesVSt, gesAufwand, '\n')

        print("7 TG MA      ", TGAufwand, "                3 RK VB MA ", gesAufwand + gesVSt)

        print("7 NG MA      ", NAufwand)
        if PKW == 0:
            print("7 Fahrtaufwand", Fahrtaufwand)
        else:
            print("7 km Geld MA", kmAufwand)
        print("2 VSt        ", gesVSt, '\n')

        Werbung.Bewirtung(1, Speisen, Getränke)

# Reisekosten.DienstreiseMitarbeiter(1, 25, 2, 125, 43, 68, 28, 0, 0, 0)
# Reisekosten.DienstreiseUnternehmerin(1, 28, 2, 125, 43, 0, 0, 29800, 1630, 0.42, 0)

Reisekosten.DienstreiseBewritung(1, 63, 5, 0, 43, 0, 0, 9000, 1200, 0.42, 0, 420, 250)

# Refactoring self init, nur 2 funct + Bewirtung, von Kontoerstellung erben, buchungen