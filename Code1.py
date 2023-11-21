import requests
from bs4 import BeautifulSoup
url_livre="http://books.toscrape.com/catalogue/how-to-stop-worrying-and-start-living_431/index.html"

def recuperation_information_livre(url):
    # On va récupérer le code html de cette page
    response=requests.get(url)
    # Créer un objet BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')
    # Extraire les différentes informations :

    # 1. le titre du livre 
    title=soup.find('h1').text

    all_td=soup.find_all('td')

    # 2. universal_ product_code (upc)
    upc=all_td[0].text

    # 3. Prix TTC :
    ttc=all_td[3].text

    return title,upc,ttc

title,upc,ttc=recuperation_information_livre(url_livre)
print(upc,ttc,title)
   