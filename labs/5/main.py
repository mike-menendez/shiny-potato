from PIL import Image
import numpy as np


def main():
    # mona = Image.open("mona.dat", "1")
    d = []
    f = open(file="mona.dat", mode="r")
    temp = f.readlines()
    for x in temp:
        d.append([int (i) for i in x.replace(";", "").strip().split(" ")])

    d = np.array(d)
    d = d.astype(np.uint8)
    print(d)
    mona = Image.fromarray(d)

    mona.show(title="Mona")

if __name__ == "__main__":
    main()
