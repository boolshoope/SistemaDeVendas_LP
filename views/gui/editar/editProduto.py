from time import strftime
from tkinter import *
from tkinter import ttk, messagebox

from libs import database
from views.gui.gerir import produtos


class EditProduto:
    def __init__(self, idProd):
        self.idProd = idProd
        p_edit.geometry("1366x768")
        p_edit.resizable(0, 0)
        p_edit.title("Actualizar Produto")

        self.label1 = Label(p_edit)
        self.label1.place(relx=0, rely=0, width=1366, height=768)
        self.img = PhotoImage(file="public/imagens/addProduto.png")
        self.label1.configure(image=self.img)

        self.labelTop = Label(p_edit, text="Actualizar Produto")
        self.labelTop.place(x=485, y=75, width=400, height=70)
        self.labelTop.configure(font="-family {Poppins Bold} -size 31", background="#ffffff")

        self.clock = Label(p_edit)
        self.clock.place(relx=0.84, rely=0.065, width=102, height=36)
        self.clock.configure(font="-family {Poppins Light} -size 12")
        self.clock.configure(foreground="#000000", background="#ffffff")

        self.txtIdProduto = Entry(p_edit)
        self.txtIdProduto.place(relx=0.132, rely=0.296, width=450, height=30)
        self.txtIdProduto.configure(font="-family {Poppins} -size 12", relief="flat")


        self.txtNome = Entry(p_edit)
        self.txtNome.place(relx=0.132, rely=0.413, width=450, height=30)
        self.txtNome.configure(font="-family {Poppins} -size 12", relief="flat")

        self.r2 = p_edit.register(self.testint)

        self.txtDescricao = Entry(p_edit)
        self.txtDescricao.place(relx=0.132, rely=0.529, width=450, height=120)
        self.txtDescricao.configure(font="-family {Poppins} -size 12", relief="flat")

        self.txtPreco = Entry(p_edit)
        self.txtPreco.place(relx=0.527, rely=0.296, width=450, height=30)
        self.txtPreco.configure(font="-family {Poppins} -size 12", relief="flat")

        self.txtQuantStock = Entry(p_edit)
        self.txtQuantStock.place(relx=0.527, rely=0.413, width=450, height=30)
        self.txtQuantStock.configure(font="-family {Poppins} -size 12", relief="flat")
        self.txtQuantStock.configure(validate="key", validatecommand=(self.r2, "%P"))

        val = []
        for i in database.lstCateg:
            val.append(i.nome)

        self.listCboCategoria=val
        self.cboCategoria=ttk.Combobox(p_edit, values=self.listCboCategoria)
        self.cboCategoria.place(relx=0.527, rely=0.535, width=450, height=30)
        self.cboCategoria.configure(font="-family {Poppins} -size 12")

        self.txtCodBarras = Entry(p_edit)
        self.txtCodBarras.place(relx=0.527, rely=0.646, width=450, height=30)
        self.txtCodBarras.configure(font="-family {Poppins} -size 12", relief="flat")
        self.txtCodBarras.configure(validate="key", validatecommand=(self.r2, "%P"))

        self.btnActualizar = Button(p_edit, text="ACTUALIZAR", command=self.btnActualizar_click)
        self.btnActualizar.place(x=535, rely=0.836, width=120, height=34)
        self.btnActualizar.configure(relief="flat", overrelief="flat", borderwidth="0")
        self.btnActualizar.configure(background="#CF1E14", activebackground="#CF1E14", foreground="#ffffff")
        self.btnActualizar.configure(cursor="hand2", font="-family {Poppins SemiBold} -size 14")

        self.btnLimpar = Button(p_edit, text='LIMPAR', command=self.btnLimpar_click)
        self.btnLimpar.place(relx=0.526, rely=0.836, width=86, height=34)
        self.btnLimpar.configure(relief="flat", overrelief="flat", borderwidth="0")
        self.btnLimpar.configure(background="#CF1E14", activebackground="#CF1E14", foreground="#ffffff")
        self.btnLimpar.configure(cursor="hand2", font="-family {Poppins SemiBold} -size 14")

    def testint(self, val):
        if val.isdigit():
            return True
        elif val == "":
            return True
        return False

    def time(self):
        string = strftime("%H:%M:%S %p")
        self.clock.config(text=string)
        self.clock.after(1000, self.time)

    def preencherTxt(self):
        for i in range(len(database.lstProd)):
            if int(database.lstProd[i].idProd) == self.idProd:
                self.txtIdProduto.insert(0, database.lstProd[i].idProd)
                self.txtNome.insert(0, database.lstProd[i].nomeProd)
                self.txtDescricao.insert(0, database.lstProd[i].descricao)
                self.txtPreco.insert(0, database.lstProd[i].preco)
                self.txtQuantStock.insert(0, database.lstProd[i].stock)
                self.txtCodBarras.insert(0, database.lstProd[i].codBarras)

                for c in database.lstCateg:
                    if database.lstProd[i].idCat == c.idCateg:
                        self.cboCategoria.set(c.nome)


    def btnActualizar_click(self):
        nomePro = self.txtNome.get()
        descricao = self.txtDescricao.get()
        preco = self.txtPreco.get()
        qtdStock = self.txtQuantStock.get()
        codBarras = self.txtCodBarras.get()
        listCtg = self.cboCategoria.get()

        categ = None
        for c in database.lstCateg:
            if listCtg == c.nome:
                categ = c.idCateg

        database.db.updProd(self.idProd, nomePro, descricao, preco, qtdStock, codBarras, categ)
        messagebox.showinfo("Sucesso!", "As informações foram adicionadas com sucesso.", parent=p_edit)
        database.db.lerProduto()
        produtos.updList()
        p_edit.destroy()

    def btnLimpar_click(self):
        self.txtIdProduto.delete(0, END)
        self.txtNome.delete(0, END)
        self.txtDescricao.delete(0, END)
        self.txtPreco.delete(0, END)
        self.txtQuantStock.delete(0, END)
        # self.listCboCategoria.delete(0, END)
        # self.txtCodBarras.delete(0, END)


def callEditProdutos(idProd):
    global p_edit
    global page3
    p_edit = Toplevel()
    page3 = EditProduto(idProd)
    page3.time()
    page3.preencherTxt()
    p_edit.mainloop()