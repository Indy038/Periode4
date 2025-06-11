import pandas as pd
import matplotlib.pyplot as plt
from openpyxl import Workbook
from openpyxl.drawing.image import Image as XLImage
from io import BytesIO

# Data inlezen
branches = pd.read_csv("branches.csv")
bedrijven = pd.read_csv("bedrijven.csv")

branches.columns = branches.columns.str.strip()
bedrijven.columns = bedrijven.columns.str.strip()

# Vraag gebruiker om een grafiek te kiezen
print("Kies een grafiek:")
print("1: Aantal bedrijven per branche (staafdiagram)")
print("2: Top 5 bedrijven met hoogste winst uit een bepaalde stad (taartdiagram)")
keuze = input("Voer je keuze in (1 of 2): ")

# Excel voorbereiden
wb = Workbook()
ws = wb.active

def save_plot(fig, titel):
    img_data = BytesIO()
    plt.tight_layout()
    fig.savefig(img_data, format='png')
    img_data.seek(0)
    plt.close(fig)

    ws.title = titel[:30]
    img = XLImage(img_data)
    img.anchor = 'A1'
    ws.add_image(img)
    wb.save("grafieken_output.xlsx")
    print(f"✅ Grafiek '{titel}' opgeslagen in 'grafieken_output.xlsx'")

# Optie 1: Staafdiagram – aantal bedrijven per branche
if keuze == "1":
    bedrijf_tellingen = bedrijven.groupby('idbranche').size().reset_index(name='aantal')
    bedrijf_tellingen = bedrijf_tellingen.merge(branches, on='idbranche', how='left')

    fig, ax = plt.subplots()
    ax.bar(bedrijf_tellingen['omschrijving'], bedrijf_tellingen['aantal'], color='cornflowerblue')
    ax.set_title('Aantal bedrijven per branche')
    ax.set_xlabel('Branche')
    ax.set_ylabel('Aantal bedrijven')
    plt.xticks(rotation=45)

    save_plot(fig, "Aantal bedrijven per branche")

# Optie 2: Taartdiagram – top 5 winst in stad
elif keuze == "2":
    stad = input("Voer de naam van de stad in (zoals Amsterdam): ").strip()
    filtered = bedrijven[bedrijven['plaats'].str.lower() == stad.lower()]
    top5 = filtered.nlargest(5, 'winst')

    if top5.empty:
        print("⚠️ Geen gegevens gevonden voor die stad.")
    else:
        fig, ax = plt.subplots()
        ax.pie(top5['winst'], labels=top5['bedrijf'], autopct='%1.1f%%')
        ax.set_title(f"Top 5 winstgevende bedrijven in {stad}")
        save_plot(fig, f"Top 5 winst {stad}")

else:
    print("❌ Ongeldige keuze. Kies 1 of 2.")
