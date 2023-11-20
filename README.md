# Code-Python-P2-OC

L'objectif de ce projet était de créer une application exécutable à la demande qui récupère les prix des livres au moment de son exécution. 

Voici les fonctionnalités suivantes :

- Choix d'une page "Produit" ou d'un livre sur le site de Books to Scrape pour extraire les informations demandées. J'ai écrit un script Python qui visite la page sélectionnée et extrait les informations suivantes : product_page_url, universal_product_code (upc), title, price_including_tax, price_excluding_tax, number_available, product_description, category, review_rating et image_url. Les données extraites sont ensuite enregistrées dans un fichier CSV avec les en-têtes de colonnes correspondants.

- Récupération de toutes les données nécessaires pour une catégorie d'ouvrages donnée. J'ai écrit un script Python qui consulte une page de catégorie et extrait l'URL de la page "Produit" de chaque livre appartenant à cette catégorie. Ensuite, j'ai extrait les données produit de tous les livres de la catégorie choisie et les ai écrites dans un seul fichier CSV. Mon application est également capable de parcourir automatiquement les multiples pages si elles sont présentes.

- Récupération de toutes les données nécessaires de toutes les catégories de livres. J'ai écrit un script qui consulte le site de Books to Scrape pour extraire les informations produit de tous les livres appartenant à toutes les catégories différentes. Les données sont ensuite écrites dans un fichier CSV distinct pour chaque catégorie de livres.

- Extraction et enregistrement de tous les fichiers images de tous les livres de toutes les catégories consultées.

J'ai testé le système et il fonctionne correctement. 

Vous trouverez dans ce Repo que le code Python sans les outputs (fichiers CSV ou images ) générés.

