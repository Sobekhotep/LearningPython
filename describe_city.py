def run():

    def describe_city(city_name, country_name='australia'):
        print(city_name.title() + " is in " + country_name.title())

    describe_city('melbourne')
    describe_city('zhitkovichi', 'belarus')
    describe_city(country_name='germany', city_name='bonn')


if __name__ == "__main__":
    run()

