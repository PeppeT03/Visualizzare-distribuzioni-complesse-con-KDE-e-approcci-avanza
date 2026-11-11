# Importazione delle librerie
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Carichiamo il dataset Penguins
# Eliminiamo le righe contenenti valori mancanti
penguins = sns.load_dataset("penguins").dropna()

# Estraiamo la colonna della lunghezza del becco
# Convertendola in un array NumPy
data = np.array(penguins["bill_length_mm"])


# Creiamo la figura
plt.figure(figsize=(10, 5))

# ISTOGRAMMA
# bins=18: numero di intervalli
# stat="density": utilizza la scala della densità,
# così possiamo confrontarlo con le curve KDE
sns.histplot(
    data,
    bins=18,
    stat="density",
    label="Istogramma"
)

# KDE CON METODO DI SCOTT
# Calcola automaticamente il bandwidth con la regola di Scott
sns.kdeplot(
    data,
    bw_method="scott",
    label="Scott"
)

# KDE CON METODO DI SILVERMAN
# Utilizza una regola alternativa per calcolare il bandwidth
sns.kdeplot(
    data,
    bw_method="silverman",
    label="Silverman"
)

# KDE CON BANDWIDTH MANUALE
# Partiamo da Scott e dimezziamo il bandwidth
# La curva diventa più sensibile alle variazioni locali
sns.kdeplot(
    data,
    bw_method="scott",
    bw_adjust=0.5,
    label="Scott (0.5)"
)

# Personalizzazione del grafico
plt.title("Confronto KDE con diversi bandwidth")
plt.xlabel("Lunghezza del becco (mm)")
plt.ylabel("Densità")
plt.legend(title="Metodo")
plt.grid(axis="y", linestyle="--", alpha=0.4)

# Sistemiamo gli spazi e salviamo l'immagine
plt.tight_layout()
plt.savefig("esercizio1.png", dpi=300)
plt.show()