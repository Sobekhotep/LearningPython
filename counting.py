def run():
    # an example with command continue

    number_list = []
    current_number = 0
    while current_number < 100:
        current_number += 1
        if current_number % 2 != 0:
            continue
        number_list.append(current_number)
    print(number_list)


if __name__ == "__main__":
    run()

