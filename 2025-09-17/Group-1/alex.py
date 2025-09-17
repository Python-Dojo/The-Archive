
import requests

url = "https://www.theguardian.com/crosswords"
response = requests.get(url)

from bs4 import BeautifulSoup

soup = BeautifulSoup(response.text, 'html.parser')
print(soup.prettify()[0:100])  

import requests
import re
from bs4 import BeautifulSoup
url = "https://www.theguardian.com/crosswords"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
hrefs = []
links = soup.find_all('href', )
for box in quote_boxes:
for box in links:
    quote_text = box.img['alt'].split(" #")
    quote = {
        'theme': box.h5.text.strip(),
        'image_url': box.img['src'],
        'lines': quote_text[0],
        'author': quote_text[1] if len(quote_text) > 1 else 'Unknown'
    }
    quotes.append(quote)
# Display extracted quotes
for q in quotes[:5]:  # print only first 5 for brevity
    print(q)