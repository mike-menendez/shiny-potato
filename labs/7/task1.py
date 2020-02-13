import math
from PIL import Image
def color_distance2(c1, c2):
 val = 0
 for i in range(3):
 	val += math.pow((c1[i]-c2[i]), 2)
 return math.sqrt(val)


im = Image.open("/Users/casscabrera/Desktop/bruns.jpg")
color_to_change = (58, 71, 36)
# using list comprehension
new_list = [ (int(p[0]*1.5), int(p[1]*.5), p[2]) for p in 
im.getdata() if color_distance2(p, color_to_change) ]
im.putdata(new_list)
im.show()