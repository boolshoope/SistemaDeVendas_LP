from tkinter import *

from views.gui import login
from views.gui.gerir import funcionarios
from views.gui.gerir import produtos, categorias
from views.gui.gerir import visualizarVendas


class MainMenu:
    def __init__(self):
        mainMenu.geometry("1366x768")
        mainMenu.resizable(False, False)
        mainMenu.title("Sistema de Gestao de vendas")
        mainMenu.iconbitmap("public/imagens/shopping_cart.ico")

        self.label1 = Label(mainMenu)
        self.label1.place(relx=0, rely=0, width=1366, height=768)
        self.img = PhotoImage(file="public/imagens/main.png")
        self.label1.configure(image=self.img)

        self.btnCaixa = Button(mainMenu, command=btnCaixaMain_click)
        self.btnCaixa.place(x=431, y=312, width=143, height=143)
        self.btnCaixa.configure(relief="flat")
        self.btnCaixa.configure(overrelief="flat")
        self.btnCaixa.configure(activebackground="#ffffff")
        self.btnCaixa.configure(cursor="hand2")
        self.btnCaixa.configure(foreground="#ffffff")
        self.btnCaixa.configure(background="#ffffff")
        self.btnCaixa.configure(borderwidth="0")
        self.img2 = PhotoImage(file="public/imagens/btnEmpMain.png")
        self.btnCaixa.configure(image=self.img2)

        self.btnAdmin = Button(mainMenu, command=btnAdmMain_click)
        self.btnAdmin.place(x=771, y=312, width=143, height=143)
        self.btnAdmin.configure(relief="flat")
        self.btnAdmin.configure(overrelief="flat")
        self.btnAdmin.configure(activebackground="#ffffff")
        self.btnAdmin.configure(cursor="hand2")
        self.btnAdmin.configure(foreground="#ffffff")
        self.btnAdmin.configure(background="#ffffff")
        self.btnAdmin.configure(borderwidth="0")
        self.img3 = PhotoImage(file="public/imagens/btnAdmMain.png")
        self.btnAdmin.configure(image=self.img3)


# Menu do adiministrador
class AdminMenu:
    def __init__(self):
        admMenu.geometry("1366x768")
        admMenu.resizable(False, False)
        admMenu.title("Sistema de Gestao de vendas")
        admMenu.iconbitmap("public/imagens/shopping_cart.ico")

        self.label1 = Label(admMenu)
        self.label1.place(relx=0, rely=0, width=1366, height=768)
        self.img2 = PhotoImage(file='public/imagens/menuBG.png')
        self.label1.configure(image=self.img2)

        self.lblUser = Label(admMenu, text="Administrador")
        self.lblUser.place(relx=0.046, rely=0.056, width=105, height=30)
        self.lblUser.configure(font="-family {Calibri} -size 12")
        self.lblUser.configure(background="#FE6B61", foreground="#ffffff")

        self.imgBtnProdutos = PhotoImage(file='public/imagens/btnProdutos.png')
        self.btnProdutos = Button(admMenu, image=self.imgBtnProdutos, bg='#3d8ea2', activebackground='#3d8ea2')
        self.btnProdutos.place(relx=0.14, rely=0.4, width=150, height=150)
        self.btnProdutos.configure(borderwidth="0", cursor="hand2")
        self.btnProdutos.configure(command=btnProdutos_click)

        self.imgBtnEmpregados = PhotoImage(file='public/imagens/btnEmpregados.png')
        self.btnEmpregados = Button(admMenu, image=self.imgBtnEmpregados, bg='#3d8ea2', activebackground='#3d8ea2')
        self.btnEmpregados.place(relx=0.338, rely=0.4, width=150, height=150)
        self.btnEmpregados.configure(borderwidth="0", cursor="hand2")
        self.btnEmpregados.configure(command=btnFuncionarios_click)

        self.imgBtnCategorias = PhotoImage(file='public/imagens/btnCategorias.png')
        self.btnCategorias = Button(admMenu, image=self.imgBtnCategorias, bg='#3d8ea2', activebackground='#3d8ea2')
        self.btnCategorias.place(relx=0.536, rely=0.4, width=150, height=150)
        self.btnCategorias.configure(borderwidth="0", cursor="hand2")
        self.btnCategorias.configure(command=btnCategorias_click)

        self.btnVisualizarVendas = Button(admMenu, text="Visualizar Vendas")
        self.btnVisualizarVendas.place(relx=0.732, rely=0.508, width=150, height=150)
        self.btnVisualizarVendas.configure(background="#ffffff", activebackground="#DEE2E6", borderwidth="0")
        self.btnVisualizarVendas.configure(cursor="hand2")
        self.btnVisualizarVendas.configure(font="-family {Calibri} -size 12")
        self.btnVisualizarVendas.configure(command=btnVisualizarVendas_click)

        self.imgBtnVendas = PhotoImage(file='public/imagens/btnVendas.png')
        self.btnVendas = Button(admMenu, image=self.imgBtnVendas, bg='#3d8ea2', activebackground='#3d8ea2')
        self.btnVendas.place(relx=0.14, rely=0.63, width=150, height=150)
        self.btnVendas.configure(borderwidth="0", cursor="hand2")


def btnProdutos_click():
    admMenu.withdraw()
    produtos.callProdutos()


def btnFuncionarios_click():
    admMenu.withdraw()
    funcionarios.callFuncionarios()


def btnCategorias_click():
    admMenu.withdraw()
    categorias.callCategorias()


def btnReVisible():
    admMenu.deiconify()


def btnVisualizarVendas_click():
    admMenu.withdraw()
    visualizarVendas.callVendas()


def startAdmMenu():
    global admMenu
    global page
    admMenu = Tk()
    page = AdminMenu()
    admMenu.mainloop()


def startMainMenu():
    global mainMenu
    global page
    mainMenu = Tk()
    page = MainMenu()
    mainMenu.mainloop()


def btnAdmMain_click():
    mainMenu.destroy()
    login.callLogin("adm")


def btnCaixaMain_click():
    mainMenu.destroy()
    login.callLogin("caixa")
