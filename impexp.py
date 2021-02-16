import json
from Steuern import Steuern
from Land import Land

class Umrechnung():
    #FWbetrag = x
    #Fremdwährung = ['USD, SEK, DKK, GBP']
    # Kauf = ['Kaufen, Kaufen1, Verkaufen, Verkaufen1']

    def inEUR(FWbetrag, Fremdwährung, Kauf):
        with open('Währungen.json') as data_file:
            Fremdwährungen = json.load(data_file)

        WEUR = Fremdwährungen['EUR']

        USDK = WEUR['USD']['Kaufen']
        USDK1 = WEUR['USD']['Kaufen1']
        USDV = WEUR['USD']['Verkaufen']
        USDV1 = WEUR['USD']['Verkaufen1']
        SEKK = WEUR['SEK']['Kaufen']
        SEKK1 = WEUR['SEK']['Kaufen1']
        SEKV = WEUR['SEK']['Verkaufen']
        SEKV1 = WEUR['SEK']['Verkaufen1']
        GBPK = WEUR['GBP']['Kaufen']
        GBPK1 = WEUR['GBP']['Kaufen1']
        GBPV = WEUR['GBP']['Verkaufen']
        GBPV1 = WEUR['GBP']['Verkaufen1']
        SFRK = WEUR['SFR']['Kaufen']
        SFRK1 = WEUR['SFR']['Kaufen1']
        SFRV = WEUR['SFR']['Verkaufen']
        SFRV1 = WEUR['SFR']['Verkaufen1']
        #print(FWbetrag, Kauf, Fremdwährung)

        if Kauf == 'Verkaufen' or Kauf == 'Verkaufen1':
            print('Verkauf')
            #Buchungssatz
            if Fremdwährung == 'USD' and Kauf == 'Verkaufen':
                print(USDV)
                UmrechnungEUR = FWbetrag / USDV
            if Fremdwährung == 'USD' and Kauf == 'Verkaufen1':
                print(USDV1)
                UmrechnungEUR = FWbetrag / USDV1

            if Fremdwährung == 'GBP' and Kauf == 'Verkaufen':
                print(GBPV)
                UmrechnungEUR = FWbetrag / GBPV
            if Fremdwährung == 'GBP' and Kauf == 'Verkaufen1':
                print(GBPV1)
                UmrechnungEUR = FWbetrag / GBPV1

            if Fremdwährung == 'SEK' and Kauf == 'Verkaufen':
                print(SEKV)
                UmrechnungEUR = FWbetrag / SEKV
            if Fremdwährung == 'SEK' and Kauf == 'Verkaufen1':
                print(SEKV1)
                UmrechnungEUR = FWbetrag / SEKV1

            if Fremdwährung == 'SFR' and Kauf == 'Verkaufen':
                print(SFRV)
                UmrechnungEUR = FWbetrag / SFRV
            if Fremdwährung == 'SFR' and Kauf == 'Verkaufen1':
                print(SFRV1)
                UmrechnungEUR = FWbetrag / SFRV1

        if Kauf == 'Kaufen' or Kauf == 'Kaufen1':
            print('Kauf')
            if Fremdwährung == 'USD' and Kauf == 'Kaufen':
                print(USDK)
                UmrechnungEUR = FWbetrag / USDK
            if Fremdwährung == 'USD' and Kauf == 'Kaufen1':
                print(USDK1)
                UmrechnungEUR = FWbetrag / USDK1

            if Fremdwährung == 'GBP' and Kauf == 'Kaufen':
                print(GBPK)
                UmrechnungEUR = FWbetrag / GBPK
            if Fremdwährung == 'GBP' and Kauf == 'Kaufen1':
                print(GBPK1)
                UmrechnungEUR = FWbetrag / GBPK1

            if Fremdwährung == 'SEK' and Kauf == 'Kaufen':
                print(SEKK)
                UmrechnungEUR = FWbetrag / SEKV
            if Fremdwährung == 'SEK' and Kauf == 'Kaufen1':
                print(SEKK1)
                UmrechnungEUR = FWbetrag / SEKK1

            if Fremdwährung == 'SFR' and Kauf == 'Kaufen':
                print(SFRK)
                UmrechnungEUR = FWbetrag / SFRK
            if Fremdwährung == 'SFR' and Kauf == 'Kaufen1':
                print(SFRK1)
                UmrechnungEUR = FWbetrag / SFRK1

        print(UmrechnungEUR)

        return UmrechnungEUR

    def Export(Umgerechnet, UmrechnungRabatt, Kundenbezahlung):

        # Verkauf
        print('\n', "2 KFD Export ", Umgerechnet, "4 Exporterlöse", Umgerechnet, '\n')

        # Nachträglicher Rabatt
        print("4 Erlösberichtigung Export", UmrechnungRabatt, "2 KFD Export", UmrechnungRabatt,'\n')

        Rest = Umgerechnet - UmrechnungRabatt
        Kursgewinn = Kundenbezahlung - Rest

        # Einreichung des Schecks bei der Bank
        print("2 Bank", Rest, "2 KFD Export", Kundenbezahlung)
        print("                         4 Kursgewinn", Kursgewinn)

        #Bsp:
        # c = Umrechnung.inEUR(60000, 'SFR', 'Kaufen')
        # c1 = Umrechnung.inEUR(5000, 'SFR', 'Kaufen')
        #
        # Umrechnung.Export(c, c1, 34209.30)

    def Import(Umgerechnet):

        # Einkauf
        print(" 5 HW-Verbrauch ", Umgerechnet, "3 LVB Import", Umgerechnet)
        # print("2 EUSt entrichtet", Umgerechnet)
        # print("2 VSt", Umgerechnet)

        # Überweisung der ER
        print("3 LVB", Umgerechnet, "2 Bank", Umgerechnet,'\n')
        # print("7 Kursverlust", Umgerechnet, "5 Skontoertrag Import", Umgerechnet, '\n')
        # print("7 Spesen des Geldverkehrs ", Umgerechnet, "2 Bank", Umgerechnet, '\n')

    def igL(Gesnet, UmrechnungRabatt, Skonto):

        # AR Lieferung nach Mailand
        print("2 KFD igL", Gesnet, "4 Erlöse", Gesnet)
        # print("2 EUSt entrichtet", Umgerechnet)
        # print("2 VSt", Umgerechnet)

        # AG Nachträglich gewährter Rabat
        if UmrechnungRabatt is not UmrechnungRabatt == 0 or None:
            print(". 4 Erlösberichtigung", UmrechnungRabatt, "2 KFD igL", UmrechnungRabatt,'\n')
            # print("7 Kursverlust", Umgerechnet, "5 Skontoertrag Import", Umgerechnet, '\n')
            # print("7 Spesen des Geldverkehrs ", Umgerechnet, "2 Bank", Umgerechnet, '\n')

        # BK Überweisung der ER
        if Skonto is not Skonto == 0 or None:
            print("2 Bank", Gesnet, "2 KFD igL", Gesnet, '\n')
            print("4 Skontoaufwand igL", Skonto, "4 Kursgewinn", Skonto, '\n')
            # print("7 Spesen des Geldverkehrs ", Umgerechnet, "2 Bank", Umgerechnet, '\n')

        #reverse charge
        # Transporte ganz normal

    def igE(Gesnet, Gutschrift, Skonto):

        # ER Wareneinkauf in Nürnberg
        Gesamtbrutto = Steuern.getafter20(Gesnet)
        VSt = Gesamtbrutto - Gesnet
        print("5 HW-Verbrauch ", Gesnet, "3 LVB igE", Gesnet)
        print("2 VSt igE ", VSt, "3 USt igE", VSt, '\n')
        # print("2 EUSt entrichtet", Umgerechnet)
        # print("2 VSt", Umgerechnet)

        # EG Gutschrift
        if Gutschrift is not Gutschrift == 0 or None:
            print("3 LVB igE", Gutschrift, "5 HW-Verbrauch", Gutschrift, '\n')
            print("2 VSt igE ", VSt, "3 USt igE", VSt, '\n')
            # print("7 Spesen des Geldverkehrs ", Umgerechnet, "2 Bank", Umgerechnet, '\n')

        # BK Überweisung der ER
        if Skonto is not Skonto == 0 or None:
            print("3 LVB", Gesnet, "2 Bank ", Gesnet, '\n')
            print("3 USt igE", Skonto, "2 VSt igE", Skonto, '\n')
            print("7 Spesen des Geldverkehrs", Skonto, "2 Bank", Skonto, '\n')
            # print("7 Spesen des Geldverkehrs ", Umgerechnet, "2 Bank", Umgerechnet, '\n')

    def Außenhandel(Gesnet, Gutschrift, Skonto):

        pass