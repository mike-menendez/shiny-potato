#Authors: Miek Menendd, Cass Cabrera
#Date: April 4, 2020
#Course: CST 205
#Description: This code will use Flask to generate the pictures that will be displayed.

from flask import Flask, render_template, url_for
from flask_bootstrap import Bootstrap
from PIL import Image
import os, random, pickle, image_info

# Read in info from image_info
info = image_info.image_info

# Initalizes flask server with bootstrap4 (psst, we went above and beyond by using animate css and a material design)
app = Flask(__name__)
Bootstrap(app)

# Display three random images from /img directory
@app.route('/', methods=["GET"])
def index():
    imgs = os.listdir("static/picture")
    img1 = imgs.pop(random.randrange(0, len(imgs) - 1))
    img2 = imgs.pop(random.randrange(0, len(imgs) - 1))
    img3 = imgs.pop(random.randrange(0, len(imgs) - 1))
    return render_template('index.html', listy=[img1, img2, img3])

# Renders page based on provided image id as url parameter
# Depends on image_info.py from instructor
@app.route('/picture/<img_id>', methods=['GET'])
def get_img(img_id):
    try:
        for i in info:
            if i["id"] == img_id.split(".")[0]:
                temp = Image.open("static/picture/" + img_id)
                res = {
                    "id": img_id,
                    "title": i["title"],
                    "auth": i["flickr_user"],
                    "mode": temp.mode,
                    "width": temp.size[0],
                    "height": temp.size[1],
                    "format": temp.format
                }
                return render_template('img.html', info=res, linky=url_for('index'))

        # Image not found, throw exception
        raise ValueError()
    except ValueError as v:
        print("image not found", img_id, v)
    except Exception as e:
        print("issue with indexing on", img_id, e)
    return render_template('404.html', linky=url_for('index'))

# Yes, we have a 404 to yeet the visitor to
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html', linky=url_for('index')), 404

# Start the web server in debug mode
if __name__ == "__main__":
    app.run(debug=True)