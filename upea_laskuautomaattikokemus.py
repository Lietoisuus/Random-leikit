
# Alustetaan tarvittavat muuttujat
ensiluku = 0
numerot = []

# Määritellään yhteenlaskutoiminto, joka ottaa kuratoidun listan numeroita ja laskee ne yhteen
def add(numerolista):
    yhteensa = 0
    for n in numerolista:
        yhteensa += n
    return yhteensa

# Määritellään vähennystoiminto, joka ottaa lähtöluvun sekä kuratoidun listan numeroita, jonka miinustaa lähtöluvusta  
def subb(numero, numerolista):
    yhteensa = numero
    for n in numerolista:
        yhteensa -= n
    return yhteensa

# Määritellään tyyppitarkistus: jos syöte ei ole kokonaisluku, valitetaan käyttäjälle. Muussa tapauksessa lisätään se listaan kokonaislukuna.    
def onko_numero(ehdotettu):
    try:
        numerot.append(int(ehdotettu))
    except ValueError:
        print("Eikun numero")

# Tarkistetaan, vieläkö käyttäjä jatkaa numeroiden antamista. Jos ei, poistutaaa, ja jos joo, viedään syöte tarkistettavaksi.        
def numeroluettelo(ehdotus):
    while True:
        ehdotus = input()
        if ehdotus == "eh":
            break
        else:
            onko_numero(ehdotus)

# Upea tervetuloviesti luo käyttäjille kotoisan olon.
print("Tervetuloa Julian upeaan laskuautomaattikokemukseen! Toivottavasti viihdyt täällä.\n")

while True:
    numerot.clear()
    valinta = input("Haluatko plussata vai miinustaa? Sano 'plus' jos plussata, ja 'miinus' jos miinustaa. Jos haluat sulkea ohjelman, sano 'poies': ")
    if valinta == "poies":
        print("\nKiitos kun osallistuit Julian upeaan laskuautomaattikokemukseen! Muista kertoa tästä kaikille ystävillesi, jotta hekin pääsevät kokeilemaan.\nHeippa!")
        break
    while valinta not in ["plus", "miinus"]:
        print("Eikun sun pitää valita.")
        valinta = input()
        
    if valinta == "plus":
        
        print("\nSyötä numeroita. Kun kyllästyt, kirjoita 'eh' lopettaaksesi.")
        numeroluettelo(None)
    
        print("Yhteensä ne tekee ", add(numerot), "\n")
        
    if valinta == "miinus":
        ensiluku = int(input("\nAnna ensin jokin numero:  "))
        print("\nNyt voit syöttää muita numeroita, jotka miinustan tuosta ensimmäisestä. Sano 'eh' kun kyllästyt.")
        numeroluettelo(None)
        print("Kaikkien vähennysten jälkeen jäljelle jää ", subb(ensiluku, numerot), "\n")

    
