#bank account problem
class BankAccount:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self._balance = balance

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            print(f"Deposited ₹{amount}. New balance: ₹{self._balance}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if 0 < amount <= self._balance:
            self._balance -= amount
            print(f"Withdrew ₹{amount}. Remaining balance: ₹{self._balance}")
        else:
            print("Insufficient balance or invalid amount.")

    def get_balance(self):
        return self._balance

# Subclass for Savings Account
class SavingsAccount(BankAccount):
    def __init__(self, account_number, balance, interest_rate):
        super().__init__(account_number, balance)
        self.interest_rate = interest_rate  # Interest rate in percentage

    def calculate_interest(self):
        interest = self._balance * (self.interest_rate / 100)
        print(f"Interest earned: ₹{interest}")
        return interest

# Subclass for Current Account
class CurrentAccount(BankAccount):
    def __init__(self, account_number, balance, min_balance):
        super().__init__(account_number, balance)
        self.min_balance = min_balance  # Minimum balance required

    def withdraw(self, amount):
        if self._balance - amount >= self.min_balance:
            self._balance -= amount
            print(f"Withdrew ₹{amount}. Remaining balance: ₹{self._balance}")
        else:
            print("Cannot withdraw. Minimum balance requirement not met.")

# **Testing the implementation**
# Creating a Savings Account
savings = SavingsAccount("SA123", 5000, 5)
savings.deposit(1000)  # Depositing ₹1000
savings.calculate_interest()  # Calculating interest
savings.withdraw(2000)  # Withdrawing ₹2000

print("\n")

# Creating a Current Account
current = CurrentAccount("CA456", 10000, 3000)
current.deposit(2000)  # Depositing ₹2000
current.withdraw(8000)  # Trying to withdraw ₹8000
current.withdraw(6000)  # Withdrawing ₹6000

#employee management
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary  # Base salary

    def calculate_salary(self):
        return self.salary  # Default salary for a basic employee

# Subclass for Regular Employee
class RegularEmployee(Employee):
    def __init__(self, name, salary, bonus):
        super().__init__(name, salary)
        self.bonus = bonus  # Additional bonus for regular employees

    def calculate_salary(self):
        return self.salary + self.bonus  # Regular salary + bonus

# Subclass for Contract Employee
class ContractEmployee(Employee):
    def __init__(self, name, hourly_rate, hours_worked):
        super().__init__(name, 0)  # No fixed salary, only hourly pay
        self.hourly_rate = hourly_rate
        self.hours_worked = hours_worked

    def calculate_salary(self):
        return self.hourly_rate * self.hours_worked  # Salary based on hours worked

# Subclass for Manager
class Manager(Employee):
    def __init__(self, name, salary, bonus, stock_options):
        super().__init__(name, salary)
        self.bonus = bonus
        self.stock_options = stock_options  # Additional benefits for managers

    def calculate_salary(self):
        return self.salary + self.bonus + self.stock_options  # Salary + bonus + stock options

# **Testing the Implementation**
regular = RegularEmployee("John", 50000, 5000)
contract = ContractEmployee("Alice", 1000, 40)
manager = Manager("David", 70000, 10000, 20000)

print(f"{regular.name}'s Salary: ₹{regular.calculate_salary()}")
print(f"{contract.name}'s Salary: ₹{contract.calculate_salary()}")
print(f"{manager.name}'s Salary: ₹{manager.calculate_salary()}")

#vehicle rental
class Vehicle:
    def __init__(self, model, rental_rate):
        self.model = model
        self.rental_rate = rental_rate  # Base rental rate per day

    def calculate_rental(self, days):
        return self.rental_rate * days  # Default rental cost

# Subclass for Car
class Car(Vehicle):
    def __init__(self, model, rental_rate, luxury_tax):
        super().__init__(model, rental_rate)
        self.luxury_tax = luxury_tax  # Additional luxury tax

    def calculate_rental(self, days):
        return (self.rental_rate + self.luxury_tax) * days  # Rental with tax

# Subclass for Bike
class Bike(Vehicle):
    def __init__(self, model, rental_rate, helmet_fee):
        super().__init__(model, rental_rate)
        self.helmet_fee = helmet_fee  # Extra helmet fee

    def calculate_rental(self, days):
        return (self.rental_rate * days) + self.helmet_fee  # Rental + helmet fee

# Subclass for Truck
class Truck(Vehicle):
    def __init__(self, model, rental_rate, cargo_fee):
        super().__init__(model, rental_rate)
        self.cargo_fee = cargo_fee  # Additional cargo fee

    def calculate_rental(self, days):
        return (self.rental_rate * days) + self.cargo_fee  # Rental + cargo fee

# **Testing the Implementation**
car = Car("BMW X5", 3000, 500)
bike = Bike("Yamaha R15", 500, 50)
truck = Truck("Tata 407", 7000, 2000)

print(f"{car.model} Rental for 3 days: ₹{car.calculate_rental(3)}")
print(f"{bike.model} Rental for 3 days: ₹{bike.calculate_rental(3)}")
print(f"{truck.model} Rental for 3 days: ₹{truck.calculate_rental(3)}")

