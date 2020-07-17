class User:
    def __init__(self, nickname, password, email, country, name1, name2, last_name1, last_name2):
        self.nickname = nickname
        self.password = password
        self.email = email
        self.country = country
        self.arrayCompleteName = [name1, name2, last_name1, last_name2]

    def validate_password(self, password) -> bool:
        if self.password == password:
            return True
        else:
            return False
