from Admin import Admin
from Avatar import Avatar
from BD import BD
from Player import Player
from User import User
from random import randint

baseDatos = BD()
current_user = None  # Usuario logeado


def generateAvatar() -> Avatar:
    velocityPoints = randint(1, 10)
    attackPoints = randint(1, 3)
    lifePoints = randint(10, 20)

    avatar: Avatar = Avatar(attackPoints, lifePoints, 0, velocityPoints)

    return avatar


def report(nick_reportar) -> bool:
    if baseDatos.existNick(nick_reportar):
        baseDatos.reportar(current_user, nick_reportar)
        return True
    else:
        return False


def closeSesion():
    current_user = None
    startMenu()


##########################################################################

# Return Boolean, True: correct login, False: incorrect password or nick
def tryLogin(nick, password):
    user_data_array = baseDatos.getUserDataArray(nick, password)  # es nulo si no encuentra usuario con este nick y pass
    if user_data_array is not None:
        current_user = User(user_data_array[0], user_data_array[1], user_data_array[2], user_data_array[3],
                            user_data_array[4], user_data_array[5], user_data_array[6], user_data_array[7])
        return True
    else:
        return False


def register(nick, password, email, country, array_complete_name):
    if baseDatos.existNick(nick):
        print("*Nick en uso, intente con otro*")
    else:
        baseDatos.registerUser(nick, password, email, country, array_complete_name)
        print("*Usuario creado*")


def menuLog():
    print("\n    *Inicio de sesión*\n")
    nick = input("nickname: ")
    password = input("password: ")

    if tryLogin(nick, password):
        print("\n    *Bienvenido " + nick + ", has iniciado sesión*")
    else:
        print("\n    **CONTRASEÑA O NICKNAME INCORRECTO**\n")
        startMenu()


def menuRegister():
    print("\n    *Registrate*\n")
    nick = input("        Nickname: ")

    if baseDatos.existNick(nick):
        print("\n    **NICK EN USO, INTENTE CON OTRO**\n")
        menuRegister()
    else:
        password = input("        Password: ")
        email = input("           Email: ")
        country = input("            País: ")
        name1 = input("      1er nombre: ")
        name2 = input("      2do nombre: ")
        lastname1 = input("Apellido materno: ")
        lastname2 = input("Apellido paterno: ")

        register(nick, password, email, country, [name1, name2, lastname1, lastname2])
        current_user = User(nick, password, email, country, name1, name2, lastname1, lastname2)

        print("    **TE HAS REGISTRADO EXITOSAMENTE " + current_user.nickname + "**")
        print()

        startMenu()


def startMenu():
    print("    *Bienvenido*\n"
          "1 - Iniciar sesión\n"
          "2 - Registrarse\n")

    option = input("opción: ")

    if option == "1":
        menuLog()
    elif option == "2":
        menuRegister()
    else:
        print("\n    **OPCIÓN INVÁLIDA**\n")
        startMenu()


def main():
    startMenu()


main()
