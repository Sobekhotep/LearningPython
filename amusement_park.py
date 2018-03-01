def run():
    # constructions if/elif/else

    age = 64
    if age < 4:
        price = 0
    elif age < 18:
        price = 5
    elif age < 65:
        price = 10
    elif age >= 65:
        price = 5
    print("Your admission cost is $" + str(price) + ".")


if __name__ == "__main__":
    run()

