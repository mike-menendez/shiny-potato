from PIL import Image

"""
Task 2:
    - Pick three (small) images and place them on a blank canvas such that they do not overlap.
    - Steps:
        - Read in images
        - Traverse images one by one, plotting their pixels.
        - Print Newly created image
"""

def main():
    print("Enter first image path:")
    img1 = Image.open(input().strip(), 'r')
    print("Enter second image path:")
    img2 = Image.open(input().strip(), 'r')
    print("Enter third image path:")
    img3 = Image.open(input().strip(), 'r')

    canvas_x = img1.width + img2.width + img3.width
    canvas = Image.new("RGB", (canvas_x,img1.height), "white")

    target_x = 0
    for source_x in range(img1.width):
    	target_y = 0
    	for source_y in range(img1.height):
    		color = img1.getpixel((source_x, source_y)) 
    		canvas.putpixel((target_x, target_y), color)
    		target_y += 1
    	target_x +=1

    for source_x in range(img2.width):
    	target_y = 0
    	for source_y in range(img2.height):
    		color = img1.getpixel((source_x, source_y)) 
    		canvas.putpixel((target_x, target_y), color)
    		target_y += 1
    	target_x +=1

    for source_x in range(img3.width):
    	target_y = 0
    	for source_y in range(img3.height):
    		color = img1.getpixel((source_x, source_y)) 
    		canvas.putpixel((target_x, target_y), color)
    		target_y += 1
    	target_x +=1

    canvas.show()

    


if __name__ == "__main__":
    main()