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
    for x in img.height:
        for y in img.width:
            if img.get_pixel(x, y)[0] in mappy.keys():
                mappy.get(img.get_pixel(x, y)[0]).append((x, y))
            else:
                mappy[(img.get_pixel(x, y)[0])] = [(x, y)]

    print("Coordinates of all pixels with the max red channel: ", mappy.get(mappy.keys().sort().reverse()[0]))


if __name__ == "__main__":
    main()
