from User import User
from Avatar import Avatar


class Player(User):
    def __init__(self, nickname, password, email, country, name1, name2, last_name1, last_name2, baneado_s_n , avatar: Avatar):
        self.baneado_s_n: bool = baneado_s_n
        self.avatar: Avatar = avatar

        User.__init__(self, nickname, password, email, country, name1, name2, last_name1, last_name2)
