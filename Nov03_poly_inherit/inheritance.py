class Vehicle :

    def __init__(self, make, model, year):
        self._make = make
        self._model = model
        self._year = year
    
    def __str__(self):
        pass

    def start(self):
        print("Starting...")

    def stop(self):
        print("Stopping...")

class Car(Vehicle):

    def __init__(self, make, model, year, num_doors):
        super().__init__(make, model, year)
        self._num_doors = num_doors

    def __str__(self):
        return f"I m a {self._make} {self._model} produced in {self._year} with {self._num_doors} doors"       

    def honk_horn(self):
        print("Honking the horn with champions style!")

    def fuel_up(self):
        print("I m fueling the depo!")        

class Bicycle(Vehicle):

    def __init__(self, make, model, year, num_gears):
        super().__init__(make, model, year)
        self._num_gears = num_gears

    def __str__(self):
        return f"I m a {self._make} {self._model} produced in {self._year} with {self._num_gears} gears"       
    
    def ring_bell(self):
        print('Ringing the bell but for whom!')

    def lock_into_parking_lot(self):
        print("Locking it into parking lot!")

class Motorcycle(Vehicle):

    def __init__(self, make, model, year, num_gears):
        super().__init__(make, model, year)
        self._num_gears = num_gears

    def __str__(self):
        return f"I m a {self._make} {self._model} produced in {self._year} with {self._num_gears} gears"       
  
    def park(self):
        print("Parking the motorcycle!")

def main():
    car1 = Car("Toyota", "Corolla RT5", 2322, 4)
    car2 = Car("Saab", "Vesteros 11", 2307, 2)
    bike = Bicycle("Trek", "Mania-3400", 2330, 24)
    moto = Motorcycle("BMW", "Tysk-tr520", 2314, 8)

    print(car1)
    print(car2)
    print(bike)
    print(moto)
    car1.fuel_up()
    car2.honk_horn()
    bike.ring_bell()
    moto.park()

if __name__ == '__main__':
    main()



