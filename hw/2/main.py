from PIL import Image
import os 
# HW: Temporal Processing of Images
# Steps:
#   - Read in all images
#   - Create a list for each pixel location
#   - Create a new image with largest combined dimensions (largest: x, y)
#   - Insert the mode value from each list into the new image

def generate_res(imgs):
    res = []

def aggregate(imgs):
    aggr = []
    tmp = (0, 0, 0)
    for i in len(imgs):
        for x in range(i.width):
            for y in range(i.height):
                aggr[i].append(i.getpixel(x,y))
    return aggr


def readin():
    imgs = []
    for f in os.listdir(input("Please enter path to images").strip()):
        print("Opening image: ", f)
        imgs.append(Image.open(f))
    return imgs

def main():
    imgs = readin()
    # imgs = padding(imgs) # this function should create additional padding values of (0, 0, 0) for uniform image shape if we really need it
    imgs = aggregate(imgs)
    result = generate_res(imgs)



if __name__ == "__main__":
    main()