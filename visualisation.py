import pymysql
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

try:
    conn = pymysql.connect(
        host="localhost",
        user="root",
        password="",
        database="ecommerce_scraping"
    )

    cursor = conn.cursor()  # Création de mon curseur

    print("Connexion à la base de donnée réussie !")
except pymysql.MySQLError as err:
    print(f"Erreur de connexion à la base de donnée: {err}")

# recupération des données enregistrer dans un dataframe
df = pd.read_sql("SELECT * FROM produits", conn)


# print(df.dtypes)  # vérification des types de mes donnés apres recupération

# ----------------PERTINENCE-------------------------


def definir_gamme(prix):
    if prix < 30:
        return "Bas"
    elif prix < 40:
        return "Moyen"
    else:
        return "Haut"


df["Prix_TTC"] = df["prix"] * 1.20  # Ajoute 20% de TVA
df["Gamme_Prix"] = df["prix"].apply(definir_gamme)
# df["Popularité"] = df["Avis"].apply(lambda x: "Faible" if x <= 2 else ("Moyenne" if x == 3 else "Élevée"))
df["Taux_TVA"] = df["Prix_TTC"] - df["prix"]

df["Range_Prix"] = pd.cut(df["prix"], bins=[0, 30, 50, float("inf")], labels=["Faible", "Moyen", "Élevé"])

# ----------------- AFFICHAGE DU DATAFRAME ------------------------
pd.set_option("display.max_columns", None)  # Affiche toutes les colonnes
pd.set_option("display.width", 1000)  # Ajuste la largeur pour éviter les coupures (mettre sur une ligne)

print(df.head())  # Afficher les 5 premières lignes
# -----------------------------------------

print(df.dtypes)  # vérification des types de mes donnés apres recupération

# Histogramme : répartition des prix par produit
plt.figure(figsize=(8, 5))
df["prix"].hist(bins=10, edgecolor="black", color="skyblue")
plt.xlabel("Prix (€)")
plt.ylabel("Nombre de produits")
plt.title("Répartition des prix des produits")
plt.show()

# Nombre de produit par catégorie
# Récupérer d'autres catégorie ici et le diagramme sera beaucoup plus beau à voir et à analyser

df["categorie"].value_counts().plot(kind="bar", color="orange", figsize=(8, 5))
plt.xlabel("Catégorie")
plt.ylabel("Nombre de produits")
plt.title("Nombre de produits par catégorie")
plt.xticks(rotation=45)
plt.show()

# Répartition des gammes de prix

df["Gamme_Prix"].value_counts().plot(kind="pie", autopct="%1.1f%%", figsize=(6, 6), colors=["gold", "lightblue", "red"])
plt.title("Répartition des produits par gamme de prix")
plt.show()

# Nuage de points : Prix vs Avis

plt.figure(figsize=(8, 5))
plt.scatter(df["prix"], df["avis"], color="green", alpha=0.5)
plt.xlabel("Prix (€)")
plt.ylabel("Avis (1 à 5 étoiles)")
plt.title("Relation entre le prix et l'avis")
plt.show()

# Top 10 des produits les plus cher

df_top = df.sort_values(by="prix", ascending=False).head(10)

plt.figure(figsize=(8, 5))
plt.barh(df_top["nom"], df_top["prix"], color="purple")
plt.xlabel("Prix (€)")
plt.ylabel("Nom du produit")
plt.title("Top 10 des produits les plus chers")
plt.gca().invert_yaxis()  # Inverser l'ordre des produits
plt.show()

# Taux de TVA par gamme de prix
plt.figure(figsize=(8, 5))
sns.boxplot(x="Range_Prix", y="Taux_TVA", data=df, palette="Set3")
plt.title("Répartition du Taux de TVA par gamme de prix")
plt.xlabel("Gamme de Prix")
plt.ylabel("Taux de TVA (€)")
plt.show()

# repartition par gamme
plt.figure(figsize=(6, 5))
sns.countplot(x="Range_Prix", data=df, hue="Range_Prix", palette="muted", legend=False)
plt.title("Répartition des produits selon la gamme de prix")
plt.xlabel("Gamme de Prix")
plt.ylabel("Nombre de produits")
plt.show()