# Python

## Operator Overloading

Each operator can be used in a different way for different types of operands. For example, + operator is used for adding two integers to give an integer as a result but when we use it with float operands, then the result is a float value and when + is used with string operands then it concatenates the two operands provided.
This different behavior of a single operator for different types of operands is called `Operator Overloading`.

Operator Overloading is achieved by defining a special method in the class definition. The special method used to overload + operator is called __add__().

Both int class and str class implements __add__() method. The int class version of the __add__() method simply adds two numbers whereas the str class version concatenates the string.

`Examples: `

```
>>> x, y = 10, 20 
>>> x + y 
30 
>>> x.__add__(y) # same as x + y 
30 
>>> x, y = [11, 22], [1000, 2000] 
>>> x.__add__(y) # same as x + y 
[11, 22, 1000, 2000]
```

<img src="overloading.jpg>


Notice that last two items in table are not operators instead they are built-in functions. But if you want to use then with your class you should define their respective special methods.

Operator overloading is used to customize the function of an operator for a user-defined class. It is necessary to overload the operator we want to use with the user-defined data type, without it, the compiler does not know which variables of the user-defined type to add, multiply, or compare.

### Can + Operator Add anything?
T
`No`, it cannot. Can you use the + operator to add two objects of a class. 
The + operator can add two integer values, two float values or can be used to concatenate two strings only because these behaviors have been defined in python.
So if you want to use the same operator to add two objects of some user defined class then you will have to defined that behavior yourself and inform Python interpreter about that.

`Example: `

```
class Complex:
    def __init__(self, real, img):
        self.real = real
        self.img = img
    
    def __add__(self, sec):
        real = self.real + sec.real
        img = self.img + sec.img
        return complex(real, img)
    
    def __str__(self):
        return str(self.real)+' + '+str(self.img)+'i'
    
c1 = Complex(5, 3)
c2 = Complex(2 ,4)
print("Sum = ", c1+c2)
```
In the program above, __add__() is used to overload the + operator i.e. when + operator is used with two Complex class objects then the function __add__() is called.
__str__() is another special function which is used to provide a format of the object that is suitable for printing.

