import requests
from bs4 import BeautifulSoup

url = "https://books.toscrape.com/index.html"

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                         "Chrome/110.0.5481.104 Safari/537.36"}

response = requests.get(url)  # Envoie une requête GET

# Vérifier si la requête est réussie
if response.status_code == 200:
    print("Requête réussie ! Information du site " + url + " récuperer avec succès ")
    html_content = response.text  # Contenu HTML de la page

    soup = BeautifulSoup(response.text, "html.parser")

    # print(soup.prettify())

    category_links = soup.find_all('a')

    all_category = []  # Initialiser une liste vide

    for category_link in category_links:
        if len(all_category) < 10:
            all_category.append(category_link["href"])  # Ajoute le lien à la liste
        else:
            break  # j'arrete la boucle si la limite est atteinte

    print("Liste finale " + str(all_category))  # Afficher la liste finale

    # Supprimer "index.html" et garder tout avant
    categories_clean = [cat.rsplit("/", 1)[0] for cat in all_category]

    print(categories_clean)