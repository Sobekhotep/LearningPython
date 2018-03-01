def run():
    # constructions with if/elif/else

    age = 1
    if age < 2:
        human = 'newborn baby'
    elif 2 <= age < 4:
        human = 'baby'
    elif 4 <= age < 13:
        human = 'child'
    elif 13 <= age < 20:
        human = 'teenager'
    elif 20 <= age < 65:
        human = 'adult'
    elif age >= 65:
        human = 'old'
    print("Now human is " + human + ".")


if __name__ == "__main__":
    run()

