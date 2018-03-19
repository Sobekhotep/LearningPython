def run():

    def build_person(first_name, last_name, age=''):
        """Return dictionary with information about person."""
        person = {'first': first_name, 'last': last_name}
        if age:
            person['age'] = age
        return person

    builded_person = build_person('jimi', 'hendrix', 27)
    print(builded_person)


if __name__ == "__main__":
    run()

