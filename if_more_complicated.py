try:
    a = int(input("Give me a number pls "))
    b = int(input("Give me another number pls "))
except ValueError:
    print("one of the numbers was invalid")
    exit(1)

if a > b:
    print(a, ">", b)
elif a < b:
    print(a, "<", b)
else:
    print(a, "=", b)

try:
    a = int(input("Give me a number pls "))
    b = int(input("Give me another number pls "))
except ValueError:
    print("one of the numbers was invalid")

else:
    if a > b:
        print(a, ">", b)
    elif a < b:
        print(a, "<", b)
    else:
        print(a, "=", b)