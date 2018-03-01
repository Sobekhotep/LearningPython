# This module contains run code, construction name - main

from users import User, Admin


def run():
    admin = Admin('sarah', 'connor', 'female', 42, 'american')
    admin.show_privileges()
    admin.describe_user()


if __name__ == "__main__":
    run()

