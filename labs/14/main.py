from bs4 import BeautifulSoup as bs
from urllib.request import urlopen
from PIL import Image
import numpy as np
import requests, cv2

r = bs(requests.get("https://www.mandatory.com/fun/1235945-nicolas-cage-memes-are-his-legacy").text, features='lxml').find_all("img")[3]['src']
image = np.array(Image.open(requests.get(r, stream=True).raw))
image = cv2.imdecode(image, cv2.IMREAD_COLOR)