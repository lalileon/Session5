name = input("What is your name? ")
age = input("How old will yoou be this year? ")
birth_year = 2023 - int(age)
print(name, "you were born in", birth_year)

name = input("What is your name? ")
age = int(input("How old will yoou be this year? ")) #other way to convert
birth_year = 2023 - age
print(name, "you were born in", birth_year)

name = input("What is your name? ")
age = input("How old will yoou be this year? ")
age = int(age)
#or like this
birth_year = 2023 - age
print(name, "you were born in", birth_year)

