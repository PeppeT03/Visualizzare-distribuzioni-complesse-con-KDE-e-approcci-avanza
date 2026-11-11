# Importiamo le librerie
import seaborn as sns
import matplotlib.pyplot as plt

# Carichiamo il dataset Iris
# dropna() elimina eventuali righe con valori mancanti
iris = sns.load_dataset("iris").dropna()

# Selezioniamo due colonne numeriche:
# lunghezza e larghezza del sepalo
X = iris[["sepal_length", "sepal_width"]].values


# COSTRUZIONE DELLA KDE BIDIMENSIONALE

sns.kdeplot(
    data=iris,                   # DataFrame di partenza
    x="sepal_length",            # Variabile sull'asse X
    y="sepal_width",             # Variabile sull'asse Y
    fill=True,                   # Riempie le aree della densità
    cmap="mako",                 # Sceglie la scala di colori
    thresh=0.05,                 # Soglia minima di densità visualizzata
    levels=8                     # Numero di livelli di densità
)


# AGGIUNGIAMO I PUNTI REALI

plt.scatter(
    X[::5, 0],                   # Prende un punto ogni 5 dalla prima colonna
    X[::5, 1],                   # Prende gli stessi punti dalla seconda colonna
    s=20,                        # Dimensione dei punti
    color="white",               # Colore interno
    edgecolor="black",           # Bordo nero
    alpha=0.7,                   # Trasparenza
    label="Osservazioni"         # Nome nella legenda
)

# Personalizzazione del grafico
plt.title("KDE bidimensionale – Iris")
plt.xlabel("Lunghezza del sepalo (cm)")
plt.ylabel("Larghezza del sepalo (cm)")
plt.legend()

# Sistemiamo gli spazi e salviamo l'immagine
plt.tight_layout()
plt.savefig("esercizio2.png", dpi=300)
plt.show()