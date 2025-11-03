area=lambda a:a*a
side=int(input("enter the side of square:"))
print("Area of square is :",area(side))
rarea=lambda l,b:l*b
l=int(input("Enter the length of the rectangle:"))
b=int(input("enter the breadth of the rectangle:"))
print("Area of the rectangle:",rarea(l,b))
tarea=lambda c,h:0.5*c*h
c=int(input("Enter the breadth of the triangle:"))
h=int(input("Enter the height of the triangle:"))
print("Area is :",tarea(c,h))