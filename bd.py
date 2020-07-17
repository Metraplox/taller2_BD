import psycopg2


class BD:
    def __init__(self):
        self.conn = psycopg2.connect("host=localhost dbname=Taller2 user=postgres password=postgres")
        self.cur = self.conn.cursor()

    def existNick(self, nick):
        self.cur.execute("SELECT * FROM usuario WHERE nick = %s;", (nick,))
        user = self.cur.fetchone()
        if user is not None:
            return True
        else:
            return False

    def getUserDataArray(self, nick, password):
        self.cur.execute("SELECT * FROM usuario WHERE nick = %s AND password = %s;", (nick, password, ))
        return self.cur.fetchone()

    def registerUser(self, nick, password, email, country, array_complete_name):
        self.cur.execute("INSERT INTO usuario (nick, password, email, pais, name1, name2, lastname1, lastname2)"
                         " VALUES (%s, %s, %s, %s, %s, %s, %s, %s);",
                         (nick, password, email, country, array_complete_name[0], array_complete_name[1],
                          array_complete_name[2], array_complete_name[3]))
        self.conn.commit()

