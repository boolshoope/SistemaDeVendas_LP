from tkinter import *


# classe do adiministrador
class AdminMenu:
    def __init__(self, top=None):
        top.geometry("1366x768")
        top.resizable(False, False)
        top.title("Sistema de Gestao de vendas")
        top.iconbitmap("imagens/shopping_cart.ico")

        self.label1 = Label(admMenu)
        self.label1.place(relx=0, rely=0, width=1366, height=768)

        self.lblUser = Label(admMenu, text="Administrador")
        self.lblUser.place(relx=0.046, rely=0.056, width=105, height=30)
        self.lblUser.configure(font="-family {Calibri} -size 12")
        self.lblUser.configure(background="#FE6B61", foreground="#ffffff")

        self.btnProdutos = Button(admMenu, text="Produtos")
        self.btnProdutos.place(relx=0.14, rely=0.508, width=146, height=63)
        self.btnProdutos.configure(background="#ffffff", activebackground="#DEE2E6", borderwidth="0")
        self.btnProdutos.configure(cursor="hand2")
        self.btnProdutos.configure(font="-family {Calibri} -size 12")

        self.btnEmpregados = Button(admMenu, text="Empregados")
        self.btnEmpregados.place(relx=0.338, rely=0.508, width=146, height=63)
        self.btnEmpregados.configure(background="#ffffff", activebackground="#DEE2E6", borderwidth="0")
        self.btnEmpregados.configure(cursor="hand2")
        self.btnEmpregados.configure(font="-family {Calibri} -size 12")

        self.button3 = Button(admMenu, text="Estatisticas")
        self.button3.place(relx=0.536, rely=0.508, width=146, height=63)
        self.button3.configure(background="#ffffff", activebackground="#DEE2E6", borderwidth="0")
        self.button3.configure(cursor="hand2")
        self.button3.configure(font="-family {Calibri} -size 12")

        self.btnVendas = Button(admMenu, text="Registar Vendas")
        self.btnVendas.place(relx=0.732, rely=0.508, width=146, height=63)
        self.btnVendas.configure(background="#ffffff", activebackground="#DEE2E6", borderwidth="0")
        self.btnVendas.configure(cursor="hand2")
        self.btnVendas.configure(font="-family {Calibri} -size 12")


admMenu = Tk()
page = AdminMenu(admMenu)
admMenu.mainloop()
