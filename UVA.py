from Steuern import Steuern

class UVA():

    Vorsteuer = 0
    VStigE20 = 0
    VStigE10 = 0
    EUstgeschuldet = 0
    erhalteneAnzahlung20 = 0
    erhalteneAnzahlung10 = 0
    Umsatzsteuer20 = 0
    UstErwerbsteuer20 = 0
    Umsatzerloese20 = 0
    Exporterloese0 = 0
    igL = 0
    Erloesberichtigung20 = 0
    Erlösberichtigung10 = 0
    Skontoaufwand10 = 0
    Skontoaufwand20 = 0
    SkontoaufwandigL = 0
    Eigenverbrauch20 = 0
    Mieterträge20 = 0
    Mieterträge10 = 0

    def Saldenerlöse(self, ErhalteneAnzahlung20,  Umsatzerlöse10, Umsatzerlöse20, Mieterträge10, igL, Eigenverbrauch10, Eigenverbrauch20, Exporterlöse0):

        if ErhalteneAnzahlung20 == 0 or None:
            ErhalteneAnzahlung20 = 0
        if Umsatzerlöse10 == 0 or None:
            Umsatzerlöse10 = 0
        if Umsatzerlöse20 == 0 or None:
            Umsatzerlöse20 = 0
        if Mieterträge10 == 0 or None:
            Mieterträge10 = 0
        if igL == 0 or None:
            igL = 0
        if Eigenverbrauch10 == 0 or None:
            Eigenverbrauch10 = 0
        if Eigenverbrauch20 == 0 or None:
            Eigenverbrauch20 = 0
        if Exporterlöse0 == 0 or None:
            Exporterlöse0 = 0

        Gesamt = ErhalteneAnzahlung20 + Umsatzerlöse10 + Umsatzerlöse20 + Mieterträge10 + igL + Eigenverbrauch10 + Eigenverbrauch20 + Exporterlöse0
        return Gesamt

    def Saldenaufwand(self, Skontoaufwand10, Skontoaufwand20, SkontoaufwandigL, SkontoaufwandExport, Erlösberichtigung10, Erlösberichtigung20):

        if Skontoaufwand10 == 0 or None:
            Skontoaufwand10 = 0
        if Skontoaufwand20 == 0 or None:
            Skontoaufwand20 = 0
        if SkontoaufwandigL == 0 or None:
            SkontoaufwandigL = 0
        if SkontoaufwandExport == 0 or None:
            SkontoaufwandExport = 0
        if Erlösberichtigung10 == 0 or None:
            Erlösberichtigung10 = 0
        if Erlösberichtigung20 == 0 or None:
            Erlösberichtigung20 = 0


        Gesamt = Skontoaufwand10 + Skontoaufwand20 + SkontoaufwandigL + SkontoaufwandExport + Erlösberichtigung10 + Erlösberichtigung20
        return Gesamt

    def Saldensteuern(self, Vorsteuer, Umsatzsteuer,  EUStgeschuldet, USTigE10, USTigE20, VStiGE20, VStiGE10, USTErwerbsteuer20, VSTErwerbsteuer20):

        if Vorsteuer == 0 or None:
            Vorsteuer = 0
        if Umsatzsteuer == 0 or None:
            Umsatzsteuer = 0
        if EUStgeschuldet == 0 or None:
            EUStgeschuldet = 0
        if USTigE10 == 0 or None:
            USTigE10 = 0
        if USTigE20 == 0 or None:
            USTigE20 = 0
        if VStiGE20 == 0 or None:
            VStiGE20 = 0
        if VStiGE10 == 0 or None:
            VStiGE10 = 0
        if USTErwerbsteuer20 == 0 or None:
            USTErwerbsteuer20 = 0
        if VSTErwerbsteuer20 == 0 or None:
            VSTErwerbsteuer20 = 0



        Ust = Umsatzsteuer + EUStgeschuldet + USTigE10 + USTigE20 + USTErwerbsteuer20
        Vst = Vorsteuer + VStiGE20 + VStiGE10 + VSTErwerbsteuer20

        Gesamt = Ust - Vst

        return Gesamt



#Beispiel:
# s = UVA.Saldensteuern(3157,3715.50,571,0,0,0,0,897,897)
# e = UVA.Saldenerlöse(0,8300,13500,0,3800,0,1310,5200)
# a = UVA.Saldenaufwand(85,0,110,0,0,340)
# x = a - e + s
#
#
# Eigenverbrauch = 1310
# Exporterlöse = 5200
# Umsatzerlöse20 = 13500
# Umsatzerlöse10 = 8300
# Skontoaufwand10 = 85
# Erlösberichtigung = 340
# LLsumme = e - Eigenverbrauch - a
# Ustermittlungssume = e - a
#
# Umsatzerlöse2 = Umsatzerlöse20 + Eigenverbrauch - Erlösberichtigung
# Umsatzerlöse1 = Umsatzerlöse10 - Skontoaufwand10
#
# ust2 = Steuern.getafter20(Umsatzerlöse2) - Umsatzerlöse2
# ust1 = Steuern.getafter10(Umsatzerlöse1) - Umsatzerlöse1
# igL = 3800  - 110 #igL - SkontoaufwandigL,
# USTErwerbsteuer20 = 897
#
# Gesamtbetrag = Ustermittlungssume - (Exporterlöse + igL)
#
# ustigE = 5 * USTErwerbsteuer20
# Vorsteuer = 3157
# Einfuhr = 571
# VstigE = 897
# Vstgesamt = Vorsteuer + Einfuhr + VstigE
# Ustgesamt = ust2 + ust1 + USTErwerbsteuer20
# Überschuss = Vstgesamt - Ustgesamt
#
#
#
# print('4. Berechnung der Ust')
# print('4.1 Lieferungen, Leistungen', LLsumme)
# print('4.2 zuzüglich Eigenverbrauch', Eigenverbrauch)
# print('4.4 Summe', Ustermittlungssume)
#
# print('4.5 steuerfrei MIT Steuerabzug', Exporterlöse)
# print('4.8 igL', igL)
# print('4.13 Gesamtbetrag', Gesamtbetrag)
#
# print('4.14 20% Steuern Bemessungsgrundlage:', Umsatzerlöse2, 'Umsatzsteuer:', ust2)
# print('4.15 10% Steuern Bemessungsgrundlage:', Umsatzerlöse1, 'Umsatzsteuer:', ust1)
#
# print('4.25 igE:', ustigE)
# print('4.27 Gesamt igE:', ustigE)
# print('4.28 davon zu versteuern mit 20%:', ustigE, 'Umsatzsteuer:', USTErwerbsteuer20)
# #print('4.29 davon zu versteuern mit 10%:', ustigE1, 'Umsatzsteuer:', USTErwerbsteuer10)
#
# print('5. Berechnung der Vst')
# print('5.1 Gesamte Vorsteuern', Vorsteuer)
# print('5.3 Vst Einfuhr', Einfuhr)
# print('5.4 Vst igE', VstigE)
# print('5.13 Vstgesamt ', Vstgesamt)
#
# if Überschuss > 0:
#     print('6. Überschuss', Überschuss)
# if Überschuss < 0:
#     Überschuss = Überschuss * -1
#     print('6. Vorrauszahlung', Überschuss)

# Kontennummern hinzufügen
