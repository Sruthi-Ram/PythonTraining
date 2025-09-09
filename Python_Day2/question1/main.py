from shapes import circle, rectangle

shape = input("Enter shape (circle/rectangle): ").strip().lower()

if shape == "circle":
    r = float(input("Enter radius: "))
    print("Area:", circle.area(r))
    print("Perimeter:", circle.perimeter(r))
elif shape == "rectangle":
    l = float(input("Enter length: "))
    w = float(input("Enter width: "))
    print("Area:", rectangle.area(l, w))
    print("Perimeter:", rectangle.perimeter(l, w))
else:
    print("Invalid shape")
