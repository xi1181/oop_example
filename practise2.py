class Item:
    def __init__(self, n, p):
        self.name = n
        self.price = p


class ShoppingCart:
    def __init__(self):
        self.items = []
        self.total_cost = 0

    def add_item(self, item):
        self.items.append(item)
        self.total_cost += item.price
        print(item.name + " has been added to cart")

    def remove_item(self, item):
        if item in self.items:
            self.items.remove(item)
            self.total_cost -= item.price
            print(item.name + " has been removed from cart")
        else:
            print(item.name + " does not exist in cart")

    def empty_cart(self):
        self.items.clear()
        self.total_cost = 0
        print("Cart has been cleared")

    def print_cart_info(self):
        total_cost = 0
        keeptrack = []
        for item in self.items:
            if item not in keeptrack:
                item_count = self.items.count(item)
                print(f"{item.name} : ${item.price} x {item_count} = ${item.price * item_count}")
                keeptrack.append(item)
            total_cost += item.price
        print("--------------------------------")
        print(f"Total Cost : ${self.total_cost}")


choco = Item("Chocolate", 3)
candy = Item("Candy", 1)
apple = Item("Apple", 2)

cart = ShoppingCart()

cart.add_item(candy)
cart.add_item(apple)
cart.add_item(choco)
cart.add_item(choco)
cart.print_cart_info()

cart.empty_cart()
cart.print_cart_info()
