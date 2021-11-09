from abc import ABC, abstractmethod

class Vehicle(ABC):
    __x = 0
    __y = 0
    __speed = 0
    __price = None
    __year = None

    def __init__(self, speed, year, price):
        self.speed = speed
        self.year = year
        self.price = price

    @abstractmethod
    def makeSound():pass
    @abstractmethod
    def toString():pass

    def getPos(self):
        return self.__x, self.__y

    def setPos(self, x, y):
        self.__x = x
        self.__y = y

    @property
    def price(self):
        return self.__price

    @property
    def year(self):
        return self.__year

    @property
    def speed(self):
        return self.__speed

    @price.setter
    def price(self, price):
        self.__price = price
    
    @year.setter
    def year(self, year):
        self.__year = year

    @speed.setter
    def speed(self, speed):
        self.__speed = speed

class Plane(Vehicle):
    __height = 0
    __passengers = 0

    def __init__(self, speed, year, price, passengers):
        super().__init__(speed, year, price)
        self.__passengers = passengers

    @property
    def height(self):
        return self.__height

    @property
    def passengers(self):
        return self.__passengers

    @height.setter
    def height(self, height):
        self.__height = height

    @passengers.setter
    def passengers(self, passengers):
        self.__passengers = passengers
    
    def makeSound(self):
        print('Вжух!')

    def toString(self):
        return 'Скорость: ' + str(self.speed) + '\nГод выпуска: ' + str(self.year) + '\nСтоимость: ' + str(self.price) + '\nКоличество пассажиров: ' + str(self.passengers)

class Car(Vehicle):
    def __init__(self, speed, year, price):
        super().__init__(speed, year, price)
    
    def makeSound(self):
        print('Бип Бип!')

    def toString(self):
        return 'Скорость: ' + str(self.speed) + '\nГод выпуска: ' + str(self.year) + '\nСтоимость: ' + str(self.price)

class Ship(Vehicle):
    __passengers = 0
    __port = None

    def __init__(self, speed, year, price, passengers):
        super().__init__(speed, year, price)
        self.__passengers = passengers

    @property
    def port(self):
        return self.__port
        
    @property
    def passengers(self):
        return self.__passengers

    @port.setter
    def port(self, port):
        self.__port = port

    @passengers.setter
    def passengers(self, passengers):
        self.__passengers = passengers
    
    def makeSound(self):
        print('*двойной гудок*')

    def toString(self):
        return 'Скорость: ' + str(self.speed) + '\nГод выпуска: ' + str(self.year) + '\nСтоимость: ' + str(self.price) + '\nКоличество пассажиров: ' + str(self.passengers) + '\nПорт: ' + str(self.port)

def main():
    plane = Plane(800, 2004, 2_000_000, 400)
    car = Car(256, 2015, 14_000)
    ship = Ship(60, 2010, 100_000_000, 12_000)

    plane.makeSound()
    car.makeSound()
    ship.makeSound()
    print(plane.toString())

if __name__ == '__main__':
    main()