"""
Basic list operations

"""

def main():
    numbers=[]
    for i in range (5):
        number=int(input("Number:"))
        numbers.append(number)
        total=sum(numbers)
        numbers_total=len(numbers)
        average=total/numbers_total
    print("The fist number is ",numbers[0])
    print("The last number is ", numbers[-1])
    print("The smallest number is",min(numbers))
    print("The largest number is", max(numbers))
    print("The average of those numbers is",average )

main()

"""
Woefully inadequate security checker
"""

usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface', 'BaseStdIn', 'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']

username=input("Please enter your username: ")
if username in usernames:
    print("Access granted")
else:
    print("Access denied")
