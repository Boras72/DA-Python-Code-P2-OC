# Projet-P2-Scraping-OC

L'objectif de ce projet était de créer une application exécutable à la demande qui récupère des données de livres depuis un site web, les enregistrer dans des fichiers CSV et télécharger les images des couvertures des livres.
 

**Voici les fonctionnalités suivantes :**

- Choix d'une page "Produit" ou d'un livre sur le site de Books to Scrape pour extraire les informations demandées. J'ai écrit un script Python qui visite la page sélectionnée et extrait les informations suivantes : product_page_url, universal_product_code (upc), title, price_including_tax, price_excluding_tax, number_available, product_description, category, review_rating et image_url. Les données extraites sont ensuite enregistrées dans un fichier CSV avec les en-têtes de colonnes correspondants.
`extraire_infos_livre(url)`: Cette fonction extrait les informations d'un livre en utilisant son URL, telles que l'UPC, le titre, les prix avec et sans taxe, la disponibilité, la description, la catégorie, l'évaluation et l'URL de l'image.

- Récupération de toutes les données nécessaires pour une catégorie d'ouvrages donnée. J'ai écrit un script Python qui consulte une page de catégorie et extrait l'URL de la page "Produit" de chaque livre appartenant à cette catégorie. Ensuite, j'ai extrait les données produit de tous les livres de la catégorie choisie et les ai écrites dans un seul fichier CSV. Mon application est également capable de parcourir automatiquement les multiples pages si elles sont présentes.
`extraire_liens_categorie(url_categorie)`: Elle récupère les liens de tous les livres d'une catégorie donnée.
`extraire_donnees_categorie(url_categorie, nom_categorie)`: Cette fonction utilise `extraire_liens_categorie` pour obtenir les liens de tous les livres d'une catégorie et ensuite extraire leurs données pour les sauvegarder dans un CSV.

- Récupération de toutes les données nécessaires de toutes les catégories de livres. J'ai écrit un script qui consulte le site de Books to Scrape pour extraire les informations produit de tous les livres appartenant à toutes les catégories différentes. Les données sont ensuite écrites dans un fichier CSV distinct pour chaque catégorie de livres.
`extraire_liens_toutes_categories()`: Elle extrait les liens de toutes les catégories de livres disponibles sur le site.

- Extraction et enregistrement de tous les fichiers images de tous les livres de toutes les catégories consultées :
 `telecharger_image(url_image, nom_fichier)`: Cette fonction télécharge une image à partir de son URL.


Vous trouverez dans ce Repo que le code Python final dans la branche principale, sans les outputs générés.

