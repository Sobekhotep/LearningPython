# This module contains a dictionary

from collections import OrderedDict


def run():
    favorite_languages = OrderedDict()
    favorite_languages['jen'] = 'python'
    favorite_languages['sarah'] = 'c'
    favorite_languages['edward'] = 'ruby'
    favorite_languages['phil'] = 'python'

    for name, language in favorite_languages.items():
        print(name.title() + "'s favorite language is " +
              language.title() + ".")


if __name__ == "__main__":
    run()

