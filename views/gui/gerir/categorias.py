from time import strftime
from tkinter import *
from tkinter import ttk, messagebox

from views.gui.adicionar import addCategoria
from views.gui import menu
from views.gui.editar import editCategoria


class Categorias:
    def __init__(self, top=None):
        top.geometry("1366x768")
        top.resizable(0, 0)
        top.title("Categorias")
        top.protocol("WM_DELETE_WINDOW", X_windowsBtn_click)

        self.label1 = Label(mainLbl)
        self.label1.place(relx=0, rely=0, width=1366, height=768)
        self.img = PhotoImage(file="public/imagens/gCategorias.png")
        self.label1.configure(image=self.img)

        self.message = Label(mainLbl, text="ADMIN")
        self.message.place(relx=0.046, rely=0.055, width=136, height=30)
        self.message.configure(font="-family {Poppins} -size 10")
        self.message.configure(background="#ffffff", foreground="#000000", anchor="w")

        self.clock = Label(mainLbl)
        self.clock.place(relx=0.9, rely=0.065, width=102, height=36)
        self.clock.configure(font="-family {Poppins Light} -size 12")
        self.clock.configure(foreground="#000000")
        self.clock.configure(background="#ffffff")

        self.txtIdProduto = Entry(mainLbl)
        self.txtIdProduto.place(relx=0.040, rely=0.286, width=240, height=28)
        self.txtIdProduto.configure(font="-family {Poppins} -size 12")
        self.txtIdProduto.configure(relief="flat")

        self.txtNomeProduto = Entry(mainLbl)
        self.txtNomeProduto.place(relx=0.040, rely=0.399, width=240, height=28)
        self.txtNomeProduto.configure(font="-family {Poppins} -size 12")
        self.txtNomeProduto.configure(relief="flat")

        self.btnProcurarId = Button(mainLbl, text="Procurar", command=self.btnProcurarIdCategorias_click)
        self.btnProcurarId.place(relx=0.229, rely=0.289, width=76, height=23)
        self.btnProcurarId.configure(relief="flat", overrelief="flat", borderwidth="0")
        self.btnProcurarId.configure(background="#023e8a", activebackground="#023e8a", foreground="#ffffff")
        self.btnProcurarId.configure(cursor="hand2", font="-family {Poppins SemiBold} -size 12")

        self.btnProcurarNome = Button(mainLbl, text="Procurar", command=self.btnProcurarNomeCategorias_click)
        self.btnProcurarNome.place(relx=0.229, rely=0.4, width=76, height=23)
        self.btnProcurarNome.configure(relief="flat", overrelief="flat", borderwidth="0")
        self.btnProcurarNome.configure(background="#023e8a", activebackground="#023e8a", foreground="#ffffff")
        self.btnProcurarNome.configure(cursor="hand2", font="-family {Poppins SemiBold} -size 12")

        self.btnLogout = Button(mainLbl, text="Logout")
        self.btnLogout.place(relx=0.035, rely=0.106, width=76, height=23)
        self.btnLogout.configure(relief="flat", overrelief="flat", borderwidth="0")
        self.btnLogout.configure(background="#CF1E14", activebackground="#CF1E14", foreground="#ffffff")
        self.btnLogout.configure(cursor="hand2", font="-family {Poppins SemiBold} -size 12")

        self.btnAddCategoria = Button(mainLbl, text="ADICIONAR CATEGORIA")
        self.btnAddCategoria.place(relx=0.052, rely=0.535, width=306, height=28)
        self.btnAddCategoria.configure(relief="flat", overrelief="flat", borderwidth="0")
        self.btnAddCategoria.configure(background="#023e8a", activebackground="#023e8a", foreground="#ffffff")
        self.btnAddCategoria.configure(cursor="hand2", font="-family {Poppins SemiBold} -size 12")
        self.btnAddCategoria.configure(command=btnAddCategoria_click)

        self.btnUpdCategoria = Button(mainLbl, text="ACTUALIZAR CATEGORIA", command=self.btnUpdCategoria_click)
        self.btnUpdCategoria.place(relx=0.052, rely=0.605, width=306, height=28)
        self.btnUpdCategoria.configure(relief="flat", overrelief="flat", borderwidth="0")
        self.btnUpdCategoria.configure(background="#023e8a", activebackground="#023e8a", foreground="#ffffff")
        self.btnUpdCategoria.configure(cursor="hand2", font="-family {Poppins SemiBold} -size 12")

        self.btnDelCategoria = Button(mainLbl, text="REMOVER CATEGORIA", command=self.btnDelCategoria_click)
        self.btnDelCategoria.place(relx=0.052, rely=0.675, width=306, height=28)
        self.btnDelCategoria.configure(relief="flat", overrelief="flat", borderwidth="0")
        self.btnDelCategoria.configure(background="#023e8a", activebackground="#023e8a", foreground="#ffffff")
        self.btnDelCategoria.configure(cursor="hand2", font="-family {Poppins SemiBold} -size 12")

        self.btnSair = Button(mainLbl, text="Voltar", command=sair)
        self.btnSair.place(relx=0.135, rely=0.885, width=76, height=23)
        self.btnSair.configure(relief="flat", overrelief="flat", borderwidth="0")
        self.btnSair.configure(background="#CF1E14", activebackground="#CF1E14", foreground="#ffffff")
        self.btnSair.configure(cursor="hand2", font="-family {Poppins SemiBold} -size 12")

        self.scrollbarx = Scrollbar(mainLbl, orient=HORIZONTAL)
        self.scrollbary = Scrollbar(mainLbl, orient=VERTICAL)
        self.tree = ttk.Treeview(mainLbl)
        self.tree.place(relx=0.307, rely=0.203, width=880, height=550)
        self.tree.configure(
            yscrollcommand=self.scrollbary.set, xscrollcommand=self.scrollbarx.set
        )
        self.tree.configure(selectmode="extended")

        self.tree.bind("<<TreeviewSelect>>", self.on_tree_select)

        self.scrollbary.configure(command=self.tree.yview)
        self.scrollbarx.configure(command=self.tree.xview)

        self.scrollbary.place(relx=0.954, rely=0.203, width=22, height=548)
        self.scrollbarx.place(relx=0.307, rely=0.924, width=884, height=22)

        self.tree.configure(
            columns=(
                "idCategoria",
                "Nome"
            )
        )

        self.tree.heading("idCategoria", text="idCategoria", anchor=W)
        self.tree.heading("Nome", text="Nome", anchor=W)

        self.tree.column("#0", stretch=NO, minwidth=0, width=0)
        self.tree.column("#1", stretch=NO, minwidth=0, width=80)

        # self.DisplayData()

    sel = []

    def on_tree_select(self, Event):
        self.sel.clear()
        for i in self.tree.selection():
            if i not in self.sel:
                self.sel.append(i)

    def time(self):
        string = strftime("%H:%M:%S %p")
        self.clock.config(text=string)
        self.clock.after(1000, self.time)

    def btnProcurarIdCategorias_click(self):
        print("btnProcurarIdCategoria clicado")

    def btnProcurarNomeCategorias_click(self):
        print("btnProcurarNomeCategoria clicado")

    def btnUpdCategoria_click(self):
        editCategoria.callEditCategoria()

    def btnDelCategoria_click(self):
        print("btnDel clicado")


def sair():
    sure = messagebox.askyesno("Voltar", "Tem a certeza que deseja voltar?", parent=mainLbl)
    if sure:
        mainLbl.destroy()
        menu.btnReVisible()


def X_windowsBtn_click():
    sure = messagebox.askyesno("Sair", "Tem a certeza que deseja fechar o programa?", parent=mainLbl)
    if sure:
        exit()


def btnAddCategoria_click():
    addCategoria.callAddCategoria()


def callCategorias():
    global mainLbl
    global page3
    mainLbl = Toplevel()
    page3 = Categorias(mainLbl)
    page3.time()
    mainLbl.mainloop()
