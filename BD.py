import psycopg2


class BD:
    def __init__(self):
        self.conn = psycopg2.connect("host=localhost dbname=Taller2 user=postgres password=postgres")
        self.cur = self.conn.cursor()

    def existNick(self, nick) -> bool:
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

    ###########################################

    def getPlayerDataArray(self, nick):
        self.cur.execute("SELECT * FROM jugador WHERE nick = %s", (nick, ))
        return self.cur.fetchone()

    def getAvatarFromPlayer_Array(self, nick):
        self.cur.execute("SELECT ptos_ataque, ptos_exp, ptos_velocidad, ptos_vida FROM avatar WHERE  nick = %s", (nick, ))
        return self.cur.fetchone()

    def getCantReports(self, nick):
        self.cur.execute("SELECT count(nick_reportado) FROM reporta_jugador WHERE nick_reportado = %s "
                         "GROUP BY nick_reportado", (nick, ))
        return self.cur.fetchone()

    def getReporte(self, nick_reporta, nick_reportado):
        self.cur.execute("SELECT * FROM reporta_jugador WHERE nick_reporta = %s AND nick_reportado = %s", (nick_reporta, nick_reportado, ))
        return  self.cur.fetchone()

    def registerPlayer(self, nick):
        self.cur.execute("INSERT INTO jugador (baneado_s_n, nick) VALUES (FALSE, %s)", (nick, ))
        self.conn.commit()

    def registerAvatar(self, nick, attack_points, exp_points, velocity_points, life_points):
        self.cur.execute("INSERT INTO avatar (nick, ptos_exp, ptos_velocidad, ptos_vida, ptos_ataque) "
                         "VALUES (%s, %s, %s, %s, %s)", (nick, exp_points, velocity_points, life_points, attack_points, ))
        self.conn.commit()

    def registerAdmin(self, nick):
        self.cur.execute("INSERT INTO administrador (nick) VALUES (%s)", (nick, ))
        self.conn.commit()

    def reportar(self, nick_reporta, nick_reportado):
        self.cur.execute("INSERT INTO reporta_jugador (nick_reportado, nick_reporta) VALUES (%s, %s)", (nick_reportado, nick_reporta, ))
        self.conn.commit()