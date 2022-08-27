def order_pizza(name, address, **toppings):
    print(f"order is for {name}")
    print(f"delivery to {address}")
    price = 20.99
    for key, value in toppings.items():
        price += 2.0
    print(f"total price is {price}")
    return price


order_pizza("jake", "1234 main st", jalapenos=True, extra_cheese=True, pepproni=True)
