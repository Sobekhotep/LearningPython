def run():
    # An example of construction with "not in"

    banned_users = ['andrew', 'ostap', 'taras']
    user = 'marie'

    if user not in banned_users:
        print(user.title() + ", you can post a response if you wish.")


if __name__ == "__main__":
    run()

