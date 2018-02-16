class User():
    """Основные атрибуты пользователей"""
    def __init__(self, first_name, last_name, male, age, nationality):
        self.first_name = first_name
        self.last_name = last_name
        self.male = male
        self.age = age
        self.nationality = nationality
        self.login_attempts = 0

    def describe_user(self):
        """Выводит сводку с информацией с информацией о пользователе"""
        print("\nThe user's name is " + self.first_name.title() + " " + self.last_name.title()
               + ". " + "\nThe male of user is " + self.male + ". " + "\nUser is "
               + str(self.age) + " years old. " + "\nUser is " + self.nationality + ".")

    def greet_user(self):
        """Выводит приветствие пользователя"""
        print("\nHello, dear " + self.first_name.title() + " " + self.last_name.title() + "!")

    def increment_login_attempts(self):
        """Увеличивает количество попыток входа пользователя в систему на 1"""
        self.login_attempts += 1

    def reset_login_attempts(self):
        """Обнуляет количество попыток входа пользователя в систему"""
        self.login_attempts = 0


class Admin(User):
    """Позволяет зарегистрировать администратора"""
    def __init__(self, first_name, last_name, male, age, nationality, privileges=['add messages', 'delete users', 'ban users']):
        super().__init__(first_name, last_name, male, age, nationality)
        self.privileges = privileges

    def show_privileges(self):
        """Выводит сообщение о привилегиях администратора"""
        print("The Aministrator " + "is allowed to " + ', '.join(self.privileges) + ".")

