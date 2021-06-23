import json
import io

class Konto():



    def __init__(self, kontonummer = "",
                 kontostand=0, soll=0, haben=0, kontokorrent=0):
        # self.__Inhaber = inhaber
        self.__Kontonummer = kontonummer
        self.__Kontostand = kontostand
        self.__Soll = soll
        self.__Haben = haben
        self.__Kontokorrent = kontokorrent

        # Bank = (self, "2000 Bank", 0,0,0)

    def buchen(self, ziel, betrag):
        # print(self.__Kontostand, ziel.__Kontostand)

        if self.__Kontostand == 0:
            print("Kontostand ist 0")

        if self.__Kontostand < betrag:
            print("Kontostand ist kleiner als der zu Buchende Betrag")


        if (self.__Kontostand - betrag < -self.__Kontokorrent):
            # Deckung nicht genuegend
            return False
        else:
            self.__Kontostand -= betrag
            self.__Haben += betrag
            ziel.__Kontostand += betrag
            ziel.__Soll += betrag
            return True

    def einzahlen(self, betrag):
        self.__Kontostand += betrag

    def auszahlen(self, betrag):
        self.__Kontostand -= betrag

    def chkn(self, kontonummer):
        self.__Kontonummer = kontonummer

    def chks(self, kontostand):
        self.__Kontostand = kontostand

    def chs(self, soll):
        self.__Soll = soll

    def chh(self, haben):
        self.__Haben = haben

    def kontostand(self):
        return self.__Kontostand

    def sollhaben(self):
        return self.__Soll, self.__Haben

    def alles(self):
        return self.__Kontonummer, self.__Kontostand, self.__Soll, self.__Haben


with open('Kontenliste1.json') as data_file:
            Kontenliste = json.load(data_file)


    # def speichern(self):
    #     pass in json
    # def laden(self):
    #     pass

    # funct returns


# print(Kontenliste)
# print(list(Kontenliste.keys())[0])
# print(list(Kontenliste.values())[0])


# list(Kontenliste.values())[0] = Konto(list(Kontenliste.keys())[0])

# print(list(Kontenliste.values())[0])
# print(list(Kontenliste.keys())[0])
#
# list(Kontenliste.keys())[0] = Konto(list(Kontenliste.keys())[0])
#
# # Bank = Konto("2000 Bank")
# print(list(Kontenliste.keys())[0].alles())

# Ich = Konto(2)
#

# Bank.einzahlen(200)
# Ich.ueberweisen(Bank, 20)
# # Ich.einzahlen(200)
#
# print(Bank.alles())
# print(Ich.kontostand())
# print(Ich.sollhaben())


#
#     def __init__(self):
#         self.Kontostand = 0
#
#     def setK(self,x,y):
#         try:
#             to_unicode = unicode
#         except NameError:
#             to_unicode = str
#         with open('Kontenliste1.json') as data_file:
#             Konten = json.load(data_file)
#         print(Konten)
#
#         x = {}
#         x = input()
#         y = input()
#
#         Konten.update({x: y})
#
#         # Write JSON file
#         with io.open('Kontenliste1.json', 'w', encoding='utf8') as outfile:
#             str_ = json.dumps(Konten,
#                               indent=4, sort_keys=True,
#                               separators=(',', ': '), ensure_ascii=False)
#             outfile.write(to_unicode(str_))
#
#         print(Konten)
#
#
#     def hinzufügen(self, Menge):
#         self.Kontostand += Menge
#         return self.Kontostand
#
#     def abziehen(self, Menge):
#         self.Kontostand -= Menge
#         return self.Kontostand
#
# #setKonto.setK(1,2)
# class setSollHaben():
#
#     Soll = []
#     Haben = []
#     xi = 1
#
#     def setKSH(self,x,Soll,Haben):
#         try:
#             to_unicode = unicode
#         except NameError:
#             to_unicode = str
#         with open('SollHaben.json') as data_file:
#             SollHaben = json.load(data_file)
#
#         print(SollHaben)
#
#         x = input()
#         Soll = input()
#         Haben = input()
#
#         SollHaben.update({x : {"Soll": [Soll], "Haben": [Haben]}})
#
#         # Write JSON file
#         with io.open('SollHaben.json', 'w', encoding='utf8') as outfile:
#             str_ = json.dumps(SollHaben,
#                               indent=4, sort_keys=True,
#                               separators=(',', ': '), ensure_ascii=False)
#             outfile.write(to_unicode(str_))
#
#         print(SollHaben)
#
#     def setSH(self,x,xi,Soll,Haben):
#         try:
#             to_unicode = unicode
#         except NameError:
#             to_unicode = str
#         with open('SollHaben.json') as data_file:
#             SollHaben = json.load(data_file)
#
#         print(SollHaben)
#
#         x = input()
#         xi = input()
#         Soll = input()
#         Haben = input()
#
#         SollHaben.update({x: {"Soll": {xi: Soll}, "Haben": {xi: Haben}}})
#
#
#         # Write JSON file
#         with io.open('SollHaben.json', 'w', encoding='utf8') as outfile:
#             str_ = json.dumps(SollHaben,
#                               indent=4, sort_keys=True,
#                               separators=(',', ': '), ensure_ascii=False)
#             outfile.write(to_unicode(str_))
#
#         print(SollHaben)

#setSollHaben.setSH(1,1,2000,3000)



        # Fremdwährung = ["NOK, EU"]
        # Kaufen = []
        # Verkaufen = []
        #
        # #if Fremdwährung == "NOK" or "SEK" or "USD" or "EU":
        #
        #
        # Tageskurs1 = 13.31
        # Tageskurs2 = 13.21
        #
        # ersteBuchung = []
        # zweiteBuchung = []
        # dritteBuchung = []
        #
        #
        # if Tageskurs1 > Tageskurs2:
        #     Gewinn = Tageskurs1 - Tageskurs2
        #
        # if Tageskurs1 < Tageskurs2:
        #     Verlust =  Tageskurs2  - Tageskurs1
        #
        #
        # return Gewinn or Verkaufen

    #
    # def danach(später):
    #
    #     pass

#
#
# class Buchungssatz():
#
#     Quellkonto = []
#     Zielkonto = []




# Konten =  {'90': 'Kumulierte Abschreibung',
#                          '630': 'PKW',
#                          '640': 'LKW'}


# class check():
#     def getKonto(Quellkonto, Zielkonto):
#
#         if Quellkonto and Zielkonto in locals():
#             print(Quellkonto, Zielkonto, 'exists')
#         #check if Konto and transactions exist, if yes print amount -> getTransaktions
#         # Soll und haben checken
#
#         return
#
#     def setKonto(FWbetrag, Quellkonto, Zielkonto):
#
#
#         return




