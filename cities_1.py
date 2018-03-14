def run():
    # example of construction with the loop while and command break

    prompt = "\nPlease enter the name of a city you have visited:"
    prompt += "\n(Enter 'quit' when you are finished.) "

    while True:
        city = input(prompt)

        if city == 'quit':
            break
        else:
            print("I'd love to go to " + city.title() + "!")


if __name__ == "__main__":
    run()

