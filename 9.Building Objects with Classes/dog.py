# defines a class called Dog
class Dog:
  def __init__(self, name): # this is the constructor method that is called each time we create a Dog object
    self.name = name # the dog is given a property called name, and we assign the passed argument to the name property
    # self means that each Dog object will have a name associated with it, which may be different or the same
  def bark(self):
    print("Woof!")

d = Dog('Fido') # since we pass the argument 'Fido', we assign the name field to be 'Fido'
print(d.name) # we can access the instance field by using the dot operator
d.bark() # now we have a method (function defined for a class) associated with the Dog class
# only Dog objects are allowed to access these functions
