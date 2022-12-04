from bs4 import BeautifulSoup
import requests

url = "https://www.plus500.com/en/"
ua = {"User-Agent":"Mozilla/5.0"}

page = requests.get(url, headers=ua)
doc = BeautifulSoup(page.text, "html.parser")

filltered_list = str(doc).split("var feedApp;")
filltered_list = str(filltered_list[1]).split("document.addEventListener('DOMContentLoaded', function (){")
filltered_list = str(filltered_list[0]).split("\"instrumentId\":")

x = 1
items = str(filltered_list[x]).replace("}","").replace("\"","").replace(']','').split(",")

for item in filltered_list:

    items = str(filltered_list[x]).replace("}","").replace("\"","").replace(']','').split(",")
    name, price, change_rate = items[3], items[7], items[8]
    print(name,"\n", price,"\n", change_rate, "\n ------------------")
    x += 1

    if len(filltered_list) == x: break