import Tkinter as tk
import tkMessageBox as messagebox
import sqlite3
#db = sqlite3.connect(':memory:')
db = sqlite3.connect('BARRON CAPITAL')
cursor1 = db.cursor()
cursor2 = db.cursor()
#cursor1.execute('''CREATE TABLE custs(accno TEXT UNIQUE,username TEXT,bal INTEGER, phone_no TEXT, pin TEXT)''')
#if cursor1.execute('''INSERT INTO custs(accno,username,bal,phone_no,pin) VALUES(?,?,?,?,?)''',('MBSC1001','john','1000','9835612024','1234')):
    #print 'record inserted successfully!'
db.commit()
global x
class SeaofBTCapp(tk.Tk):

    def __init__(self, *args, **kwargs):

        tk.Tk.__init__(self, *args, **kwargs)

        container = tk.Frame(self,bg = 'orange')

        container.pack(side="top", fill="both", expand = True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (StartPage, PageOne, PageTwo, PageThree,PageFour,PageFive,PageSix):

            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    def show_frame(self, cont):

        frame = self.frames[cont]
        frame.tkraise()


class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent,bg="white")
        self.controller = controller
        label1 = tk.Label(self, text= "WELCOME TO BARON CAPITAL!" ,font=("Times new Roman",30),bg="navy",fg="yellow",height=3,width=200)
        label1.grid(row=1, column=0)
        label1.pack(pady=10,padx=0)
        label2 = tk.Label(self, text="LOGIN OR REGISTER !!!", font=("Times new Roman",20),fg="yellow",bg="navy",height=1,width=200)
        label2.grid(row=10, column=10)
        label2.pack(pady=10, padx=0)
        button1 = tk.Button(self, text="REGISTER", font=("Times new Roman", 18), bg="sky blue", fg="black",
                            command=lambda: controller.show_frame(PageOne))
        button1.pack(pady=20, padx=20)
        button2 = tk.Button(self, text="LOGIN",font=("Times new Roman", 18), bg="light green", fg="black",
                            command=lambda: controller.show_frame(PageTwo))
        button2.pack(pady=20,padx=20)



class PageOne(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller=controller
        leftframe = tk.Frame(self)
        leftframe.pack(side="left")
        rightframe = tk.Frame(self)
        rightframe.pack(side="right")
        bottomframe = tk.Frame(self)
        bottomframe.pack(side="bottom")

        L5 = tk.Label(leftframe, text="Account No.", fg="yellow", bg="navy")
        L5.config(font=("Times new Roman", 17), width=15)
        L5.pack(pady=10, padx=10)
        E5 = tk.Entry(rightframe, bd=8, fg="black", bg="white")
        E5.config(font=("Times new Roman", 17), width=15)
        E5.pack(pady=10, padx=10)
        L1 = tk.Label(leftframe, text="Username", fg="yellow", bg="navy")
        L1.config(font=("Times new Roman", 17), width=15)
        L1.pack(pady=10, padx=10)
        E1 = tk.Entry(rightframe, bd=8, fg="black", bg="white")
        E1.config(font=("Times new Roman", 17), width=15)
        E1.pack(pady=10, padx=10)
        L2 = tk.Label(leftframe, text="Pin", fg="yellow", bg="navy")
        L2.config(font=("Times new Roman", 17), width=15)
        L2.pack(pady=10, padx=10)
        E2 = tk.Entry(rightframe, bd=8, fg="black", bg="white")
        E2.config(font=("Times new Roman", 17), width=15)
        E2.pack(pady=10, padx=10)
        L3 = tk.Label(leftframe, text="Phone No.", fg="yellow", bg="navy")
        L3.config(font=("Times new Roman", 17), width=15)
        L3.pack(pady=10, padx=10)
        E3 = tk.Entry(rightframe, bd=8, fg="black", bg="white")
        E3.config(font=("Times new Roman", 17), width=15)
        E3.pack(pady=10, padx=10)
        L4 = tk.Label(leftframe, text=" First Deposit", fg="yellow", bg="navy")
        L4.config(font=("Times new Roman", 17), width=15)
        L4.pack(pady=10, padx=10)
        E4 = tk.Entry(rightframe, bd=8, fg="black", bg="white")
        E4.config(font=("Times new Roman", 17), width=15)
        E4.pack(pady=10, padx=10)
        button1 = tk.Button(self, text="BACK",
                            command=lambda: controller.show_frame(StartPage), fg='black', bg='sky blue')
        button1.config(font=("Times new Roman", 20), height=0, width=10)
        button1.pack(side="bottom", pady=20, padx=20)


        def reg():
            if cursor1.execute('''INSERT INTO custs (accno,username, bal, phone_no, pin) VALUES(?,?,?,?,?)''',
                               (E5.get(),E1.get(), E4.get(), E3.get(), E2.get())):
                print("Account Created :)")
            db.commit()
            messagebox.showinfo("CONGRATULATIONS !!!","Acount Created! :)")
            controller.show_frame(StartPage)

        button2 = tk.Button(self, text="REGISTER",
                            command=reg, fg='black', bg='sky blue')
        button2.config(font=("Times new Roman", 20), height=0, width=10)
        button2.pack(side="bottom", pady=20, padx=20)

class PageTwo(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        leftframe = tk.Frame(self)
        leftframe.pack(side="left")
        rightframe = tk.Frame(self)
        rightframe.pack(side="right")
        bottomframe = tk.Frame(self)
        bottomframe.pack(side="bottom")

        L1 = tk.Label(leftframe, text="Account No.", fg="yellow", bg="navy")
        L1.config(font=("Times new Roman", 20), width=15)
        L1.pack(pady=10, padx=10)
        E1 = tk.Entry(rightframe, bd=8, fg="black", bg="white")
        E1.config(font=("Times new Roman", 17), width=15)
        E1.pack(pady=10, padx=10)
        L2 = tk.Label(leftframe, text="Pin", fg="yellow", bg="navy")
        L2.config(font=("Times new Roman", 20), width=15)
        L2.pack(pady=10, padx=10)
        E2 = tk.Entry(rightframe, bd=8, fg="black", bg="white")
        E2.config(font=("Times new Roman", 17), width=15)
        E2.pack(pady=10, padx=10)

        def login():
            if cursor1.execute('''SELECT pin FROM custs WHERE accno=?''', (E1.get(),)):
                print('Records fetched!')
            ps = str(cursor1.fetchone())
            print(ps)
            ps1 = str(E2.get())
            global x
            x= E1.get()
            ps1 = "(u'" + ps1 + "',)"
            print(ps1)
            if (ps == ps1):
                messagebox.showinfo("WELCOME",'LOGIN SUCCESSFUL')
                controller.show_frame(PageThree)
            else:
                messagebox.showwarning("ERROR",'INCORRECT ACCOUNT NO. OR PIN !!!')

        button1 = tk.Button(self, text="BACK",
                            command=lambda: controller.show_frame(StartPage), fg='black', bg='sky blue')
        button1.config(font=("Times New Roman", 20), height=0, width=10)
        button1.pack(side="bottom", pady=70, padx=20)

        button2 = tk.Button(self, text="LOGIN",
                            command=login, fg='black', bg='sky blue')
        button2.config(font=("Times New Roman", 20), height=0, width=10)
        button2.pack(side="bottom", pady=20, padx=20)



class PageThree(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        b1 = tk.Button(self, text="WITHDRAW", font=("Times New Roman", 20),bg="navy" ,fg="yellow",width=20,command=lambda: controller.show_frame(PageFour))
        b1.grid(row=10, column=10)
        b1.pack(pady=0, padx=0)
        def balancecheck():
            if cursor1.execute('''SELECT bal FROM custs WHERE accno=?''', (x,)):
                print('Records fetched!')
            bal = str(cursor1.fetchone())
            bal1=bal[1:-2]
            print(bal1)
            messagebox.showinfo("BALANCE",("RS "+bal1))
        b2 = tk.Button(self, text="BALANCE CHECK", font=("Times New Roman", 20),bg="navy" ,fg="yellow",width=20,command=balancecheck)
        b2.grid(row=10, column=10)
        b2.pack(pady=50, padx=50)
        b3 = tk.Button(self, text="CHANGE PIN", font=("Times New Roman", 20),bg="navy" ,fg="yellow",width=20,command=lambda: controller.show_frame(PageFive))
        b3.grid(row=10, column=10)
        b3.pack(pady=50, padx=50)
        b4 = tk.Button(self, text="DEPOSIT", font=("Times New Roman", 20),bg="navy" ,fg="yellow",width=20,command=lambda: controller.show_frame(PageSix))
        b4.grid(row=10, column=10)
        b4.pack(pady=50, padx=50)
        b5 = tk.Button(self, text="CANCEL", font=("Times New Roman", 20),bg="navy" ,fg="yellow",width=20,command=lambda: controller.show_frame(StartPage))
        b5.grid(row=10, column=10)
        b5.pack(pady=50, padx=50)


class PageFour(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        L1 = tk.Label(self,text="ENTER THE AMOUNT YOU WANT TO WITHDRAW",bg="navy" ,fg="yellow")
        L1.config(font=("Times New Roman", 20), width=50)
        L1.pack(pady=10, padx=10)
        E1 = tk.Entry(self,bd=8, fg="black", bg="white")
        E1.config(font=("Times New Roman", 20), width=20)
        E1.pack(pady=10, padx=10)


        def withdraw():
            if cursor1.execute('''SELECT bal FROM custs WHERE accno=?''', (x,)):
                print('Records fetched!')
            bal = str(cursor1.fetchone())
            print bal
            newbal=bal[1:-2]
            print(newbal)
            newbal1=int(newbal)
            y = int(E1.get())
            print y
            if newbal1>=y :
                if y%50==0:
                   newbal1=newbal1-y
                   if cursor2.execute('''UPDATE custs SET bal = ? WHERE accno = ? ''',(newbal1 ,x)):
                     print('Amount Withdrawn')
                     messagebox.showinfo("TRANSACTION SUCCESSFUL","AMOUNT WITHDRAWN !!!")
                     db.commit()

                else:
                    messagebox.showinfo("ERROR:","AMOUNT NOT IN MULTIPLES OF 50..PLEASE ENTER AGAIN")
            else:

                messagebox.showinfo("ERROR:","AMOUNT NOT AVAILABLE")

        b5 = tk.Button(self, text="WITHDRAW", font=("Times New Roman", 20), bg="sky blue" ,fg="black",
                       command=withdraw)
        b5.grid(row=10, column=10)
        b5.pack(pady=50, padx=50)
        b5 = tk.Button(self, text="CANCEL", font=("Times New Roman", 20), bg="sky blue" ,fg="black",
                       command=lambda: controller.show_frame(PageThree))
        b5.grid(row=10, column=10)
        b5.pack(pady=50, padx=50)


class PageFive(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        L1 = tk.Label(self, text="ENTER THE NEW PIN", fg="yellow", bg="navy")
        L1.config(font=("Times New Roman", 20), width=50)
        L1.pack(pady=10, padx=10)
        E1 = tk.Entry(self, bd=8, fg="black", bg="white")
        E1.config(font=("italic", 20), width=20)
        E1.pack(pady=10, padx=10)

        def pinchange():
              if cursor2.execute('''UPDATE custs SET pin = ? WHERE accno = ? ''', (E1.get(), x)):
                  print('PIN changed successfully')
                  db.commit()
                  messagebox.showinfo("PIN UPDATE","PIN CHANGED SUCCESSFULLY !!!")
                  controller.show_frame(PageThree)

        b5 = tk.Button(self, text="CHANGE PIN", font=("Times New Roman", 20),bg="sky blue", fg="black",
                       command=pinchange)
        b5.grid(row=10, column=10)
        b5.pack(pady=50, padx=50)
        b5 = tk.Button(self, text="CANCEL", font=("Times New Roman", 20),bg="sky blue",fg="black",
                       command=lambda: controller.show_frame(PageThree))
        b5.grid(row=10, column=10)
        b5.pack(pady=50, padx=50)


class PageSix(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        L1 = tk.Label(self, text="ENTER THE AMOUNT YOU WANT TO DEPOSIT", fg="yellow", bg="navy")
        L1.config(font=("Times New Roman", 20), width=50)
        L1.pack(pady=10, padx=10)
        E1 = tk.Entry(self, bd=8, fg="black", bg="white")
        E1.config(font=("italic", 20), width=20)
        E1.pack(pady=10, padx=10)

        def deposit():
            if cursor1.execute('''SELECT bal FROM custs WHERE accno=?''', (x,)):
                print('Records fetched!')
            bal = str(cursor1.fetchone())
            newbal = bal[1:-2]
            print(newbal)
            newbal1=int(newbal)
            y = E1.get()
            y=int(y)
            print y
            newbal1=newbal1+y
            if cursor2.execute('''UPDATE custs SET bal = ? WHERE accno = ? ''', (newbal1, x)):
                    print('Amount Deposited')
                    messagebox.showinfo("TRANSACTION SUCCESSFUL","AMOUNT DEPOSITED !!!")
                    db.commit()

        b5 = tk.Button(self, text="DEPOSIT", font=("Times New Roman", 20),bg="sky blue" ,fg="black",
                       command=deposit)
        b5.grid(row=10, column=10)
        b5.pack(pady=50, padx=50)
        b5 = tk.Button(self, text="CANCEL", font=("Times New Roman", 20),bg="sky blue", fg="black",
                       command=lambda: controller.show_frame(PageThree))
        b5.grid(row=10, column=10)
        b5.pack(pady=50, padx=50)


app=SeaofBTCapp()
app.mainloop()
