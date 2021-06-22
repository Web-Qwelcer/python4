from random import *
from datetime import *
from time import *


class Passport:

    def __init__(self, name, surname, patronymic, gender: str, city, birth_date) -> None:
        self.name = name
        self.surname = surname
        self.patronymic = patronymic
        self.gender = gender.upper()
        self.city = city
        self.birth_date = strptime(birth_date, '%d.%m.%Y')

        self.authority = randint(1111, 9999)
        self.__number = randint(10000000, 999999999)
        self.create_date = datetime.today().strftime("%d-%m-%Y")

    def __str__(self) -> str:
        return f'Passport: {self.name}, {self.surname}'

    def _print(self):
        print(f'Passport info:\n\
            \tName: {self.name}\n\
            \tSurname: {self.surname}\n\
            \tPatronymic: {self.patronymic}\n\
            \tGender: {self.gender}\n\
            \tCity: {self.city}\n\
            \tBirth date: {self.birth_date[2]}-{self.birth_date[1]}-{self.birth_date[0]}\n\
            \tAuthority: {self.authority}\n\
            \tSerial number: {self.__number}\n\
            \tDate: {self.create_date}')

    def _printBirthdate(self):
        """
        Метод для виводу дати народження у форматі (25-09-2016)
        """
        print(f'\tBirth date: {self.birth_date[2]}-{self.birth_date[1]}-{self.birth_date[0]}\n\
            ')


class ForeignPassport(Passport):

    def __init__(self, name, surname, patronymic, gender: str, city, birth_date) -> None:
        super().__init__(name, surname, patronymic, gender, city, birth_date)

        self.__number = randint(10000000, 999999999)
        self.visa = []

    def set_visa(self, country, end_time):
        end_time = strptime(end_time, '%d.%m.%Y')
        self.visa.append({country: end_time})

    def _print(self):
        print(f'Passport info:\n\
            \tName: {self.name}\n\
            \tSurname: {self.surname}\n\
            \tPatronymic: {self.patronymic}\n\
            \tGender: {self.gender}\n\
            \tCity: {self.city}\n\
            \tBirth date: {self.birth_date[2]}-{self.birth_date[1]}-{self.birth_date[0]}\n\
            \tSerial number: {self.__number}')
        print('Visa info:')
        for item in self.visa:
            print('\t', list(item.keys())[
                0], ':', f'{list(item.values())[0][2]}-{list(item.values())[0][1]}-{list(item.values())[0][0]}')

    def countryVisaInfo(self):
        """
        Метод для виводу країн які були відвідані
        """
        print('Visited Country Info:')
        for item in self.visa:
            print('\t', list(item.keys())[0])

    def timeVisa(self):
        """
        Метод для виводу незакінчених віз
        """
        print('Acting Visas info:')
        today = strptime(datetime.today().strftime('%d-%m-%Y'), '%d-%m-%Y')
        for item in self.visa:
            if list(item.values())[0][0] >= today[0]:
                if list(item.values())[0][1] > today[1]:
                    print('\t', list(item.keys())[
                        0], ':', f'{list(item.values())[0][2]}-{list(item.values())[0][1]}-{list(item.values())[0][0]}')
                elif list(item.values())[0][1] == today[1]:
                    if list(item.values())[0][2] > today[2]:
                        print('\t', list(item.keys())[
                            0], ':', f'{list(item.values())[0][2]}-{list(item.values())[0][1]}-{list(item.values())[0][0]}')


Bob = Passport('Bob', 'Bobich', 'Bobovich', 'm', 'London', '25.06.2016')
print(Bob)
Bob._print()
# Bob._printBirthdate()


Bill = ForeignPassport('Bill', 'Bobich', 'Bobovich', 'm', 'London', '25.06.2016')
Bill.set_visa('Poland', '01.09.2021')
Bill.set_visa('USA', '26.05.2021')
Bill.set_visa('France', '21.06.2021')
Bill.set_visa('Austria', '23.06.2021')
