import requests
import csv
from bs4 import BeautifulSoup

def recuperation_information_livre(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    product_page_url = url
    upc = soup.find('th', string='UPC').find_next('td').text
    title = soup.find('h1').text
    price_including_tax = soup.find('th', string='Price (incl. tax)').find_next('td').text
    price_excluding_tax = soup.find('th', string='Price (excl. tax)').find_next('td').text
    number_available = soup.find('th', string='Availability').find_next('td').text
    product_description = soup.find('h2', string='Product Description').find_next('p').text
    category = soup.find('ul', class_='breadcrumb').find_all('li')[-1].text.strip()
    review_rating = soup.find('p', class_='star-rating')['class'][1]
    image_url = soup.find('div', class_='carousel-inner').find('img')['src']
    
    data = {'product_page_url': url,
        'universal_product_code': upc,
        'title': titre,
        'price_including_tax': prix_ttc,
        'price_excluding_tax': prix_ht,
        'number_available': disponibilite,
        'product_description': description,
        'category': categorie,
        'review_rating': evaluation,
        'image_url': image_url}
    
    with open('donnees_extraites.csv', 'a', newline='', encoding='utf-8') as fichier_csv:
        writer = csv.writer(fichier_csv, delimiter=',') # la ',' est le delimiter par défaut donc pas obligatoire ici mais obligatoire quand le delimiter est autre que ','
        writer.writerow(data)
        
        return data

def recuperation_information_category(url_category):
    headers_written = False
    while url_category:
        response = requests.get(url_category)
        soup = BeautifulSoup(response.text, 'html.parser')
        
        if not headers_written:
            headers = ["URL de la page du produit", "UPC", "Titre", "Prix TTC", "Prix hors taxe", "Disponibilité", "Description du produit", "Catégorie", "Note de l'évaluation", "URL de l'image"]
            with open('donnees_extraites.csv', 'w', newline='', encoding='utf-8') as fichier_csv:
                writer = csv.writer(fichier_csv,)
                writer.writerow(headers)
            headers_written = True

        for book in soup.find_all("h3"):
            book_url = "http://books.toscrape.com/catalogue" + book.a['href'][8:]
            recuperation_information_livre(book_url)
        
        next_button = soup.find('li', class_='next')
        if next_button:
            url_category = "http://books.toscrape.com/catalogue/category/books/mystery_3/" + next_button.a['href']
        else:
            url_category = None

# Test des fonctions
url_category = "http://books.toscrape.com/catalogue/category/books/mystery_3/index.html"
recuperation_information_category(url_category)

# Affichage du contenu du fichier CSV (pour vérification)
with open('donnees_extraites.csv', 'r', encoding='utf-8') as fichier_csv:
    reader = csv.DictReader(fichier_csv) # ou csv.reader(fichier_csv)
    for row in reader:
        print(row)
