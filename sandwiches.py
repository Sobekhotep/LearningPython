def run():
    # Moving list elements from first list to second list

    print("Sorry, but there is no Pastrami in menu.")

    sandwich_orders = [
        'Bacon sandwich', 'PASTRAMI', 'Bagel toast', 'Baked bean', 'Barbecue',
        'Butterbrot', 'pastrami', 'Cheese', 'Cheesesteak', 'Chicken salad',
        'PastrAMI', 'Chili burger', 'Pastrami', 'Churrasco', 'PAStrami'
    ]
    formatted_sandwich_orders = []

    # Formatting elements from sandwiches_order to lower
    while sandwich_orders:
        formatted_name = sandwich_orders.pop(0).lower()
        formatted_sandwich_orders.append(formatted_name)

    finished_sandwiches = []

    while formatted_sandwich_orders:
        # Removing 'pastrami' from formatted_sandwich_order list
        if 'pastrami' in formatted_sandwich_orders:
            formatted_sandwich_orders.remove('pastrami')
        # We remove first sandwich in sandwich order list
        finished_sandwich = formatted_sandwich_orders.pop(0)
        print("I made you " + finished_sandwich.title() + ".")

        # and add them into finished_sandwiches list
        finished_sandwiches.append(finished_sandwich)

    print("\nI made you next sandwiches:")
    for sandwich in finished_sandwiches:
        print("\t" + str(1 + finished_sandwiches.index(sandwich)) + ". " +
              sandwich.title())


if __name__ == "__main__":
    run()

