def run():
    # while loop for found and delete elements

    pets = ['dog', 'cat', 'parrot', 'goldfish', 'cat', 'cat', 'rabbit', 'cat']
    print(pets)
    while 'cat' in pets:
        pets.remove('cat')
    print(pets)


if __name__ == "__main__":
    run()

