# # # #
# # # #
class House:
# #     #     # #     # class method example meaning method we can use without any objects created
# #     #     # #     # a library could be created by grouping class methods
# # so this is a class method which will be available to all objects created from this class
# #     #     # #     # we can use it without creating any objects
    @classmethod
    def add(cls, a, b):
        print(a, b, a + b, cls.all_house_prop)
        return a + b

# #     #     #
    all_house_prop = "Brick"  # class property generally meant to be shared among instances

# #     #
# #     #     # # # # # #     # do not share lists, dictionaries other mutable structures in class properties
    def print_house_prop(self):  # method definition which is function associated with objects
        print(f"This house is built from {self.all_house_prop}")

# #     #
# #     #     #
# #     #     # # # #     # so __init__ has to be exact name for constructor to be called
# #     #     # # # #     # __init__ is so called double under - dunder method
# # so good practice to have sane default values
    def __init__(self, color="green", nails=0, owner=""):  # constructor method called upon creation of object
#         #         # we add everything that we want done when we first create object from our class blueprints
        self.color = color  # self.color is a property of the object
        self.color = None  # of course we could have stuck with self.color = color
        self.set_color(color)  # by calling built in method we can perform extra validation
        self.nails = nails
        self.owner = owner
        print(f"Initialized class instance with {self.color=} {self.nails=} {self.all_house_prop=} {self.owner=}")

# #     # so called setter method
    def set_color(self, new_color):  # so called setter method
#         # some verification on sane color here maybe
#         # idea is to control how we set the value
        self.color = new_color
        print(f"Changed color to {self.color}")
        return self  # by returning self we can chain methods

# #     #
# #     #     #
# #     #     # # #     # regular methods, so method is a function declared in class definition
    def build_house(self):
        print(f"Building a house of {self.all_house_prop}")
        print(f"Its color will be {self.color}")
        return self

# #     #
    def simple_print(self):
        print(f"Oh {self.color=} {self.nails=}")
        return self  # this lets us chain our methods


# # #
# # #

# # # class definition ends here


# # # # #
# # # #
# # # # #
# # # # #
# # # # #
# # # # #
# # # no houses yet, so this is class method
print(House.add(5, 11))


# # # # #
# # # #
# # # #
new_house = House()  # I create a new object instance from House class blueprint
print(new_house.all_house_prop)
new_house.print_house_prop()  # so we call method associated with this object, (self does not have to be specified!!)
print(new_house.all_house_prop)  # could access the property directly
print("This particular house is built from", new_house.all_house_prop)
print(type(new_house), type(5), type("Valdis"))
# # # # #
# # # # # #
another_house = House()  # so each time we creat a new object __init__ is called for that object
print(another_house.all_house_prop)
another_house.print_house_prop()
another_house.all_house_prop = "Straw"
another_house.print_house_prop()
new_house.print_house_prop()  # my original house is still from brick
# # # # # #
my_house = House(owner="Valdis") # creaing new object, in other class instance
print(my_house.color, my_house.nails)
print(my_house.all_house_prop)
my_house.build_house()
# # # # # # # # my_house.all_house_prop = "Clay" # not very OOP style to mutate
# # # # # # # # print(my_house.all_house_prop)
my_house.build_house() # i am calling a method, notice no self needed
summer_house = House(nails=500)  # another object instance of same House class
summer_house.build_house()
print(summer_house.nails)
red_house = House(color='red')  # so self is not mentioned
print("Color", red_house.color)
######third_house.build_house()
my_house.set_color("Orange")
print("Type", my_house.all_house_prop)
my_house.build_house()
# # # # # # # # # # # # # # # # # # # # i've created an object my_house based on House class blueprints
# # # # # # # # # # # # # print(type(my_house))
my_house.simple_print() # calling object's method
# # # # # #
friends_house = House(color="blue", nails=1_000, owner="Edgars")  # so new object based on same template
print(friends_house.color)
friends_house.build_house().set_color("yellow").build_house().simple_print()
# # same as
# # friends_house.build_house()
# # friends_house.set_color("yellow")
# # friends_house.build_house()
# # friends_house.simple_print()
# # just in one line
# # # friends_house.simple_print().set_color("yellow").build_house()
friends_house.set_color("Violet").simple_print()  # this works because simple_print return self
# # #
# # #
# # # # # # # class methods can return self if they have nothing useful to return
# # # #
my_house.simple_print()
my_house.set_color("red")
my_house.simple_print()
# # # #