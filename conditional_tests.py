# Модуль, содержащий проверки с Булевыми операторами


def run():

    first_string = 'first string'
    second_string = 'second string'
    third_string = 'first string'
    fourth_string = 'FIRST STRING'

    test_list = ['one', 'two', 'three',
                 'four', 'five', 'nail',
                 'rabbit', 'Obi-Van', 'neutron',
                 42, 'year', 'obstacle',
                 'ONE', 'TWO', 'NAIL',
                 '42', 'tibbar', 'SEVEN'
                 ]

    if first_string.lower() == fourth_string.lower() \
            or third_string > fourth_string and \
            tird_string != fourth_string:

        """print(first_string == second_string)
        print(first_string > second_string)
        print(first_string < second_string)
        print(first_string > fourth_string)
        print(first_string < fourth_string)
        print(second_string == third_string)
        print(first_string == third_string)
        print(first_string.lower() == fourth_string.lower())"""

        print("OK")

    if 'one' and 'two' in test_list:
        print('awesome!')
    if test_list[-1].lower() == 'seven':
        print('I like you, Python!')

    print(test_list[0].upper() == test_list[-6])
    print((str(test_list[9])) == test_list[-3])


if __name__ == "__main__":
    run()

