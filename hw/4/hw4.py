from flask import Flask, render_template
import os
import random


def map_gen():
    temp = os.listdir("picture")
    dict = {}
    for i in len(temp):
        dict[i] = temp[i]
    return dict


# Display three random images from /img directory
@app.route('/', methods=["GET"])
def index():
    dict = map_gen()
    img1 = dict.pop(random.randrange(0, len(dict.keys())))
    img2 = dict.pop(random.randrange(0, len(dict.keys())))
    img3 = dict.pop(random.randrange(0, len(dict.keys())))
    return

if __name__ == "__main__":
    app = Flask(__name__)