def vraag_naam():
    naam = input("Wat is je naam? ")
    return naam

def vraag_leeftijd():
    leeftijd = int(input("Hoe oud ben je? "))
    return leeftijd

def bereken_jaar_100(leeftijd):
    huidig_jaar = 2025
    jaren_tot_100 = 100 - leeftijd
    jaar_100 = huidig_jaar + jaren_tot_100
    return jaar_100

def main():
    naam = vraag_naam()
    leeftijd = vraag_leeftijd()
    jaar_100 = bereken_jaar_100(leeftijd)
    print(f"{naam}, jij wordt 100 jaar in het jaar {jaar_100}.")

if __name__ == "__main__":
    main()