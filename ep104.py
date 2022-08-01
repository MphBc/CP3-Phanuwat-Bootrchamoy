class Customer:
    name = ""
    lastname = ""
    age = 0

    def addCart(self):
        print("Added to " + self.name + " " + self.lastName + "'s cart")
        print("Age:" + str(self.age))


customer1 = Customer()
customer1.name = "Cat"
customer1.lastName = "Cool"
customer1.age = 12
customer1.addCart()

customer2 = Customer()
customer2.name = "Nat"
customer2.lastName = "Mink"
customer2.age = 28
customer2.addCart()

customer3 = Customer()
customer3.name = "Pha"
customer3.lastName = "Moo"
customer3.age = 27
customer3.addCart()