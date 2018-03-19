def run():

    def get_formatted_name(first_name, last_name, middle_name=''):
        if middle_name:
            full_name = first_name + ' ' + middle_name + ' ' + last_name
        else:
            full_name = first_name + ' ' + last_name
        return full_name.title()

    musician = get_formatted_name(first_name=input("Print your first name: "),
                                  middle_name=input("Print your middle name: "),
                                  last_name=input("Print your last name: "))

    print(musician)


if __name__ == "__main__":
    run()

