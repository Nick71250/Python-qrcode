import re
import requests
from bs4 import BeautifulSoup as bs

r = requests.get('https://keithgalli.github.io/web-scraping/example.html')

soup = bs(r.content, 'lxml')
# Find all h1 and h2 as an array
headers = soup.find_all(['h1', 'h2'])

# Find all paragraphs "p" that contains attr "id" equals to "paragraph-id"
paragraph = soup.find_all("p", attrs={"id": "paragraph-id"})

# Nesting find/find_all
body = soup.find("body")
div = body.find("div")
header = div.find("h1")

# Search for specific strings in our find/find_all calls, using regular expressions
paragraphs = soup.find_all("p", string=re.compile("Some"))
h2_headers = soup.find_all("h2", string=re.compile("([Hh])eader"))

# select (CSS selector)
content = soup.select("p")

# select paragraph inside div
p_inside_div = soup.select("div p")

# select paragraph right after h2 tag
p_after_h2 = soup.select("h2 ~ p")

# select bold text inside paragraph with id="paragraph-id"
bold_text = soup.select("p#paragraph-id b")

print(bold_text)
