def run():
    # Write your name and I will greet you

    prompt = "If you tell us who are, we can personalize the message you see."
    prompt += "\nWhat is your first name? "

    name = input(prompt)
    print("\nHello, " + name.title() + "!")


if __name__ == "__main__":
    run()

