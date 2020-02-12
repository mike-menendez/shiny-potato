from PIL import Image, ImageOps


print("Enter image path:")

im = Image.open(input().strip())

print("negating image...")

inv1 = ImageOps.invert(im)

inv1.show()

print("double negation...")

inv2 = ImageOps.invert(inv1)

inv2.show()
