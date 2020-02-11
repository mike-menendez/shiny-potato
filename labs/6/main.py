import asyncio
import uvloop
import PIL
import os
import time


async def task_master():
    Task()


class Task:
    # Member variables of the Task object
    path, task, img = "", "", ""

    @staticmethod
    def sAsSyCoMmEnTaRy():
        print("Ready?")
        time.sleep(.6)
        print("Set?")
        time.sleep(.5)
        print("Go!")
        time.sleep(.4)

    @staticmethod
    async def negate(self):
        self.img = PIL.ImageOps.invert(self.img)

    @staticmethod
    async def img_init(self):
        self.img = PIL.Image.open(self.path)
        return

    # Fulfills task1 of the assignment
    # Creates double negative
    @staticmethod
    async def task1(self):
        # Creating coroutine tasks for double inversion
        inv1 = asyncio.create_task(self.negate(self))
        inv2 = asyncio.create_task(self.negate(self))

        print("Inverting image in background thread for the first time...")
        await inv1
        print("Finished first inversion!")
        print("Starting second inversion in a background thread...")
        await inv2
        print("Finished second inversion!")
        print("Now displaying image...")
        self.img.open()

    # Fulfills task 2 of the assignment
    @staticmethod
    async def task2(self):
        scalar = int(input().strip())
        print("Creating filter in background thread...")
        # Create generic masking based off of the image dimensions
        print("Applying filter in background thread...")
        # Apply filter
        print("Now displaying new image!")

    # Fulfills task 3 of the assignment
    @staticmethod
    async def task3(self):
        print("We completed Mona, no need to work on it")

    # Init of the Task object and calls helper functions to handle the specified task
    def __init__(self):
        if not os.environ.get('DEV'):
            self.sAsSyCoMmEnTaRy()
        valid = False
        while not valid:
            try:
                print("Please enter task number:")
                self.task = int(input().strip())
                print("Please enter image path: ")
                self.path = input().strip()
                valid = True
            except:
                print("Invalid format, please try again")

        if self.task == 1:
            asyncio.run(self.imgInit(self))
            self.task1(self)

        elif self.task == 2:
            asyncio.run(self.imgInit(self))
            self.task2(self)

        elif self.task == 3:
            asyncio.run(self.imgInit(self))
            self.task3(self)

        else:
            print("Error, invalid input")
            exit(69)


async def main():
    await asyncio.create_task(Task(), debug=not os.environ.get('DEV'))


if __name__ == '__main__':
    # Switch to C event loop policy for better throughput
    print("NoW pRePaRiNg To Go AbOvE aNd BeYoNd")
    time.sleep(1)
    print("Setting binding to libuv...")
    time.sleep(.9)
    asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())
    time.sleep(.8)
    print("Instantiating event loop with C binding for higher performance....")
    time.sleep(.7)
    asyncio.run(main())
    exit(0)
