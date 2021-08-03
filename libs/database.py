import sqlite3

import mysql.connector

from config import config
from libs.objects import *

lstCateg = list()
lstFunc = list()
lstLogin = list()
lstProd = list()
lstVendas = list()


class Database:
    mydb = None

    def conectar(self):
        self.mydb = mysql.connector.connect(
            host=config.HOST,
            user=config.USER,
            password=config.PASSWORD,
            port=config.PORT,
            database=config.DB
        )

    def lerCategoria(self):
        lstCateg.clear()
        cursor.execute('select * from categoria')
        categ = cursor.fetchall()
        for c in categ:
            lstCateg.append(Categoria(c[0], c[1]))

    def lerVendas(self):
        lstVendas.clear()
        cursor.execute('select * from venda')
        venda = cursor.fetchall()
        for v in venda:
            lstVendas.append(Venda(v[0], v[1], v[2], v[3]))

    def lerFuncionario(self):
        lstFunc.clear()
        cursor.execute('select * from funcionario')
        func = cursor.fetchall()
        for f in func:
            lstFunc.append(Funcionario(f[0], f[1], f[2], f[3], f[4], f[5], f[6], f[7], f[8], f[9], f[10]))

    def lerProduto(self):
        lstProd.clear()
        cursor.execute('select * from produto')
        prod = cursor.fetchall()
        for p in prod:
            lstProd.append(Produto(p[0], p[1], p[3], p[4], p[6], p[2], p[5]))

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
        self.lerProduto()
        self.lerVendas()

    def addProd(self, nomePro, descricao, preco, qtdStock, codBarras, listCtg):
        insert = "INSERT INTO produto(nome, descricao, preco, stock, codBarras, idCategoria) " \
                 "VALUES(?,?,?,?,?,?)"
        cursor.execute(insert, [nomePro, descricao, preco, qtdStock, codBarras, listCtg])
        dbb.commit()

    def addCateg(self, nome):
        insert = "INSERT INTO categoria(nome) VALUES(?)"
        cursor.execute(insert, [nome])
        dbb.commit()

    def addFunc(self, pNome, apelido, dataNascimento, sexo, nrBI, bairro, nrCasa, quarteirao, tel1, tel2):
        insert = "INSERT INTO funcionario(pNome, apelido, dataNascimento, sexo, nrBI, bairro, nrCasa," \
                 "quarteirao, tel1, tel2) VALUES(?,?,?,?,?,?,?,?,?,?)"
        cursor.execute(insert, [pNome, apelido, dataNascimento, sexo, nrBI, bairro, nrCasa, quarteirao, tel1, tel2])
        dbb.commit()

    def addLogin(self, username, password, nivel):
        id = lstFunc[len(lstFunc) - 1].idFunc
        insert = "INSERT INTO login(idFuncionario, username, password, nivel) VALUES(?,?,?,?)"
        cursor.execute(insert, [id,username, password, nivel])
        dbb.commit()

    def addVenda(self, data, preco, idFunc):
        insert = "INSERT INTO venda(data, precoTotal, idFuncionario) VALUES(?,?,?)"
        cursor.execute(insert, [data, preco, idFunc])
        dbb.commit()

    def getIdVenda(self):
        id = lstVendas[len(lstVendas) - 1].idVenda
        return id

    def addProdVenda(self, idVenda, idProd, quant):
        insert = "INSERT INTO prodVenda(idVenda, idProduto, quantidade) VALUES(?,?,?)"
        cursor.execute(insert, [idVenda, idProd, quant])
        dbb.commit()

    def updProd(self, idProd, nomePro, descricao, preco, qtdStock, codBarras, listCtg):
        update = "UPDATE produto SET nome = ?, descricao = ?, preco = ?, stock = ?, codBarras = ?," \
                 "idCategoria = ? WHERE idProduto = ?"
        cursor.execute(update, [nomePro, descricao, preco, qtdStock, codBarras, listCtg, int(idProd)])
        dbb.commit()

    def updCateg(self, idCateg, nome):
        update = "UPDATE categoria SET nome = ? WHERE idCategoria = ?"
        cursor.execute(update, [nome, int(idCateg)])
        dbb.commit()

    def updFunc(self, idFunc, pNome, apelido, dataNascimento, sexo, nrBI, bairro, nrCasa, quarteirao, tel1, tel2):
        update = "UPDATE funcionario SET pNome = ?, apelido = ?, dataNascimento = ?, sexo = ?, nrBI = ?, bairro = ?," \
                 "nrCasa = ?, quarteirao = ?, tel1 = ?, tel2 = ? WHERE idFuncionario = ?"
        cursor.execute(update, [pNome, apelido, dataNascimento, sexo, nrBI, bairro, nrCasa, quarteirao, tel1, tel2,
                                int(idFunc)])
        dbb.commit()

    def updLogin(self, idFunc, username, password, nivel):
        update = "UPDATE login SET username = ?, password = ?, nivel = ? WHERE idFuncionario = ?"
        cursor.execute(update, [username, password, nivel, int(idFunc)])
        dbb.commit()

    def delete(self, tableName, id):
        delete = "DELETE FROM {} WHERE id{} = ?".format(tableName, tableName)
        cursor.execute(delete, [id])
        # self.mydb.commit()
        dbb.commit()


db = Database()
with sqlite3.connect("libs/vendas.db") as dbb:
    cursor = dbb.cursor()
# db.conectar()
# cursor = db.mydb.cursor()
db.lerBD()
