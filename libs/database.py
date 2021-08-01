import mysql.connector

from config import config
from libs.objects import Categoria

lstCateg = list()


class Database:
    mydb = None

    def conectar(self):
        self.mydb = mysql.connector.connect(host=config.HOST, user=config.USER, password=config.PASSWORD,
                                            port=config.PORT, database=config.DB)

    def lerBD(self):
        cursor.execute('select * from categoria')
        categ = cursor.fetchall()
        for c in categ:
            lstCateg.append(Categoria(c[0], c[1]))

    def updCateg(self, idCateg, nome):
        update = "UPDATE categoria SET nome = %s WHERE idCategoria = %s"
        cursor.execute(update, [nome, int(idCateg)])
        self.mydb.commit()


db = Database()
db.conectar()
cursor = db.mydb.cursor()
db.lerBD()
