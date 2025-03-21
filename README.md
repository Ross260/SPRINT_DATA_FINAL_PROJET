# 📌 Projet de Web Scraping et Analyse des Données d'un site ecommerce avec Python

## 📖 Description
Ce projet est un outil complet de **scraping web** et **d'analyse de données** utilisant **Python**, **BeautifulSoup**, **pandas**, et **MySQL**. Il permet de récupérer des informations sur des produits à partir de sites e-commerce, de les stocker dans une base de données, de les analyser avec **pandas**, et de les visualiser avec **matplotlib**.

### 🔹 Fonctionnalités principales
✅ **Scraping Web** : Extraction des noms, prix, catégories, avis et liens des produits.  
✅ **Stockage dans MySQL** : Enregistrement structuré des données dans une base de donnée MySQL.  
✅ **Nettoyage et Transformation des Données** : Normalisation, correction des valeurs manquantes et ajout de nouvelles métriques.  
✅ **Visualisation des Données** : Graphiques pour l'analyse des tendances et des corrélations par des **diagrammes**.  
✅ **Export CSV** : Possibilité d'enregistrer les résultats sous forme de fichier CSV.

---

## 🛠️ Installation
### 1️⃣ **Cloner le projet**
```bash
git clone https://github.com/Ross260/SPRINT_DATA_FINAL_PROJET.git
```

### 2️⃣ **Installer les dépendances**
Assure-toi d’avoir **Python 3** installé, puis exécute :
```bash
pip install -r requirements.txt
```

### 3️⃣ **Configurer la base de données**
Assure-toi que **MySQL** est installé et démarré. Ensuite, crée la base de données :
```sql
CREATE DATABASE ecommerce_scraping;
USE ecommerce_scraping;

CREATE TABLE produits (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nom VARCHAR(255),
    prix DECIMAL(10,2),
    categorie VARCHAR(255),
    avis VARCHAR(50),
    lien TEXT
);
```

### 4️⃣ **Configurer la connexion MySQL**
Dans le fichier `config.py`, renseigne tes informations MySQL :
```python
DB_CONFIG = {
    "host": "localhost",
    "user": "hostname",
    "password": "your_password",
    "database": "ecommerce_scraping"
}
```

---

## 🚀 Utilisation
### 1️⃣ **Lancer le scraping**
```bash
python main.py
```
Le script va récupérer les données et les **stocker dans la base MySQL**.

### 2️⃣ **Nettoyage des données**
```bash
python nettoyage.py
```
Ce script va **nettoyer les données**, ajouter de nouvelles colonnes au dataframe et les mettre dans un fichier CSV.

---

## 📊 Visualisation des Données
Le projet propose plusieurs graphiques :
- **Répartition des prix** 📈
- **Nombre de produits par catégorie** 📊
- **Corrélation entre prix et avis** 🔎
- **Evolution des prix dans le temps** ⏳


###  **Visualisation des données**
```bash
python visualisation.py
```


---

## 🛠️ Technologies Utilisées
- **Python 3.x** 🐍
- **BeautifulSoup** 🌐 (Scraping Web)
- **pandas** 🐼 (Analyse des données)
- **Matplotlib & Seaborn** 📊 (Visualisation)
- **MySQL & SQLAlchemy** 🗄️ (Base de données)


---

## 🤝 Contribuer
💡 Tu veux améliorer ce projet ? **Fork, clone et propose tes améliorations !** 🚀
```bash
git https://github.com/Ross260/SPRINT_DATA_FINAL_PROJET.git
```

---

## 📜 Licence
Ce projet est sous **MIT License** - Utilisation libre avec mention
