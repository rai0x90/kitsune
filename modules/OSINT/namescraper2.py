
import requests
from bs4 import BeautifulSoup


def namescrape(name):
    URL = "http://www.fastpeoplesearch.com/name/bongseob-moon"
    page = requests.get(URL)

    soup = BeautifulSoup(page.content, 'html.parser')

    card = soup.find("div", class_="card")

    for parts in card:
       p1 = card.find_all("h2", class_="card-title") 
       p2 = card.find("h3")
       p3 = card.find("strong")
       print(p1.text.strip())
       print(p2.text.strip())
       print(p3.text.strip())

   

    

    


