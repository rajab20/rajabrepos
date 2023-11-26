# HOME_day2_advance
# creating a class named Animal
class Animal:
    passport = True
    vaccinate = False

    def __init__(self, name, age, color, height, year):
        self.name = name
        self.age = age
        self.color = color
        self.height = height
        self.year = year

# writing the functions: get_color & get_height
# (as an extra function: writing a function returning all the info via get_info)
    def get_color(self):
        return self.color

    def get_height(self):
        return self.height

    def get_info(self):
        return f"Name: {self.name} | Age: {self.age} | Color: {self.color} | Height: {self.height} | Year: {self.year}"

    @classmethod
    def opposite_passport(cls):
        cls.passport = not cls.passport

    @classmethod
    def opposite_vaccination(cls):
        cls.vaccinate = not cls.vaccinate

    @classmethod
    def reverse_passport_and_vaccination(cls):
        cls.passport = not cls.passport
        cls.vaccinate = not cls.vaccinate


# printing the passport and vaccine fields without the object
print("Passport:", Animal.passport)
print("Vaccine:", Animal.vaccinate)

# creating two different objects
horse = Animal("Dad", 4, "Brown", 0.8, 2021)
duck = Animal("Bob", 3, "White", 0.3, 2019)

# calling the get_color function and printing them on the objects
print(horse.get_color())
print(duck.get_color())

# calling for passport and vaccine fields on those objects to be printed
print("Animal eShoper Passport:", horse.passport)
print("Animal eShoper Vaccination:", horse.vaccinate)
print("Animal 2 Passport:", duck.passport)
print("Animal 2 Vaccination:", duck.vaccinate)

# then after calling these class methods on the objects we created above
# print and see the result
Animal.opposite_passport()
Animal.opposite_vaccination()

print("Animal eShoper Passport:", horse.passport)
print("Animal eShoper Vaccine:", horse.vaccinate)
print("Animal 2 Passport:", duck.passport)
print("Animal 2 Vaccine:", duck.vaccinate)


Animal.reverse_passport_and_vaccination()

print("Animal eShoper Passport:", horse.passport)
print("Animal eShoper Vaccine:", horse.vaccinate)
print("Animal 2 Passport:", duck.passport)
print("Animal 2 Vaccine:", duck.vaccinate)
# ----------------------#
# day2_advance
# eShoper


class Country:  # continent class
    continent = "Australia"
# creating the name, language, territory, country_code parameters in the constructors

    def __init__(self, name, language, region, country_code):
        self.name = name
        self.language = language
        self.region = region
        self.country_code = country_code

    @classmethod
    def get_continent(cls):
        return cls.continent


print("Continent: ", Country.continent)

country = Country("New Zealand", "english", "Australia", 64)
print("Continent:", country.get_continent())
print("Name:", country.name)
print("Language:", country.language)
print("Region:", country.region)
print("Country Code:", country.country_code)


# 4

class Person:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"

    @staticmethod
    def is_underage(age):
        return age < 18


person = Person("A", "B", 20)

print(person.get_full_name())
print(f"{person.get_full_name()} is underage: {Person.is_underage(person.age)}")

# ====================

# 2


class Country:
    continent = "Asia"

    def __init__(self, name, language, territory, country_code):
        self.name = name
        self.language = language
        self.territory = territory
        self.country_code = country_code

    @classmethod
    def update_meteric(cls, mine):
        cls.continent = mine


azerbaijan = Country("Azerbaijan", "Azerbaijani", "86.6", "+994")
azerbaijan.update_meteric("Europe")
print(azerbaijan.continent)

# =========================


class Country:
    continent = "Asia"

    def __init__(self, name, language, territory, country_code):
        self.name = name
        self.language = language
        self.territory = territory
        self.country_code = country_code

    @classmethod
    def update_continent(cls, mine):
        cls.continent = mine

    @classmethod
    def say_smth(cls):
        return "I'm so proud"


azerbaijan = Country("Azerbaijan", "Azerbaijani", "86.6", "+994")
azerbaijan.update_continent("Europe")
print(azerbaijan.continent)
print(azerbaijan.say_smth())

# =======================


@classmethod
def toggle_vaccine(cls):
    cls.vaccine = not cls.vaccine


lion = Animal('Lion', 10, 'yellow', 1.12, 2012)
print(lion.vaccinate)
lion.toggle_vaccine()
print(lion.vaccinate)

