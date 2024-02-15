import requests
from bs4 import BeautifulSoup

def page_scanner(url):
  response = requests.get(url)
  soup = BeautifulSoup(response.content, 'html.parser')
  api_links = soup.find_all('a')