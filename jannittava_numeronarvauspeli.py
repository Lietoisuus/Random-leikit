# Pelin nimi on arvaa numero!

# Tarttee generoida random numero, haetaan randomointikamat
from random import *

# Alustetaan arvattava numero ja arvauslaskuri
numero = randint(-100, 100)
arvauslaskuri = 0
uudestaan = "joo!"

# Määritellään voittovunktio
def voitit():
    global uudestaan
    global arvauslaskuri
    global numero
    print("Onneksi olkoon, oikein arvattu! Voitit pelin ", arvauslaskuri, " arvauksella!\n")
    with open("tulokset.txt", "a") as f:
        f.write("\n" + str(arvauslaskuri) + " " + input("Jätä alle nimesi, niin tallennan sen tulostaulukkoon: "))
    arvauslaskuri = 0
    numero = randint(-100, 100)
    
    katso = input("\nJos haluat nähdä sijoituksesi, sano 'saisinko nähdä tulostaulukon, kiitos!': ")
    if katso == "saisinko nähdä tulostaulukon, kiitos!":
        tulokset()
    
    uudestaan = input("	\nHaluatko pelata uudestaan? Sano 'nääh' tai 'joo!': ")
    while uudestaan not in ["nääh", "joo!"]:
        print("...valitse nyt vaan ei se oo niin vaikeeta.\n")
        uudestaan = input()
        
def tulokset():
    print("Tulostaulukko:\n")
    with open("tulokset.txt") as f:
        rivit = f.readlines()
        tulokset = []

        for rivi in rivit:
            osat = rivi.strip().split(maxsplit=1)
            pisteet = int(osat[0])
            nimi = osat[1]
            tulokset.append((pisteet, nimi))
            tulokset.sort()
        for pisteet, nimi in tulokset:
            print(pisteet, nimi)
    
# Numeronarvauksen tarkistus ja epäonnistumisesta vittuilu   
def arvataan_numero():
    global arvauslaskuri
    while True:
        try:
            arvaus = int(input("\nArvaa jokin numero: "))
            arvauslaskuri += 1
            return arvaus    
        except ValueError:
            print("Kirjota vaan se numero. ")
    
   
# Määritellään helppo peli 
def helppo():
    while True:
        arvaus = arvataan_numero()
        if arvaus == numero:
            voitit()
            break
        elif arvaus > numero:
            print("Liian iso!")
        elif arvaus < numero:
            print("Liian pieni!")
 
# Määritellään vaikea peli            
def vaikea():
    while True:
        arvaus = arvataan_numero()
        if arvaus == numero:
            voitit()
            break
        else:
            print("Arvaa uudestaan. :)") 
    
# Tervetuloviesti
print("\nTervetuloa Julian Jännittävään Numeronarvauspeliin! Peli toimii siten, että tämä ohjelma miettii jotain numeroa, ja sun tehtävä on arvata se mahdollisimman nopeasti.\n")


# Pelataan niin monta kertaa kuin pelaaja haluaa
while uudestaan == "joo!":

    print("\nEnsin voisit valita vaikeustason. Jos haluat helpon pelin, kirjoita 'helppo', ja jos taas haluat vaikean pelin, kirjoita 'vaikea': \n")

# Otetaan syötteenä toivottu vaikeustaso ja valitetaan jos se ei ole valinnoissa
    vaikeustaso = input()

    while vaikeustaso not in ["helppo", "vaikea"]:
        print("\nSori, tässä on vain kaksi vaikeustasoa. Valitse jompi kumpi. ")
        vaikeustaso = input()
    
    if vaikeustaso == "helppo":
        helppo()
    
    if vaikeustaso == "vaikea":
        vaikea()

# Lopetusviesti
print("\nKiitos kun pelasit Julian Jännittävää Numeronarvauspeliä! Haasta ensi kerralla myös kaverisi tiukkaan ja hulvattomaan numeronarvailukisaan!")

    
