def check_odd_even(number):
    if number % 2 == 0:
        print("Number", number, "is Even")
    else:
        print("Number", number, "is Odd")

num = int(input("Enter a number: "))
check_odd_even(num)
