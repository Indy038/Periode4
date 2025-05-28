import pandas as pd
import matplotlib.pyplot as plt
import os
print("Bestanden in deze map:", os.listdir())

def laad_data():
    Branches = pd.read_csv('Branches.csv')
    Bedrijven = pd.read_csv('Bedrijven.csv')
    return Branches, Bedrijven

def bedrijven_per_branche(Branches, Bedrijven):
    counts = Bedrijven['branche_id'].value_counts().rename_axis('branche_id').reset_index(name='aantal_bedrijven')
    merged = counts.merge(Branches, left_on='branche_id', right_on='id')
    plt.figure(figsize=(10,6))
    plt.bar(merged['naam'], merged['aantal_bedrijven'])
    plt.xlabel('Branche')
    plt.ylabel('Aantal bedrijven')
    plt.title('Aantal bedrijven per branche')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

def top5_omzet(Bedrijven):
    top5 = Bedrijven.nlargest(5, 'omzet')
    plt.pie(top5['omzet'], labels=top5['naam'], autopct='%1.1f%%')
    plt.title('Top 5 bedrijven met hoogste omzet')
    plt.show()

def top5_winst_stad(Bedrijven):
    stad = input("Uit welke stad wil je de top 5 bedrijven met hoogste winst zien? ")
    bedrijven_stad = Bedrijven[Bedrijven['plaats'].str.lower() == stad.lower()]
    top5 = bedrijven_stad.nlargest(5, 'winst')
    plt.pie(top5['winst'], labels=top5['naam'], autopct='%1.1f%%')
    plt.title(f'Top 5 winst in {stad}')
    plt.show()

def winst_lijn_bedrijf(Bedrijven):
    bedrijf = input("Van welk bedrijf wil je de winstontwikkeling zien? ")
    data = Bedrijven[Bedrijven['naam'].str.lower() == bedrijf.lower()]
    if data.empty:
        print("Bedrijf niet gevonden.")
        return
    data = data.sort_values('jaar')
    plt.plot(data['jaar'], data['winst'], marker='o')
    plt.title(f'Winstontwikkeling {bedrijf}')
    plt.xlabel('Jaar')
    plt.ylabel('Winst')
    plt.show()

def top5_omzet_vs_rest(bedrijven):
    top5 = bedrijven.nlargest(5, 'omzet')
    rest = bedrijven[~bedrijven['id'].isin(top5['id'])]
    waarden = list(top5['omzet']) + [rest['omzet'].sum()]
    labels = list(top5['naam']) + ['Rest']
    plt.pie(waarden, labels=labels, autopct='%1.1f%%')
    plt.title('Top 5 omzet t.o.v. rest')
    plt.show()

def top10_branches_omzet_jaar(branches, bedrijven):
    jaar = int(input("Voor welk jaar wil je de top 10 branches met hoogste omzet zien? "))
    data = bedrijven[bedrijven['jaar'] == jaar]
    omzet_per_branche = data.groupby('branche_id')['omzet'].sum().reset_index()
    top10 = omzet_per_branche.nlargest(10, 'omzet').merge(branches, left_on='branche_id', right_on='id')
    plt.pie(top10['omzet'], labels=top10['naam'], autopct='%1.1f%%')
    plt.title(f'Top 10 branches hoogste omzet in {jaar}')
    plt.show()

def top10_branches_gem_winst(branches, bedrijven):
    laatste_jaar = bedrijven['jaar'].max()
    data = bedrijven[bedrijven['jaar'] >= laatste_jaar - 4]
    gem_winst = data.groupby('branche_id')['winst'].mean().reset_index()
    top10 = gem_winst.nlargest(10, 'winst').merge(branches, left_on='branche_id', right_on='id')
    plt.pie(top10['winst'], labels=top10['naam'], autopct='%1.1f%%')
    plt.title('Top 10 branches hoogste gemiddelde winst (laatste 5 jaar)')
    plt.show()

def main():
    branches, bedrijven = laad_data()
    while True:
        print("\nKies een grafiek:")
        print("1. Staafdiagram: aantal bedrijven per branche")
        print("2. Taartgrafiek: top 5 bedrijven hoogste omzet")
        print("3. Taartgrafiek: top 5 bedrijven hoogste winst uit een stad")
        print("4. Lijngrafiek: winstontwikkeling bedrijf")
        print("5. Taartgrafiek: top 5 omzet bedrijven vs rest")
        print("6. Taartgrafiek: top 10 branches hoogste omzet in een jaar")
        print("7. Taartgrafiek: top 10 branches hoogste gemiddelde winst laatste 5 jaar")
        print("0. Stoppen")
        keuze = input("Maak een keuze: ")
        if keuze == "1":
            bedrijven_per_branche(branches, bedrijven)
        elif keuze == "2":
            top5_omzet(bedrijven)
        elif keuze == "3":
            top5_winst_stad(bedrijven)
        elif keuze == "4":
            winst_lijn_bedrijf(bedrijven)
        elif keuze == "5":
            top5_omzet_vs_rest(bedrijven)
        elif keuze == "6":
            top10_branches_omzet_jaar(branches, bedrijven)
        elif keuze == "7":
            top10_branches_gem_winst(branches, bedrijven)
        elif keuze == "0":
            break
        else:
            print("Ongeldige keuze.")

if __name__ == "__main__":
    main()