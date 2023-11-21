import requests
import csv
from bs4 import BeautifulSoup

#import pkg_resources
#print(pkg_resources.get_distribution("requests").version)
#import sys
#print(sys.version)


#-------------------------------------------  PHASE 1 -------------------------------------
# Extraction des informations sur 1 livre :
def extraire_infos_livre(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    product_page_url = url
    upc = soup.find('th', string='UPC').find_next_sibling('td').text
    title = soup.find('h1').text
    price_including_tax = soup.find('th', string='Price (incl. tax)').find_next_sibling('td').text
    price_excluding_tax = soup.find('th', string='Price (excl. tax)').find_next_sibling('td').text
    number_available = soup.find('th', string='Availability').find_next_sibling('td').text
    product_description = soup.find('h2', string='Product Description').find_next('p').text
    category = soup.find('ul', class_='breadcrumb').find_all('a')[-1].text.strip()
    review_rating = soup.find('p', class_='star-rating')['class'][1]
    image_url = soup.find('img')['src'].replace('../../', 'http://books.toscrape.com/')
    
    return {'url': product_page_url,
        'code universel produit': upc,
        'titre': title,
        'prix_ttc': price_including_tax,
        'prix_ht': price_excluding_tax,
        'disponibilité': number_available,
        'description': product_description,
        'categorie': category,
        'evaluation': review_rating,
        'url_image': image_url}
    
# Ecriture des informations extraites sur 1 livre :        
def ecrire_csv(donnees_extraites, nom_fichier):
    with open(nom_fichier, 'w', newline='', encoding='utf-8') as fichier:  
        ecrire = csv.DictWriter(fichier, fieldnames=donnees_extraites.keys())
        ecrire.writeheader()
        ecrire.writerow(donnees_extraites)

# Exécution du code de la fonction
url_livre = "http://books.toscrape.com/catalogue/how-to-stop-worrying-and-start-living_431/index.html"
donnees_livre = extraire_infos_livre(url_livre)
ecrire_csv(donnees_livre, 'infos_livre.csv')
#ecrire_csv(extraire_infos_livre("http://books.toscrape.com/catalogue/how-to-stop-worrying-and-start-living_431/index.html"), 'infos_livre.csv')


#-------------------------------------------  PHASE 2 -------------------------------------

#Extraction des liens des livres de la catégorie "Mystery":
def extraire_liens_livres(url_categorie):
    response = requests.get(url_categorie)
    soup = BeautifulSoup(response.text, 'html.parser')

    livres = soup.find_all('h3')
    next=soup.find('li', class_='next')
    while next:
        next_url=url_categorie.replace('index.html', next.find('a')['href']) 
        response = requests.get(next_url)
        soup = BeautifulSoup(response.text, 'html.parser')
        livres += soup.find_all('h3')
        next=soup.find('li', class_='next')
    
    return [livre.find('a')['href'].replace('../../../', 'http://books.toscrape.com/catalogue/') for livre in livres]
    

#Extraction et écriture des informations de tous les livres de la catégorie "Mystery":
def extraire_donnees_categorie(url_categorie, nom_categorie):
    liens_livres=extraire_liens_livres(url_categorie)
    donnees_livres=[extraire_infos_livre(lien) for lien in liens_livres]
    with open(nom_categorie + ".csv", "w", newline='', encoding='utf-8') as fichier:
        ecrire = csv.DictWriter(fichier, fieldnames=donnees_livres[0].keys()) 
        ecrire.writeheader()
        for donnees in donnees_livres:
            ecrire.writerow(donnees)

# Exécution du code de la fonction
#extraire_donnees_categorie('https://books.toscrape.com/catalogue/category/books/mystery_3/index.html', 'Mystery')


#-------------------------------------------  PHASE 3 -------------------------------------

# Extraction des liens de toutes les catégories :
def extraire_liens_toutes_categories():
    url = "http://books.toscrape.com/index.html"
    reponse = requests.get(url)
    soup = BeautifulSoup(reponse.text, 'html.parser')
    categories = soup.find('div', class_='side_categories').find_all('a')
    liens_categories = ['http://books.toscrape.com/' + categorie['href'] for categorie in categories[1:]]  # Nous excluons le premier élément car il représente "All books"
    
    return liens_categories


# Extraction et écriture des informations pour tous les livres de toutes les catégories :
def extraire_et_ecrire_infos_toutes_categories():
    liens_categories = extraire_liens_toutes_categories()
    for lien_categorie in liens_categories:
        nom_categorie = lien_categorie.split('/')[-2]
        nom_fichier = nom_categorie + '.csv'
        extraire_donnees_categorie(lien_categorie, nom_fichier)
        #extraire_et_ecrire_infos_categorie(lien_categorie, nom_fichier)
        
# Exécution du code de la fonction
extraire_et_ecrire_infos_toutes_categories()


#-------------------------------------------  PHASE 4 -------------------------------------


# Extraction des images de tous les livres :       
def telecharger_image(url_image, nom_fichier):
    reponse = requests.get(url_image)
    with open(nom_fichier, 'wb') as fichier:
        fichier.write(reponse.content)

# Sauvegarde des images de tous les livres :
def extraire_et_sauvegarder_images_tous_livres():
    liens_categories = extraire_liens_toutes_categories()
    for lien_categorie in liens_categories:
        liens_livres = extraire_tous_liens_categorie(lien_categorie)
        for lien in liens_livres:
            infos_livre = extraire_infos_livre(lien)
            url_image = infos_livre['image_url']
            nom_image = url_image.split('/')[-1]
            telecharger_image(url_image, 'images/' + nom_image)  # Les images seront enregistrées dans un dossier nommé "images"
            
# Exécution du code de la fonction
extraire_et_sauvegarder_images_tous_livres()