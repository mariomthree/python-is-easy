# Python Program to find Area of a Rectangle

width = float(input('Please Enter the Width of a Rectangle: '))
height = float(input('Please Enter the Height of a Rectangle: '))

if width < 0 :
    print("\033[31mPlease enter a positive number for width.\033[m")
elif height < 0:
    print("\033[31mPlease enter a positive number for height.\033[m")
else:
    # calculate the area
    Area = width * height
    # calculate the Perimeter
    Perimeter = 2 * (width + height)
    print("\nArea of a Rectangle is: %.2f" %Area)
    print("Perimeter of Rectangle is: %.2f" %Perimeter)