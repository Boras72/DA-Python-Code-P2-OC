# Books to Scrape - Système ETL pour l'extraction de données de librairie

Ce projet vise à créer un système ETL (Extract, Transform, Load) automatisé qui récupère les informations de livres à partir du site fictif "Books to Scrape". L'application exécutable à la demande extrait les prix des livres et d'autres métadonnées pertinentes au moment de son exécution et les stocke de manière structurée pour une analyse ultérieure.

## Fonctionnalités
- **Extraction des données du produit** : Permet de sélectionner une page produit spécifique pour extraire des informations telles que l'URL de la page produit, le code UPC, le titre, les prix (avec et sans taxes), la disponibilité, la description du produit, la catégorie, le classement par étoiles et l'URL de l'image pour les enregistrer dans un fichier CSV.
- **Collecte de données par catégorie** : Extrait les informations de tous les livres d'une catégorie donnée et les enregistre dans un fichier CSV unique.
- **Collecte de données globale** : Récupère les informations de tous les livres de toutes les catégories disponibles sur le site et les enregistre dans des fichiers CSV distincts.
- **Extraction et sauvegarde des images** : Télécharge et enregistre les images de couverture de tous les livres extraites.

## Processus ETL
### Extraction
Utilisation de `requests` pour interroger les pages web et de `BeautifulSoup` pour parser le code HTML. Les données sont extraites et compilées dans le format CSV.

### Transformation
Les données sont ensuite transformées pour assurer la cohérence et la qualité. Cela inclut la validation des formats, l'organisation des dossiers d'images et de fichiers CSV, et l'harmonisation des URLs des images.

### Chargement
Les données finales sont chargées dans des fichiers CSV pour les métadonnées textuelles et les images sont stockées dans un dossier séparé.

## Structure du code
- Importation des bibliothèques python (Requests, BeautifulSoup, CSV, OS).
- Le dossier `images` est créé s'il n'existe pas pour stocker les images téléchargées.
- Le dossier `csv` est créé pour organiser les fichiers CSV générés.
- Les fonctions sont définies pour extraire les informations d'un livre, les données d'une catégorie de livres, les images, et pour effectuer le processus sur toutes les catégories.

## Utilisation

## Prérequis

Avant de commencer à utiliser ce projet, vous devez avoir installé Python sur votre système. Ce projet a été testé avec Python 3.x.

## Configuration de l'environnement

Il est recommandé d'utiliser un environnement virtuel pour exécuter ce projet afin de gérer les dépendances de manière isolée. Pour configurer et activer un environnement virtuel, suivez ces étapes :

### Création de l'environnement virtuel
Ouvrez un terminal et exécutez la commande suivante à la racine de votre projet :
```bash
python3 -m venv 'nom_de_votre_environnement'      
(cela créera un nouveau dossier nom_de_votre_environnement contenant l'environnement virtuel)
```
### Pour activer l'environnement virtuel :   
Windows : 
```nom_de_votre_environnement\Scripts\activate```
MacOS et Linux : 
```source nom_de_votre_environnement/bin/activate```
Une fois l'environnement virtuel activé, votre invite de commande se positionnera dans le nouvel environnement virtuel (*).

### Installation des dépendances
Installez les dépendances nécessaires en exécutant :
```bash
pip install -r requirements.txt
(Le fichier requirements.txt contient les bibliothèques du projet "Requests" et "BeautifulSoup4")
```
### Exécution du code
Pour exécuter le script d'extraction, assurez-vous que l'environnement virtuel est activé, puis exécutez la commande suivante dans votre terminal :
```bash
python3 main.py
(Désactiver l'environnement virtuel en exécutant : "deactivate")
```

## Contribution
Pour contribuer au projet, veuillez 'forker' le dépôt, créer une branche de fonctionnalités, puis soumettre une pull request pour examen.

## Licence
Ce projet est sous licence Opensource. Veuillez consulter le fichier LICENSE pour plus d'informations.

## Contact
Pour toute question ou suggestion, n'hésitez pas à ouvrir un problème ("Issue") dans le dépôt GitHub du projet.
