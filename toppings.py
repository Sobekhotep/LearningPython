def run():
    # An example of construction with "in"

    available_toppings = [
        'mushrooms', 'olives', 'green peppers',
        'pepperoni', 'pineapple', 'extra cheese'
        ]

    requested_toppings = [
        'mushrooms', 'french fries', 'extra cheese'
        ]

    for requested_topping in requested_toppings:
        if requested_topping in available_toppings:
            print("Adding " + requested_topping + ".")
        else:
            print("Sorry, we don't have " + requested_topping + ".")
    print("\nFinished making your pizza!")


if __name__ == "__main__":
    run()

