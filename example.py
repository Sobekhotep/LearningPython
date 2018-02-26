def run():
    count_list = []

    for value in range(1, 11):
        count_list.append(value**3)

    print(count_list)

    count_list_2 = [value for value in range(1, 11)]
    for value in count_list_2[1:6]:
        print(value)


if __name__ == "__main__":
    run()

