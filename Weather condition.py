def squareperi(x):
    perimeter = 4 * x
    print("The perimeter of the square is:", perimeter)
    
def rectangleperi(l, b):
    perimeter = 2 * (l + b)
    print("The perimeter of the rectangle is:", perimeter)
        
def circumference(r):
    c = 2 * 3.14 * r
    print("The circumference of the circle is:", c)
    
r = int(input("Enter the radius of circle: "))
circumference(r)

x = int(input("Enter the side of square: "))
squareperi(x)

l = int(input("Enter the length of rectangle: "))
b = int(input("Enter the breadth of rectangle: "))
print(rectangleperi(l, b))