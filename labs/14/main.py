from bs4 import BeautifulSoup as bs
from urllib.request import urlopen
import numpy as np
import requests
import cv2

r = urlopen(bs(requests.get("https://www.mandatory.com/fun/1235945-nicolas-cage-memes-are-his-legacy").text, features='lxml').find_all("img")[3]['src'])
image = np.asarray(bytearray(r.read()), dtype="uint8")
image = cv2.imdecode(image, cv2.IMREAD_COLOR)