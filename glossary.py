def run():
    # We have a one glossary, that contains keys and values with
    # Pythons expressions

    glossary = {
        'variable': 'is something that holds a value that may change',
        'string': 'is simply a list of characters in order',
        'tuple': 'is a sequence of values like a list but they are immutable',
        'cycle': 'is for loops',
        'function': 'is a convenient way to divide code into useful blocks',
    }

    # New couples of keys and values is added as a training
    glossary['list'] = 'is a set of elements following in a certain order'
    glossary['glossary'] = 'is a structure of data to combine information'
    glossary['str'] = 'is a string data'
    glossary['int'] = 'is a integer (not float) data'
    glossary['float'] = 'is float data'

    for key, value in glossary.items():
        print("\nKey: " + key)
        print("Value: " + value)


if __name__ == "__main__":
    run()

