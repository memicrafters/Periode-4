import os

def main():
    # Vraag om de mapnaam
    mapnaam = input("Geef de naam van de map met afbeeldingen: ")

    # Controleer of de map bestaat
    if not os.path.isdir(mapnaam):
        print(f"De map '{mapnaam}' bestaat niet.")
        return

    # Haal de bestandsnamen op
    bestandsnamen = os.listdir(mapnaam)

    # Filter alleen echte bestanden (geen submappen)
    bestandsnamen = [f for f in bestandsnamen if os.path.isfile(os.path.join(mapnaam, f))]

    # Schrijf de bestandsnamen naar een tekstbestand
    with open("bestanden.txt", "w", encoding="utf-8") as f:
        for naam in bestandsnamen:
            f.write(naam + "\n")

    print("De bestandsnamen zijn opgeslagen in 'bestanden.txt'.")

if __name__ == "__main__":
    main()