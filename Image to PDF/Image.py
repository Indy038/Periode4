from PIL import Image
import os

def afbeeldingen_naar_pdf(map_pad, uitvoer_pdf):
    # Zoek alle afbeeldingsbestanden in de map
    extensies = ('.png', '.jpg', '.jpeg', '.bmp', '.gif')
    bestanden = [f for f in os.listdir(map_pad) if f.lower().endswith(extensies)]
    bestanden.sort()  # Sorteer voor consistente volgorde

    if not bestanden:
        print("Geen afbeeldingen gevonden in de map.")
        return

    afbeeldingen = []
    for bestand in bestanden:
        pad = os.path.join(map_pad, bestand)
        img = Image.open(pad).convert('RGB')
        afbeeldingen.append(img)

    eerste_afbeelding = afbeeldingen[0]
    overige_afbeeldingen = afbeeldingen[1:]

    eerste_afbeelding.save(
        uitvoer_pdf,
        save_all=True,
        append_images=overige_afbeeldingen
    )
    print(f"PDF opgeslagen als: {uitvoer_pdf}")

if __name__ == "__main__":
    map_pad = input("Geef het pad naar de map met afbeeldingen: ")
    uitvoer_pdf = input("Geef de naam van het uitvoer PDF-bestand (bijv. output.pdf): ")
    afbeeldingen_naar_pdf(map_pad, uitvoer_pdf)