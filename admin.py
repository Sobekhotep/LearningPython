from users import User

class Admin(User):
    """Позволяет зарегистрировать администратора"""
    def __init__(self, first_name, last_name, male, age, nationality, privileges=['add messages', 'delete users', 'ban users']):
        super().__init__(first_name, last_name, male, age, nationality)
        self.privileges = privileges

    def show_privileges(self):
        """Выводит сообщение о привилегиях администратора"""
        print("The Aministrator " + "is allowed to " + ', '.join(self.privileges) + ".")

