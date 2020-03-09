from bs4 import BeautifulSoup as bs
import requests

print(bs(requests.get("https://www.mandatory.com/fun/1235945-nicolas-cage-memes-are-his-legacy").text, features='lxml').find_all("img")[3]['src'])
