class LowCreditsError(Exception): pass
class LowStockError(Exception): pass
class MissingItemError(Exception): pass


class User:
    users = {}

    def __init__(self, name, password, credit):
        self.name = name
        self.password = password
        self.credit = credit
        self.items = {}

    @classmethod
    def create(cls, name, password, credit=100):
        if name in cls.users:
            raise ValueError('name already exist')
        cls.users[name] = cls(name, password, credit)

    def login(self, password):
        if password == self.password:
            return True

    def logout(self, password):
        if password == self.password:
            return True

    def buy(self, item, price):
        if self.credit >= price:
            self.credit -= price
            if item in self.items:
                self.items[item] += 1
            else:
                self.items[item] = 1
        raise LowCreditsError("price:{} > credits:{}".format(price, self.credit))

    def sell(self, item, price):
        if item in self.items:
            if self.items[item] > 0:
                self.credit += price
                self.items[item] -= 1
            else:
                raise LowStockError
        else:
            raise MissingItemError
