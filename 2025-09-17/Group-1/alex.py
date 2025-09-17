
import requests

url = "https://www.theguardian.com/crosswords"
response = requests.get(url)

from bs4 import BeautifulSoup

soup = BeautifulSoup(response.text, 'html.parser')
print(soup.prettify()[0:100])  