from PIL import Image
im = Image.open("/Users/casscabrera/Desktop/CST205/download2.jpeg")
def negative_image(pixel):
	return tuple(map(lambda a : 255 - a, pixel))
negative_list = map(negative_image, im.getdata() )
im.putdata(list(negative_list))
im.show()