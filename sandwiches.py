def run():
    # Moving list elements from first list to second list

    sandwich_orders = [
        'Bacon sandwich', 'Bagel toast', 'Baked bean', 'Barbecue',
        'Butterbrot', 'Cheese', 'Cheesesteak', 'Chicken salad'
    ]

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

