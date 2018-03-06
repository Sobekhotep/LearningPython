def run():
    # construction with multi-level dictionary

    cities = {
        'zhitkovichi': {
            'country': 'belarus',
            'population': 12000,
            'fact': 'clean air'
        },
        'gomel': {
            'country': 'belarus',
            'population': 500000,
            'fact': 'regional polyclinic'
        },
        'salavat': {
            'country': 'russian',
            'population': 50000,
            'fact': 'chemistry plant'
        }
    }

    for city, information in cities.items():
        print("\nCity name is: " + city.title() + "\nInformation about " +
              city.title() + ":")
        print("\tCountry: " + information['country'].title())
        print("\tIn " + city.title() + " there are " +
              str(information['population']) + " people.")
        print("\t" + city.title() + " has a " + information['fact'] + ".")


if __name__ == "__main__":
    run()

