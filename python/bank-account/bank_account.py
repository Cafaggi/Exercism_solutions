import threading


class BankAccount(object):
    balance = 0
    oppened = False  # False closed

    def __init__(self):
        self.balance = 0
        self._lock = threading.Lock()

    def get_balance(self):
        if self.oppened == False:
            raise ValueError("Account Closed!")
        return self.balance

    def open(self):
        if self.oppened == 1:
            raise ValueError("Account Is Already Open!")
        with self._lock:
            self.oppened = True

    def deposit(self, amount):
        if self.oppened == False:
            raise ValueError("Account Closed!")
        if amount < 0:
            raise ValueError("Negative deposits are not allowed!")
        with self._lock:
            copy = self.balance
            copy += amount
            self.balance = copy

    def withdraw(self, amount):
        if self.oppened == False:
            raise ValueError("Account Closed!")
        if amount > self.balance:
            raise ValueError("Insufficient funds to withdraw!")
        if amount < 0:
            raise ValueError("Negative withdrawls are not allowed!")
        with self._lock:
            copy = self.balance
            copy -= amount
            self.balance = copy

    def close(self):
        if self.oppened == False:
            raise ValueError("Account Closed!")
        with self._lock:
            self.oppened = False
            self.balance = 0