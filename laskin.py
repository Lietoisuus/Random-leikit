def add(numerolista):
    yhteensa = 0
    for n in numerolista:
        yhteensa += n
    return yhteensa

numerot =[]

print("Syötä numeroita. Kun kyllästyt, kirjoita 'eh' lopettaaksesi.")

while True:
    ehdotus = input()
    if ehdotus == "eh":
        break
    else:
        try:
            lisaa = int(ehdotus)
            numerot.append(lisaa)

        except ValueError:
            print("Eikun numero")

print("Yhteensä ne tekee ", add(numerot))