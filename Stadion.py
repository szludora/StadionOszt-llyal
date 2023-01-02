from Csapat import Csapat


class Stadion:

    def __init__(self, fajlnev):
        self.__fajlnev = fajlnev
        self.__lista = []

    def betolt(self):

        x = open(self.__fajlnev, "r", encoding="utf-8")
        fejlec = x.readline()
        sorok = x.readlines()
        # print(sorok)

        i = 0
        while i < len(sorok):
            sor = sorok[i].strip().split(";")
            elem = Csapat(sor[0], sor[1], sor[2], sor[3], sor[4])
            self.__lista.append(elem)
            # print(elem)
            i += 1

    def __str__(self):
        return f"{self.__lista}"

    def hany_stadion_varosban(self, varos):
        db = 0
        i = 0
        while i < len(self.__lista):
            csapat = self.__lista[i]
            if csapat.varos == varos:
                db += 1
            i += 1

        return f"\nÖsszesen {db} db stadion található {varos} -ban"

    def ossz_csapatszam(self):
        i = 0
        csapszam = []

        while i < len(self.__lista):
            csapat = self.__lista[i]
            if csapat.csapatok_szama not in csapszam:
                csapszam.append(csapat.csapatok_szama)
            i += 1

        return f"\nÖsszesen {len(csapszam)} csapat van."

    def elso_merkozes(self, datum):
        db = 0
        i = 0
        lista = []

        while i < len(self.__lista):
            csapat = self.__lista[i]
            if csapat.elso < datum:
                db += 1
            if csapat.stadion not in lista:
                lista.append(csapat.stadion)
            i += 1

        return f"\n{db} db stadionban {datum} előtt rendezték meg az első mérkőzést\n{lista}"

    def nincs_merkozes_datum_ota(self, datum):
        db = 0
        i = 0

        while i < len(self.__lista):
            csapat = self.__lista[i]
            if csapat.utolso < datum:
                db += 1
            i += 1

        return f"\n{db} db stadionban nem volt mérkőzés {datum} óta."

    def hany_csapat_jatszott_varosban(self, varos):
        db = 0
        i = 0

        while i < len(self.__lista):
            csapat = self.__lista[i]
            if csapat.varos == varos:
                db += 1
            i += 1

        return f"\nÖsszesen {db} db csapat játszott {varos}-ban"
