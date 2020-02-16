import seaborn as sns
import pickle as pk
import matplotlib.pyplot as plt


def read_in():
    print("Enter file path for data source:")
    return pk.load(open(input().strip(), "rb"))


def sorting(m):
    return {
        "red" : sorted(m.get('red')),
        "green": sorted(m.get('green')),
        "blue": sorted(m.get('blue'))
    }


def task1():
    dat = read_in()
    mappy = {
        0: [0, 0, 0, 0],
        1: [0, 0, 0, 0],
        2: [0, 0, 0, 0]
    }
    for x in range(len(dat)):
        for y in range(len(dat[0])):
            for z in range(0, 3):
                if dat[x][y][z] in range(0, 63):
                    mappy[z][0] = mappy[z][0] + 1
                elif dat[x][y][z] in range(64, 127):
                    mappy[z][1] = mappy[z][1] + 1
                elif dat[x][y][z] in range(128, 191):
                    mappy[z][2] = mappy[z][2] + 1
                else:
                    mappy[z][3] = mappy[z][3] + 1

    return {
        "red": mappy[0],
        "green": mappy[1],
        "blue": mappy[2]
    }


def task2(m):
    print("Sorted map: ", sorting(m))
    print("keys: ", m.keys())
    for key in m.keys():
        sns.countplot(data=m.get(key), color=key, x='intensity')
        plt.title(label=key, loc='center')
        plt.show()


def main():
    mappy = task1()
    print("Task 1:", mappy)
    task2(mappy)


if __name__ == "__main__":
    main()
