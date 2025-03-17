import pymysql
import pandas as pd
import re

# Connexion à la base de données
try:
    conn = pymysql.connect(
        host="localhost",
        user="root",
        password="",
        database="ecommerce_scraping"
    )
    cursor = conn.cursor()
    print("Connexion à la base de données réussie !")
except pymysql.MySQLError as err:
    print(f"Erreur de connexion à la base de donnée: {err}")

# Récupération des données sous forme de DataFrame
df = pd.read_sql("SELECT * FROM produits", conn)

# Suppression des doublons
# df.drop_duplicates(inplace=True)

# Suppression des valeurs manquantes
df.dropna(inplace=True)

# Nettoyage des noms de produits (suppression des espaces superflus)
df["nom"] = df["nom"].str.strip()

# Normalisation de la casse des catégories
df["categorie"] = df["categorie"].str.lower()


# Nettoyage et conversion des avis en float
def nettoyer_avis(avis):
    try:
        avis = str(avis).replace(",", ".")  # Remplacer la virgule par un point si nécessaire
        avis_float = float(avis)
        if 0 <= avis_float <= 5:  # S'assurer que l'avis est entre 0 et 5
            return avis_float
        else:
            return None  # Mettre à None si la valeur est aberrante
    except ValueError:
        return None  # Si conversion échoue


df["avis"] = df["avis"].apply(nettoyer_avis)


# Fonction pour valider et nettoyer les liens URL
def nettoyer_lien(url):
    if isinstance(url, str) and re.match(r"^https?://", url):
        return url.strip()
    return None  # Remplace les liens invalides par None


df["lien"] = df["lien"].apply(nettoyer_lien)


# Fonction pour définir la gamme de prix
def definir_gamme(prix):
    if prix < 30:
        return "Bas"
    elif prix < 40:
        return "Moyen"
    else:
        return "Haut"


# Ajout d'une colonne Prix TTC avec TVA de 20%
df["Prix_TTC"] = df["prix"] * 1.20

# Ajout de la gamme de prix
df["Gamme_Prix"] = df["prix"].apply(definir_gamme)

# Vérification des types de données
print(df.dtypes)

# Sauvegarde en CSV
df.to_csv("produits.csv", index=False, encoding="ISO-8859-1")
print("Fichier CSV généré avec succès !")

# Affichage des premières lignes du DataFrame
pd.set_option("display.max_columns", None)
pd.set_option("display.width", 1000)
print(df.head())
