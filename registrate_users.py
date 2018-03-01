def run():
    # construction with if/elif/else

    current_users = [
        'maks', 'fil', 'vlad',
        'olga', 'sveta', 'lilia',
        'bob', 'anton', 'mich',
        'denis', 'alla'
        ]

    new_users = [
        'natali', 'kostya', 'fil',
        'rob', 'sveta', 'andy',
        'MICH', 'deNis', 'Alla'
        ]

    for user in new_users:
        if user.lower() in current_users:
            print("We are sorry, but login " + '"' + user + '"' +
                  " is already used, please choose another")
        else:
            print("Dear " + user.title() + "! This login is available to "
                                           "registration!")


if __name__ == "__main__":
    run()

