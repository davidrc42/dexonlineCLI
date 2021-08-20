#!/usr/bin/env python3
import requests
from sys import argv
from bs4 import BeautifulSoup

def main():
    url = "https://dexonline.ro/definitie/" + argv[1]
    req = requests.get(url)
    reqHtml = BeautifulSoup(req.content, "html.parser")
    if reqHtml.find(class_="def"):
        result = reqHtml.find(class_="def").text
        print(result)
    else:
        print("no such word")
