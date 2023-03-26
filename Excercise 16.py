## Task A: create a person inheritance hierarchy

## design atleast three classes: Perosn, Employee and Customer.

## consider appropriate constructors, properties and methods for these classes.

##demonstrate your understanding of encapsulation, inheritance and polymorphism

## create a client script and initiate objects based on the above classes. call
## their methods and set their properties to demontsrate working functionally.

## Task B: create an account inheritance heirachy

## as above, design a separate heirarchy for bank account types and a client
## script to demonstrate functionality.
# class Person:
#     def __init__(self, first_name, last_name, age):
#         self.first_name = first_name
#         self.last_name = last_name
#         self.age = age
#         self.__gender = None
#     def set_gender(self, gender):
#         self.__gender = gender
#     def get_gender(self):
#         return self.__gender
#
#     def __repr__ (self):
#         return f"Person: first_name: {self.first_name}, last_name: {self.last_name}, age: {self.age}, gender: {self.get_gender()} "
# person1 = Person('andy', 'thomas', 30,)
# person1.set_gender('male')
# person2 = Person('katrina', 'dematos', 29,)
# person2.set_gender('female')
# person3 = Person('anya', 'legg', 25,)
# person3.set_gender('female')
# print(person1)
# print(person2)
# print(person3)
#
# class employee(Person):
#     def __init__(self, first_name, last_name, age, location):
#         super().__init__(first_name, last_name, age,)
#         self.location = location
#     def __repr__(self):
#         return f"employee: first_name: {self.first_name}, last_name: {self.last_name}, age: {self.age}, location {self.location}"
#
# employee1 = employee ('ben', 'adams', 25, 'pembroke')
# employee2 = employee ('amanda', 'bevan', 32, 'swansea')
# employee3 = employee ('chad', 'bodwick', 18, 'hereford')
# print(employee1)
# print(employee2)
# print(employee3)
#
# class Customer(Person) :
#     def __init__(self, first_name, last_name, age, payment):
#         super().__init__(first_name, last_name, age,)
#         self.payment = payment
#
#     def __repr__(self):
#         return f"Customer: first_name: {self.first_name} last_name: {self.last_name} age: {self.age} payment: {self.payment}"
#
# customer1 = Customer('logan', 'fierce', 22, 'card')
# customer2 = Customer('mat', 'leblanc', 65, 'cash')
# customer3 = Customer('jason', 'yates', 44, 'cash')
#
# print(customer1)
# print(customer2)
# print(customer3)

class Account:
    numCreated = 0
    def __init__(self,name):
        self.balance = name
print("hello welcome to your account")

def deposit(self):
        super().__init__(self, amount)
        amount = float(input('enter amount to be deposited:'))
        self.balance += amount

def __repr__(self):
        return f"amount: {self.balance}"
print("amount deposited", )

def withdraw(self):
    super().__init__(self, amount, withdraw)
    withdraw = float(input("enter amount to be withdrawn"))
print("amount withdrew")


