from time import strftime
from tkinter import *
from tkinter import ttk, messagebox

from libs import database
from views.gui.adicionar import addFuncionario
from views.gui import menu
from views.gui.editar import editFuncionario


class Funcionario:
    def __init__(self, top=None):
        top.geometry("1366x768")
        top.resizable(0, 0)
        top.title("Funcionarios")
        top.protocol("WM_DELETE_WINDOW", X_windowsBtn_click)

        self.label1 = Label(mainLbl)
        self.label1.place(relx=0, rely=0, width=1366, height=768)
        self.img = PhotoImage(file="public/imagens/gFuncionarios.png")
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

        self.txtIdFuncionario = Entry(mainLbl)
        self.txtIdFuncionario.place(relx=0.040, rely=0.286, width=240, height=28)
        self.txtIdFuncionario.configure(font="-family {Poppins} -size 12")
        self.txtIdFuncionario.configure(relief="flat")

        self.txtNomeFuncionario = Entry(mainLbl)
        self.txtNomeFuncionario.place(relx=0.040, rely=0.399, width=240, height=28)
        self.txtNomeFuncionario.configure(font="-family {Poppins} -size 12")
        self.txtNomeFuncionario.configure(relief="flat")

        self.btnProcurarId = Button(mainLbl, text="Procurar", command=self.btnProcurarIdFuncionario_click)
        self.btnProcurarId.place(relx=0.229, rely=0.289, width=76, height=23)
        self.btnProcurarId.configure(relief="flat", overrelief="flat", borderwidth="0")
        self.btnProcurarId.configure(background="#023e8a", activebackground="#023e8a", foreground="#ffffff")
        self.btnProcurarId.configure(cursor="hand2", font="-family {Poppins SemiBold} -size 12")

        self.btnProcurarNome = Button(mainLbl, text="Procurar", command=self.btnProcurarNomeFuncionario_click)
        self.btnProcurarNome.place(relx=0.229, rely=0.4, width=76, height=23)
        self.btnProcurarNome.configure(relief="flat", overrelief="flat", borderwidth="0")
        self.btnProcurarNome.configure(background="#023e8a", activebackground="#023e8a", foreground="#ffffff")
        self.btnProcurarNome.configure(cursor="hand2", font="-family {Poppins SemiBold} -size 12")

        self.btnLogout = Button(mainLbl, text="Logout")
        self.btnLogout.place(relx=0.035, rely=0.106, width=76, height=23)
        self.btnLogout.configure(relief="flat", overrelief="flat", borderwidth="0")
        self.btnLogout.configure(background="#CF1E14", activebackground="#CF1E14", foreground="#ffffff")
        self.btnLogout.configure(cursor="hand2", font="-family {Poppins SemiBold} -size 12")

        self.btnAddFuncionario = Button(mainLbl, text="ADICIONAR FUNCIONARIO")
        self.btnAddFuncionario.place(relx=0.052, rely=0.535, width=306, height=28)
        self.btnAddFuncionario.configure(relief="flat", overrelief="flat", borderwidth="0")
        self.btnAddFuncionario.configure(background="#023e8a", activebackground="#023e8a", foreground="#ffffff")
        self.btnAddFuncionario.configure(cursor="hand2", font="-family {Poppins SemiBold} -size 12")
        self.btnAddFuncionario.configure(command=btnAddProdutos_click)

        self.btnUpdFuncionario = Button(mainLbl, text="ACTUALIZAR FUNCIONARIO", command=self.btnUpdFuncionario_click)
        self.btnUpdFuncionario.place(relx=0.052, rely=0.605, width=306, height=28)
        self.btnUpdFuncionario.configure(relief="flat", overrelief="flat", borderwidth="0")
        self.btnUpdFuncionario.configure(background="#023e8a", activebackground="#023e8a", foreground="#ffffff")
        self.btnUpdFuncionario.configure(cursor="hand2", font="-family {Poppins SemiBold} -size 12")

        self.btnDelFuncionario = Button(mainLbl, text="REMOVER FUNCIONARIO", command=self.btnDelFuncionario_click)
        self.btnDelFuncionario.place(relx=0.052, rely=0.675, width=306, height=28)
        self.btnDelFuncionario.configure(relief="flat", overrelief="flat", borderwidth="0")
        self.btnDelFuncionario.configure(background="#023e8a", activebackground="#023e8a", foreground="#ffffff")
        self.btnDelFuncionario.configure(cursor="hand2", font="-family {Poppins SemiBold} -size 12")

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
                "idFuncionario",
                "Apelido",
                "Nome",
                "Sexo",
                "Nivel",
            )
        )

        self.tree.heading("idFuncionario", text="idFuncionario", anchor=W)
        self.tree.heading("Apelido", text="Apelido", anchor=W)
        self.tree.heading("Nome", text="Nome", anchor=W)
        self.tree.heading("Sexo", text="Sexo", anchor=W)
        self.tree.heading("Nivel", text="Nivel", anchor=W)

        self.tree.column("#0", stretch=NO, minwidth=0, width=0)
        self.tree.column("#1", stretch=NO, minwidth=0, width=80)
        self.tree.column("#2", stretch=NO, minwidth=0, width=260)
        self.tree.column("#3", stretch=NO, minwidth=0, width=100)
        self.tree.column("#4", stretch=NO, minwidth=0, width=120)

        self.DisplayData()

    sel = []

    def on_tree_select(self, Event):
        self.sel.clear()
        for i in self.tree.selection():
            if i not in self.sel:
                self.sel.append(i)

    def DisplayData(self):
        self.tree.delete(*self.tree.get_children())
        for i in range(len(database.lstFunc)):
            sexo = ""
            nivel = ""
            if database.lstFunc[i].sexo == 'M':
                sexo = "Masculino"
            elif database.lstFunc[i].sexo == 'F':
                sexo = "Feminino"

            for j in range(len(database.lstLogin)):
                if database.lstFunc[i].idFunc == database.lstLogin[j].idFunc:
                    nivel = database.lstLogin[j].nivel

            self.tree.insert('', 'end', values=(database.lstFunc[i].idFunc, database.lstFunc[i].apelido, database.lstFunc[i].pNome,
                                                sexo, nivel))

    def time(self):
        string = strftime("%H:%M:%S %p")
        self.clock.config(text=string)
        self.clock.after(1000, self.time)

    def btnProcurarIdFuncionario_click(self):
        val = []
        for i in self.tree.get_children():
            val.append(i)
            for j in self.tree.item(i)["values"]:
                val.append(j)

        if self.txtIdFuncionario.get() == "":
            messagebox.showerror("Erro!!", "Id Funcionario Invalido.", parent=mainLbl)
        else:
            for search in val:
                if search == int(self.txtIdFuncionario.get()):
                    self.tree.selection_set(val[val.index(search) - 1])
                    self.tree.focus(val[val.index(search) - 1])
                    messagebox.showinfo("Sucesso!!", "Id Funcionario: {} encotrado.".format(self.txtIdFuncionario.get())
                                        , parent=mainLbl)
                    break
            else:
                messagebox.showerror("Erro!!", "Id Funcionario: {} não encontrado.".format(self.txtIdFuncionario.get()),
                                     parent=mainLbl)

    def btnProcurarNomeFuncionario_click(self):
        val = []
        for i in self.tree.get_children():
            val.append(i)
            for j in self.tree.item(i)["values"]:
                val.append(j)

        for search in val:
            if search == self.txtNomeFuncionario.get():
                print()
                if val.index(search)%3 == 0:
                    self.tree.selection_set(val[val.index(search) - 3])
                    self.tree.focus(val[val.index(search) - 3])
                    messagebox.showinfo("Sucesso!!", "Nome: {} encotrado.".format(self.txtNomeFuncionario.get()),
                                        parent=mainLbl)
                    break
        else:
            messagebox.showerror("Erro!!", "Nome: {} não encontrado.".format(self.txtNomeFuncionario.get()),
                                 parent=mainLbl)

    def btnUpdFuncionario_click(self):
        editFuncionario.callEditFuncionario()

    def btnDelFuncionario_click(self):
        print("btnDelete clicado")


def sair():
    sure = messagebox.askyesno("Voltar", "Tem a certeza que deseja voltar?", parent=mainLbl)
    if sure:
        mainLbl.destroy()
        menu.btnReVisible()


def X_windowsBtn_click():
    sure = messagebox.askyesno("Sair", "Tem a certeza que deseja fechar o programa?", parent=mainLbl)
    if sure:
        exit()


def btnAddProdutos_click():
    addFuncionario.callAddFuncionario()


def callFuncionarios():
    global mainLbl
    global page3
    mainLbl = Toplevel()
    page3 = Funcionario(mainLbl)
    page3.time()
    mainLbl.mainloop()
