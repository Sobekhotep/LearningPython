def run():
    # this module contains examples of dict
    # information about a person

    john_info = {
        'first_name': 'john',
        'last_name': 'connor',
        'age': 13,
        'city': 'los angeles'
        }

    sarah_info = {
        'first_name': 'sarah',
        'last_name': 'connor',
        'age': 33,
        'city': 'los angeles'
        }

    kyle_info = {
        'first_name': 'kyle',
        'last_name': 'rives',
        'age': 22,
        'city': 'los angeles'
        }

    info_list = [john_info, sarah_info, kyle_info]

    for user in info_list:
        print("\nUser's information is: ")
        for key, value in sorted(user.items(), reverse=True):
            if type(value) is int:
                print("\t" + key.title() + ": " + str(value) + ".")
            else:
                print("\t" + key.title() + ": " + value.title() + ".")


if __name__ == "__main__":
    run()

