import threading


class BankAccount(object):
    balance = 0
    oppened = False  # False closed

    def __init__(self):
        self.balance = 0
        self._lock = threading.Lock()

    def get_balance(self):
        if not self.oppened : raise ValueError("Account is closed")
        return self.balance

    def open(self):
        if self.oppened: raise ValueError("Account is already open!")
        with self._lock:
            self.oppened = True

    def deposit(self, amount):
        if not self.oppened: raise ValueError("Account is closed")
        if amount < 0: raise ValueError("Negative deposits are not allowed")

        with self._lock:
            copy = self.balance
            copy += amount
            self.balance = copy

    def withdraw(self, amount):
        if not self.oppened: raise ValueError("Account is closed")
        if amount > self.balance: raise ValueError("Insufficient funds to withdraw")
        if amount < 0: raise ValueError("Negative withdrawls are not allowed")

        with self._lock:
            copy = self.balance
            copy -= amount
            self.balance = copy

    def close(self):
        if not self.oppened : raise ValueError("Account is closed")
        with self._lock:
            self.oppened = False
            self.balance = 0