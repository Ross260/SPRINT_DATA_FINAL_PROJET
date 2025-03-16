import requests
from bs4 import BeautifulSoup
import re
import pymysql

try:
    conn = pymysql.connect(
        host="localhost",
        user="root",
        password="",
        database="ecommerce_scraping"
    )
    print("Connexion à la base de donnée réussie !")
    conn.close()
except pymysql.MySQLError as err:
    print(f"Erreur de connexion à la base de donnée: {err}")

url = "https://books.toscrape.com/catalogue/category/books/mystery_3/index.html"
urlc = "https://books.toscrape.com/catalogue/category/books/mystery_3/"
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                         "Chrome/110.0.5481.104 Safari/537.36"}

response = requests.get(url)  # Envoie une requête GET

# Vérifier si la requête est réussie
if response.status_code == 200:
    print("Requête réussie ! Information du site " + url + " récuperer avec succès ")
    html_content = response.text  # Contenu HTML de la page

    # On crée un objet BeautifulSoup pour analyser le HTML
    soup = BeautifulSoup(response.text, "html.parser")

    # print(soup.prettify()) # affichage des informations de la page mais de manière formaté

    titles = soup.find_all('h3')
    prices = soup.find_all('p', class_='price_color')
    categories = soup.find('h1')
    rating_elements = soup.find_all("p", class_="star-rating")
    h3_tags = soup.find_all("h3")  # Trouve toutes les balises <h3> qui contiennent les balises <a>

    # Affichage du html de manière plus lisible
    print(soup.title.string)

    # Dictionnaire pour convertir les nombres en texte vers des chiffres
    stars_mapping = {
        "One": 1,
        "Two": 2,
        "Three": 3,
        "Four": 4,
        "Five": 5
    }

    # Les noms de produits
    for i, (title, price, rating_element, h3) in enumerate(zip(titles, prices, rating_elements,h3_tags)):
        if i >= 5:  # après 5 itérations j'arrête
            break

        price_text = price.get_text(strip=True)  # Pour nettoyer les espaces inutiles
        clean_price = re.sub(r"[^\d.,]", "",
                             price_text)  # supprésion de tous les caractères sauf chiffres, points et virgules

        # les avis clients
        if rating_element:
            # Extraire la classe exacte (ex: "star-rating Four")
            class_list = rating_element.get("class")  # Liste des classes CSS

            # Vérifier quelle valeur correspond à une étoile
            rating_value = next((stars_mapping[cls] for cls in class_list if cls in stars_mapping), None)

            if rating_value:
                print(f"⭐ Avis client : {rating_value} étoiles")
            else:
                print("❌ Impossible de détecter le nombre d'étoiles.")
                rating_value = 0
        else:
            print("❌ Avis non trouvé.")

        # lien des articles
        link = h3.find("a")  # Trouve un <a> à l'intérieur de <h3>
        if link and link.has_attr("href"):
            print("Lien trouvé :")  # Afficher seulement les liens dans <h3>
            url_produit = urlc + link["href"]
        else:
            print("❌ Aucun lien dans ce <h3>.")

        print(title.string + ", [Prix] : " + clean_price + ", [Catégories] : " + categories.string + ", [Avis] : " + str(rating_value) + ", [Lien] :" + url_produit)

    # Les catégories
    """
  for category in categories:
        print(category.string)  # une seule catégorie par page

    # Dictionnaire pour convertir les nombres en texte vers des chiffres
    stars_mapping = {
        "One": 1,
        "Two": 2,
        "Three": 3,
        "Four": 4,
        "Five": 5
    }

    # Trouver l'élément qui contient la classe des étoiles
    for rating_element in rating_elements:
        if rating_element:
            # Extraire la classe exacte (ex: "star-rating Four")
            class_list = rating_element.get("class")  # Liste des classes CSS

            # Vérifier quelle valeur correspond à une étoile
            rating_value = next((stars_mapping[cls] for cls in class_list if cls in stars_mapping), None)

            if rating_value:
                print(f"⭐ Avis client : {rating_value} étoiles")
            else:
                print("❌ Impossible de détecter le nombre d'étoiles.")
        else:
            print("❌ Avis non trouvé.")

    # Récupérer tous les liens qui sont dans des <h3>
    # Lien du produit == lien de la catégorie + lien produit
    h3_tags = soup.find_all("h3")  # Trouve toutes les balises <h3>

    for h3 in h3_tags:
        link = h3.find("a")  # Trouve un <a> à l'intérieur de <h3>
        if link and link.has_attr("href"):
            print("Lien trouvé :", urlc + link["href"])  # Afficher seulement les liens dans <h3>
        else:
            print("❌ Aucun lien dans ce <h3>.")"""
else:
    print(f"Erreur {response.status_code}")
