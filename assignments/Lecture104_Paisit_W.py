class Customer:
    name = ""
    lastName = ""
    age = 0

    def addCart(self):
        print("Add product to "+self.name+" "+self.lastName+"'s cart")

customer1 = Customer()
customer1.name = "Paisit"
customer1.lastName = "Wisattayarak"
customer1.addCart()

customer2 = Customer()
customer2.name = "Pairat"
customer2.lastName = "Atichart"
customer2.addCart()

customer3 = Customer()
customer3.name = "Pinitnan"
customer3.lastName = "Sombutpoonpon"
customer3.addCart()

customer4 = Customer()
customer4.name = "Wanchai"
customer4.lastName = "Taintanawat"
customer4.addCart()