def run():
    # Ticket price depends of age

    phrase = "\nPlease enter your age and I will tell you the price of the " \
              "ticket. \nDo not write the word 'age', just numbers." \
             " Write 'quit' when done. "

    flag = True
    while flag:
        # The message of user
        message = input(phrase)
        # Here we want to catch an exception ValueError
        # if user will enter not integer value
        try:
            # The word 'quit' will end the program
            if message == 'quit':
                flag = False
            # Lower is how much tickets to any age
            elif 0 < int(message) <= 3:
                print("\nFor kids free of charge!")
            elif 3 < int(message) <= 12:
                print("\nThe price of tickets is 10$ for children over three years "
                      "old.")
            elif 12 < int(message) <= 100:
                print("\nThe price of tickets is 15$.")
            elif int(message) > 100:
                print("\nFor this kind of people is free of charge! "
                      "Please, bring your passport when you buy tickets.")
            else:
                print("\nYou just think you're the most clever person on Earth, "
                      "don't you?")

        except ValueError:
            print("\nYou must enter only numbers.")


if __name__ == "__main__":
    run()

