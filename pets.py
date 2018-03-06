def run():
    # pets dictionary

    pets = {
        'willie': {
            'animal': 'dog',
            'master': 'anna'
        },
        'barsik': {
            'animal': 'cat',
            'master': 'vanya'
        },
        'sunny': {
            'animal': 'parrot',
            'master': 'bob'
        }
    }

    for pet_name, pet_info in pets.items():
        print("\nPet name: " + pet_name.title())
        kind_animal = pet_info['animal']
        pet_master = pet_info['master']
        print("\tIt's a " + kind_animal + ".")
        print("\tThe name of it's master is " + pet_master.title())


if __name__ == "__main__":
    run()

