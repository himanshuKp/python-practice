# Call type() on the integer 5 and print the results.
#print(type(5))

my_dict={}
#Print out the type() of my_dict.
# print(type(my_dict))

my_list = []
#Print out the type() of my_list.
# print(type(my_list))

#output
# <class 'int'>
# <class 'dict'>
# <class 'list'>

#this will work
#pass keyword is used to indicate that, body of the class is intentionally left blank
#else it will cause error: SyntaxError: unexpected EOF while parsing
class CoolClass:
    pass

#here we are creating an instance of class, obly declaring class is of no use, we have to make use of it by creating an instance of that class
cool_instance = CoolClass()

class Dog():
    dog_time_dilation = 7 
#methods inside class needs compulsory one paramter, the first argument in a method is always the object that is calling the method. Convention recommends that we name this first argument self.    
    def time_explanation(self):
        print("Dog experiences {} years for every 1 human year".format(self.dog_time_dilation))

# pipi_pitbull = Dog()
# pipi_pitbull.time_explanation()

class DistanceConverter:
    kms_in_a_mile = 1.609
    def how_many_kms(self, miles):
        return miles*self.kms_in_a_mile

converter = DistanceConverter()
kms_in_5_miles = converter.how_many_kms(5)
# print(kms_in_5_miles)

# CONSTRUCTORS IN PYTHON
# class Shouter:
#     def __init__(self):
#         print("HELLO!!!!")

#__init__ method is called every time class is instantiated, is also called as constructor
# one_call = Shouter()
# second_call = Shouter()

# pass the value to the constructor
class Shouter:
    def __init__(self, phrase):
        #make sure the phrase is a string
        if type(phrase) == str:
            #shout it
            print(phrase.upper())
        else:
            print("You sir has just entered a value other than a string")

# one_call = Shouter("shout")
# second_call = Shouter("let's hear it out")
# #pass a integer as a parameter now
# third_call = Shouter(4)    #this will not be printed

#print the paramter value passed through using .format() method
class Circle:
    def __init__(self,diameter):
        print("New circle with diameter: {}".format(diameter))

# teaching_table = Circle(36)

class Area:
    def __init__(self, radius):
        area = 2*3.14*radius
        return area

# __init__ cannot return any value, it can only return none or no value
# one_call = Area(12) #error: TypeError: __init__() should return None, not 'float'

class FakeDict:
    pass

fake_dict1 = FakeDict()
fake_dict2 = FakeDict()

#two instances created for different object of same class having same name "fake_key"
#can store any data type mostly
fake_dict1.fake_key = "This Works!!"
fake_dict2.fake_key = 8

#lets join the string together
working_string = "{}{}".format(fake_dict1.fake_key, fake_dict2.fake_key)

#print(working_string)

class SearchEngineEntity:
    secure_prefix = "https://"
    def __init__(self, url):
        self.url = url
    
    def secure_url(self):
        return "{prefix}{site}".format(prefix=self.secure_prefix,site=self.url)
    
codecademy = SearchEngineEntity("www.codecademy.com")
wikipedia = SearchEngineEntity("www.wikipedia.com")

# print(codecademy.secure_url())
# print(wikipedia.secure_url())

class Circle:
    pi = 3.14
    
    def __init__(self, diameter):
        print("Creating circle with diameter {d}".format(d=diameter))
    # Add assignment for self.radius here:
        self.radius = diameter/2
    
    def circumference(self):
        circumference = 2*self.pi*self.radius
        return circumference
    
# medium_pizza = Circle(12)
# teaching_table = Circle(36)
# round_room = Circle(11460)

# print(medium_pizza.circumference())
# print(teaching_table.circumference())
# print(round_room.circumference())

# class Employee():
#     def __init__(self, name):
#         self.name = name

# argus = Employee("Argus Filch")
# print(argus)    #class Employee():
#   def __init__(self, name):
#     self.name = name

# argus = Employee("Argus Filch")
# print(argus)
# prints "<__main__.Employee object at 0x104e88390>"

#INHERITANC EXAMPLE
# class User:
#     is_admin = False
#     def __init__(self,username):
#         self.username = username
# #Admin is a subclass of User
# class Admin(User):
#     is_admin = True
    
# class Message:
#     def __init__(self, sender, recipient, text):
#         self.sender = sender
#         self.recipient = recipient
#         self.text = text
        
# class User:
#     def __init__(self, username):
#         self.username = username
    
#     def edit_message(self, message, new_text):
#         if message.sender == self.username:
#             message.text = new_text
    
# class Admin(User):
#     def edit_message(self, message, new_text):
#         # here we are overriding the superclass method with new definition for the admin
#         message.text = new_text
    
#INTERFACE
#When two classes have the same method names and attributes, we say they implement the same interface. An interface in Python usually refers to the names of the methods and the arguments they take.
# class InsurancePolicy:
#     def __init__(self, price_of_item):
#         self.price_of_insured_item = price_of_item
        
# class VehicleInsurance(InsurancePolicy):
#     def get_rate(self):
#         return self.price_of_insured_item * .001
    
# class HomeInsurance(InsurancePolicy):
#     def get_rate(self):
#         return self.price_of_insured_item * .00005
    
# For an int and an int, + returns an int
2 + 4 == 6

# For a float and a float, + returns a float
3.1 + 2.1 == 5.2

# For a string and a string, + returns a string
"Is this " + "addition?" == "Is this addition?"

# For a list and a list, + returns a list
[1, 2] + [3, 4] == [1, 2, 3, 4]

# a_list = [1, 18, 32, 12]
# a_dict = {'value': True}
# a_string = "Polymorphism is cool!"

# print(len(a_list)) #4
# print(len(a_dict)) #1
# print(len(a_string)) #21

# class UserGroup:
#     def __init__(self, users, permissions):
#         self.user_list = users
#         self.permissions = permissions
    
#     def __iter__(self):
#         return iter(self.user_list)
    
#     def __len__(self):
#         return len(self.user_list)
    
#     def __contains__(self):
#         return user in self.user_list
    
# class User:
#     def __init__(self, username):
#         self.username = username

# diana = User('diana')
# frank = User('frank')
# jenn = User('jenn')

# can_edit = UserGroup([diana, frank],{'can_edit_page':True})
# can_delete = UserGroup([diana, jenn],{'can_delete_page':True})

# # print(len(can_edit))

# for user in can_edit:
#     print(user.username)
    