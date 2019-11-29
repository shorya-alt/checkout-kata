class Checkout:
    a_individualPrice = 50
    b_individualPrice = 30
    c_individualPrice = 20
    d_individualPrice = 15
    a_disc_price = 130
    b_disc_price = 45

    def __init__(self):
      self.product = input("Enter the products and get total bill")
    def getquantity(self):
         a_count = sum(map(lambda x : 1 if 'A' in x else 0, self.product))
         b_count = sum(map(lambda x: 1 if 'B' in x else 0, self.product))
         c_count = sum(map(lambda x: 1 if 'C' in x else 0, self.product))
         d_count = sum(map(lambda x: 1 if 'D' in x else 0, self.product))
         self.dict_count = {"A":a_count,"B":b_count,"C":c_count,"D": d_count}

    def getprice(self):
        self.a_price = 0
        self.b_price = 0
        self.c_price = 0
        self.d_price = 0
        self.getquantity()
        #print(self.dict_count)
        for key in self.dict_count.keys():
            key_value = self.dict_count[key]
            if key == 'A':
                multipler = key_value//3
                remainder = key_value%3
                self.a_price = multipler*self. a_disc_price + remainder * self.a_individualPrice
            if key == 'B':
                multipler = key_value//2
                remainder = key_value%2
                self.b_price = multipler * self.b_disc_price + remainder * self.b_individualPrice
            if key == 'C':
                self.c_price = key_value * self.c_individualPrice
            if key == 'D':
                self.d_price = key_value * self.d_individualPrice
    def totalbill(self):
        self.getprice()
        total = self.a_price + self.b_price + self.c_price + self.d_price
        return total


checkout = Checkout()
print(checkout.totalbill())