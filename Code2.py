import requests
from bs4 import BeautifulSoup
# URL de la page Web à scraper
url='http://books.toscrape.com/catalogue/how-to-stop-worrying-and-start-living_431/index.html'
# Envoi d'une requête GET pour obtenir le contenu HTML de la page
response=requests.get(url)
# Affichage du code HTML récupéré
#print(response.text)

# Vérification que la requête s'est bien déroulée
if response.status_code == 200:
    # Analyse du contenu HTML avec BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')

    # Extraction des informations
    product_page_url = url
    upc = soup.find('th', text='UPC').find_next('td').text
    title = soup.find('h1').text
    price_including_tax = soup.find('th', text='Price (incl. tax)').find_next('td').text
    price_excluding_tax = soup.find('th', text='Price (excl. tax)').find_next('td').text
    number_available = soup.find('th', text='Availability').find_next('td').text
    product_description = soup.find('h2', text='Product Description').find_next('p').text
    category = soup.find('ul', class_='breadcrumb').find_all('li')[-1].text
    review_rating = soup.find('p', class_='star-rating')['class'][1]
    image_url = soup.find('div', class_='carousel-inner').find('img')['src']

    # Affichage des informations
    print("URL de l'image:", image_url)
    print("Titre:", title)
    print("Note de l'évaluation:", review_rating)
    print("Description du produit:", product_description)
    print("Catégorie:", category)
    print("UPC:", upc)
    print("Prix TTC:", price_including_tax)
    print("Prix hors taxe:", price_excluding_tax)
    print("Disponibilité:", number_available)
    print("URL de la page du produit:", product_page_url)
else:
    print("La requête a échoué. Statut de la réponse:", response.status_code)
