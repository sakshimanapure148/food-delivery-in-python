
class Food:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def display(self):
        print(f"{self.name} - Rs.{self.price}")


class Restaurant:
    def __init__(self, name):
        self.name = name
        self.menu = []

    def add_food(self, food):
        self.menu.append(food)

    def show_menu(self):
        print(f"\n--- {self.name} Menu ---")
        for i, food in enumerate(self.menu, start=1):
            print(f"{i}. ", end="")
            food.display()


class Order:
    def __init__(self, customer):
        self.customer = customer
        self.items = []

    def add_item(self, food):
        self.items.append(food)
        print(f"{food.name} added to cart!")

    def show_bill(self):
        print("\n--- Order Bill ---")
        print("Customer:", self.customer)

        total = 0
        for food in self.items:
            print(f"{food.name}: Rs.{food.price}")
            total += food.price

        print("Total Amount: Rs.", total)
        print("Order placed successfully!")


# Create restaurant and food items
restaurant = Restaurant("Food Corner")

restaurant.add_food(Food("Pizza", 199))
restaurant.add_food(Food("Burger", 99))
restaurant.add_food(Food("Pasta", 149))
restaurant.add_food(Food("Sandwich", 79))

# Display menu
restaurant.show_menu()

# Take customer order
customer = input("\nEnter your name: ")
order = Order(customer)

while True:
    choice = input(
        "\nEnter food number (1-4) or 'done' to finish: "
    )

    if choice.lower() == "done":
        break

    if choice.isdigit():
        number = int(choice)

        if 1 <= number <= len(restaurant.menu):
            order.add_item(restaurant.menu[number - 1])
        else:
            print("Invalid food number!")
    else:
        print("Please enter a valid number or 'done'.")

# Display final bill
if order.items:
    order.show_bill()
else:
    print("Your cart is empty.")