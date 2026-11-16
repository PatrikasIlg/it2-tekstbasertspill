# Spiller klasse
class Spiller:
    def __init__(self, navn, helse):
        self.navn = navn
        self.helse = helse

    def angrip(self, fiende):
        skade = 10
        fiende.ta_skade(skade)  # Kaller metoden ta_skade() i Fiende-klassen

    def ta_skade(self, skade):
        self.helse = self.helse - skade  # Trekker skaden fra spillerens helse


# Fiende klasse
class Fiende:
    def __init__(self, navn, helse, styrke):
        self.navn = navn
        self.helse = helse
        self.styrke = styrke

    def ta_skade(self, skade):
        self.helse = self.helse - skade


# Boss fiende klasse
class BossFiende(Fiende):  # BossFiende arver egenskaper og metoder fra Fiende
    def __init__(self, navn, helse, styrke, spesialangrep):
        super().__init__(navn, helse, styrke)  # Bruker __init__ fra Fiende-klassen
        self.spesialangrep = spesialangrep

    def bruk_spesialangrep(self, spiller):
        spiller.ta_skade(self.spesialangrep)  # Gir spilleren skade basert på bossens spesialangrep
        print(self.navn, "bruker spesialangrep")


# Spill klasse
class Spill:
    def __init__(self):
        self.spiller = Spiller("Spiller", 100)  # Lager et spillerobjekt med 100 helse

        # Lager en liste med fem fiendeobjekter
        self.fiender = [
            Fiende("Goblin", 30, 5),
            Fiende("Ork", 40, 10),
            Fiende("Troll", 50, 15),
            Fiende("Drage", 70, 20),
            BossFiende("Demonkonge", 100, 25, 30)
        ]

        self.gjeldende_fiende = 0  # Holder styr på hvilken fiende spilleren møter

    def start(self):
        print("Velkommen til Quiz Battle!")
        print("Du skal kjempe mot fem fiender.")

    def neste_fiende(self):
        self.gjeldende_fiende = self.gjeldende_fiende + 1  # Går videre til neste fiende

        # Sjekker om det fortsatt finnes flere fiender i listen
        if self.gjeldende_fiende < len(self.fiender):
            print("Neste fiende:", self.fiender[self.gjeldende_fiende].navn)
        else:
            print("Du har beseiret alle fiendene!")