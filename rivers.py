def run():
    # dictionary with rivers

    rivers = {
        'nile': 'egypt',
        'pripyat': 'belarus',
        'amazon': 'brazil'
    }

    for river, country in rivers.items():
        print("The " + river.title() + " runs trough " +
              country.title() + ".")

    for river in rivers.keys():
        print(river.title())

    for country in rivers.values():
        print(country.title())


if __name__ == "__main__":
    run()

