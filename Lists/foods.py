def run():
    food_list = ['pizza', 'frighten eggs', 'ice cream', 'bananas', 'vegetables',
                 'fruits', 'milk', 'meat', 'hamburger', 'beans', 'tea']
    print("The first three items in the list are:")
    for food in food_list[:3]:
        print(food.title())
    print("The middle four items in the list are:")
    for food in food_list[3:7]:
        print(food.title())
    print("The last four items in the list are:")
    for food in food_list[7:]:
        print(food.title())


if __name__ == "__main__":
    run()