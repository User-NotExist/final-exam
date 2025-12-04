class DeliveryOrder:
    def __init__(self, customer, item):
        self.customer = customer
        self.item = item
        self.status = "preparing"
        self.__driver = None

    def assign_driver(self, driver):
        self.__driver = driver
    
    def summary(self):
        print("Order Summary:")
        print(f"Item: {self.item}")
        print(f"Customer: {self.customer.name}")
        print(f"Status: {self.status}")
        print(f"Driver: {self.__driver.name}")


class Person:
    def __init__(self, name):
        self.name = name
    
    def introduce(self):
        print(f"Hi, I'm {self.name}")
    

class Customer(Person):
    def __init__(self, name, address):
        super().__init__(name)
        self.address = address
    
    def place_order(self, item):
        return DeliveryOrder(self, item)


class Driver(Person):
    def __init__(self, name, vehicle):
        super().__init__(name)
        self.vehicle = vehicle
    
    def deliver(self, order):
        print(f"{self.name} is delivering {order.item} to {order.customer.name} using {self.vehicle}.")
        order.status = "delivered"


c1 = Customer("Alice", "192.168.0.2")
c2 = Customer("Bob", "192.168.0.3")
d1 = Driver("David", "motorcycle")

c1.introduce()
c2.introduce()
d1.introduce()

print()

o1 = c1.place_order("Laptop")
o2 = c2.place_order("Headphones")

o1.assign_driver(d1)
o2.assign_driver(d1)

o1.summary()
print()
o2.summary()
print()

d1.deliver(o1)
d1.deliver(o2)

print()

print("Final Status:")
print(f"Order for {o1.item}: → {o1.status}")
print(f"Order for {o2.item}: → {o2.status}")