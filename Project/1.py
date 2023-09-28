#  import http requests
import requests
#  import beautiful soup
from bs4 import BeautifulSoup


url = "https://play.stream4.me"

#  get the html content
html_content = requests.get(url).text

print(html_content)
