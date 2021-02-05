# importing libraries

import requests
from bs4 import BeautifulSoup

# Making get request and storing the response in a variable
# webpage = requests.get('https://www.twinword.co.kr/blog')
webpage = requests.get('https://www.adobe.com/kr/about-adobe/contact.html')

# # Parsing the content of web page by html parser
# soup = BeautifulSoup(webpage.content, 'html.parser')
#
# # Finding all meta tags present, stored in a list format
# meta_tag = soup.find('meta' {"name":"Description"})
# # Looping the meta tag list
# # for x in meta_tag:
# #     print(x.attrs['content'])
# #     print('-----------------')
#
# print(meta_tag)


soup = BeautifulSoup(webpage.content, 'html.parser')
soup_text = BeautifulSoup(webpage.text, 'html.parser')

def crawl():
    for tag in soup.find_all("meta"):
        if tag.get("name") == "description":
            print("description - ", tag.get("content"))
        elif tag.get("property") == "og:title":
            print("og:title - ", tag.get("content"))
        elif tag.get("property") == "og:description":
            print("og:description - ", tag.get("content"))
        elif tag.get("property") == "og:url":
            print("og:url - ", tag.get("content"))
        elif tag.get("property") == "og:ㅑimage":
            print("og:image - ", tag.get("content"))


crawl()



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
