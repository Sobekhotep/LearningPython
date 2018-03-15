def run():
    # Begin with two lists: users to check
    # and an empty list for storing trusted users
    unconfirmed_users = ['alice', 'brian', 'candace']
    confirmed_users = []

    # Check each user while unchecked users remain
    # Each checked user moving in confirmed_users list
    while unconfirmed_users:
        current_user = unconfirmed_users.pop()

        print("Verifying user: " + current_user.title())
        confirmed_users.append(current_user)

    # Output all verifying users
    print("\nThe following users have been confirmed:")
    for confirmed_user in confirmed_users:
        print(confirmed_user.title())


if __name__ == "__main__":
    run()

