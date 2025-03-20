import requests
from bs4 import BeautifulSoup
import json
URL = "http://books.toscrape.com/"

# install git
# create repository in github
# go to git bash
# git config - global user.name "smarika rajaura"
# git config -global user.email"smarikarajaura55@gmail.om"
# git init
# git status ->if you want to check what are the status of File
# git diff ->if you want to check what are the changes
# git add.
# git commit -m "your message"
# copy paste git code from github



# git add . - track files and folders
# git commit -m "your message" -- "your messange"/save changes
# git push -upload changes or save to github.

def  scrape_books(url):
    response =requests.get(url)
    # print(response)
    # print(response.status_code)
    # print(response.text)
    if response.status_code !=200:
        print("Failed to fetch the page")
        return
    
    response.encoding = response.apparent_encoding
    soup = BeautifulSoup(response.text,"html.parser")
    books = soup.find_all("article",class_="product_pod")

    book_list = []
    for book in books:
        title=(book.h3.a["title"])
        price_text = book.find("p",class_="price_color").text
        currency = price_text[0]
        price = price_text [1:]
        print(title, currency,price)

        book_list.append({
            "title":title,
            "currency":currency,
            "price":price
        })

    with open("books.json","w",encoding="utf-8")as file:
        json.dump(book_list,file,indent =4,ensure_ascii = False)
    

    print("Data saved to books.json")
scrape_books(URL)