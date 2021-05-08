import requests
import time
from bs4 import BeautifulSoup

def Get():
    page = requests.get('https://ultrontheai.github.io/PYBattery/battry.html')
    soup = BeautifulSoup(page.content, 'html.parser')
    location = soup.find('div', class_='percent')
    return location.text

# print(Get())