"""
Odd numbers between 1 and 20
"""

for i in range(1, 21, 2):
    print(i, end=" ")

"""
countdown in 10s from 0 to 100
"""
print()
for i in range(0, 101, 10):
    print(i, end=" ")

"""
countdown from 20 to 1
"""
print()
for i in range(20, 0, -1):
    print(i, end=" ")

"""
Stars
"""
print()
stars = int(input("Number of stars: "))
print(stars * "*")
for i in range(stars + 1):
    print(i * "*")
