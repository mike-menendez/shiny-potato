import math
from PIL import Image 

"""
Task 3:
    - Create a chroma key photo.
    - Steps:
        - grab pixel from background
        - make background different with chroma key
        - display newly created image
"""
def distance(color_1, color_2):
	red_diff = math.pow((color_1[0] - color_2[0]), 2)
	green_diff = math.pow((color_1[1] - color_2[1]), 2)
	blue_diff = math.pow((color_1[2] - color_2[2]), 2)
	return math.sqrt(red_diff + green_diff + blue_diff)

def main():
    print("Enter green/blue image path:")
    img1 = Image.open(input().strip(), 'r')
    print("Enter background image path:")
    img2 = Image.open(input().strip(), 'r')

    for x in range(img1.width):
    	for y in range(img1.height):
    		cur_pixel = img1.getpixel((x,y))
    		green = (0, 190, 60)
    		if distance(cur_pixel, green) < 150:
    			img1.putpixel((x,y), img2.getpixel((x,y)))

    img1.show()


if __name__ == "__main__":
    main()