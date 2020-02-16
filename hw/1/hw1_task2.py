import seaborn as sns
import pickle as pk
import matplotlib.pyplot as plt
from hw1_hist_plotter import hist_plotter as hp
def read_in():
    print("Enter file path for data source:")
    return pk.load(open(input().strip(), "rb"))

def sorting(m):
    return {
        "red" : sorted(m.get('red')),
        "green": sorted(m.get('green')),
        "blue": sorted(m.get('blue'))
    }

def task2(m):
	red = []
	green = []
	blue = []
	for x in range(len(m)):
		for y in range(len(m[0])):
			red.append(m[x][y][0])
			green.append(m[x][y][1])
			blue.append(m[x][y][2])
	red.sort()
	green.sort()
	blue.sort()
	return [red,green,blue]

def main():
    mappy = read_in()
    hp(task2(mappy))


if __name__ == "__main__":
    main()