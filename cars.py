def run():
    # Simple examples of constructions "if/elif/else"

    cars = [
        'audi', 'bmw',
        'subaru', 'toyota'
        ]

    for car in cars:
        if car == 'bmw':
            print(car.upper())
        else:
            print(car.title())


if __name__ == "__main__":
    run()

