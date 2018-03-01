def run():
    # The list that contains type of pizza
    my_pizza = [
        'peperoni', 'neapolitan',
        'chicago', 'new york style',
        'sicilian'
        ]

    friend_pizza = my_pizza[:]
    my_pizza.append('italian')
    friend_pizza.append('siberian')

    print("My favorite pizzas are:")
    for my_favorit_pizza in my_pizza:
        print(my_favorit_pizza.title())

    print("\nMy friend's favorite pizzas are:")
    for friends_favorite_pizza in friend_pizza:
        print(friends_favorite_pizza.title())


if __name__ == "__main__":
    run()

