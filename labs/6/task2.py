from PIL import Image
im = Image.open('/Users/casscabrera/Desktop/CST205/download.jpeg')
new_list = map(lambda a : (int(a[0]), int(a[1]*0.5), int(a[2]*0.5)), im.getdata())
im.putdata(list(new_list))
im.show()