from bs4 import BeautifulSoup as bs
from urllib.request import urlopen, Request
import numpy as np
import requests, cv2

r = bs(requests.get("https://www.mandatory.com/fun/1235945-nicolas-cage-memes-are-his-legacy").text, features='lxml').find_all("img")[3]['src']
r = bytearray(urlopen(Request(r, headers={'User-Agent': "Mozilla/5.0"})).read())
image = cv2.imdecode(np.asarray(r, dtype="uint8"), cv2.IMREAD_COLOR)