def run():
    # Preservation of information about the ordered pizza

    pizza = {
        'crust': 'thick',
        'toppings': ['mushrooms', 'extra cheese']
    }

    # Order description
    print("You ordered a " + pizza['crust'] + "-crust pizza " +
          "with the following toppings:")

    for topping in pizza['toppings']:
        print("\t" + topping)


if __name__ == "__main__":
    run()

