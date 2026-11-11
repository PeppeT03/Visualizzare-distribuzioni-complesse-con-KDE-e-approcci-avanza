# Importazione delle librerie
import seaborn as sns
import matplotlib.pyplot as plt

# Carichiamo il dataset Tips
# dropna() elimina eventuali righe con valori mancanti
tips = sns.load_dataset("tips").dropna()


# KDE CONFRONTANDO FUMATORI E NON FUMATORI

sns.kdeplot(
    data=tips,              # Dataset utilizzato
    x="total_bill",         # Variabile da analizzare: conto totale
    hue="smoker",           # Divide i dati tra fumatori e non fumatori
    common_norm=False,      # Normalizza separatamente ogni gruppo
    fill=True               # Riempie le aree sotto le curve
)

# Sistemiamo gli spazi del grafico
plt.tight_layout()

# Salviamo il grafico a 300 DPI
plt.savefig("esercizio3.png", dpi=300)

# Mostriamo il risultato
plt.show()