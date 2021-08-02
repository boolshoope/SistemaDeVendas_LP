from tkinter import *


class Login:
    def __init__(self, tipo):
        p_add.geometry("1366x768")
        p_add.resizable(0, 0)
        p_add.title("Login")

        print(tipo)
        self.label1 = Label(p_add)
        self.label1.place(relx=0, rely=0, width=1366, height=768)
        self.img = PhotoImage(file="public/imagens/login.png")
        self.label1.configure(image=self.img)

        self.txtUsername = Entry(p_add)
        self.txtUsername.place(relx=0.373, rely=0.273, width=374, height=24)
        self.txtUsername.configure(font="-family {Poppins} -size 10")
        self.txtUsername.configure(relief="flat")

        self.txtPassword = Entry(p_add)
        self.txtPassword.place(relx=0.373, rely=0.384, width=374, height=24)
        self.txtPassword.configure(font="-family {Poppins} -size 10")
        self.txtPassword.configure(relief="flat")
        self.txtPassword.configure(show="*")

        self.button1 = Button(p_add)
        self.button1.place(relx=0.366, rely=0.685, width=356, height=43)
        self.button1.configure(relief="flat")
        self.button1.configure(overrelief="flat")
        self.button1.configure(activebackground="#D2463E")
        self.button1.configure(cursor="hand2")
        self.button1.configure(foreground="#ffffff")
        self.button1.configure(background="#D2463E")
        self.button1.configure(font="-family {Poppins SemiBold} -size 20")
        self.button1.configure(borderwidth="0")
        self.button1.configure(text="""LOGIN""")
        self.button1.configure(command=self.login)

    def login(self):
        print("login")



def callLogin(tipo):
    global p_add
    global page3
    p_add = Tk()
    page3 = Login(tipo)
    p_add.mainloop()