from Stadion import Stadion

stad = Stadion("stadionok.txt")
Stadion.betolt(stad)
# print(stad)



print(stad.hany_stadion_varosban("New York"))
print(stad.ossz_csapatszam())
print(stad.elso_merkozes("1900-01-01"))
print(stad.nincs_merkozes_datum_ota("1999-12-31"))
print(stad.hany_csapat_jatszott_varosban("Buffalo"))
