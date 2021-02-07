import requests
import lxml
from bs4 import BeautifulSoup

countries = ['Frankrijk', 'Spanje', 'Portugal', 'Italie', 'Duitsland']

def get_travel_advice(countries):
    
    baseUrl = 'https://diplomatie.belgium.be/nl/Diensten/Op_reis_in_het_buitenland/reisadviezen/{}' 
    
    for country in countries:
        
        print('Scraping info for {}...\n\n'.format(country))
        
        scrapeUrl = baseUrl.format(country)
        
        res = requests.get(scrapeUrl)
        soup = BeautifulSoup(res.text, 'lxml')

        info = soup.select('body table')
        
        filename = country + '.txt'
        f = open(file=filename, mode='w', encoding='UTF-8')

        for item in info:
            f.write(item.get_text())
            f.write('\n')
        
get_travel_advice(countries)



