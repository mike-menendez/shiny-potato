#Adding async support
import asyncio


async def task_master():
    Task()


class Task:
    # Member variables of the Task object
    task, red, green, blue, hex = "", 0, 0, 0, 0

    # Init the passed Task object's RGB members
    @staticmethod
    def rgb_setup(self):
        fmt = False
        while not fmt:
            try:
                print("Please enter the RGB tuple with each color separated with the return carriage")
                self.red, self.green, self.blue = int(input()), int(input()), int(input())
                fmt = True
            except:
                print("Invalid format, please try again")

    # Init the passed Task object's hex member
    @staticmethod
    def hex_setup(self):
        fmt = False
        while not fmt:
            try:
                print("Please enter the hexadecimal color string in standard format (ex: #FFFFFF)")
                self.hex = input().strip()[1:]
                fmt = True
            except:
                print("Invalid format, please try again")

    # Fulfills task1 of the assignment
    # Checks if a RGB tuple is a primary color
    @staticmethod
    def task1(self):
        if self.green < self.red > self.blue:
            print("The color is reddish")

        elif self.blue < self.green > self.red:
            print("The color is greenish")

        else:
            print("The color is blueish")

    # Fulfills task 2 of the assignment
    # Checks if a RGB tuple is a secondary color
    @staticmethod
    def task2(self):
        if self.red == self.blue:
            print("The color is a shade of magenta")

        elif self.red == self.green:
            print("The color is a shade of yellow")

        elif self.blue == self.green:
            print("The color is a shade of cyan")

    # Fulfills task 3 of the assignment
    # Converts hex string to RGB tuple
    @staticmethod
    def task3(self):
        print()

    # Fulfills task 4 of the assignment
    # Converts RGB tuple to hex
    @staticmethod
    def task4(self):
        print()

    # Given any RGB tuple, can determine the hue of the tuple whether it be a primary or secondary color
    @staticmethod
    def task5(self):
        if self.red == self.green or self.red == self.blue or self.blue == self.green:
            self.task2(self)
        else:
            self.task1(self)

    # Init of the Task object and calls helper functions to handle the specified task
    def __init__(self):
        super().__init__()
        valid = False
        while not valid:
            try:
                print("Please enter task number:")
                self.task = int(input())
                valid = True
            except:
                print("Invalid format, please try again")

        if self.task == 1:
            self.rgb_setup(self)
            self.task1(self)

        elif self.task == 2:
            self.rgb_setup(self)
            self.task2(self)

        elif self.task == 3:
            self.hex_setup(self)
            self.task3(self)

        elif self.task == 4:
            self.task4(self)

        elif self.task == 5:
            self.task5(self)
        else:
            print("Error, invalid input")
            exit(69)


# Creates the main Task object which handles processing of a given RGB tuple or Hex color string
# noinspection PyTypeChecker
async def main():
    await asyncio.create_task(task_master())


if __name__ == '__main__':
    asyncio.run(main())
    exit(0)
