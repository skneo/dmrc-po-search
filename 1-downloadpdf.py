import requests
from bs4 import BeautifulSoup

url = "https://www.delhimetrorail.com/pages/en/corporate/list-of-purchase-order-for-store-department"
response = requests.get(url)

soup = BeautifulSoup(response.content, "html.parser")
pdf_files = [link["href"] for link in soup.find_all("a") if link["href"].endswith(".pdf")]

for pdf_file in pdf_files:
    pdf_url = url + "/" + pdf_file
    response = requests.get(pdf_url)
    open(pdf_file, "wb").write(response.content)
 