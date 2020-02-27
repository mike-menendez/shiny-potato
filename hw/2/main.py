'''
Authors: Cassandra Cabrera & Mike Menendez
Date: February 24, 2020
Professor: Wes Modes
'''
from PIL import Image
import glob
# HW 2: Temporal Processing of Images
# Steps:
#   - Read in all images
#   - Create a list for each pixel location
#   - Create a new image with largest combined dimensions (largest: x, y)
#   - Insert the median value from each list into the new image

#will iterate through the pixels of each image and find the median of the pixels
#will add the median pixel to a new "final" image
def aggregate(imgs):
	pic = Image.new("RGB", (imgs[0].width,imgs[0].height), "white")
	for x in range(imgs[0].width):
		for y in range(imgs[0].height):
			pix = []
			for i in imgs:
				pix.append(i.getpixel((x,y)))

			pix.sort()
			val = int(len(pix)/2)
			pic.putpixel((x,y), pix[val])
	pic.save("images/final.png")
	pic.show()

#uses the python Glob library to read in multiple images from a directory
#and will add them into a list
def readin():
	imgs = glob.glob("images/*")
	imgs = [Image.open(image) for image in imgs]
	return imgs

#main function will call all functions
def main():
    imgs = readin()

    aggregate(imgs)

if __name__ == "__main__":
    main()