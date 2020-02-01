def task1():
    return {
        "red": (255, 0, 0),
        "blue": (0, 0, 255),
        "green": (0, 128, 0),
        "magenta": (255, 0, 255),
        "cyan": (0, 255, 255),
        "yellow": (255, 255, 0)
        }

def task2(cd):
    print("The blue channel of magenta has a value of:", cd.get("magenta")[2])
    print("The green channel of yellow has a value of:", cd.get("yellow")[1])
    print("The red channel of cyan has a value of:", cd.get("cyan")[0])
    print("The RGB tuples of any colors in color_dictionary whose second letter is 'e' are as follows.")
    for color in color_dictionary:
    	if color[1] == 'e':
    		print(color_dictionary[color])

def task3():
    tineye_sample = {
        "status": "ok",
        "error": [],
        "method": "extract_collection_colors",
        "result": [
            {
                "color": (141, 125, 83),
                "weight": 76.37,
                "name": "Clay Creek",
                "rank": 1,
                "class": "Grey"
            },
            {
                "color": (35, 22, 19),
                "weight": 23.63,
                "name": "Seal Brown",
                "rank": 2,
                "class": "Black"
            }
        ]
    }
    print("The red channel of Clay Creek is:", tineye_sample.get("result")[0].get("color")[0])
    print("The blue channel of Seal Brown is:", tineye_sample.get("result")[1].get("color")[2])

def task4():
    print("Lab 2 was completed successfully, no need to work on it for this lab")

if __name__ == '__main__':
    color_dictionary = task1()
    task2(color_dictionary)
    task3()
    task4()
    exit(0)
