# construction that contains dictionary and method keys()


def run():

    favorite_languages = {
        'jen': ['python', 'ruby'],
        'sarah': ['c'],
        'edward': ['ruby'],
        'phil': ['python', 'haskell']
    }

    for name, languages in favorite_languages.items():
        if len(languages) > 1:
            print("\n" + name.title() + "'s favorite languages are:")
        else:
            print("\n" + name.title() + "'s favorite language is:")
        for language in languages:
            print("\t" + language.title())

    """interview_list = ['albert', 'diana', 'jen', 'irina', 'phil']

    for name in favorite_languages.keys():
        if name in interview_list:
            print("Hello " + name.title() + "! Thank you for participating "
                                            "in the survey!")
        else:
            print("Hello " + name.title() + ", we invite you to participate"
                                            " in the survey.")

    friends = ['phil', 'sarah']
    for name in favorite_languages.keys():
        print(name.title())

        if name in friends:
            print("  Hi  " + name.title() +
                  ", I see your favorite language is " +
                  favorite_languages[name].title() + "!")"""


if __name__ == "__main__":
    run()

