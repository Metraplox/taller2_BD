from User import User


class Admin(User):
    def __init__(self, nickname, password, email, country, name1, name2, last_name1, last_name2):
        User.__init__(self, nickname, password, email, country, name1, name2, last_name1, last_name2)
