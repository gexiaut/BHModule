from Steuern import Steuern


class Rückstellungen():


    def RnB(self, Kostenexkl, Verlustexkl, Ausgang):
        print("7 R+B", Kostenexkl, "                     3 sonstige Rückstellung ", Kostenexkl, '\n')

        if Ausgang == 'verloren':

            if Kostenexkl < Steuern.getbefore20(Verlustexkl):
                print("7 R+B", Steuern.getbefore20(Verlustexkl), "                     3 LVB ", Verlustexkl)
                print("2 VSt", Verlustexkl - Steuern.getbefore20(Verlustexkl), '\n')
                print("3 sonstige Rückstellung ", Kostenexkl, "  7 R+B", Kostenexkl,)

            if Kostenexkl > Steuern.getbefore20(Verlustexkl):
                #Erträge aus der Auflösung
                Erträge = Kostenexkl - Steuern.getbefore20(Verlustexkl)
                print("7 R+B", Steuern.getbefore20(Verlustexkl), "                     3 LVB ", Verlustexkl)
                print("2 VSt", Verlustexkl - Steuern.getbefore20(Verlustexkl), '\n')

                print("3 sonstige Rückstellung ", Kostenexkl, "  7 R+B", Steuern.getbefore20(Verlustexkl), )
                print("                        4 Erträge aus der Auflösung", Erträge )

        if Ausgang == 'gewonnen':
            print("3 sonstige Rückstellung ", Kostenexkl, "  4 Erträge aus der Auflösung", Kostenexkl)

# Rückstellungen.RnB(1, 3500, 3840,'gewonnen')
# Rückstellungen.RnB(1, 3500, 3840,'verloren')

# mehr beispiele
