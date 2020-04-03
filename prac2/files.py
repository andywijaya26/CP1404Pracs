"""
Write the name into the file
"""

namelist="name.txt"
name_file=open(namelist,'w')

username=input("Please enter your name: ")
print("{}".format(username),file=name_file)

name_file.close()



"""
Write the name from the file
"""
name_file=open(namelist,'r')
read_the_name=name_file.read()
print("Your name is {}".format(read_the_name))

name_file.close()

"""
Number
"""
numberlist="numbers.txt"
number_list=open(numberlist,'r')
number1=int(number_list.readline())
number2=int(number_list.readline())
total_number=number1+number2
print(total_number)

number_list.close()

"""
Total of all numbers
"""
total1 =0
number_list=open(numberlist,'r')
total1 =0
for line in number_list:
    number=int(line)
    total1 +=number
number_list.close()
print(total1)



