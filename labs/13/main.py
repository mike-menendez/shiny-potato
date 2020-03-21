# Authors: Mike Menendez, Crassinadra Cavrolet
# Date: 3/12/2020
# Purpose: scrapes website to print out an arbitrary image's url (Nic Cages)
from bs4 import BeautifulSoup as bs
import requests

print(bs(requests.get("https://www.mandatory.com/fun/1235945-nicolas-cage-memes-are-his-legacy").text, features='lxml').find_all("img")[3]['src'])
