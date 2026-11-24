
# Spiller klasse
class Spiller:
    def __init__(self, navn, helse):
        self.navn = navn
        self.helse = helse

    def angrip(self, fiende):
        skade = 10
        fiende.ta_skade(skade)
        print("Du angriper", fiende.navn, "og gir", skade, "skade!")

    def ta_skade(self, skade):
        self.helse = self.helse - skade
        print("Du fikk", skade, "skade!")
        print("Din helse:", self.helse)


# Fiende klasse
class Fiende:
    def __init__(self, navn, helse, styrke):
        self.navn = navn
        self.helse = helse
        self.styrke = styrke

    def ta_skade(self, skade):
        self.helse = self.helse - skade
        print(self.navn, "har", self.helse, "helse igjen.")

        
# Boss fiende klasse
class BossFiende(Fiende):
    def __init__(self, navn, helse, styrke, spesialangrep):
        super().__init__(navn, helse, styrke)
        self.spesialangrep = spesialangrep

    def bruk_spesialangrep(self, spiller):
        print(self.navn, "bruker spesialangrep!")
        spiller.ta_skade(self.spesialangrep)


# Spill klasse
class Spill:
    def __init__(self):
        self.spiller = Spiller("Spiller", 100)

        self.fiender = [
            Fiende("Goblin", 30, 5),
            Fiende("Ork", 40, 10),
            Fiende("Troll", 50, 15),
            Fiende("Drage", 70, 20),
            BossFiende("Demonkonge", 100, 25, 30)
        ]

        self.gjeldende_fiende = 0

        # Spørsmål og riktige svar
        self.sporsmal = [
            ("Hva er 5 + 5?", "10"),
            ("Hva er hovedstaden i Norge?", "oslo"),
            ("Hvor mange dager er det i en uke?", "7"),
            ("Hva er 10 * 2?", "20"),
            ("Hva heter planeten vi bor på?", "jorden")
        ]

        self.gjeldende_sporsmal = 0
        self.svar = ""

    # Starter spillet
    def start(self):
        print("\nVelkommen til Quiz Battle!")
        print("Du skal kjempe mot fem fiender.")
        print("Svar riktig på spørsmålene for å angripe.")
        print("Hvis du svarer feil, angriper fienden deg.")

        # Fortsetter så lenge spilleren har helse og det finnes fiender
        while self.spiller.helse > 0 and self.gjeldende_fiende < len(self.fiender):

            fiende = self.fiender[self.gjeldende_fiende]

            print("\n--------------------------")
            print("Du møter:", fiende.navn)
            print("Din helse:", self.spiller.helse)
            print("Fiendens helse:", fiende.helse)

            self.still_sporsmal()

            if self.sjekk_svar():
                print("Riktig svar!")
                self.spiller.angrip(fiende)
            else:
                print("Feil svar!")

                # Sjekker om fienden er en boss
                if isinstance(fiende, BossFiende):
                    fiende.bruk_spesialangrep(self.spiller)
                else:
                    self.spiller.ta_skade(fiende.styrke)

            # Sjekker om fienden er beseiret
            if fiende.helse <= 0:
                print("\nDu beseiret", fiende.navn, "!")
                self.neste_fiende()

        # Sjekker hvordan spillet endte
        if self.spiller.helse <= 0:
            print("\nDu tapte! Spilleren er beseiret.")
        else:
            print("\nGratulerer! Du har beseiret alle fiendene!")
            print("Du har vunnet Quiz Battle!")


    # Viser spørsmål til spilleren
    def still_sporsmal(self):
        sporsmal = self.sporsmal[self.gjeldende_sporsmal]

        print("\nSpørsmål:", sporsmal[0])
        self.svar = input("Ditt svar: ").lower().strip()


    # Sjekker om svaret er riktig
    def sjekk_svar(self):
        riktig_svar = self.sporsmal[self.gjeldende_sporsmal][1]

        # Går videre til neste spørsmål
        self.gjeldende_sporsmal = self.gjeldende_sporsmal + 1

        # Starter på første spørsmål igjen hvis listen er brukt opp
        if self.gjeldende_sporsmal >= len(self.sporsmal):
            self.gjeldende_sporsmal = 0

        if self.svar == riktig_svar:
            return True
        else:
            return False


    # Går videre til neste fiende
    def neste_fiende(self):
        self.gjeldende_fiende = self.gjeldende_fiende + 1

        if self.gjeldende_fiende < len(self.fiender):
            print("\nNeste fiende:", self.fiender[self.gjeldende_fiende].navn)
        else:
            print("\nDu har beseiret alle fiendene!")


# Oppretter spillet og starter det
spill = Spill()
spill.start()
