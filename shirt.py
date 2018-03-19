def run():

    def make_shirt(size='L', print_text='I love Python'):
        print("Your " + str(size) + "-size shirt is ready now!")
        print("There are " + '"' + print_text + '"' + " printing on your shirt.")

    make_shirt()
    make_shirt(print_text='Samsung', size='XL')


if __name__ == "__main__":
    run()

