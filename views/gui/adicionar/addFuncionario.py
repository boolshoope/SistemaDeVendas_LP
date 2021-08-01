from datetime import datetime
from time import strftime
from tkinter import *
from tkinter import ttk, messagebox
from tkcalendar import *
from libs import database
from views.gui.gerir import funcionarios


class AddFuncionario:
    def __init__(self, top=None):
        top.geometry("1366x768")
        top.resizable(0, 0)
        top.title("Adicionar Funcionario")

        self.label1 = Label(p_add)
        self.label1.place(relx=0, rely=0, width=1366, height=768)
        self.img = PhotoImage(file="public/imagens/addFuncionario.png")
        self.label1.configure(image=self.img)

        self.labelTop = Label(p_add, text="Adicionar Funcionario")
        self.labelTop.place(x=450, y=75, width=480, height=70)
        self.labelTop.configure(font="-family {Poppins Bold} -size 31", background="#ffffff")

        self.clock = Label(p_add)
        self.clock.place(relx=0.84, rely=0.065, width=102, height=36)
        self.clock.configure(font="-family {Poppins Light} -size 12")
        self.clock.configure(foreground="#000000", background="#ffffff")

        self.txtIdFuncionario = Entry(p_add)
        self.txtIdFuncionario.place(x=177, y=144, width=200, height=30)
        self.txtIdFuncionario.configure(font="-family {Poppins} -size 12", relief="raised")

        self.txtNrBI = Entry(p_add)
        self.txtNrBI.place(x=179, y=209, width=450, height=30)
        self.txtNrBI.configure(font="-family {Poppins} -size 12", relief="flat")

        self.txtApelido = Entry(p_add)
        self.txtApelido.place(x=179, y=299, width=191, height=30)
        self.txtApelido.configure(font="-family {Poppins} -size 12", relief="flat")

        self.txtNome = Entry(p_add)
        self.txtNome.place(x=389, y=299, width=244, height=30)
        self.txtNome.configure(font="-family {Poppins} -size 12", relief="flat")

        self.r2 = p_add.register(self.testint)
        # self.txtQuantStock.configure(validate="key", validatecommand=(self.r2, "%P"))

        self.listCboSexo = ['Masculino', 'Feminino']
        self.cboSexo = ttk.Combobox(p_add, values=self.listCboSexo, state="readonly")
        self.cboSexo.place(x=178, y=389, width=190, height=30)
        self.cboSexo.configure(font="-family {Poppins} -size 12")

        self.txtDataNasc = DateEntry(p_add, date_pattern='dd/mm/y')
        self.txtDataNasc.place(x=407, y=389, width=227, height=30)
        self.txtDataNasc.configure(font="-family {Poppins} -size 12")

        self.txtTel1 = Entry(p_add)
        self.txtTel1.place(x=178, y=479, width=199, height=30)
        self.txtTel1.configure(font="-family {Poppins} -size 12", relief="flat")

        self.txtTel2 = Entry(p_add)
        self.txtTel2.place(x=407, y=479, width=227, height=30)
        self.txtTel2.configure(font="-family {Poppins} -size 12", relief="flat")

        self.txtBairro = Entry(p_add)
        self.txtBairro.place(x=178, y=577, width=200, height=30)
        self.txtBairro.configure(font="-family {Poppins} -size 12", relief="flat")

        self.txtNrCasa = Entry(p_add)
        self.txtNrCasa.place(x=720, y=209, width=227, height=30)
        self.txtNrCasa.configure(font="-family {Poppins} -size 12", relief="flat")

        self.txtQuarteirao = Entry(p_add)
        self.txtQuarteirao.place(x=967, y=209, width=205, height=30)
        self.txtQuarteirao.configure(font="-family {Poppins} -size 12", relief="flat")

        self.txtUsername = Entry(p_add)
        self.txtUsername.place(x=752, y=353, width=227, height=30)
        self.txtUsername.configure(font="-family {Poppins} -size 12", relief="flat")

        self.txtPassword = Entry(p_add)
        self.txtPassword.place(x=752, y=445, width=227, height=30)
        self.txtPassword.configure(font="-family {Poppins} -size 12", relief="flat")

        self.listCboNivel = ['Administrador', 'Caixa']
        self.cboNivel = ttk.Combobox(p_add, values=self.listCboNivel, state="readonly")
        self.cboNivel.place(x=752, y=537, width=227, height=30)
        self.cboNivel.configure(font="-family {Poppins} -size 12")

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
        pNome = self.txtNome.get()
        apelido = self.txtApelido.get()
        dataNasc = datetime.strptime(self.txtDataNasc.get(), "%d/%m/%Y").strftime('%Y-%m-%d')
        sexo = ""
        if self.cboSexo.get() == "Masculino":
            sexo = 'M'
        elif self.cboSexo.get() == "Feminino":
            sexo = 'F'
        nrBI = self.txtNrBI.get()
        bairro = self.txtBairro.get()
        nrCasa = self.txtNrCasa.get()
        quarteirao = self.txtQuarteirao.get()
        tel1 = self.txtTel1.get()
        tel2 = self.txtTel2.get()

        ### Login
        username = self.txtUsername.get()
        password = self.txtPassword.get()
        nivel = self.cboNivel.get()

        database.db.addFunc(pNome, apelido, dataNasc, sexo, nrBI, bairro, nrCasa, quarteirao, tel1, tel2)
        database.db.addLogin(username, password, nivel)
        messagebox.showinfo("Sucesso!", "As informações foram adicionadas com sucesso.", parent=p_add)
        database.db.lerFuncionario()
        database.db.lerLogin()
        funcionarios.updList()
        p_add.destroy()

    def btnLimpar_click(self):
        self.txtNome.delete(0, END)
        self.txtApelido.delete(0, END)
        self.txtNrBI.delete(0, END)
        self.txtBairro.delete(0, END)
        self.txtNrCasa.delete(0, END)
        self.txtQuarteirao.delete(0, END)
        self.txtTel1.delete(0, END)
        self.txtTel2.delete(0, END)
        self.txtUsername.delete(0, END)
        self.txtPassword.delete(0, END)


def callAddFuncionario():
    global p_add
    global page3
    p_add = Toplevel()
    page3 = AddFuncionario(p_add)
    page3.time()
    p_add.mainloop()
