class Smartphone:

    def __init__(self, device, brand):
        self.device = device
        self.brand = brand

    def desc(self):
        print( f'{self.device} of {self.brand} supports A14')


phone = Smartphone('phone', 'samdung')
phone.desc()