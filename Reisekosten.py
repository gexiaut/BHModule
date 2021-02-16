from Land import Land
from Steuern import Steuern

class Reisekosten():

    # if Reisedauer < 3h kein Tagesgeld
    # Nächtigung, Pauschale 15€/Nacht oder Belege
    # Öffis Aufwendungen voll
    # kmges < 15000

    def DienstreiseMitarbeiter(Reisedauer, Nächte, Nächtigungsbeleg, Ländercode, Bahnticket, Taxi, km, kmSatz, Tagsatz):

        Tage = Reisedauer / 12


        # Taggeld
        if Tagsatz is not 0:
            Taggeld = Tage * Tagsatz
        else:
            Tagsatz = Land.getdnmoney(Ländercode)
            Taggeld = Tage * Tagsatz
        sttg = Steuern.getbefore10(Taggeld)

        # Nächtigung
        if Nächtigungsbeleg is not 0:
            Nächtigung = Nächtigungsbeleg
        else:
            Nachtsatz = Land.getdnmoney(Ländercode)
            Nächtigung = Nächte * Nachtsatz
        stng = Steuern.getbefore10(Nächtigungsbeleg)

        # Fahrt
        Fahrt = Bahnticket + Taxi
        stFahrt = Steuern.getbefore10(Fahrt)

        # PKW
        if kmSatz is not 0.42:
            PKW = km * kmSatz
        else:
            kmSatz = 0.42
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


        # Beispiel:  Reisekosten.DienstreiseMitarbeiter(25, 2, 125, 43, 68, 28, 0, 0, 0)
        print("Text  Auszahlung   Frei       Pflichtig   VSt     Aufwand")
        print("TG     ", Taggeld,   Taggeld,    "    -   ",  TGVSt ,     TGAufwand)
        print("NG     ", Nächtigung,Nächtigung, "      -   ",  NGVSt ,     NGAufwand)
        if PKW == 0:
            print("Fahrt     ", Fahrt, Fahrt, "    -   ", FahrtVSt, Fahrtaufwand)
        else:
            print("KM     ", PKW,   PKW,              "    -   ",  KMVSt ,     kmAufwand)
        print("Gesamt ", gesa, gesa,            "    -",  gesVSt,      gesAufwand, '\n')


        print("7 TG MA", TGAufwand, "                     3 RK VB MA ", gesAufwand)
        print("7 NG MA ", NGAufwand )
        if PKW == 0:
            print("7 Fahrtaufwand", Fahrtaufwand)
        else:
            print("7 km Geld MA", kmAufwand)
        print("2 VSt", gesVSt, '\n')

    def DienstreiseUnternehmerin(Reisedauer, Nächte, Nächtigungsbeleg, Ländercode, Bahnticket, Taxi, km, kmSatz, Tagsatz):

        Tage = Reisedauer / 12

        # Taggeld
        if Tagsatz is not 0:
            Taggeld = Tage * Tagsatz
        else:
            Tagsatz = Land.getdnmoney(Ländercode)
            Taggeld = Tage * Tagsatz
        sttg = Steuern.getbefore10(Taggeld)

        # Nächtigung
        if Nächtigungsbeleg is not 0:
            Nächtigung = Nächtigungsbeleg
        else:
            Nachtsatz = Land.getdnmoney(Ländercode)
            Nächtigung = Nächte * Nachtsatz
        stng = Steuern.getbefore10(Nächtigungsbeleg)

        # Fahrt
        Fahrt = Bahnticket + Taxi
        stFahrt = Steuern.getbefore10(Fahrt)

        # PKW
        if kmSatz is not 0.42:
            PKW = km * kmSatz
        else:
            kmSatz = 0.42
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


        # Beispiel:  Reisekosten.DienstreiseMitarbeiter(25, 2, 125, 43, 68, 28, 0, 0, 0)
        print("Text  Auszahlung   Frei       Pflichtig   VSt                    Aufwand")
        print("TG     ", Taggeld,   Taggeld,    "    -   ",  TGVSt ,            TGAufwand)
        print("NG     ", Nächtigung,Nächtigung, "      -   ",  NGVSt ,          NGAufwand)
        if PKW == 0:
            print("Fahrt     ", Fahrt, Fahrt, "    -   ", FahrtVSt,             Fahrtaufwand)
        else:
            print("KM     ", PKW,   PKW,              "    -   ",  KMVSt ,      kmAufwand)
        print("Gesamt ", gesa, gesa,            "    -",  gesVSt,               gesAufwand, '\n')

        print("Text  Auszahlung   Abzug  n.abzug         VSt                Aufwand")
        print("TG     ", Taggeld, Taggeld, "    -   ", TGVSt,               TGAufwand)
        print("NG     ", Nächtigung, Nächtigung, "      -   ", NGVSt,       NGAufwand)
        if PKW == 0:
            print("Fahrt     ", Fahrt, Fahrt, "    -   ", FahrtVSt,         Fahrtaufwand)
        else:
            print("KM     ", PKW, PKW, "    -   ", KMVSt,                   kmAufwand)
        print("Gesamt ", gesa, gesa, "    -", gesVSt,                       gesAufwand, '\n')


        print("7 TG MA", TGAufwand, "                     3 RK VB MA ", gesAufwand)
        print("7 NG MA ", NGAufwand )
        if PKW == 0:
            print("7 Fahrtaufwand", Fahrtaufwand)
        else:
            print("7 km Geld MA", kmAufwand)
        print("2 VSt", gesVSt, '\n')

    def DienstreiseBewirtung(Reisedauer):
        Reisedauer
        Taggeld = 0
        Nächtigung = 135
        PKW = 1610
        # kmges < 15000
        # Bahnticket = 68
        # Taxirechnung = 28
        km = PKW * 0, 42
        Taggeldf = 0
        Nächtigungf = 0
        kmf = 0
        TGAufwand = 0
        NGAufwand = 0
        kmAufwand = 0
        TGVSt = 0
        NGVSt = 0
        KMVSt = 0

        gesa = Taggeld + Nächtigung + km
        gesf = Taggeldf + Nächtigungf + kmf
        gesVSt = TGVSt + NGVSt + KMVSt
        gesAufwand = TGAufwand + NGAufwand + kmAufwand
        # BK  Vorschüsse
        print("Text  Auszahlung  Frei       Pflichtig   VSt     Aufwand")
        print("TG", Taggeld, Taggeldf, "-", TGVSt, TGAufwand)
        print("NG", Nächtigung, Nächtigungf, "-", NGVSt, NGAufwand)
        print("KM", km, kmf, "-", KMVSt, kmAufwand)
        print("Gesamt", gesa, gesf, "-", gesVSt, gesAufwand)


Reisekosten.DienstreiseMitarbeiter(25, 2, 125, 43, 68, 28, 0, 0, 0)