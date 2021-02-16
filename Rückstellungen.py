from Steuern import Steuern


class Rückstellungen():


    def RnB(Kostenexkl, Verlustexkl, Ausgang):


        print("7 R+B", Kostenexkl, "                     3 sonstige Rückstellung ", Kostenexkl, '\n')


        if Ausgang == 'verloren':

            print("7 R+B", Verlustexkl, "                     3 LVB ", Steuern.getafter20(Verlustexkl))
            print("2 VSt",  Steuern.getafter20(Verlustexkl) - Verlustexkl, '\n')


            if Kostenexkl <= Verlustexkl:
                print("3 sonstige Rückstellung ", Kostenexkl, "  7 R+B", Kostenexkl,)

            if Kostenexkl > Verlustexkl:
                #Erträge aus der Auflösung
                Erträge = Kostenexkl - Verlustexkl
                print("3 sonstige Rückstellung ", Kostenexkl, "  7 R+B", Kostenexkl, )
                print("                        4 Erträge aus der Auflösung", Erträge )

        if Ausgang == 'gewonnen':
            print("3 sonstige Rückstellung ", Kostenexkl, "  4 Erträge aus der Auflösung", Kostenexkl)



# Beispiel testen


Rückstellungen.RnB(3500, 0,0)

