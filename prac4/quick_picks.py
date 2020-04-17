import random

def main():
    quick = int(input("How many quick picks? "))
    for i in range(quick):
        list=[random.randint(1,45) for i in range (6)]
        list.sort()
        for count in range(0, len(list)):
            print(list[count], end =" ".center(1))

        print("".center(1))



main()