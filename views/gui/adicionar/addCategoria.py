from time import strftime
from tkinter import *
from tkinter import messagebox

from libs import database


class AddCategoria:
    def __init__(self, top=None):
        top.geometry("1366x768")
        top.resizable(0, 0)
        top.title("Adicionar Categoria")

        self.label1 = Label(p_add)
        self.label1.place(relx=0, rely=0, width=1366, height=768)
        self.img = PhotoImage(file="public/imagens/addCategoria.png")
        self.label1.configure(image=self.img)

        self.labelTop = Label(p_add, text="Adicionar Categoria")
        self.labelTop.place(x=485, y=75, width=430, height=70)
        self.labelTop.configure(font="-family {Poppins Bold} -size 31", background="#ffffff")

        self.clock = Label(p_add)
        self.clock.place(relx=0.84, rely=0.065, width=102, height=36)
        self.clock.configure(font="-family {Poppins Light} -size 12")
        self.clock.configure(foreground="#000000", background="#ffffff")

        self.txtIdCategoria = Entry(p_add)
        self.txtIdCategoria.place(relx=0.132, rely=0.296, width=450, height=30)
        self.txtIdCategoria.configure(font="-family {Poppins} -size 12", relief="flat")

        self.txtNome = Entry(p_add)
        self.txtNome.place(relx=0.132, rely=0.413, width=450, height=30)
        self.txtNome.configure(font="-family {Poppins} -size 12", relief="flat")

        self.btnAdicionar = Button(p_add, text="ADICIONAR", command=self.btnAdicionar_click)
        self.btnAdicionar.place(x=535, rely=0.836, width=120, height=34)
        self.btnAdicionar.configure(relief="flat", overrelief="flat", borderwidth="0")
        self.btnAdicionar.configure(background="#CF1E14", activebackground="#CF1E14", foreground="#ffffff")
        self.btnAdicionar.configure(cursor="hand2", font="-family {Poppins SemiBold} -size 14")

        self.btnLimpar = Button(p_add, text='LIMPAR', command=self.btnLimpar_click)
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

    def btnAdicionar_click(self):
        idCateg = self.txtIdCategoria.get()
        nome = self.txtNome.get()
        database.db.addCateg(idCateg, nome)
        messagebox.showinfo("Sucesso!!", "As informações foram adicionadas com sucesso.", parent=p_add)
        p_add.destroy()

    def btnLimpar_click(self):
        self.txtNome.delete(0, END)


def callAddCategoria():
    global p_add
    global page3
    p_add = Toplevel()
    page3 = AddCategoria(p_add)
    page3.time()
    p_add.mainloop()
