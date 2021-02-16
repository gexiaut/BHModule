import json
import io

class setKonto():

    def setK(x,y):
        try:
            to_unicode = unicode
        except NameError:
            to_unicode = str
        with open('Kontenliste1.json') as data_file:
            Konten = json.load(data_file)
        print(Konten)

        x = {}
        x = input()
        y = input()

        Konten.update({x: y})

        # Write JSON file
        with io.open('Kontenliste1.json', 'w', encoding='utf8') as outfile:
            str_ = json.dumps(Konten,
                              indent=4, sort_keys=True,
                              separators=(',', ': '), ensure_ascii=False)
            outfile.write(to_unicode(str_))

        print(Konten)

#setKonto.setK(1,2)

class setSollHaben():

    Soll = []
    Haben = []
    xi = 1

    def setKSH(x,Soll,Haben):
        try:
            to_unicode = unicode
        except NameError:
            to_unicode = str
        with open('SollHaben.json') as data_file:
            SollHaben = json.load(data_file)

        print(SollHaben)

        x = input()
        Soll = input()
        Haben = input()

        SollHaben.update({x : {"Soll": [Soll], "Haben": [Haben]}})

        # Write JSON file
        with io.open('SollHaben.json', 'w', encoding='utf8') as outfile:
            str_ = json.dumps(SollHaben,
                              indent=4, sort_keys=True,
                              separators=(',', ': '), ensure_ascii=False)
            outfile.write(to_unicode(str_))

        print(SollHaben)

    def setSH(x,xi,Soll,Haben):
        try:
            to_unicode = unicode
        except NameError:
            to_unicode = str
        with open('SollHaben.json') as data_file:
            SollHaben = json.load(data_file)

        print(SollHaben)

        x = input()
        xi = input()
        Soll = input()
        Haben = input()

        SollHaben.update({x: {"Soll": {xi: Soll}, "Haben": {xi: Haben}}})


        # Write JSON file
        with io.open('SollHaben.json', 'w', encoding='utf8') as outfile:
            str_ = json.dumps(SollHaben,
                              indent=4, sort_keys=True,
                              separators=(',', ': '), ensure_ascii=False)
            outfile.write(to_unicode(str_))

        print(SollHaben)

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




