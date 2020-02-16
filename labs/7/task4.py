import math
import numpy as np
from PIL import Image 
from colormath.color_objects import sRGBColor, LabColor
from colormath.color_conversions import convert_color
from colormath.color_diff import delta_e_cie2000

"""
Task 4:
    - Create a chroma key photo.
    - Steps:
        - grab pixel from background
        - make background different with chroma key
        - use delta function to compare pixels
        - display newly created image
"""
def distance(color_1, color_2):
	color1_rgb = sRGBColor(color_1[0],color_1[1],color_1[2], True)
	color2_rgb = sRGBColor(color_2[0],color_2[1],color_2[2], True)

	color1_lab = convert_color(color1_rgb, LabColor)
	color2_lab = convert_color(color2_rgb, LabColor)

	return delta_e_cie2000(color1_lab, color2_lab)

def main():
    print("Enter green/blue image path:")
    img1 = Image.open(input().strip(), 'r')
    print("Enter background image path:")
    img2 = Image.open(input().strip(), 'r')

    for x in range(img1.width):
    	for y in range(img1.height):
    		cur_pixel = img1.getpixel((x,y))
    		green = (0, 190, 60)
    		if distance(cur_pixel, green) < 100:
    			img1.putpixel((x,y), img2.getpixel((x,y)))

    img1.show()


if __name__ == "__main__":
    main()