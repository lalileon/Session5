name = input("What is your name? ")
age = input("How old will yoou be this year? ")
try:
    age = int(age)
#or like this
except ValueError: #except without ValueError will catch all errors so u define it so python still gives you other errors that could be yours
    #so we define which the error we expect to happen by the user
    print("sorry, that was not a valid number")
    exit()
birth_year = 2023 - age
print(name, "you were born in", birth_year)


name = input("What is your name? ")
age = input("How old will you be this year? ")
try:
    age = int(age)
    birth_year = 2023 - age
except ValueError:
    print("sorry, that was not a valid number")
except NameError:
    print("oh, it's not you, it's me :)")
else:
    print(name, "you were born in", birth_year) #do it if no exceptions happen
finally:
    print("Thanks for playing, come again") #will always be executed at the end not mattering what happened before

name = input("What is your name? ")
age = input("How old will yoou be this year? ")
try:
    age = integer(age) #doesn't work because of my mistake
#or like this
except ValueError:
    print("sorry, that was not a valid number")
    exit()
except NameError: #we can use more than one except
    print("oh, it's not you, it's me :)")
    exit()
birth_year = 2023 - age
print(name, "you were born in", birth_year)