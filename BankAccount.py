
from datetime import datetime, timedelta
import time
import random
import shelve

class BankAccount:
    def __init__(self, account_id, fullname_owner, balance):
        self.account_id = account_id
        self.fullname_owner = fullname_owner
        self.balance = balance
        #self.created_at = datetime.now()
        self.created_at = datetime.now() - \
                          timedelta(minutes=random.randint(5, 25))
    def __str__(self):
        return f"BankAccount owner={self.fullname_owner} balance={self.balance}" +\
               f" \n   .. created at=[{self.created_at}]"

    def __repr__(self):
        return f"BankAccount({self.account_id}, '{self.fullname_owner}', {self.balance})"

    def __eq__(self, other):
        return self.balance == other.balance

    def __ne__(self, other):
        return not self == other

    def __gt__(self, other):
        return self.balance > other.balance

    def __le__(self, other):
        return not self > other

    def __lt__(self, other):
        return self.balance < other.balance

    def __ge__(self, other):
        if isinstance(other, int):
            return not self.balance < other
        elif isinstance(other, BankAccount):
            return not self.balance < other.balance
        raise TypeError('ge does not support this type', type(other))

    def __add__(self, other):
        if isinstance(other, BankAccount):
            new_account_id = random.randint(1000000, 9999999)
            new_full_name = f"{self.fullname_owner} and {other.fullname_owner}"
            new_balance = self.balance + other.balance
            new_account = BankAccount(new_account_id, new_full_name, new_balance)
            # new_account.created_at = ...
            return new_account

    def __sub__(self, other):
        return self.balance - other.balance

    def __min__(self, other):
        return self if self.balance < other.balance else other

    def __mul__(self, other):
        return self.balance * other.balance

    def __len__(self):
        return (datetime.now() - self.created_at).seconds // 60


## create manually the bank accounts
# b1 = BankAccount(8676230, 'arya stark', 28000)
# time.sleep(random.random() / 5)
# bg = BankAccount(6875533, 'golum', 28000)
# time.sleep(random.random() / 5)
# b2 = BankAccount(5979982, 'jon snow', 79011)

## read from file
sh = shelve.open('accounts')
b1 = sh['b1']
bg = sh['bg']
b2 = sh['b2']

## save to  file
# sh = shelve.open('accounts')
# sh['b1'] = b1
# sh['bg'] = bg
# sh['b2'] = b2

sh.close()

joined_account = b1 + b2
print(b1)
print(b2)
print(b1 - b2)
print('min', min(b1, b2))
print(datetime.now())
print(len(b1))
#  min(5, 4, 3, 1 -1)
#
# print(b1)
# print(bg)
# print(b2)
#
# print([b1, b2, bg])
# print(repr(bg))
#
# bg2 = BankAccount(6875533, 'golum', 28000)
#
# print('b1 == bg', b1 == bg)
# # print('b1 != bg', b1 != bg)  # False
#
# # print(b1 >= "100")
#
