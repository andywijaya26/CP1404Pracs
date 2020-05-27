from car import Car


def main():
    my_car = Car("limo",100)
    my_car.add_fuel(20)
    my_car.drive(100)
    print("fuel =", my_car.fuel)
    print("odo =", my_car.odometer)
    print(my_car)

    print("Car {}, {}".format(my_car.fuel, my_car.odometer))
    print("Car {self.fuel}, {self.odometer}".format(self=my_car))


main()