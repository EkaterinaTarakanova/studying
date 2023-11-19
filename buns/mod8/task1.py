class Transport():
    def __init__(self, coordinates, speed, brand, year, number, *args):
        self.coordinates = coordinates
        self.speed = speed
        self.brand = brand
        self.year = year
        self.number = number

    @property
    def coordinates(self):
        return self._coordinates

    @coordinates.setter
    def coordinates(self, coordinates):
        if not isinstance(coordinates, int):
            raise TypeError("Координаты должны быть целым числом")
        self._coordinates = coordinates

    @property
    def speed(self):
        return self._speed

    @speed.setter
    def speed(self, speed):
        if not isinstance(speed, int):
            raise TypeError("Скорость должна быть целым числом")
        elif speed < 0:
            raise ValueError("Скорость должна быть больше нуля")
        self._speed = speed

    @property
    def brand(self):
        return self._brand

    @brand.setter
    def brand(self, brand):
        if not isinstance(brand, str):
            raise TypeError("Название бренда должно быть строкой")
        self._brand = brand

    @property
    def year(self):
        return self._year

    @year.setter
    def year(self, year):
        if not isinstance(year, int):
            raise TypeError("Год должен быть целым числом")
        elif year < 0:
            raise ValueError("Год не может быть отрицательным")
        self._year = year

    @property
    def number(self):
        return self._number

    @number.setter
    def number(self, number):
        if not isinstance(number, int):
            raise TypeError("Значение должно быть целочисленным")
        elif number < 0:
            raise ValueError("Значение не может быть меньше нуля")
        self._number = number

    def __str__(self):
        '''
           Представление всей информации для вывода в методе print()
        '''
        return f'{self.coordinates}, {self.speed}, {self.brand}, {self.year}, {self.number}'

    def isInArea(self, pos_x, pos_y, length, width) -> bool:
        '''
        Присутствие транспортного средства в пределах заданнй области
        pos_x, pos_y - координата левого верхнего угла области
        length, width - длина и ширина области
        '''
        x, y = self.coordinates
        if (pos_x <= x <= pos_x + length and pos_y <= y <= pos_y + width):
            return True
        return False

class Passenger():
    @property
    def passengers_capacity(self):
        return self.__passengers_capacity

    @passengers_capacity.setter
    def passengers_capacity(self, passengers_capacity):
        if isinstance(passengers_capacity, int) and passengers_capacity > 0:
            self.__passengers_capacity = passengers_capacity
        else:
            TypeError("Вместимость должна быть целым положительным числом")

    @property
    def number_of_passengers(self):
        return self.__number_of_passengers

    @number_of_passengers.setter
    def number_of_passengers(self, number_of_passengers):
        if isinstance(number_of_passengers, int) and number_of_passengers > 0 and number_of_passengers <= self.passengers_capacity:
            self.__number_of_passengers = number_of_passengers
        else:
            raise ValueError("Количество пассажиров - целое положительное число, не превышающее вместимость")

class Cargo():
    @property
    def carrying(self):
        return self.__carrying

    @carrying.setter
    def carrying(self, carrying):
        if carrying > 0:
            self.__carrying = carrying
        else:
            raise ValueError("Грузоподъёмность не может быть отрицательной")

class Plane(Transport):
    def __init__(self, *args):
        self.height = height
        super().__init__(self, *args)

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        if isinstance(height, int) and height >= 0:
            self.__height = height
        else:
            raise ValueError("Высота полёта должна быть целым неотрицательным числом")

class Auto(Transport):
    def __init__(self, model, *args):
        self.model = model
        super().__init__(*args)

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, model):
        if isinstance(model, str):
            self.__model = model
        else:
            raise TypeError("Название модели должно быть строкой")

class Ship(Transport):
    def __init__(self, port, *args):
        self.port = port
        super().__init__(*args)

    @property
    def port(self):
        return self.__port

    @port.setter
    def port(self, port):
        if isinstance(port, str):
            self.__port = port
        else:
            raise ValueError("Название порта должно быть строкой")

class Car(Auto):
    def __init__(self, fuel, *args):
        self.fuel = fuel
        super()._init__(*args)

    @property
    def fuel(self):
        return self.__fuel

    @fuel.setter
    def fuel(self, fuel):
        if not isinstance(fuel, int) and not isinstance(fuel, float):
            raise TypeError("Расход топлива должен быть числом")
        elif fuel < 0:
            raise ValueError("Расход топлива должен быть больше нуля")
        self.__fuel = fuel

class Bus(Auto, Passenger):
    def __init__(self, weight, model, passangers_capacity, number_of_passangers, *args):
        self.weight = weight
        Auto.__init__(model, *args)
        Passenger.__init__(passangers_capacity, number_of_passangers)

    @property
    def weight(self):
        return self.__weight

    @weight.setter
    def weight(self, weight):
        if not isinstance(weight, int):
            raise TypeError("Масса автобуса должна быть числом")
        elif weight < 0:
            raise ValueError("Масса автобуса не может быть отрицательной")
        self.__weight = weight

class CargoAuto(Auto, Cargo):
    def __init__(self, cargo_weight, carrying, *args):
        self.cargo_weight = cargo_weight
        Auto.__init__(self,*args)
        Cargo.__init__(self, carrying)

    @property
    def cargo_weight(self):
        return self.__cargo_weight

    @cargo_weight.setter
    def cargo_weight(self, cargo_weight):
        if not isinstance(cargo_weight, int) and not isinstance(cargo_weight, float):
            raise TypeError("Вес груза должен быть числом")
        elif cargo_weight < 0:
            raise ValueError("Вес груза не может быть меньше нуля")
        self.__cargo_weight = cargo_weight

class Boat(Ship):
    def __init__(self, color, *args):
        self.color = color
        super().__init__(self, *args)

    @property
    def color(self):
        return self.__color

    @color.setter
    def color(self, color):
        if not isinstance(color, str):
            raise TypeError("Название цвета должно быть строкой")
        self.__color = color

class PassengerShip(Ship, Passenger):
    def __init__(self, name, passangers_capacity, number_of_passangers, *args):
        self.name = name
        Ship.__init__(self, *args)
        Passenger.__init__(self, passangers_capacity, number_of_passangers)

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if not isinstance(name, str):
            raise TypeError("Название должно быть строкой")
        self.__name = name

class CargoShip(Ship, Cargo):
    def __init__(self, name, carrying, *args):
        self.name = name
        Ship.__init__(self, *args)
        Cargo.__init__(self, carrying, *args)

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if not isinstance(name, str):
            raise TypeError("Название должно быть строкой")
        self.__name = name

class Airplane(Plane):
    def __init__(self, model, *args):
        self.model = model
        super().__init__(self, *args)

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, model):
        if not isinstance(model, str):
            raise TypeError("Название модели должно быть строкой")
        self.__model = model

class PassangerPlane(Plane, Passenger):
    def __init__(self, max_flight, passangers_capacity, number_of_passangers, *args):
        self.max_flight = max_flight
        Passenger.__init__(self, passangers_capacity, number_of_passangers)
        Plane.__init__(self, *args)

    @property
    def max_flight(self):
        return self.__max_flight

    @max_flight.setter
    def max_flight(self, max_flight):
        if not isinstance(max_flight, int) and not isinstance(max_flight, float):
            raise TypeError("Максимальная высота должна быть числом")
        elif max_flight < 0:
            raise ValueError("Максимальная выоста не должна быть неотрицательным числом")
        self.__max_flight = max_flight

class CargoPlane(Plane, Cargo):
    def __int__(self, carrying, *args):
        Plane.__init__(self, *args)
        Cargo.__init__(self, carrying)

    @property
    def cargo_weight(self):
        return self.__cargo_weight

    @cargo_weight.setter
    def cargo_weight(self, cargo_weight):
        if not isinstance(cargo_weight, int) and not isinstance(cargo_weight, float):
            raise TypeError("Вес груза должен быть числом")
        elif cargo_weight < 0:
            raise ValueError("Вес груза не может быть меньше нуля")
        self.__cargo_weight = cargo_weight

class Seaplane(Plane, Ship):
    def __init__(self, displacement, port, height, *args):
        self.displacement = displacement
        Ship.__port = port
        Plane.__height = height

    @property
    def displacement(self):
        return self.__displacement

    @displacement.setter
    def displacement(self, displacement):
        if not (isinstance(displacement, int) and not isinstance(displacement, float)):
            raise TypeError("Водоизмещение должно быть числом")
        elif displacement < 0:
            raise ValueError("Водоизмещение не должно быть отрицательным")
        self.__displacement = displacement


