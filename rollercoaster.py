def run():
    # entering users data with function int()

    height = input("How tall are you, in inches? ")
    height = int(height)

    if height >= 36:
        print("\nYou're tall enough to ride!")
    else:
        print("\nYou'll be able to ride when you're a little order.")


if __name__ == "__main__":
    run()

