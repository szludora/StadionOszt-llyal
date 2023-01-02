class Csapat:

    def __init__(self, stadion, varos, csapatok_szama, elso, utolso):
        self.stadion = stadion
        self.varos = varos
        self.csapatok_szama = csapatok_szama
        self.elso = elso
        self.utolso = utolso

    def __str__(self):
        return f"{self.stadion}, {self.varos}, {self.csapatok_szama}, {self.elso}, {self.utolso}"
