import requests
from bs4 import BeautifulSoup

response = requests.get("http://www.tutorialspoint.com/")
html_data = response.text
soup = BeautifulSoup(html_data)
for a in soup.findAll('a'):
    finurl = a['href']
    print(finurl)
