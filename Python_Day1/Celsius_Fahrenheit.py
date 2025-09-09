def c_to_f(celsius):
    fahrenheit = celsius * 9 / 5 + 32
    print(str(celsius) + "°C = " + str(fahrenheit) + "°F")

def f_to_c(fahrenheit):
    celsius = (fahrenheit - 32) * 5 / 9
    print(str(fahrenheit) + "°F = " + str(round(celsius, 2)) + "°C")

c = float(input("Enter temperature in Celsius: "))
f = float(input("Enter temperature in Fahrenheit: "))

c_to_f(c)
f_to_c(f)
