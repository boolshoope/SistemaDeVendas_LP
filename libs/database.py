from itertools import takewhile

import mysql.connector

from config import config
from libs.objects import *

lstCateg = list()
lstFunc = list()
lstLogin = list()


class Database:
    mydb = None

    def conectar(self):
        self.mydb = mysql.connector.connect(host=config.HOST, user=config.USER, password=config.PASSWORD,
                                            port=config.PORT, database=config.DB)

    def lerCategoria(self):
        lstCateg.clear()
        cursor.execute('select * from categoria')
        categ = cursor.fetchall()
        for c in categ:
            lstCateg.append(Categoria(c[0], c[1]))

    def lerFuncionario(self):
        lstFunc.clear()
        cursor.execute('select * from funcionario')
        func = cursor.fetchall()
        for f in func:
            lstFunc.append(Funcionario(f[0], f[1], f[2], f[3], f[4], f[5], f[6], f[7], f[8], f[9], f[10]))

    def lerLogin(self):
        lstLogin.clear()
        cursor.execute('select * from login')
        login = cursor.fetchall()
        for f in login:
            lstLogin.append(Login(f[0], f[1], f[2], f[3]))

    def lerBD(self):
        self.lerCategoria()
        self.lerFuncionario()
        self.lerLogin()

    def addCateg(self, idCateg, nome):
        insert = "INSERT INTO categoria(idCategoria, nome) VALUES(%s,%s)"
        cursor.execute(insert, [int(idCateg), nome])
        self.mydb.commit()

    def updCateg(self, idCateg, nome):
        update = "UPDATE categoria SET nome = %s WHERE idCategoria = %s"
        cursor.execute(update, [nome, int(idCateg)])
        self.mydb.commit()

    def delete(self, tableName, id):
        delete = "DELETE FROM {} WHERE id{} = %s".format(tableName, tableName)
        cursor.execute(delete, [id])
        self.mydb.commit()


db = Database()
db.conectar()
cursor = db.mydb.cursor()
db.lerBD()
