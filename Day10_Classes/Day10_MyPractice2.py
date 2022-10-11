class Garage:
# #     g_name = "just a garage"  # not needed better to use sparingly we can run in some weird effects

# #     @classmethod  # this means that this method is a class method can be called without any objects
# #     def add(cls, a, b):
# #         print(a, b, a + b, cls.all_house_prop)
# #         return a + b

# #     #
# #     #     # # # #     # classes constructor method called when we make a new object instance from this class
# #     #     # # # #     # dunder syntax __init__
    def __init__(self, color="green", nails=0, name="My garage", nail_color="metal", secret="gold"):
        self.color = color
        self.nails = nails
        self.name = name
        self._nail_color = nail_color  # convention of private do not touch properties
        self.__secret_stash = secret  # private property whose name is mangled to outside
        print(f"Initialized class instance with {self.color=} {self.nails=} {self.name=}")

# there are other dunder methods
# list of all dunder methods
# https://rszalski.github.io/magicmethods/
# official docs
# https://docs.python.org/3/reference/datamodel.html#special-method-names

# #     #
# #     #     #
# #     #     # # #     # will be useful when we want to print our object
    def __str__(self):  # this is responsible for string representation for print etc
        # so naturally for __str__ we return a string
        return f"Garage name: {self.name} color {self.color} nails: {self.nails} secret: {self.__secret_stash}"

# #     #
# #     #
    def __add__(self, other):  # + operator overloading in other languages
        # return self.nails + other.nails
        new_color = self.color + "_" + other.color  # TODO make your color mixer
        new_nails = self.nails + other.nails
        # so I return a new garage with a mix of properties from incoming garages
        return Garage(color=new_color, nails=new_nails)  # i create new instance  with new attributes

# #     #
# #     #     #
    def __eq__(self, other):  # so == will work
        # we come up some logic for object comparison
        return self.color == other.color and self.nails == other.nails  # not a full comparison

# #     #
# #     #     #
# #     #     # # # #     # i could just live with __str__ no need for simple_print anymore
    def simple_print(self):  # so this name i just made up myself
        print(f"Oh {self.name=} {self.color=} {self.nails=}")
        return self

# #     #
    def add_nails(self, new_nails=1):
        # here could be code for checking validity of new nails
        self.nails += new_nails
        return self

# #     #
# #     #     #
# #     #     # so i can control how secret is to be given out
    def get_secret(self):
        # here i could check if secret should be given out and how
        return self.__secret_stash

# #     #
# #     #     #
    # so called setter method - we control how secret is changed
    def set_secret(self, new_secret):
        # here we can check if new secret is valid to be set
        if len(new_secret) >= 6:
            print("Good secret, setting it")
            self.__secret_stash = new_secret
        else:
            print("Secret is too short, needs to be at least 6 characters long")
        return self  # for chaining

# #     #     #
    def set_nails(self, new_nail_count=0):
        self.nails = new_nail_count
        return self


# # #
# # #
# # # # # # # # end of our class definition, that is end of our blueprint
# # # #
# # # #
simple_garage = Garage()
print(simple_garage)  # without __str__ definition not very useful
print(simple_garage.color)
print(simple_garage.name)
print(simple_garage._nail_color) # we can access this semi-private property
# single _ simply means this should not be messed with
# but I could if I really wanted to
# # # solution controlled access to private variables using methods
# so called getter or accessor methods
print(simple_garage.get_secret())
simple_garage.set_secret("12345") # too short
simple_garage.set_secret("123456") # number on my garage door
print(simple_garage.get_secret())
#print(simple_garage) # this will not look too good, just a memory address
print(simple_garage)
#print(simple_garage.__secret_stash) # so __property is renamed using name mangling
print(simple_garage.get_secret()) # using getter to obtain private information
# # # #
#print(simple_garage.g_name)
# # # # # # simple_garage.g_name = "Mana garāža"
# # # # # # print(simple_garage.g_name)
# # # # # # # # # # # to avoid always initalize by hand constructors were created
# # # #

homer_garage = Garage(color="yellow", nails=33)
flanders_garage = Garage(color="blue", nails=55, name="Property of Flanders")
print(homer_garage)  # this works because we wrote our own __str__ method
print(flanders_garage)
mutant_garage = homer_garage + flanders_garage  # we created our own __add__ method, gaining syntax sugar
print(mutant_garage)
print("end")
mut_garage = homer_garage.__add__(flanders_garage)  # same as above

print(mutant_garage)
print(mut_garage)

print("end")
mutant_garage.simple_print().add_nails(77).simple_print().set_nails(500).add_nails(10).simple_print()