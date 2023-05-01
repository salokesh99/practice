class Total:
    
    def __init__(self, quantity, price):
        self.quantity = quantity
        self.price = price
    
    def __index__(self):
        return self.price * self.quantity
    
    def __str__(self):
        print(f'Quantity- {self.quantity}')
        print(f'Price-{ self.price}')

        return f'Quantity- {self.quantity} Price-{ self.price}'
    

total_price = Total(5,5)

print('10',int(total_price),bin(total_price))
print('11',total_price.__str__())
print('12',total_price.__repr__())
print('13',str(total_price))
print('14',total_price)
# x = repr(total_price)
# print(x)
