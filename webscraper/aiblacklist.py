from bs4 import BeautifulSoup
import requests
import base64
import re



""" html text sends a get requiest to the url which would send back a status code , add the '.text' to get the page back in text format """
html_text = requests.get("https://riskofrain2.fandom.com/wiki/Category:AIBlacklist_Items").text
soup = BeautifulSoup(html_text, "lxml")

list = soup.find_all("ul")
print(len(list))
for x in range(10,24):
    a= list[x].find_all("li")

    for y in range (0, len(a)):
        d = a[y].get_text()
        print(d)