import pandas as pd
import matplotlib.pyplot as plt
import xlsxwriter
import os

print("✅ Je draait nu het juiste script vanuit:", __file__)


# Inlezen van data
bedrijven = pd.read_csv("Bedrijven.csv")
branches = pd.read_csv("Branches.csv")
financieel = pd.read_csv("Financieel.csv")

# Merge tabellen
bedrijven = bedrijven.merge(branches, on="idbranche", how="left")
data = financieel.merge(bedrijven, on="idbedrijf", how="left")

# Zorg dat output-map bestaat
os.makedirs("output", exist_ok=True)

def save_plot(fig, naam):
    pad = f"output/{naam}.png"
    fig.savefig(pad)
    return pad

def export_excel(afbeeldingen):
    workbook = xlsxwriter.Workbook("output/grafieken.xlsx")
    worksheet = workbook.add_worksheet()
    for i, afbeelding in enumerate(afbeeldingen):
        worksheet.insert_image(f"A{(i * 20) + 1}", afbeelding)
    workbook.close()

grafieken = []

# 1. Staafdiagram: bedrijven per branche
fig1 = plt.figure()
data.groupby('omschrijving')['idbedrijf'].nunique().plot(kind='bar', title="Bedrijven per Branche")
grafieken.append(save_plot(fig1, "bedrijven_per_branche"))

# 2. Taartgrafiek: top 5 bedrijven hoogste omzet
fig2 = plt.figure()
top5 = data.groupby("naam")["omzet"].sum().nlargest(5)
top5.plot(kind="pie", autopct="%1.1f%%", title="Top 5 Bedrijven Op Omzet")
grafieken.append(save_plot(fig2, "top5_omzet"))

# 3. Taartgrafiek: top 5 winst uit bepaalde stad
stad = input("Voer een stad in voor winst-analyse (bijv. Amsterdam): ")
filtered = data[data['plaats'].str.lower() == stad.lower()]
fig3 = plt.figure()
top_winst_stad = filtered.groupby('naam')['winst'].sum().nlargest(5)
top_winst_stad.plot(kind='pie', autopct='%1.1f%%', title=f"Top 5 Winst in {stad}")
grafieken.append(save_plot(fig3, "top5_winst_stad"))

# 4. Lijngrafiek: winst over tijd voor bedrijf
bedrijf = input("Voer de naam van een bedrijf in (bijv. Coolblue): ")
bedrijf_data = data[data['naam'].str.lower() == bedrijf.lower()]
fig4 = plt.figure()
bedrijf_data.groupby('jaar')['winst'].sum().plot(kind='line', marker='o', title=f"Winst per Jaar - {bedrijf}")
grafieken.append(save_plot(fig4, "winst_per_jaar_bedrijf"))

# 5. Top 5 bedrijven omzet vs rest
fig5 = plt.figure()
total_omzet = data.groupby('naam')['omzet'].sum()
top5 = total_omzet.nlargest(5)
rest = total_omzet.sum() - top5.sum()
top5["Overige"] = rest
top5.plot(kind='pie', autopct='%1.1f%%', title="Top 5 Omzet vs Overige")
grafieken.append(save_plot(fig5, "top5_vs_rest"))

# 6. Top 10 branches met hoogste omzet in een bepaald jaar
jaar = int(input("Voer een jaar in (bijv. 2022): "))
filtered_year = data[data['jaar'] == jaar]
fig6 = plt.figure()
top10_omzet = filtered_year.groupby('omschrijving')['omzet'].sum().nlargest(10)
top10_omzet.plot(kind='pie', autopct='%1.1f%%', title=f"Top 10 Branches Omzet ({jaar})")
grafieken.append(save_plot(fig6, "top10_branche_omzet_jaar"))

# 7. Top 10 branches gemiddelde winst over laatste 5 jaar
max_jaar = data['jaar'].max()
recent_data = data[data['jaar'] >= max_jaar - 4]
fig7 = plt.figure()
top10_winst = recent_data.groupby('omschrijving')['winst'].mean().nlargest(10)
top10_winst.plot(kind='pie', autopct='%1.1f%%', title="Top 10 Branches Gemiddelde Winst (Laatste 5 Jaar)")
grafieken.append(save_plot(fig7, "top10_branche_winst_5jr"))

# Exporteer alle grafieken naar Excel
export_excel(grafieken)

print("✅ Alle grafieken zijn gegenereerd en opgeslagen in 'output/grafieken.xlsx'")
