def run():

    def city_country(city_name, country_name):
        # Return formatted city name
        format_name = city_name + ", " + country_name
        return format_name.title()

    city_list = []
    while True:
        print("Tell me please, were do you come from?")
        user_city = city_country(input("Print your city: "),
                                 input("Print your country: "))
        city_list.append(user_city)
        print("Do you want to continue?")
        message = input("Print 'q' if you want to stop: ")
        if message == 'q':
            break
    print(city_list)


if __name__ == "__main__":
    run()

