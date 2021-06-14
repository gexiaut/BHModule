import json
from Steuern import Steuern
from Land import Land
from Kontenerstellung import Konto
from Skonto import Skonto


class Umrechnung(Konto):
    #FWbetrag = x
    #Fremdwaehrung = ['USD, SEK, DKK, GBP']
    # Kauf = ['Kaufen, Kaufen1, Verkaufen, Verkaufen1']

    def inEUR(self, FWbetrag, Fremdwaehrung, Kauf):
        with open('Waehrungen.json') as data_file:
            Fremdwaehrungen = json.load(data_file)

        WEUR = Fremdwaehrungen['EUR']

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
        #print(FWbetrag, Kauf, Fremdwaehrung)

        if Kauf == 'Verkaufen' or Kauf == 'Verkaufen1':
            print('Verkauf')
            #Buchungssatz
            if Fremdwaehrung == 'USD' and Kauf == 'Verkaufen':
                print(USDV)
                UmrechnungEUR = FWbetrag / USDV
            if Fremdwaehrung == 'USD' and Kauf == 'Verkaufen1':
                print(USDV1)
                UmrechnungEUR = FWbetrag / USDV1

            if Fremdwaehrung == 'GBP' and Kauf == 'Verkaufen':
                print(GBPV)
                UmrechnungEUR = FWbetrag / GBPV
            if Fremdwaehrung == 'GBP' and Kauf == 'Verkaufen1':
                print(GBPV1)
                UmrechnungEUR = FWbetrag / GBPV1

            if Fremdwaehrung == 'SEK' and Kauf == 'Verkaufen':
                print(SEKV)
                UmrechnungEUR = FWbetrag / SEKV
            if Fremdwaehrung == 'SEK' and Kauf == 'Verkaufen1':
                print(SEKV1)
                UmrechnungEUR = FWbetrag / SEKV1

            if Fremdwaehrung == 'SFR' and Kauf == 'Verkaufen':
                print(SFRV)
                UmrechnungEUR = FWbetrag / SFRV
            if Fremdwaehrung == 'SFR' and Kauf == 'Verkaufen1':
                print(SFRV1)
                UmrechnungEUR = FWbetrag / SFRV1

        if Kauf == 'Kaufen' or Kauf == 'Kaufen1':
            print('Kauf')
            if Fremdwaehrung == 'USD' and Kauf == 'Kaufen':
                print(USDK)
                UmrechnungEUR = FWbetrag / USDK
            if Fremdwaehrung == 'USD' and Kauf == 'Kaufen1':
                print(USDK1)
                UmrechnungEUR = FWbetrag / USDK1

            if Fremdwaehrung == 'GBP' and Kauf == 'Kaufen':
                print(GBPK)
                UmrechnungEUR = FWbetrag / GBPK
            if Fremdwaehrung == 'GBP' and Kauf == 'Kaufen1':
                print(GBPK1)
                UmrechnungEUR = FWbetrag / GBPK1

            if Fremdwaehrung == 'SEK' and Kauf == 'Kaufen':
                print(SEKK)
                UmrechnungEUR = FWbetrag / SEKV
            if Fremdwaehrung == 'SEK' and Kauf == 'Kaufen1':
                print(SEKK1)
                UmrechnungEUR = FWbetrag / SEKK1

            if Fremdwaehrung == 'SFR' and Kauf == 'Kaufen':
                print(SFRK)
                UmrechnungEUR = FWbetrag / SFRK
            if Fremdwaehrung == 'SFR' and Kauf == 'Kaufen1':
                print(SFRK1)
                UmrechnungEUR = FWbetrag / SFRK1

        print(UmrechnungEUR, '\n')

        return UmrechnungEUR

    def Export(self, Umgerechnet, UmrechnungRabatt, Kundenbezahlung):

        # Verkauf
        print("2 KDF Export ", Umgerechnet, "4 Exporterloese", Umgerechnet, '\n')
        Exporterloese.einzahlen(Umgerechnet)
        Exporterloese.buchen(KDFe, Umgerechnet)

        print(Umgerechnet)

        # Nachtraeglicher Rabatt
        print("4 Erloesberichtigung Export", UmrechnungRabatt, "2 KDF Export", UmrechnungRabatt, '\n')

        # KDFe.buchen(Erloesberichtigung, Umgerechnet)


        Rest = Umgerechnet - UmrechnungRabatt
        Kursgewinn = Kundenbezahlung - Rest

        # Einreichung des Schecks bei der Bank
        print("2 Bank", Kundenbezahlung, "2 KFD Export", Rest )
        print("                         4 Kursgewinn", Kursgewinn, '\n')
        Kursg.einzahlen(Kursgewinn)
        KDFe.buchen(Bank, Kundenbezahlung)
        Kursg.buchen(Bank, Kursgewinn)

        #Bsp:
        # c = Umrechnung.inEUR(60000, 'SFR', 'Kaufen')
        # c1 = Umrechnung.inEUR(5000, 'SFR', 'Kaufen')
        #
        # Umrechnung.Export(c, c1, 34209.30)

    def Import(self, Umgerechnet):

        # Einkauf
        print(" 5 HW-Verbrauch ", Umgerechnet, "3 LVB Import", Umgerechnet, '\n')
        # print("2 EUSt entrichtet", Umgerechnet)
        # print("2 VSt", Umgerechnet)

        # Überweisung der ER
        print("3 LVB", Umgerechnet, "2 Bank", Umgerechnet, '\n')
        # print("7 Kursverlust", Umgerechnet, "5 Skontoertrag Import", Umgerechnet, '\n')
        # print("7 Spesen des Geldverkehrs ", Umgerechnet, "2 Bank", Umgerechnet, '\n')

        Skonto(1, Umgerechnet, 0.02)

    def igL(self, Gesnet, UmrechnungRabatt, Skonto):

        # AR Lieferung nach Mailand
        print("2 KFD igL", Gesnet, "4 Erloese", Gesnet)
        # print("2 EUSt entrichtet", Umgerechnet)
        # print("2 VSt", Umgerechnet)

        # AG Nachtraeglich gewaehrter Rabat
        if UmrechnungRabatt is not UmrechnungRabatt == 0 or None:
            print(" 4 Erloesberichtigung", UmrechnungRabatt, "2 KFD igL", UmrechnungRabatt,'\n')
            # print("7 Kursverlust", Umgerechnet, "5 Skontoertrag Import", Umgerechnet, '\n')
            # print("7 Spesen des Geldverkehrs ", Umgerechnet, "2 Bank", Umgerechnet, '\n')

        # BK Überweisung der ER
        if Skonto is not Skonto == 0 or None:
            print("2 Bank", Gesnet, "2 KFD igL", Gesnet, '\n')
            print("4 Skontoaufwand igL", Skonto, "4 Kursgewinn", Skonto, '\n')
            # print("7 Spesen des Geldverkehrs ", Umgerechnet, "2 Bank", Umgerechnet, '\n')

        #reverse charge
        # Transporte ganz normal

    def igE(self, Gesnet, Gutschrift, Skonto):

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

    # def Aussenhandel(self, Gesnet, Gutschrift, Skonto):
    #     Überbegriff für Import/Export und igE/igL


Exporterloese = Konto("4123 Exporterloese")
Erloesberichtigung = Konto("4222 Erloesberichtigung")
Kursg= Konto("4111 Kursgewinn")
Kursv = Konto("7111 Kursverlust")
KDFe = Konto("2123 KDF Export")
LVBe = Konto("3123 LVB Export")
KDFigL = Konto("2111 KDFigL")
LVBigE = Konto("3111 LVBigE")





Maschinen = Konto("0100 Maschinen")
KDF = Konto("210 KDF")
KD3 = Konto("3103 KD3")
LVB = Konto("310 LVB")
Bank = Konto("2000 Bank")
Ust = Konto("3500 Ust")
Vst = Konto("2500 Vst")
Erloese = Konto("4000 Erloese")







c = Umrechnung.inEUR(1, 12500, 'USD', 'Kaufen1')
# c1 = Umrechnung.inEUR(2, 5000, 'SFR', 'Kaufen')
d = Umrechnung.Import(1, c)

print(d)

# Export
# c = Umrechnung.inEUR(1, 60000, 'SFR', 'Kaufen')
# c1 = Umrechnung.inEUR(2, 5000, 'SFR', 'Kaufen')
# Umrechnung.Export(1, c, c1, 34209.30)
# print(Bank.alles())
# print(Kursg.alles())
# print(Erloesberichtigung.alles())
# print(KDFe.alles())
# print(Exporterloese.alles())

# Import
# c = Umrechnung.inEUR(1, 12500, 'USD', 'Kaufen1')
#  c1 = Umrechnung.inEUR(2, 5000, 'SFR', 'Kaufen')
# d = Umrechnung.Import(1, c)

# print(Bank.alles())
# print(Kursg.alles())
# print(Erloesberichtigung.alles())
# print(KDFe.alles())
# print(Exporterloese.alles())