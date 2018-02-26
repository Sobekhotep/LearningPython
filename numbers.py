def run():
    # construction with if/elif/else

    numbers = []
    for n in range(1, 10):
        numbers.append(n)
    for number in numbers:
        if number == 1:
            print(str(number) + "st")
        elif number == 2:
            print(str(number) + "nd")
        elif number == 3:
            print(str(number) + "rd")
        else:
            print(str(number) + "th")


if __name__ == "__main__":
    run()

