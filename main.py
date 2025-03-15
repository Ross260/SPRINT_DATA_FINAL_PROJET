import requests
from bs4 import BeautifulSoup
import re

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
    categories = soup.find_all('h1')
    rating_elements = soup.find_all("p", class_="star-rating")
    liens = soup.find_all('span', class_='a-price-fraction')

    # Affichage du html de manière plus lisible
    print(soup.title.string)

    # Les noms de produits
    for title in titles:
        print(title.string)

    # Les prix
    for price in prices:
        price_text = price.get_text(strip=True)  # Pour nettoyer les espaces inutiles
        clean_price = re.sub(r"[^\d.,]", "", price_text)  # supprésion de tous les caractères sauf chiffres, points et virgules

        print(clean_price)

    # Les catégories
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
            print("❌ Aucun lien dans ce <h3>.")
else:
    print(f"Erreur {response.status_code}")
