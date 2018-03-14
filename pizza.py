def run():
    # Preservation of information about the ordered pizza

    # The message that will appear in dialog with user
    prompt = '\nPlease, enter toppings you want to order to pizza:'
    prompt += '\n(Enter "quit" when you complete the order.)  '

    # User order list
    order = []

    # Toppings in menu
    default_toppings = [
        'mushrooms', 'cheese', 'salami', 'green olive',
        'pineapples', 'tomatoes', 'black olive']

    topping = ""

    while topping != 'quit':
        topping = input(prompt)
        topping = topping.lower()
        if topping == 'quit':
            break
        elif topping not in default_toppings:
            print("Sorry, but we can not to add the " + topping + " in you order.")
        elif topping in order:
            print("You already ordered the " + topping + ". Please attend!")
        else:
            print("The " + topping + " is in your order now!")
            order.append(topping)

    pizza = {
        'crust': 'thick',
        'toppings': order
    }

    # Order description
    if len(order) >= 1:
        print("You ordered a " + pizza['crust'] + "-crust pizza " +
              "with the following toppings:")

        for topping in pizza['toppings']:
            print("\t" + topping.title())


if __name__ == "__main__":
    run()

