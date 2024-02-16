class Mpesa:
    def __init__(self, account_balance, phone_number):
        self.account_balance = account_balance
        self.phone_number = phone_number
        # method
    def send_money(self, amount, recipient):
        if self.account_balance >= amount:
           self.account_balance-= amount
           print(f"{amount} KSH sent to {recipient} successfully")
        else:
           print("Insufficient balance")

           # child classes
class PersonalMpesa(Mpesa):
    def __init__(self, account_balance, phone_number, id_number):
        super().__init__(account_balance,phone_number)
        self.id_number = id_number
    def buyairtime(self, amount):
      if self.account_balance>=amount:
         self.account_balance-=amount
         print(f"{amount} has successfully been credited")
      else:
         print("Insufficient balance")
            # child class 2
class BusinessMpesa(PersonalMpesa):
    def __init__(self, account_balance, phone_number, business_name, id_number):
        super().__init__(account_balance, phone_number, id_number)
        self.business_name = business_name
    def receiveMoney(self, amount, sender):
        self.account_balance += amount
        print(f"{amount} KES received from {sender}")


#Personal=PersonalMpesa(1450, 74545443,45000000)
#Personal.send_money(1000,1200)
#Personal.buyairtime(1000)


Mpesa = BusinessMpesa(1000,5665564,"Ian", 34653)
Mpesa.receiveMoney(1000, "sender")
Mpesa.buyairtime(10000)
