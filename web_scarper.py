import requests
from bs4 import BeautifulSoup
import json

url = 'https://www.plus500.com/en/'
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.3"
}
response = requests.get(url, headers=headers)
html = response.content

soup = BeautifulSoup(html,'lxml')

wanted_tag = soup.find_all('script')[7]

data = str(wanted_tag).split("document.addEventListener('DOMContentLoaded', function (){")[0].replace("<script>\r\n    var feedApp;\r\n    var initialData = ",'')

data_dict = json.loads(data)

for v in data_dict.values():
    instrument = v['instruments']
    for i in instrument:
        print(f"name: {i['name']}\nprice: {i['sellPrice']}\nchange rate: {i['changeRate']}\n---------------")
