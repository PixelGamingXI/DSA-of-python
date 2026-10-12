
# class Car:
#     def __init__(self):
#         self.acc = False
#         self.clutch = False
#         self.brk = False

#     def Start(self):
#         self.acc = True
#         self.clutch = True
#         self.brk = True
#         print("Car Started")

# Car1 = Car()
# Car1.Start()

#-------------------------------------------------------------------------------------------------------------------------------------------------------------




class Account:
    def __init__(self, bal, acc):
        self.balance = bal
        self.acc_no = acc

    def debit(self, amount):
        self.balance -= amount
        print("Rs.", amount, "was debited" )
        print("Total Balance = ", self.get_balance())


    def credit(self, amount):
        self.balance += amount
        print("Rs.", amount, "was credited" )
        print("Total Balance = ", self.get_balance())

    def get_balance(self):
        return self.balance



acc1 =Account(10000, 12345)
acc1.debit(2500)
acc1.credit(5000)


print(t"try some cheese")
