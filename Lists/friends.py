# A list with names of my friends
def run():
    my_friends = ['pasha', 'artuh', 'stas', 'fedor', 'tarik']
    for name in my_friends:
        if name != 'artuh':
            print("\nHello my friend " + name.title() + "!")
        else:
            print("\nHello my dolboeb friend " + name.title() + "!")

if __name__ == "__main__":
    run()