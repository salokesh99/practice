class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

#Use the Person class to create an object, and then execute the printname method:

x = Person("John", "Doe")
x.printname()

#child class

# class Student(Person):
#   pass
#
# x = Student("Mike", "Olsen")
# x.printname()


#if we add init function, inheritence does ot work
class Student(Person):
    def __init__(self, fname, lname, graduationyear):
    #we need to explicitely define init of parent class here.
        # Person.__init__(self, fname, lname)
    # By using the super() function, you do not have to use the name of the parent element, it will automatically inherit the methods and properties from its parent.
        super().__init__( fname, lname)
        self.graduationyear = graduationyear


    def welcome(self):
        print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)


x = Student("Mike", "Olsen", 2019)
print(x)