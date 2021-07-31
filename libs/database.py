import mysql.connector

from config import config


class Database():
    def __init__(self):
        print("DB")

    def connect(self):
        try:
            data = mysql.connector.connect(
                host=config.HOST,
                user=config.USER,
                password=config.PASSWORD,
                port=config.PORT,
                database=config.DB
            )

            query = data.cursor()
            query.execute('SELECT * FROM produto')

            categoria = query.fetchall()

            for cat in categoria:
                print(cat)
                print('nome'+cat[1])
                print('descricao'+cat[2])
                print('preco'+cat[3])
                print('stock'+cat[4])
                print('codBarras'+cat[5])
                print('idCategoria'+cat[6])


        except ModuleNotFoundError:
            print("algo deu errado")


db = Database()
db.connect()
