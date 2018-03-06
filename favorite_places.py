def run():
    # favorite places of my friends

    favorite_places = {

        'mozyr': ['denis', 'slava'],
        'zhitkovichi': ['andrey', 'slava'],
        'gorki': ['sanya', 'denis', 'dimas']
    }

    for place, man in favorite_places.items():
        if 'denis' in man:
            print("Denis loves " + place.title() + ".")
        if 'slava' in man:
            print("Slava loves " + place.title() + ".")
        if 'andrey' in man:
            print("Andrey loves " + place.title() + ".")
        if 'sanya' in man:
            print("Sanya loves " + place.title() + ".")
        if 'dimas' in man:
            print("Dimas loves " + place.title() + ".")


if __name__ == "__main__":
    run()

