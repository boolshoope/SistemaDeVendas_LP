class Categoria:
    def __init__(self, idCateg, nome):
        self.idCateg = idCateg
        self.nome = nome


class Funcionario:
    def __init__(self, idFunc, pNome, apelido, dataNascimento, sexo, nrBI, bairro, nrCasa, quarteirao, tel1, tel2):
        self.idFunc = idFunc
        self.pNome = pNome
        self.apelido = apelido
        self.dataNascimento = dataNascimento
        self.sexo = sexo
        self.nrBI = nrBI
        self.bairro = bairro
        self.nrCasa = nrCasa
        self.quarteirao = quarteirao
        self.tel1 = tel1
        self.tel2 = tel2


class Login:
    def __init__(self, idFunc, username, password, nivel):
        self.idFunc = idFunc
        self.username = username
        self.password = password
        self.nivel = nivel


class Produto:
    def __init__(self, idProd, nomeProd, preco, stock, idCat):
        self.idProd = idProd
        self.nomeProd = nomeProd
        self.preco = preco
        self.stock = stock
        self.idCat = idCat
