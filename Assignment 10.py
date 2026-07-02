import math

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def diameter(self):
        return 2 * self.radius

    def area(self):
        return math.pi * (self.radius ** 2)

    def circumference(self):
        return 2 * math.pi * self.radius


class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def total_value(self):
        return self.price * self.quantity


class BankAccount:
    def __init__(self, initial_balance=0.0):
        self.balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited: {amount}. Balance: {self.balance}")
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        if amount <= 0:
            print("Invalid withdrawal amount.")
        elif amount > self.balance:
            print("Insufficient funds.")
        else:
            self.balance -= amount
            print(f"Withdrew: {amount}. Balance: {self.balance}")


class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def check_password(self, input_password):
        return self.password == input_password


if __name__ == "__main__":
    r = Rectangle(10, 5)
    print(r.area(), r.perimeter())

    c = Circle(7)
    print(c.diameter(), f"{c.area():.2f}", f"{c.circumference():.2f}")

    p = Product("Laptop", 1200, 4)
    print(p.total_value())

    acc = BankAccount(100.0)
    acc.deposit(50)
    acc.withdraw(200)
    acc.withdraw(60)

    u = User("dev_user", "pass123")
    print(u.check_password("wrong"))
    print(u.check_password("pass123"))
