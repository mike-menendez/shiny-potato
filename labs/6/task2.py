from PIL import Image

print("Enter image path:")

im = Image.open(input().strip())

print("creating a sunset...")

new_list = map(lambda a : (int(a[0]), int(a[1]*0.15), int(a[2]*0.15)), im.getdata())

im.putdata(list(new_list))

im.show()