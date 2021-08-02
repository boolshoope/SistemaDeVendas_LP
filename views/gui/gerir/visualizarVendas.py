from time import strftime
from tkinter import *
from tkinter import ttk, messagebox

from views.gui import menu
from libs import database
from libs.database import Database

import mysql.connector


class Vendas:
    def __init__(self):
        mainLbl.geometry("1366x768")
        mainLbl.resizable(0, 0)
        mainLbl.title("Visualizar Vendas")
        mainLbl.protocol("WM_DELETE_WINDOW", X_windowsBtn_click)

        self.label1 = Label(mainLbl)
        self.label1.place(relx=0, rely=0, width=1366, height=768)
        self.img = PhotoImage(file="public/imagens/visVendas.png")
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

        self.txtData = Entry(mainLbl)
        self.txtData.place(relx=0.040, rely=0.286, width=240, height=28)
        self.txtData.configure(font="-family {Poppins} -size 12")
        self.txtData.configure(relief="flat")

        self.btnProcurarData = Button(mainLbl, text="Procurar", command=self.btnProcurarDataVenda_click)
        self.btnProcurarData.place(relx=0.229, rely=0.289, width=76, height=23)
        self.btnProcurarData.configure(relief="flat", overrelief="flat", borderwidth="0")
        self.btnProcurarData.configure(background="#023e8a", activebackground="#023e8a", foreground="#ffffff")
        self.btnProcurarData.configure(cursor="hand2", font="-family {Poppins SemiBold} -size 12")

        self.btnLogout = Button(mainLbl, text="Logout")
        self.btnLogout.place(relx=0.035, rely=0.106, width=76, height=23)
        self.btnLogout.configure(relief="flat", overrelief="flat", borderwidth="0")
        self.btnLogout.configure(background="#CF1E14", activebackground="#CF1E14", foreground="#ffffff")
        self.btnLogout.configure(cursor="hand2", font="-family {Poppins SemiBold} -size 12")

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
                "idVenda",
                "Data da Venda",
                "Preco Total",
                "ID do Funcionario"
            )
        )

        self.tree.heading("idVenda", text="idVendas", anchor=W)
        self.tree.heading("Data da Venda", text="Data da Venda", anchor=W)
        self.tree.heading("Preco Total", text="Preco Total", anchor=W)
        self.tree.heading("ID do Funcionario", text="ID do Funcionario", anchor=W)

        self.tree.column("#0", stretch=NO, minwidth=0, width=0)
        self.tree.column("#1", stretch=NO, minwidth=0, width=80)
        self.tree.column("#2", stretch=NO, minwidth=0, width=80)
        self.tree.column("#3", stretch=NO, minwidth=0, width=80)

        self.DisplayData()

    sel = []

    def on_tree_select(self, Event):
        self.sel.clear()
        for i in self.tree.selection():
            if i not in self.sel:
                self.sel.append(i)

    #modificar aqui. ja esta
    def DisplayData(self):
        self.tree.delete(*self.tree.get_children())
        for i in range(len(database.lstVendas)):
            self.tree.insert('', 'end', values=(
                database.lstVendas[i].idVenda,
                database.lstVendas[i].data,
                database.lstVendas[i].preco,
                database.lstVendas[i].idFunc
            ))

    def time(self):
        string = strftime("%H:%M:%S %p")
        self.clock.config(text=string)
        self.clock.after(1000, self.time)

    #modificar aqui
    def btnProcurarDataVenda_click(self):
        val = []
        for i in self.tree.get_children():
            val.append(i)
            for j in self.tree.item(i)["values"]:
                val.append(j)

        if self.txtData.get() == "":
            messagebox.showerror("Erro!!", "Data invalida.", parent=mainLbl)
        else:
            for search in val:
                if search == str (self.txtData.get()):
                    self.tree.selection_set(val[val.index(search) - 2])
                    self.tree.focus(val[val.index(search) - 2])
                    messagebox.showinfo("Sucesso!!", "Vendas: {} encotrado.".format(self.txtData.get()),
                                        parent=mainLbl)
                    break
            else:
                messagebox.showerror("Erro!!", "Vendas: {} não encontrado.".format(self.txtData.get()),
                                     parent=mainLbl)

def sair():
    sure = messagebox.askyesno("Voltar", "Tem a certeza que deseja voltar?", parent=mainLbl)
    if sure:
        mainLbl.destroy()
        menu.btnReVisible()


def X_windowsBtn_click():
    sure = messagebox.askyesno("Sair", "Tem a certeza que deseja fechar o programa?", parent=mainLbl)
    if sure:
        exit()

def updList():
    page3.DisplayData()


def callVendas():
    global mainLbl
    global page3
    mainLbl = Toplevel()
    page3 = Vendas()
    page3.time()
    mainLbl.mainloop()

