def run():
    # This module contains example of entering user data
    # The loop while

    prompt = "\nTell me something, and I will repeat it back to you: "
    prompt += "\nEnter 'quit' to end the program. "

    active = True
    while active:
        message = input(prompt)

        if message == 'quit':
            active = False
        else:
            print(message)


if __name__ == "__main__":
    run()

