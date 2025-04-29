# Пункт 1: (1 час 30 минут)
#
# Сделать класс перевода температуры из Цельсия в Фаренгейт.
#
# Пункт 1.1:
#
# Сделать внутри класса метод перевода Цельсия в Фаренгейт.
#
# Пункт 1.2:
#
# Сделать внутри класса метод перевода Фаренгейта в Цельсии.
#
#
# Пункт 2: (2 час 30 минут)
#
# Создать класс перевода из метрической системы в английскую.
#
# Пункт 2.1:
#
# Создать внутри класса метод перевода километров в мили и наоборот, и перевод галонов в литры, и фунты в килограммы
#
#
# Пункт 3: (3 часа 30 минут)
# Создать класс "Дробь".
#
# Пункт 3.1:
# Создать конструктор класса Дробь.
#
# Пункт 3.2:
# Создать методы для получения изменения полей класса Дробь.
#
# Пункт 3.3:
# Создать методы арифметических операций в классе.



class Temp:
    @staticmethod
    def celsius_to_fahrenheit(temp_celsius:float = 0):
        user_inp = input("Введите температуру в цельсиях: ")
        if user_inp == "":
            user_inp = temp_celsius
        result = (float(user_inp) * 9/5) + 32
        print(f"Результат перевода температуры с цельсия в фаренгейт: {result}")

    @staticmethod
    def fahrenheit_to_celsius(temp_fahrenheit:float = 0):
        user_inp = input("Введите температуру в фаренгейтах: ")
        if user_inp == "":
            user_inp = temp_fahrenheit
        result = (float(user_inp) - 32) * 5/9
        print(f"Результат перевода температуры с фаренгейта в цельсии: {result}")


# Temp.fahrenheit_to_celsius()
# Temp.celsius_to_fahrenheit()

class MetricToEnglishConverter:
    @staticmethod
    def miles_to_kilometers():
        user_inp = float(input("Введите мили: "))
        result = user_inp * 1.60934
        print(f"Результат перевода милей в километры: {result}")

    @staticmethod
    def kilometers_to_miles():
        user_inp = float(input("Введите километры: "))
        result = user_inp * 0.621371
        print(f"Результат перевода километров в мили: {result}")

    @staticmethod
    def gallons_to_liters():
        user_inp = float(input("Введите галлоны: "))
        result = user_inp * 3.78541
        print(f"Результат перевода галлонов в литры: {result}")

    @staticmethod
    def liters_to_gallons():
        user_inp = float(input("Введите литры: "))
        result = user_inp * 0.264172
        print(f"Результат перевода литров в галлоны: {result}")

    @staticmethod
    def pounds_to_kilograms():
        user_inp = float(input("Введите фунты: "))
        result = user_inp * 0.45359237
        print(f"Результат перевода фунтов в килограммы: {result}")

    @staticmethod
    def kilograms_to_pounds():
        user_inp = float(input("Введите килограммы: "))
        result = user_inp / 0.45359237
        print(f"Результат перевода килограммов в фунты: {result}")

# MetricToEnglishConverter.miles_to_kilometers()
# MetricToEnglishConverter.kilometers_to_miles()
# MetricToEnglishConverter.gallons_to_liters()
# MetricToEnglishConverter.liters_to_gallons()
# MetricToEnglishConverter.pounds_to_kilograms()
# MetricToEnglishConverter.kilograms_to_pounds()

class Fraction:
    def __init__(self, numerator: int, denominator: int):
        self.__numerator = numerator
        self.__denominator = denominator

    def get_numerator(self) -> int:
        return self.__numerator

    def get_denominator(self) -> int:
        return  self.__denominator

    def set_numerator(self, numerator: int):
        self.__numerator = numerator

    def set_denominator(self, denominator: int):
        self.__denominator = denominator

    def display(self):
        print(f"{self.__numerator} / {self.__denominator}")

    def add(self, other_fraction): # функция сложения дробей
        new_numerator = self.__numerator * other_fraction.__denominator + other_fraction.__numerator * self.__denominator
        new_denominator = self.__denominator * other_fraction.__denominator
        return Fraction(new_numerator, new_denominator)

    def sub(self, other_fraction): # функция вычитания дробей
        new_numerator = self.__numerator * other_fraction.__denominator - other_fraction.__numerator * self.__denominator
        new_denominator = self.__denominator * other_fraction.__denominator
        return Fraction(new_numerator,new_denominator)

    def multi(self, other_fraction): # функция умножения дробей
        new_numerator = self.__numerator * other_fraction.__denominator * other_fraction.__numerator * self.__denominator
        new_denominator = self.__denominator * other_fraction.__denominator
        return Fraction(new_numerator, new_denominator)

    def div(self, other_fraction): # функция деления дробей
        new_numerator = self.__numerator * other_fraction.__denominator / other_fraction.__numerator * self.__denominator
        new_denominator = self.__denominator * other_fraction.__denominator
        return Fraction(new_numerator, new_denominator)

# fraction1 = Fraction(1,4)
# fraction1.display()
# print(fraction1.get_numerator(), fraction1.get_denominator())
#
# fraction1.set_numerator(3)
# fraction1.set_denominator(9)
# fraction1.display()

# fraction1 = Fraction(1,2)
# fraction2 = Fraction(2,5)
# fraction3 = fraction1.add(fraction2)
# fraction4 = fraction1.sub(fraction2)
# fraction5 = fraction1.multi(fraction2)
# fraction6 = fraction1.div(fraction2)
# fraction3.display()
# fraction4.display()
# fraction5.display()
# fraction6.display()