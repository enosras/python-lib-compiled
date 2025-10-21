import os
import time
from platform import release


def sleepy(timing):
    #timing = int(input(print("enter preferred sleep duration : ")))
    time.sleep(timing)
def print_hi():

    print(f'Hi obunga')  # Press ⌘F8 to toggle the breakpoint.

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    #obunga = input(print(f'enter name\n'))
    print_hi()
    #timing = int(input(print("enter preferred sleep duration : ")))
    sleepy(3)
    #time.sleep(5)
    print(os.getuid())
    #time.sleep(3)
  #  timing = int(input(print("enter preferred sleep duration : ")))
   # sleepy(timing)
    print(os.name)
    #timing = int(input(print("enter preferred sleep duration : ")))
   # sleepy(timing)
    print(os.path)
    print(os.P_PID)
    print(os.environ)
    print(os.getppid())
    print(os.uname())




# See PyCharm help at https://www.jetbrains.com/help/pycharm/
