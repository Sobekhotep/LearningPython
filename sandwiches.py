def run():
    # Moving list elements from first list to second list

    print("Sorry, but there is no Pastrami in menu.")

    sandwich_orders = [
        'Bacon sandwich', 'Pastrami', 'Bagel toast', 'Baked bean', 'Barbecue',
        'Butterbrot', 'Pastrami', 'Cheese', 'Cheesesteak', 'Chicken salad',
        'Pastrami', 'Chili burger', 'Pastrami', 'Churrasco', 'Pastrami'
    ]

    # Removing 'Pastrami' from sandwiches_order
    while 'Pastrami' in sandwich_orders:
        sandwich_orders.remove('Pastrami')

    finished_sandwiches = []

    while sandwich_orders:
        # We remove first sandwich in sandwich order list
        finished_sandwich = sandwich_orders.pop(0)
        print("I made you " + finished_sandwich + ".")

        # and add them into finished_sandwiches list
        finished_sandwiches.append(finished_sandwich)

    print("\nI made you next sandwiches:")
    for sandwich in finished_sandwiches:
        print("\t" + sandwich)


if __name__ == "__main__":
    run()

