# CS 16X Git Assignment

# Project requires TWO functions:
# 1. rect_area (length, width) which will return the area of a rectangle
# 2. rect_solid_area (length, width, height) which will return the area of a solid rectangular object

# The following four lines are just there to make the code work without errors until functions are added
def rect_solid_area(x, y, z):
    return 1
length = 1; width = 1; height = 1
rect_solid_area (length, width, height)

def rect_area(x,y,z):
    area = width * height
    return area

# Request the dimension of a solid rectangular object
length = int(input("Enter the length of the object as in integer: "))
width = int(input("Enter the width of the object as in integer: "))
height = int(input("Enter the height of the object as in integer: "))

def rect_surface_area(x,y,z):
    area = 0
    area = area + rect_area(x, y) * 2
    area = area + rect_area(x, z) * 2
    area = area + rect_area(y, z) * 2
    return area

rect_surface_area = rect_solid_area(length, width, height)

print("Length = ", length, "Width = ", width, "Height = ", height)
print("Total Surface Area = ", rect_surface_area)

#end