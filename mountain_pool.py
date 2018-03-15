def run():
    # This construction requests name of participation and his answer

    responses = {}

    # Setting the continuation flag
    polling_active = True

    while polling_active:
        # Request users name and answer
        name = input("\nWhat is your name? ")
        response = input("Which mountain would you like to climb someday? ")

        # The answer saves in dictionary:
        responses[name] = response

        # Check the continuation of quiz
        repeat = input("Would you like to let another person respond? (yes/no) ")
        if repeat == 'no':
            polling_active = False

    # The quiz is done, output the results
    print("\n--- Poll Results ---")
    for name, response in responses.items():
        print(name + " would like to climb " + response + ".")


if __name__ == "__main__":
    run()

