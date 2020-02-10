#Authors: Mike Menendez and Cassandra Cabrera
#The purpose of this code is to read in the pixel digits and create the 
#Mona Lisa picture using Pillow.
from PIL import Image
import numpy as np


def main():
    # mona = Image.open("mona.dat", "1")
    d = []
    f = open(file="mona.dat", mode="r") #read in from file
    temp = f.readlines()
    #create list of pixels
    for x in temp:
        d.append([int (i) for i in x.replace(";", "").strip().split(" ")])

    d = np.array(d)
    d = d.astype(np.uint8)
    print(d)
    mona = Image.fromarray(d)

    mona.show(title="Mona") #show image

if __name__ == "__main__":
    main()
