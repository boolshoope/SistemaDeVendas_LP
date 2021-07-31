from time import strftime
from tkinter import *
from tkinter import ttk


class EditProduto:
    def __init__(self, top=None):
        top.geometry("1366x768")
        top.resizable(0, 0)
        top.title("Adicionar Produto")

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

        self.listCboCategoria=['Frutos', 'Sumos']
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

    def btnActualizar_click(self):
        print("btnActualizar clicado")

    def btnLimpar_click(self):
        print("btnLimpar clicado")


def callEditProdutos():
    global p_edit
    global page3
    p_edit = Toplevel()
    page3 = EditProduto(p_edit)
    page3.time()
    p_edit.mainloop()

