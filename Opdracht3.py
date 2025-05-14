import os

def hernoem_en_nummer(mapnaam):
    bestanden = [f for f in os.listdir(mapnaam) if os.path.isfile(os.path.join(mapnaam, f))]
    bestanden.sort()

    nieuwe_namen = []
    with open("bestanden.txt", "w", encoding="utf-8") as f:
        for i, oudenaam in enumerate(bestanden, start=1):
            _, ext = os.path.splitext(oudenaam)
            nieuwenaam = f"movie_poster_{i:02}{ext}"
            os.rename(os.path.join(mapnaam, oudenaam), os.path.join(mapnaam, nieuwenaam))
            nieuwe_namen.append(nieuwenaam)
            f.write(oudenaam + "\n")

    with open("bestanden2.txt", "w", encoding="utf-8") as f:
        for naam in nieuwe_namen:
            f.write(naam + "\n")

    print("Bestanden zijn hernoemd en namen zijn opgeslagen in bestanden.txt en bestanden2.txt.")

def herstel_bestanden(mapnaam):
    try:
        with open("bestanden.txt", "r", encoding="utf-8") as f1, open("bestanden2.txt", "r", encoding="utf-8") as f2:
            originele_namen = [regel.strip() for regel in f1.readlines()]
            hernoemde_namen = [regel.strip() for regel in f2.readlines()]

        if len(originele_namen) != len(hernoemde_namen):
            print("Aantal regels in bestanden.txt en bestanden2.txt komt niet overeen.")
            return

        for oud, nieuw in zip(originele_namen, hernoemde_namen):
            oudpad = os.path.join(mapnaam, nieuw)
            nieuwpad = os.path.join(mapnaam, oud)
            if os.path.exists(oudpad):
                os.rename(oudpad, nieuwpad)

        print("Bestanden succesvol hernoemd naar hun originele naam.")
    except FileNotFoundError:
        print("Zorg ervoor dat zowel bestanden.txt als bestanden2.txt aanwezig zijn.")

def main():
    print("1. Hernoem en nummer bestanden")
    print("2. Hernoem bestanden naar originele naam")
    keuze = input("Keuze? ")

    mapnaam = input("Geef de naam van de map met afbeeldingen: ").strip()

    if not os.path.isdir(mapnaam):
        print(f"De map '{mapnaam}' bestaat niet.")
        return

    if keuze == "1":
        hernoem_en_nummer(mapnaam)
    elif keuze == "2":
        herstel_bestanden(mapnaam)
    else:
        print("Ongeldige keuze.")

if __name__ == "__main__":
    main()