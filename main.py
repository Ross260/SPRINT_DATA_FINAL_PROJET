import requests
from bs4 import BeautifulSoup
import re


url = "https://books.toscrape.com/catalogue/category/books/mystery_3/index.html"
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
    fractions = soup.find_all('span', class_='a-price-fraction')

    # Affichage du html de manière plus lisible
    print(soup.title.string)

    #for title in titles:
     #   print(title.string)

    for price in prices:
        price_text = price.get_text(strip=True)  # Pour nettoyer les espaces inutiles
        clean_price = re.sub(r"[^\d.,]", "", price_text)  # Supprimer tous les caractères sauf chiffres, points et virgules

        print(clean_price)


else:
    print(f"Erreur {response.status_code}")