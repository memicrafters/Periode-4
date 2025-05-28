import os
from deep_translator import GoogleTranslator
import pyttsx3
import tkinter as tk
from tkinter import simpledialog, messagebox

# Vaste mappen (relatief aan dit script)
source_map = "Teksten"
target_map = "Vertaalde teksten"

def vertaal_bestanden(src_map, dst_map, src_lang='en', tgt_lang='nl'):
    if not os.path.exists(dst_map):
        os.makedirs(dst_map)

    for bestandsnaam in os.listdir(src_map):
        pad = os.path.join(src_map, bestandsnaam)
        if os.path.isfile(pad):
            print(f"Vertalen: {bestandsnaam}")
            with open(pad, 'r', encoding='utf-8') as f:
                inhoud = f.read()

            chunks = [inhoud[i:i+4000] for i in range(0, len(inhoud), 4000)]
            vertaalde_tekst = ''
            for chunk in chunks:
                try:
                    vertaalde_tekst += GoogleTranslator(source=src_lang, target=tgt_lang).translate(chunk) + '\n'
                except Exception as e:
                    print(f"Fout bij vertalen: {e}")
                    vertaalde_tekst += "[VERTAALFOUT]\n"

            output_pad = os.path.join(dst_map, bestandsnaam + ".txt")  # Voeg .txt toe aan output
            with open(output_pad, 'w', encoding='utf-8') as f:
                f.write(vertaalde_tekst)
            print(f"Opgeslagen in: {output_pad}")

def voorlees_bestand(bestandspad):
    with open(bestandspad, 'r', encoding='utf-8') as f:
        tekst = f.read()

    engine = pyttsx3.init()
    engine.say(tekst)
    engine.runAndWait()

def main():
    vertaal_bestanden(source_map, target_map)

    root = tk.Tk()
    root.withdraw()

    bestanden = [f for f in os.listdir(target_map) if os.path.isfile(os.path.join(target_map, f))]
    if not bestanden:
        messagebox.showinfo("Geen bestanden", "Geen vertaalde bestanden gevonden.")
        return

    gekozen_bestand = simpledialog.askstring("Bestand kiezen", f"Kies een van de volgende bestanden:\n\n" + "\n".join(bestanden))
    if gekozen_bestand and gekozen_bestand in bestanden:
        voorlees_bestand(os.path.join(target_map, gekozen_bestand))
    else:
        messagebox.showinfo("Ongeldige keuze", "Geen geldig bestand gekozen.")

if __name__ == "__main__":
    main()