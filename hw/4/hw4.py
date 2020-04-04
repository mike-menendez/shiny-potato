from flask import Flask, render_template, url_for
from flask_bootstrap import Bootstrap
from PIL import Image
import os, random, pickle

# Read in info from image_info
info = [
     {
           "id" : "34694102243_3370955cf9_z",
           "title" : "Eastern",
           "flickr_user" : "Sean Davis",
           "tags" : ["Los Angeles", "California", "building"]
      },
      {
           "id" : "37198655640_b64940bd52_z",
           "title" : "Spreetunnel",
           "flickr_user" : "Jens-Olaf Walter",
           "tags" : ["Berlin", "Germany", "tunnel", "ceiling"]
      },
      {
           "id" : "36909037971_884bd535b1_z",
           "title" : "East Side Gallery",
           "flickr_user" : "Pieter van der Velden",
           "tags" : ["Berlin", "wall", "mosaic", "sky", "clouds"]
      },
      {
           "id" : "36604481574_c9f5817172_z",
           "title" : "Lombardia, september 2017",
           "flickr_user" : "Mónica Pinheiro",
           "tags" : ["Italy", "Lombardia", "alley", "building", "wall"]
      },
      {
           "id" : "36885467710_124f3d1e5d_z",
           "title" : "Palazzo Madama",
           "flickr_user" : "Kevin Kimtis",
           "tags" : [ "Rome", "Italy", "window", "road", "building"]
      },
      {
           "id" : "37246779151_f26641d17f_z",
           "title" : "Rijksmuseum library",
           "flickr_user" : "John Keogh",
           "tags" : ["Amsterdam", "Netherlands", "book", "library", "museum"]
      },
      {
           "id" : "36523127054_763afc5ed0_z",
           "title" : "Canoeing in Amsterdam",
           "flickr_user" : "bdodane",
           "tags" : ["Amsterdam", "Netherlands", "canal", "boat"]
      },
      {
           "id" : "35889114281_85553fed76_z",
           "title" : "Quiet at dawn, Cabo San Lucas",
           "flickr_user" : "Erin Johnson",
           "tags" : ["Mexico", "Cabo", "beach", "cactus", "sunrise"]
      },
      {
           "id" : "34944112220_de5c2684e7_z",
           "title" : "View from our rental",
           "flickr_user" : "Doug Finney",
           "tags" : ["Mexico", "ocean", "beach", "palm"]
      },
      {
           "id" : "36140096743_df8ef41874_z",
           "title" : "Someday",
           "flickr_user" : "Thomas Hawk",
           "tags" : ["Los Angeles", "Hollywood", "California", "Volkswagen", "Beatle", "car"]
      }
]

# Initalizes flask server with bootstrap4 since can't use mdbootstrap (cst 205 :eye_roll:)
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

# TODO: Renders page based on provided image id as url parameter
# TODO: Depends on image_info.py from instructor?????
@app.route('/picture/<img_id>', methods=['GET'])
def get_img(img_id):
    try:
        for i in info:
            if i["id"] == img_id:
                temp = Image.open("picture/" + i["id"])
                res = {
                    "id": i["id"],
                    "title": i["title"],
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
    exit(1)

# Start the web server in debug mode
if __name__ == "__main__":
    app.run(debug=True)