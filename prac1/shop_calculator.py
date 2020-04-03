totalPrice = []
number_of_items = int(input("Enter the number of items:"))
while number_of_items <= 0:
    print("error")
    number_of_items = int(input("Enter the correct number"))
for i in range(number_of_items):
    price = float(input("Price of item:"))
    totalPrice.append(price)
    total = sum(totalPrice)
if total > 100:
    totalCost = total - (total * 10 / 100)
    totalCost = round(totalCost, 2)
    print("Total price for " + str(number_of_items) + " items is " + str(totalCost))
else:
    print("Total price for " + str(number_of_items) + " items is " + str(total))
