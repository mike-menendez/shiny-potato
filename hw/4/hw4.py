from flask import Flask, render_template
from flask_bootstrap import Bootstrap
import os, random

# Initalizes flask server with bootstrap4 since can't use mdbootstrap (cst 205 :eye_roll:)
app = Flask(__name__)
Bootstrap(app)

# Generates sudo enum mapping based on images in child directory
def map_gen():
    temp = os.listdir("picture")
    dict = {}
    for i in range(0, len(temp)):
        dict[i] = temp[i]
    return dict

# Display three random images from /img directory
@app.route('/', methods=["GET"])
def index():
    dict = map_gen()
    img1 = dict.pop(random.randrange(0, len(dict.keys())))
    img2 = dict.pop(random.randrange(0, len(dict.keys())))
    img3 = dict.pop(random.randrange(0, len(dict.keys())))
    return render_template('base.html', listy=[img1, img2, img3])

# TODO: Renders page based on provided image id as url parameter
# TODO: Depends on image_info.py from instructor?????
@app.route('/picture/<img_id>', methods=['GET'])
def get_img(img_id):
    pass

# Start the web server in debug mode
if __name__ == "__main__":
    app.run(debug=True)