def run():
    # the dict with favorite numbers of my friends

    favorite_nums = {
        'pavel': [1],
        'vanya': [15, 21],
        'sergey': [22, 23, 228],
        'stas': [30, 10],
        'sanya': [25, 128]
        }

    for key, value in favorite_nums.items():
        if len(value) > 1:
            print("\nFavorite numbers of " + key.title() + " is:")
            for number in value:
                print("\t" + str(number))
        else:
            print("\nFavorite number of " + key.title() + " is:")
            for number in value:
                print("\t" + str(number))


if __name__ == "__main__":
    run()

