from datetime import date
from time import strftime
from tkinter import *
from tkinter import messagebox, ttk
from tkinter import scrolledtext as tkst

from libs import database


class Item:
    def __init__(self, name, preco, qtd):
        self.name = name
        self.preco = preco
        self.qtd = qtd


class Cart:
    def __init__(self):
        self.items = []
        self.dictionary = {}

    def addItem(self, item):
        self.items.append(item)

    def delItem(self):
        self.items.pop()

    def delItens(self):
        self.items.clear()

    def total(self):
        total = 0.0
        for i in self.items:
            total += i.preco * i.qtd
        return total

    def isEmpty(self):
        if len(self.items) == 0:
            return True

    def allCart(self):
        for i in self.items:
            if (i.name in self.dictionary):
                self.dictionary[i.name] += i.qtd
            else:
                self.dictionary.update({i.name: i.qtd})


class AddVenda:
    def __init__(self):
        p_add.geometry("1366x768")
        p_add.resizable(0, 0)
        p_add.title("Adicionar Venda")

        self.label1 = Label(p_add)
        self.label1.place(relx=0, rely=0, width=1366, height=768)
        self.img = PhotoImage(file="public/imagens/addVenda.png")
        self.label1.configure(image=self.img)

        self.labelTop = Label(p_add, text="Adicionar Venda")
        self.labelTop.place(x=485, y=50, width=430, height=70)
        self.labelTop.configure(font="-family {Poppins Bold} -size 31", background="#ffffff")

        self.clock = Label(p_add)
        self.clock.place(relx=0.84, rely=0.065, width=102, height=36)
        self.clock.configure(font="-family {Poppins Light} -size 12")
        self.clock.configure(foreground="#000000", background="#ffffff")

        self.txtNomeProd = Entry(p_add)
        self.txtNomeProd.place(x=207, y=176, width=227, height=30)
        self.txtNomeProd.configure(font="-family {Poppins} -size 12", relief="flat")

        self.btnProcurarNomeProd = Button(p_add, text="Procurar", command=self.btnAdicionar_click)
        self.btnProcurarNomeProd.place(x=458, y=176, width=70, height=28)
        self.btnProcurarNomeProd.configure(relief="flat", overrelief="flat", borderwidth="0")
        self.btnProcurarNomeProd.configure(background="#023e8a", activebackground="#023e8a", foreground="#ffffff")
        self.btnProcurarNomeProd.configure(cursor="hand2", font="-family {Poppins SemiBold} -size 12")

        self.txtQtd = Entry(p_add)
        self.txtQtd.place(x=91, y=580, width=85, height=30)
        self.txtQtd.configure(font="-family {Poppins} -size 12", relief="flat")

        self.btnAdicionar = Button(p_add, text="Adicionar", command=self.addCarrinho)
        self.btnAdicionar.place(x=441, y=587, width=88, height=30)
        self.btnAdicionar.configure(relief="flat", overrelief="flat", borderwidth="0")
        self.btnAdicionar.configure(background="#CF1E14", activebackground="#CF1E14", foreground="#ffffff")
        self.btnAdicionar.configure(cursor="hand2", font="-family {Poppins SemiBold} -size 12")

        self.btnTotal = Button(p_add, text="Total", command=self.btnAdicionar_click)
        self.btnTotal.place(x=70, y=678, width=81, height=30)
        self.btnTotal.configure(relief="flat", overrelief="flat", borderwidth="0")
        self.btnTotal.configure(background="#CF1E14", activebackground="#CF1E14", foreground="#ffffff")
        self.btnTotal.configure(cursor="hand2", font="-family {Poppins SemiBold} -size 12")

        self.btnTotal = Button(p_add, text="Total", command=self.btnTotal_click)
        self.btnTotal.place(x=70, y=678, width=81, height=30)
        self.btnTotal.configure(relief="flat", overrelief="flat", borderwidth="0")
        self.btnTotal.configure(background="#CF1E14", activebackground="#CF1E14", foreground="#ffffff")
        self.btnTotal.configure(cursor="hand2", font="-family {Poppins SemiBold} -size 12")

        self.btnGerar = Button(p_add, text="Guardar", command=self.btnAdicionar_click)
        self.btnGerar.place(x=195, y=678, width=80, height=30)
        self.btnGerar.configure(relief="flat", overrelief="flat", borderwidth="0")
        self.btnGerar.configure(background="#CF1E14", activebackground="#CF1E14", foreground="#ffffff")
        self.btnGerar.configure(cursor="hand2", font="-family {Poppins SemiBold} -size 12")

        self.btnLimpar = Button(p_add, text="Limpar", command=self.limpar)
        self.btnLimpar.place(x=319, y=678, width=80, height=30)
        self.btnLimpar.configure(relief="flat", overrelief="flat", borderwidth="0")
        self.btnLimpar.configure(background="#CF1E14", activebackground="#CF1E14", foreground="#ffffff")
        self.btnLimpar.configure(cursor="hand2", font="-family {Poppins SemiBold} -size 12")

        self.btnSair = Button(p_add, text="Sair", command=sair)
        self.btnSair.place(x=442, y=678, width=80, height=30)
        self.btnSair.configure(relief="flat", overrelief="flat", borderwidth="0")
        self.btnSair.configure(background="#CF1E14", activebackground="#CF1E14", foreground="#ffffff")
        self.btnSair.configure(cursor="hand2", font="-family {Poppins SemiBold} -size 12")

        self.Scrolledtext1 = tkst.ScrolledText(p_add)
        self.Scrolledtext1.place(relx=0.439, rely=0.586, width=695, height=275)
        self.Scrolledtext1.configure(borderwidth=0)
        self.Scrolledtext1.configure(font="-family {Podkova} -size 8")
        self.Scrolledtext1.configure(state="disabled")

        self.scrollbarx = Scrollbar(p_add, orient=HORIZONTAL)
        self.scrollbary = Scrollbar(p_add, orient=VERTICAL)
        self.tree = ttk.Treeview(p_add)
        self.tree.place(x=53, y=227, width=462, height=314)
        self.tree.configure(
            yscrollcommand=self.scrollbary.set, xscrollcommand=self.scrollbarx.set
        )
        self.tree.configure(selectmode="extended")

        self.tree.bind("<<TreeviewSelect>>", self.on_tree_select)

        self.scrollbary.configure(command=self.tree.yview)
        self.scrollbarx.configure(command=self.tree.xview)

        self.scrollbary.place(x=515, y=227, width=22, height=314)
        self.scrollbarx.place(x=53, y=541, width=484, height=22)

        self.tree.configure(
            columns=(
                "CodBarras",
                "Nome",
                "Preco",
                "Stock",
                "idProduto"
            )
        )

        self.tree.heading("CodBarras", text="CodBarras", anchor=W)
        self.tree.heading("Nome", text="Nome", anchor=W)
        self.tree.heading("Preco", text="Preco", anchor=W)
        self.tree.heading("Stock", text="Stock", anchor=W)
        self.tree.heading("idProduto", text="idProduto", anchor=W)

        self.tree.column("#0", stretch=NO, minwidth=0, width=0)
        self.tree.column("#1", stretch=NO, minwidth=0, width=80)
        self.tree.column("#2", stretch=NO, minwidth=0, width=230)
        self.tree.column("#3", stretch=NO, minwidth=0, width=100)
        self.tree.column("#4", stretch=NO, minwidth=0, width=100)

        self.DisplayData()

    sel = []

    def on_tree_select(self, Event):
        self.sel.clear()
        for i in self.tree.selection():
            if i not in self.sel:
                self.sel.append(i)

    def DisplayData(self):
        self.tree.delete(*self.tree.get_children())
        for i in range(len(database.lstProd)):
            self.tree.insert('', 'end', values=(
                database.lstProd[i].codBarras,
                database.lstProd[i].nomeProd,
                database.lstProd[i].preco,
                database.lstProd[i].stock,
                database.lstProd[i].idProd
            ))

    carr = Cart()

    def addCarrinho(self):
        self.Scrolledtext1.configure(state="normal")
        strr = self.Scrolledtext1.get('1.0', END)
        if strr.find('Total') == -1:
            if len(self.sel) != 0:
                nomeProduto = self.tree.item(self.tree.focus())["values"][1]
                quant = self.txtQtd.get()
                stock = self.tree.item(self.tree.focus())["values"][3]
                preco = self.tree.item(self.tree.focus())["values"][2]
                if quant.isdigit():
                    if (stock - int(quant)) >= 0:
                        pT = preco * int(quant)
                        item = Item(nomeProduto, preco, int(quant))
                        self.carr.addItem(item)
                        self.Scrolledtext1.configure(state="normal")
                        bill_text = "{}\t\t\t\t\t\t{}\t\t\t\t\t   {}\n".format(nomeProduto, quant, pT)
                        self.Scrolledtext1.insert('insert', bill_text)
                        self.Scrolledtext1.configure(state="disabled")
                    else:
                        messagebox.showerror("Erro!", "Quantidade maior que o stock.", parent=p_add)
                else:
                    messagebox.showerror("Erro!", "Quantidade Invalida.", parent=p_add)
            else:
                messagebox.showerror("Erro!!", "Por favor, selecione um item na lista.", parent=p_add)

    def btnTotal_click(self):
        if self.carr.isEmpty():
            messagebox.showerror("Erro!", "Adicione pelomenos um produto.", parent=p_add)
        else:
            self.Scrolledtext1.configure(state="normal")
            strr = self.Scrolledtext1.get('1.0', END)
            if strr.find('Total') == -1:
                self.Scrolledtext1.configure(state="normal")
                divider = "\n\n\n" + ("─" * 61)
                self.Scrolledtext1.insert('insert', divider)
                total = "\nTotal\t\t\t\t\t\t\t\t\t\t\t {} Mts".format(self.carr.total())
                self.Scrolledtext1.insert('insert', total)
                divider2 = "\n" + ("─" * 61)
                self.Scrolledtext1.insert('insert', divider2)
                self.Scrolledtext1.configure(state="disabled")
            else:
                return

    state = 1

    def limpar(self):
        self.Scrolledtext1.configure(state="normal")
        self.Scrolledtext1.delete(1.0, END)
        self.Scrolledtext1.configure(state="disabled")
        self.carr.delItens()
        self.state = 1

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

    def btnAdicionar_click(self):
        strr = self.Scrolledtext1.get('1.0', END)
        if self.carr.isEmpty():
            messagebox.showerror("Erro!", "Carrinho vazio.", parent=p_add)
        else:
            if strr.find('Total') == -1:
                self.btnTotal_click()
                self.btnAdicionar_click()
            else:
                data = str(date.today())
                #database.db.addVenda(data, self.carr.total(), 1)
                print(database.db.getIdVenda())
                database.db.lerVendas()
                print(len(self.carr.dictionary.items()))

                self.carr.allCart()
                for name, qty in self.carr.dictionary.items():
                    print(name + "  " + str(qty))
                    for i in range(len(database.lstProd)):
                        if database.lstProd[i].nomeProd == name:
                            print("a")
                messagebox.showinfo("Success!!", "Recibo guardado", parent=p_add)
                p_add.destroy()
                callAddVenda()
                self.state = 0


def sair():
    sure = messagebox.askyesno("Sair", "Tem a certeza que deseja fechar o programa?", parent=p_add)
    if sure:
        exit()


def callAddVenda():
    global p_add
    global page3
    p_add = Toplevel()
    page3 = AddVenda()
    page3.time()
    p_add.mainloop()
