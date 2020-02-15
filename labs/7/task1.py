from PIL import Image

"""
Task 1:
    - Return a coordinate of a pixel with the highest red value (can be multiple, just return one)
    - Steps:
        - Read in image
        - Traverse Image as if it were a 3D matrix (x, y, 0 (where 0 = red channel in rgb tuple))
        - Create hashmap to store values based off red value (dynamic programming bruh :fire:)
        - Get keys from hashmap, reverse sort and display the list of the max value
"""


def main():
    print("Enter file path:")
    img = Image.open(input().strip(), 'r')
    mappy = {}
    maxxR = 0
    coor = (0,0)
    for x in range(img.width):
        for y in range(img.height):
            if img.getpixel((x,y))[0] > maxxR:
                maxxR = x
                coor = (x,y)
    print("Coordinate of pixel with the max red channel: ", coor)


if __name__ == "__main__":
    main()