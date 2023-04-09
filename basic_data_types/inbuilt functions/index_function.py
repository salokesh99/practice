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

print(int(total_price),bin(total_price))
print(total_price.__str__())
print(total_price.__repr__())
print(str(total_price))
print(total_price)
# x = repr(total_price)
# print(x)
