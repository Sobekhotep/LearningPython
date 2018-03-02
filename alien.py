def run():
    # this module contains examples of dict

    alien_0 = {'color': 'green', 'points': 5}
    print(alien_0)

    alien_0['x_position'] = 0
    alien_0['y_position'] = 25
    print(alien_0)

    new_points = alien_0['points']
    print("You just earned " + str(new_points) + " points!")


if __name__ == "__main__":
    run()

