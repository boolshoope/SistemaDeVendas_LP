import mysql.connector

from config import config


class Database():
    def __init__(self):
        print("")

    def connect(self):
        try:
            data = mysql.connector.connect(config.HOST, config.USER, config.PASSWORD, config.PORT, config.DB)
        except ModuleNotFoundError:
            print("algo deu errado")
