from django import template

register = template.Library()


@register.filter(name='is_in_cart')
def is_in_cart(item, cart):
    keys = cart.keys()
    for id in keys:
        # print(id, item.id)
        # print(type(id), type(item.id))
        if int(id) == item.id:
            return True
    return False
    # print(keys)
    # print(item, cart)
    # return True

@register.filter(name='cart_quantity')
def cart_quantity(item, cart):
    keys= cart.keys()
    for id in keys:
        if int(id) == item.id:
            return cart.get(id)
    return 0

@register.filter(name='total_base_price')
def total_base_price(item, cart):
    return item.base_price * cart_quantity(item, cart)

@register.filter(name='total_borrow_price')
def total_borrow_price(item, cart):
    return item.borrow_price * cart_quantity(item, cart)

@register.filter(name="in_total")
def in_total(products, cart):
    sum_of_base_price = 0
    sum_of_borrow_price = 0
    in_total_price = 0
    for totalbaseprice in products:
        sum_of_base_price += total_base_price(totalbaseprice, cart)

    for totalborrowprice in products:
       sum_of_borrow_price += total_borrow_price(totalborrowprice, cart)

    in_total_price = sum_of_base_price + sum_of_borrow_price
    return in_total_price
    
@register.filter(name="currency")
def currency(number):
    return " ৳"+str(number)


@register.filter(name='multiply')
def multiply(number1, number2): 
    return number1*number2

@register.filter(name='add')
def multiply(number1, number2): 
    return number1+number2