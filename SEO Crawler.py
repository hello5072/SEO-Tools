import requests
from bs4 import BeautifulSoup

i = 0
# url_list = ["https://acrobat.adobe.com/us/en/acrobat/how-to/create-pdf.html","https://acrobat.adobe.com/us/en/acrobat/how-to/fill-sign-pdf-forms-electronically.html","https://acrobat.adobe.com/us/en/acrobat/how-to/create-fillable-pdf-forms-creator.html","https://acrobat.adobe.com/us/en/acrobat/how-to/convert-ppt-to-pdf.html","https://acrobat.adobe.com/us/en/acrobat/how-to/convert-jpeg-tiff-scan-to-pdf.html","https://acrobat.adobe.com/us/en/acrobat/how-to/rearrange-pdf-pages.html","https://acrobat.adobe.com/us/en/acrobat/how-to/pdf-file-password-permissions.html","https://acrobat.adobe.com/us/en/acrobat/how-to/electronic-signatures-online-e-signatures.html","https://acrobat.adobe.com/us/en/acrobat/how-to/compare-two-pdf-files.html","https://acrobat.adobe.com/us/en/acrobat/how-to/convert-word-to-pdf.html","https://acrobat.adobe.com/us/en/acrobat/pdf-reader/volume-distribution.html","https://acrobat.adobe.com/us/en/acrobat/how-to/convert-html-to-pdf.html","https://acrobat.adobe.com/us/en/acrobat/how-to/print-to-pdf.html","https://acrobat.adobe.com/us/en/acrobat/adobe-send-track-outlook-plug-in.html","https://acrobat.adobe.com/us/en/acrobat/how-to/delete-pages-from-pdf.html"]
url_list = ["https://www.adobe.com/photoshop/online/halftone-pattern.html",
"https://www.adobe.com/photoshop/online/resize-for-instagram.html",
"https://www.adobe.com/photoshop/online/resize-for-facebook.html"]


agent = {"User-Agent": 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'}

# Built Function
def crawl_meta():
    reqs = requests.get(url, headers=agent)
    soup = BeautifulSoup(reqs.text, 'html.parser')

    for heading in soup.find_all(["title", "h1"]):
        result = (heading.name + ' - ' + heading.text.strip())
        print(result)
    for tag in soup.find_all("meta"):
        if tag.get("name") == "description":
            print("description - ", tag.get("content"))
        elif tag.get("property") == "og:title":
            print("og:title - ", tag.get("content"))
        elif tag.get("property") == "og:description":
            print("og:description - ", tag.get("content"))
        elif tag.get("property") == "og:url":
            print("og:url - ", tag.get("content"))
        elif tag.get("property") == "og:image":
            print("og:image - ", tag.get("content"))
        elif tag.get("property") == "og:image:alt":
            print("og:image alt - ", tag.get("content"))
    for image in soup.find_all("img"):
        if image.get("alt") != (""):
            print("img alt - ", image.get("alt"))

# Execution
for url in url_list:
  print(url_list[i])
  crawl_meta()
  print('\n'*2)
  i += 1


