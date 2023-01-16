#Creating class and object
class Person:                                               #creating class names as Person
  def __init__(self,name,age):
    self.name = name
    self.age = age

person = Person("Kane",18)                                  #creating object name person
print("My name is", person.name)
print("My age is", person.age)

class Student(Person):
  pass

person2 = Student("Kyle", 20)
print(person2.name)
print(person2.age)

# Application 1

# Use Shape as parent class name
# Use Square as child class that inherits the attributes of the parent class
# Use Area () and Perimeter () as methods to retrieve its values by assigning the instance of the object

class Shape:
    def __init__(self, sides):
        self.sides = sides

    def get_area(self):
        pass

    def get_perimeter(self):
        pass


class Square(Shape):
    def __init__(self, sides):
        super().__init__(sides)

    def get_area(self):
        return self.sides ** 2

    def get_perimeter(self):
        return self.sides * 4


square = Square(4)

area = square.get_area()
print(f"The area of the square is {area}")

perimeter = square.get_perimeter()
print(f"The perimeter of the square is {perimeter}")