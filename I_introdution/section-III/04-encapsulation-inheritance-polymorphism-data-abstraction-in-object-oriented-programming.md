# Python

## Encapsulation, Inheritance, Polymorphism,  and Data Abstraction in Object-Oriented Programming

## Object-oriented programming

Is a programming paradigm that uses objects and their interactions to design applications and computer programs.

There are some basic programming concepts in OOP we need to be aware of:

-   Inheritance
-   Abstraction
-   Polymorphism
-   Encapsulation

1.	`Inheritance` is a way to form new classes using classes that have already been defined.
2.	`Abstraction` is simplifying complex reality by modeling classes appropriate to the problem. 
3.	`Polymorphism` is the process of using an operator or function in different ways for different data input. 
4.	`Encapsulation` hides the implementation details of a class from other objects. 

## Inheritance
  
Is concerned with the relationship between classes and methods/functions, which is like a parent and a child class. A child can be born with some of the attributes of the parents. Inheritance ensures reusability of codes just the way multiple children can inherit the attributes of their parents.

<img src="inheritance.png" />

### Benefits of Inheritance

-   Inheritance depicts relationships that resemble real-world scenarios.
-   It provides the feature of re-usability which allows the user to add more features to the derived class without altering it.
-	If a class Y inherits from class X, then automatically all the sub-classes of Y would inherit from class X.

### Basic Terminologies

1.	Subclass/Derived class: It is a class that inherits the properties from another class (usually the base class).
2.	Superclass/Base class: It is the class from which other subclasses are derived.
3.	A derived class usually derives/inherits/extends the base class.

`Example:`

```
import datetime

class Animal:

    def __init__(self, name, yearOfBorn):
        self.name = name
        self.yearOfBorn = yearOfBorn
    
    def getName(self):
        return self.name

    def getAge(self):
        return datetime.date.today().year - self.yearOfBorn
    
class Dog(Animal):
    
    def __init__(self, name, yearOfBoth):
        super().__init__(name, yearOfBoth)

    def sound():
        print("Au au au au!")

class Cat(Animal):
    
    def __init__(self, name, yearOfBoth):
        super().__init__(name, yearOfBoth)

    def sound():
        print("Miau miau miau!")

dog = Dog("Max", 2017)
cat = Cat("Fill", 2018)

print(f"{Dog: {dog.getAge()} years old.")
print(f"Cat: {cat.getSound()}")

# output
# Dog: 3 years old.
# Son: Miau miau miau! 
```

### Encapsulation

In essence, encapsulation is achieved in Python by creating Private variables to define hidden classes in and then using public variables to call them up for use. 

With this approach, a class can be updated or maintained without worrying about the methods using them. If you are calling up a class in ten methods and you need to make changes, you don’t have to update the entire methods rather you just update a single class.

Once the class is changed, it automatically updates the methods accordingly. Encapsulation also ensures that your data is hidden from external modification. Encapsulation is also known as Data-Hidden. 

The concept of encapsulation is the same in all object-oriented programming languages. The difference is seen when the concepts are applied to particular languages.

Compared to languages like Java programming language which offers access modifiers (public or private) for variables and methods, Python provides access to all the variables and methods globally.

## Methods to Control Access

There are multiple methods that are offered by Python to limit variable and method access across the program.

## Using Single Underscore

A common Python programming convention to identify a private variable is by prefixing it with an underscore. Now, this doesn’t really make any difference on the compiler side of things. The variable is still accessible as usual.

## Using Double Underscores

If you want to make class members i.e. methods and variables private, then you should prefix them with double underscores. 

But Python offers some sort of support to the private modifier. This mechanism is called Name mangling. With this, it is still possible to access the class members from outside it.

## Name Mangling

In Python, any identifier with `__VariableName` is rewritten by a python interpreter as `_Classname__VariableName`, and the class name remains as the present class name. This mechanism of changing names is called Name Mangling in Python.

## Using Getter and Setter methods to access private variables

If we want to access and change the private variables, accessor (getter) methods and mutators(setter methods) should be used, as they are part of Class.


`Example: `


```
import datetime

class Animal:

    def __init__(self, name, yearOfBorn):
        self.__name = name
        self.__yearOfBorn = yearOfBorn
    
    def getName(self):
        return self.__name
    
    def getYearOfBorn(self):
        return self.__yearOfBorn
    
    def setName(self, name):
        self.__name = name
    
    def setYearOfBorn(self, yearOfBorn):
        self.__yearOfBorn = yearOfBorn
    
    def getAge(self):
        return datetime.date.today().year - self.yearOfBorn

animal = Animal("Fill", 2018)

print(f"Cat: {cat.getName()}")

# output
# Aninal: Fill
```

## Benefits of Encapsulation in Python

Encapsulation not only ensures better data flow but also protects the data from outside sources. The concept of encapsulation makes the code self-sufficient. 
You should hide the data in the unit to make encapsulation easy and also to secure the data.

## Polymorphism

<img src="polymorphism.png" />

With polymorphism, a method or subclass can define its behaviors and its attributes while retaining some of the functionality of its parent class. This means you can have a class that displays date and time, and then create a method to inherit the class but should display a welcome message alongside the date and time. 

You can create a class called “Move” and then four people create animals that would inherit the move class. 
But we don’t know the type of animals they would create. So polymorphism would allow the animals to move but in different forms based on the physical features.

1) creates a Snail that inherits the move class, but the snail would crawl
2) creates a Kangaroo that inherits the move class, but the Kangaroo would leap
3) creates a Dog that inherits the move class, but the dogs would walk
4) creates a Fish that inherits the move class, but the Fish would swim.


You can create a class called “Move” and then four people create animals that would inherit the move class. 
But we don’t know the type of animals they would create. So polymorphism would allow the animals to move but in different forms based on the physical features

1) creates a Snail that inherits the move class, but the snail would crawl
2) creates a Kangaroo that inherits the move class, but the Kangaroo would leap
3) creates a Dog that inherits the move class, but the dogs would walk
4) creates a Fish that inherits the move class, but the Fish would swim.

Polymorphism has ensured that these animals are all moving but in different forms of movement. How the programs would behave would not be known until its runtime.

## Abstraction

Is a programming methodology in which details of the programming codes are hidden away from the user, and only the essential things are displayed to the user. 

`Example: `

```
import datetime
import abc

class Absclass(abc.ABC):

    def __init__(self, name):
        self.name = name
    
    def getName(self):
        return self.name

    def setName(self, name):
        self.name = name

    @abc.abstractmethod
    def sound(self):
        print("Animal sound.")
    

class Dog(Absclass):
    
    def __init__(self, name):
        super().__init__(name)

    def sound(self):
        print("Au au au au!")

class Cat(Absclass):
    
    def __init__(self, name):
        super().__init__(name)

    def sound(self):
        print("Miau miau miau!")
```