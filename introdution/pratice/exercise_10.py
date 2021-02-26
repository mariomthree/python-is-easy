width = height = -1

while width < 0:  
    width = float(input('Please Enter the Width of a Rectangle: '))
    if width < 0 :
        print("\033[31mPlease enter a positive number for width.\033[m")

while height < 0:
    height = float(input('Please Enter the Height of a Rectangle: '))
    if height < 0:
        print("\033[31mPlease enter a positive number for height.\033[m")

Area = width * height
Perimeter = 2 * (width + height)
print("\nArea of a Rectangle is: %.2f" %Area)
print("Perimeter of Rectangle is: %.2f" %Perimeter)