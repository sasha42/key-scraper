# coding: utf-8

import requests
import os
from bs4 import BeautifulSoup

print("This tool downloads user keys from GOGS")

try:
    base_url = os.environ['BASE_URL']
except:
    base_url = input("Please enter your base GOGS URL: ")

users_list = []
key_list = []


# Get a list of users:
def scrape_page(soup):
    divs = soup.find_all("div", class_="item")
    for div in divs[1:21]:
        links = div.findAll('a')
        user = links[0].get('href')
        if user == "#":
            break
        users_list.append(user)

def get_pages():
    for i in range(100):
        users = requests.get(base_url + "/explore/users?page=" + str(i))
        if len(users.text) < 6000:
            break
        print("Scraping users list page {}".format(i))
        soup = BeautifulSoup(users.text, "html.parser")
        scrape_page(soup)

get_pages()

# Get their keys:
print("Scraping keys")
for user in users_list:
    key = requests.get(base_url + user + ".keys")
    key_list.append(key.text)

print("Saved keys from {} users".format(len(users_list)))

# Write to file:
target = open("keys", 'w')

for key in key_list:
    target.write(key)

target.close()
