from bs4 import BeautifulSoup
import os
import requests

url = "https://who.is/"
page = requests.get(url)
soup = BeautifulSoup(page.text, 'html.parser')
print(soup.find_all('p')[2].get_text())

