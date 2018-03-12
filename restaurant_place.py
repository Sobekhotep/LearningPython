def run():
    # example with entering user data

    user_enter = input("Good day! How many persons would you like to reserve"
                       " a table for? ")
    user_enter = int(user_enter)

    if user_enter > 8:
        print("Sorry, but you'll have to wait a bit.")
    else:
        print("Your table is ready!")


if __name__ == "__main__":
    run()

