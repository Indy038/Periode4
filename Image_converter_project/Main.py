from PIL import Image
import os

def is_image(file):
    """Check of bestand een afbeelding is op basis van extensie."""
    image_extensions = ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff']
    return any(file.lower().endswith(ext) for ext in image_extensions)

def resize_image(image_path, output_path, max_size):
    """Verklein de afbeelding als hij groter is dan max_size."""
    with Image.open(image_path) as img:
        img.thumbnail((max_size, max_size))
        img.save(output_path)
        print(f"Aangepast: {os.path.basename(image_path)}")

def main():
    # Input van gebruiker
    source_folder = input("Voer het pad in naar de bronmap met afbeeldingen: ")
    destination_folder = input("Voer het pad in naar de uitvoermap: ")
    max_size = int(input("Voer de maximale grootte in (max 2000 pixels): "))

    if max_size > 2000:
        print("Maximale grootte mag niet meer dan 2000 pixels zijn.")
        return

    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)

    # Lees bestanden
    files = os.listdir(source_folder)
    print(f"Totaal gevonden bestanden in bronmap: {len(files)}")

    for file in files:
        source_path = os.path.join(source_folder, file)
        dest_path = os.path.join(destination_folder, file)

        if os.path.isfile(source_path):
            if is_image(file):
                try:
                    resize_image(source_path, dest_path, max_size)
                except Exception as e:
                    print(f"FOUT bij verwerken van {file}: {e}")
            else:
                print(f"Overgeslagen (geen afbeelding): {file}")

if __name__ == "__main__":
    main()