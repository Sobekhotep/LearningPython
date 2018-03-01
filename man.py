def run():
    # this module contains examples of dict
    # information about a person

    man_info = {
        'first_name': 'john',
        'last_name': 'connor',
        'age': 13,
        'city': 'LA'
        }

    print(man_info['first_name'].title())
    print(man_info['last_name'].title())
    print(man_info['age'])
    print(man_info['city'].upper())


if __name__ == "__main__":
    run()

