import requests
from bs4 import BeautifulSoup
import csv   # Importation de la bibliothèque csv

# URL de la page Web à scraper
url = 'http://books.toscrape.com/catalogue/how-to-stop-worrying-and-start-living_431/index.html'

# Envoi d'une requête GET pour obtenir le contenu HTML de la page
response = requests.get(url)

# Vérification que la requête s'est bien déroulée avec l'instruction "if"
if response.status_code == 200:
    # Analyse du contenu HTML avec BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Utilisation de 'string' au lieu de 'text'
    product_page_url = url
    upc = soup.find('th', string='UPC').find_next('td').text
    title = soup.find('h1').text
    price_including_tax = soup.find('th', string='Price (incl. tax)').find_next('td').text
    price_excluding_tax = soup.find('th', string='Price (excl. tax)').find_next('td').text
    number_available = soup.find('th', string='Availability').find_next('td').text
    product_description = soup.find('h2', string='Product Description').find_next('p').text
    category = soup.find('ul', class_='breadcrumb').find_all('li')[-1].text
    review_rating = soup.find('p', class_='star-rating')['class'][1]
    image_url = soup.find('div', class_='carousel-inner').find('img')['src']
    
    

    # Création d'une liste d'en-têtes de colonnes
    headers = ["URL de la page du produit", "UPC", "Titre", "Prix TTC", "Prix hors taxe", "Disponibilité", "Description du produit", "Catégorie", "Note de l'évaluation", "URL de l'image"]
    
    # Création d'une liste de données
    data = [product_page_url, upc, title, price_including_tax, price_excluding_tax, number_available, product_description, category, review_rating, image_url]
    

    # Ouverture d'un fichier CSV en mode écriture
    with open('donnees_extraites2.csv', 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        
        # Écriture des en-têtes de colonnes
        writer.writerow(headers)
        #writer.writerow(["URL de la page du produit", "UPC", "Titre", "Prix TTC", "Prix hors taxe", "Disponibilité", "Description du produit", "Catégorie", "Note de l'évaluation", "URL de l'image"])
        
        # Écriture des données
        writer.writerow(data)
        #writer.writerow([product_page_url, upc, title, price_including_tax, price_excluding_tax, number_available, product_description, category, review_rating, image_url])    


    # Affichage du contenu du fichier CSV (mode lecture)
    with open('donnees_extraites2.csv', 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            print(row)
        
else:
    print("La requête a échoué. Statut de la réponse:", response.status_code)
