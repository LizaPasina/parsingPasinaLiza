class Phone:
    def __init__(self, name: str, price: str, url: str):
        self.name = name
        self.price = price
        self.url = url


class PhoneList:
    def __init__(self):
        self.phones_list = []

    def add(self, phones: Phone):
        self.phones_list.append(phones)
