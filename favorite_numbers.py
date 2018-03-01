def run():
    # the dict with favorite numbers of my friends

    favorite_nums = {
        'pavel': 1,
        'vanya': 15,
        'sergey': 22,
        'stas': 30,
        'sanya': 25
        }

    for key, value in favorite_nums.items():
        print("Favorite number of " + key.title() + " is " + str(value) + ".")


if __name__ == "__main__":
    run()

