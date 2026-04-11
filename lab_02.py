def apply_discount(price , discount):

    if not(isinstance(price , (int , float))):
        return "The price should be a number"
    
    if not(isinstance(discount , (int , float))):
        return "The discount should be a number"
    
    if price <= 0:
        return "The price should be greater than 0"
    
    if  discount < 0 or discount > 100:
        return "The discount should be between 0 and 100"

    else:
        discount = price * discount / 100
        final_price = price - discount
        return final_price

print(apply_discount('twenty',30))
print(apply_discount(100,'ten'))
print(apply_discount(0,100))
print(apply_discount(50,-30))
print(apply_discount(50,120))
print(apply_discount(100,20))
print(apply_discount(200,50))
print(apply_discount(50,0))
print(apply_discount(10,100))
print(apply_discount(74.5,20.0))