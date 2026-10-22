def right_triangle(a, b, c):
    sides = sorted([a, b, c])
    return (sides[0] > 0 and
            sides[0]**2 + sides[1]**2 == sides[2]**2)

a = float(input("Enter first side: "))
b = float(input("Enter second side: "))
c = float(input("Enter third side: "))

if right_triangle(a, b, c):
    print("Right-angled triangle")
else:
    print("Not a right-angled triangle")
