import requests
from bs4 import BeautifulSoup


# Input the URL in the list. The form should follow ["URL1","URL2","URL3"]
url_list = ['https://hyundai-n.com']

def crawl():
  reqs = requests.get(url)
  soup = BeautifulSoup(reqs.text, 'html.parser')
  for heading in soup.find_all(["title", 'h2']):
      result = (heading.name + ' ' + heading.text.strip())
      print(result)


i = 0

for url in url_list:
  print(url_list[i])
  crawl()
  print('\n'*2)
  i += 1





