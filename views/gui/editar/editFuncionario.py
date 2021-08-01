from datetime import datetime
from time import strftime
from tkinter import *
from tkinter import ttk

from tkcalendar import DateEntry

from libs import database


class EditFuncionario:
    def __init__(self, idFunc):
        self.idFunc = idFunc
        p_edit.geometry("1366x768")
        p_edit.resizable(0, 0)
        p_edit.title("Actualizar Funcionario")

        self.label1 = Label(p_edit)
        self.label1.place(relx=0, rely=0, width=1366, height=768)
        self.img = PhotoImage(file="public/imagens/addFuncionario.png")
        self.label1.configure(image=self.img)

        self.labelTop = Label(p_edit, text="Actualizar Funcionario")
        self.labelTop.place(x=450, y=75, width=480, height=70)
        self.labelTop.configure(font="-family {Poppins Bold} -size 31", background="#ffffff")

        self.clock = Label(p_edit)
        self.clock.place(relx=0.84, rely=0.065, width=102, height=36)
        self.clock.configure(font="-family {Poppins Light} -size 12")
        self.clock.configure(foreground="#000000", background="#ffffff")

        self.txtIdFuncionario = Entry(p_edit)
        self.txtIdFuncionario.place(x=177, y=144, width=200, height=30)
        self.txtIdFuncionario.configure(font="-family {Poppins} -size 12", relief="raised")

        self.txtNrBI = Entry(p_edit)
        self.txtNrBI.place(x=179, y=209, width=450, height=30)
        self.txtNrBI.configure(font="-family {Poppins} -size 12", relief="flat")

        self.txtApelido = Entry(p_edit)
        self.txtApelido.place(x=179, y=299, width=191, height=30)
        self.txtApelido.configure(font="-family {Poppins} -size 12", relief="flat")

        self.txtNome = Entry(p_edit)
        self.txtNome.place(x=389, y=299, width=244, height=30)
        self.txtNome.configure(font="-family {Poppins} -size 12", relief="flat")

        self.r2 = p_edit.register(self.testint)
        #self.txtQuantStock.configure(validate="key", validatecommand=(self.r2, "%P"))

        self.listCboSexo = ['Masculino', 'Feminino']
        self.cboSexo = ttk.Combobox(p_edit, values=self.listCboSexo, state="readonly")
        self.cboSexo.place(x=178, y=389, width=190, height=30)
        self.cboSexo.configure(font="-family {Poppins} -size 12")

        self.txtDataNasc = DateEntry(p_edit, date_pattern='dd/mm/y')
        self.txtDataNasc.place(x=407, y=389, width=227, height=30)
        self.txtDataNasc.configure(font="-family {Poppins} -size 12")

        self.txtTel1 = Entry(p_edit)
        self.txtTel1.place(x=178, y=479, width=199, height=30)
        self.txtTel1.configure(font="-family {Poppins} -size 12", relief="flat")

        self.txtTel2 = Entry(p_edit)
        self.txtTel2.place(x=407, y=479, width=227, height=30)
        self.txtTel2.configure(font="-family {Poppins} -size 12", relief="flat")

        self.txtBairro = Entry(p_edit)
        self.txtBairro.place(x=178, y=577, width=200, height=30)
        self.txtBairro.configure(font="-family {Poppins} -size 12", relief="flat")

        self.txtNrCasa = Entry(p_edit)
        self.txtNrCasa.place(x=720, y=209, width=227, height=30)
        self.txtNrCasa.configure(font="-family {Poppins} -size 12", relief="flat")

        self.txtQuarteirao = Entry(p_edit)
        self.txtQuarteirao.place(x=967, y=209, width=205, height=30)
        self.txtQuarteirao.configure(font="-family {Poppins} -size 12", relief="flat")

        self.txtUsername = Entry(p_edit)
        self.txtUsername.place(x=752, y=353, width=227, height=30)
        self.txtUsername.configure(font="-family {Poppins} -size 12", relief="flat")

        self.txtPassword = Entry(p_edit)
        self.txtPassword.place(x=752, y=445, width=227, height=30)
        self.txtPassword.configure(font="-family {Poppins} -size 12", relief="flat")

        self.listCboNivel = ['Administrador', 'Caixa']
        self.cboNivel = ttk.Combobox(p_edit, values=self.listCboNivel, state="readonly")
        self.cboNivel.place(x=752, y=537, width=227, height=30)
        self.cboNivel.configure(font="-family {Poppins} -size 12")

        self.btnAdicionar = Button(p_edit, text="ACTUALIZAR", command=self.btnActualizar_click)
        self.btnAdicionar.place(x=535, rely=0.836, width=120, height=34)
        self.btnAdicionar.configure(relief="flat", overrelief="flat", borderwidth="0")
        self.btnAdicionar.configure(background="#CF1E14", activebackground="#CF1E14", foreground="#ffffff")
        self.btnAdicionar.configure(cursor="hand2", font="-family {Poppins SemiBold} -size 14")

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
        for i in range(len(database.lstFunc)):
            if database.lstFunc[i].idFunc == self.idFunc:
                self.txtIdFuncionario.insert(0, database.lstFunc[i].idFunc)
                self.txtNome.insert(0, database.lstFunc[i].pNome)
                self.txtApelido.insert(0, database.lstFunc[i].apelido)
                dataNasc = datetime.strptime(str(database.lstFunc[i].dataNascimento), "%Y-%m-%d").strftime('%d/%m/%Y')
                self.txtDataNasc.delete(0, END)
                self.txtDataNasc.insert(0, dataNasc)

                sexo = ""
                if database.lstFunc[i].sexo == "M":
                    sexo = 'Masculino'
                elif database.lstFunc[i].sexo == "F":
                    sexo = 'Feminino'
                self.cboSexo.set(sexo)
                self.txtNrBI.insert(0, database.lstFunc[i].nrBI)
                self.txtBairro.insert(0, database.lstFunc[i].bairro)
                self.txtNrCasa.insert(0, database.lstFunc[i].nrCasa)
                self.txtQuarteirao.insert(0, database.lstFunc[i].quarteirao)
                self.txtTel1.insert(0, database.lstFunc[i].tel1)
                self.txtTel2.insert(0, database.lstFunc[i].tel2)
                for j in range(len(database.lstLogin)):
                    if database.lstLogin[j].idFunc == self.idFunc:
                        self.txtUsername.insert(0, database.lstLogin[j].username)
                        self.txtPassword.insert(0, database.lstLogin[j].password)
                        self.cboNivel.set(database.lstLogin[j].nivel)

    def btnActualizar_click(self):
        print("btnActualizar clicado")

    def btnLimpar_click(self):
        self.txtNome.delete(0, END)
        print("btnLimpar clicado")


def callEditFuncionario(idFunc):
    global p_edit
    global page3
    p_edit = Toplevel()
    page3 = EditFuncionario(idFunc)
    page3.time()
    page3.preencherTxt()
    p_edit.mainloop()

