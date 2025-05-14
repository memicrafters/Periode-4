import os


def main():
    mapnaam = input("Geef de naam van de map met afbeeldingen: ")

    # Controleer of de map bestaat
    if not os.path.isdir(mapnaam):
        print(f"De map '{mapnaam}' bestaat niet.")
        return

    # Haal een lijst op van alleen bestanden (geen mappen)
    bestanden = [f for f in os.listdir(mapnaam) if os.path.isfile(os.path.join(mapnaam, f))]
    bestanden.sort()  # Optioneel: gesorteerd verwerken

    nieuwe_namen = []

    # Hernoem elk bestand
    for i, oudenaam in enumerate(bestanden, start=1):
        _, extensie = os.path.splitext(oudenaam)
        nieuwenaam = f"movie_poster_{i:02}{extensie}"

        oudpad = os.path.join(mapnaam, oudenaam)
        nieuwpad = os.path.join(mapnaam, nieuwenaam)

        os.rename(oudpad, nieuwpad)
        nieuwe_namen.append(nieuwenaam)

    # Schrijf de nieuwe bestandsnamen naar bestanden.txt
    with open("bestanden2.txt", "w", encoding="utf-8") as f:
        for naam in nieuwe_namen:
            f.write(naam + "\n")

    print("Alle bestanden zijn hernoemd en opgeslagen in 'bestanden2.txt'.")


if __name__ == "__main__":
    main()
