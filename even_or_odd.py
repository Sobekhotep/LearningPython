def run():
    # residual calculation operator

    number = input("Enter a number, and I'll tell you if it's even or odd: ")
    number = int(number)

    if number % 2 == 0:
        print("\nThe number " + str(number) + " is even.")
    else:
        print("\nThe number " + str(number) + " is odd.")


if __name__ == "__main__":
    run()

