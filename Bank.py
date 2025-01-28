import tkinter as tk
from tkinter import messagebox
import pymysql
class bank():
    def __init__(self,root):
        self.root=root
        self.root.title('Bank managment system')
        scr_width=self.root.winfo_screenwidth()
        scr_height=self.root.winfo_screenheight()
        self.root.geometry(f"{scr_width}x{scr_height}+0+0")
        mainLabel=tk.Label(self.root,text='Bank account managment system',font=('Arial',40,'bold'),bg='light green',bd=5,relief='groove')
        mainLabel.pack(side='top',fill='x')
        mainFrame=tk.Frame(self.root,bg='light gray',bd='5',relief='ridge')
        mainFrame.place(x=400,y=90,width=450,height=550)
        openAcBtn=tk.Button(mainFrame,command=self.openAc,width=20,bg='light blue',text='open Account',bd=3,relief='raised',font=('arial',20,'bold'))
        openAcBtn.grid(row=0,column=0,padx=40,pady=65)
        depBtn=tk.Button(mainFrame,command = self.deposit,width=20,bg='light blue',text='Deposit',bd=3,relief='raised',font=('arial',20,'bold'))
        depBtn.grid(row=1,column=0,padx=40,pady=65)
        wtBtn=tk.Button(mainFrame,command=self.wd,width=20,bg='light blue',text='withdraw',bd=3,relief='raised',font=('arial',20,'bold'))
        wtBtn.grid(row=2,column=0,padx=40,pady=65)
    def openAc(self):
        self.openAcFrame = tk.Frame(self.root,bg='light gray',bd=5,relief='ridge')
        self.openAcFrame.place(x=400,y=90,width=450,height=550)
        uNameLabel = tk.Label(self.openAcFrame,text='User Name:',bg='light gray',font=('arial',15,'bold'))
        uNameLabel.grid(row=0,column=0,padx=20,pady=30)
        self.uNameIn = tk.Entry(self.openAcFrame,width=15,font=('Arial',15))
        self.uNameIn.grid(row=0,column=1,padx=5,pady=30)
        uPwLabel = tk.Label(self.openAcFrame,text='Enter password:',bg='light gray',font=('arial',15,'bold'))
        uPwLabel.grid(row=1,column=0,padx=20,pady=30)
        self.uPwIn = tk.Entry(self.openAcFrame,width=15,font=('Arial',15))
        self.uPwIn.grid(row=1,column=1,padx=5,pady=30)
        uConfirmPwLabel = tk.Label(self.openAcFrame,text='confirm password:',bg='light gray',font=('arial',15,'bold'))
        uConfirmPwLabel.grid(row=2,column=0,padx=20,pady=30)
        self.uConfirmPwIn = tk.Entry(self.openAcFrame,width=15,font=('Arial',15))
        self.uConfirmPwIn.grid(row=2,column=1,padx=5,pady=30)
        okBtn = tk.Button(self.openAcFrame,command=self.insert,text='ok',width=10,bg='light blue',bd=3,relief='ridge',font=('Arial',15,'bold'))
        okBtn.grid(row=3,column=0,padx=40,pady=120)
        closeBtn = tk.Button(self.openAcFrame,command=self.close_openAc,text='close',width=10,bg='light blue',bd=3,relief='ridge',font=('Arial',15,'bold'))
        closeBtn.grid(row=3,column=1,padx=40,pady=120)
    def close_openAc(self):
        self.openAcFrame.destroy()
    def insert(self):
        uName=self.uNameIn.get()
        uPW = self.uPwIn.get()
        confirm=self.uConfirmPwIn.get()

        if uPW == confirm:
            con = pymysql.connect(host='localhost',user='root',passwd='Bhuvan@12$',database='bankdb')
            cur = con.cursor()
            cur.execute("Insert into account (userName,userPW) values (%s,%s)",(uName,uPW))
            con.commit()
            con.close()
            tk.messagebox.showinfo("success","Account opend successfully!")
            self.clear()
        else:
            tk.messagebox.showerror("Error","Both Password Should Same!")
            self.clear()
    def clear(self):
        self.uNameIn.delete(0,tk.END)
        self.uPwIn.delete(0,tk.END)
        self.uConfirmPwIn.delete(0,tk.END)
    def deposit(self):
        self.depFrame = tk.Frame(self.root,bg='light gray',bd=5,relief='ridge')
        self.depFrame.place(x=400,y=90,width=450,height=550)
        NameLabel = tk.Label(self.depFrame,text='User Name:',bg='light gray',font=('arial',15,'bold'))
        NameLabel.grid(row=0,column=0,padx=20,pady=30)
        self.NameIn = tk.Entry(self.depFrame,width=15,font=('Arial',15))
        self.NameIn.grid(row=0,column=1,padx=5,pady=30)

        amountLabel = tk.Label(self.depFrame,text='Enter amount:',bg='light gray',font=('arial',15,'bold'))
        amountLabel.grid(row=1,column=0,padx=20,pady=30)
        self.amountIn = tk.Entry(self.depFrame,width=15,font=('Arial',15))
        self.amountIn.grid(row=1,column=1,padx=5,pady=30)

        okBtn = tk.Button(self.depFrame,command=self.deposit_fun,text='Deposit',width=10,bg='light blue',bd=3,relief='ridge',font=('Arial',15,'bold'))
        okBtn.grid(row=2,column=0,padx=40,pady=150)
        closeBtn = tk.Button(self.depFrame,command=self.close_deposit,text='Close',width=10,bg='light blue',bd=3,relief='ridge',font=('Arial',15,'bold'))
        closeBtn.grid(row=2,column=1,padx=40,pady=150)
    def deposit_fun(self):
        name = self.NameIn.get()
        amount = int(self.amountIn.get())
        con = pymysql.connect(host='localhost',user='root',passwd='Bhuvan@12$',database='bankdb')
        cur = con.cursor()
        cur.execute('select balance from account where userName = %s',name)
        data = cur.fetchone()
        if data:
            balance=data[0]
            if data[0] is None:
                balance=0
            update = balance+amount
            cur.execute("update account set balance = %s where userName = %s",(update,name))
            con.commit()
            con.close()
            tk.messagebox.showinfo("success","operation was successful !")
            self.clear_dep()

        else:
            tk.messagebox.showerror("Error","Invalid Customer Name!")
            self.clear_dep()


    def close_deposit(self):
        self.depFrame.destroy()
    def clear_dep(self):
        self.NameIn.delete(0,tk.END)
        self.amountIn.delete(0,tk.END)
    def wd(self):
        self.wd = tk.Frame(self.root,bg='light gray',bd=5,relief='ridge')
        self.wd.place(x=400,y=90,width=450,height=550)
        cName = tk.Label(self.wd,text='Customer Name:',bg='light gray',font=('arial',15,'bold'))
        cName.grid(row=0,column=0,padx=20,pady=30)
        self.cNameIn = tk.Entry(self.wd,width=15,font=('Arial',15))
        self.cNameIn.grid(row=0,column=1,padx=5,pady=30)
        cPw = tk.Label(self.wd,text='Enter password:',bg='light gray',font=('arial',15,'bold'))
        cPw.grid(row=1,column=0,padx=20,pady=30)
        self.cPwIn = tk.Entry(self.wd,width=15,font=('Arial',15))
        self.cPwIn.grid(row=1,column=1,padx=5,pady=30)
        cwd = tk.Label(self.wd,text='Enter amount:',bg='light gray',font=('arial',15,'bold'))
        cwd.grid(row=2,column=0,padx=20,pady=30)
        self.amountIn = tk.Entry(self.wd,width=15,font=('Arial',15))
        self.amountIn.grid(row=2,column=1,padx=5,pady=30)
        okBtn = tk.Button(self.wd,command=self.wd_fun,text='withdraw',width=10,bg='light blue',bd=3,relief='ridge',font=('Arial',15,'bold'))
        okBtn.grid(row=3,column=0,padx=40,pady=120)
        closeBtn = tk.Button(self.wd,command=self.close_wd,text='close',width=10,bg='light blue',bd=3,relief='ridge',font=('Arial',15,'bold'))
        closeBtn.grid(row=3,column=1,padx=40,pady=120)
    def wd_fun(self):
        name=self.cNameIn.get()
        pw = self.cPwIn.get()
        amount = int(self.amountIn.get())
        con = pymysql.connect(host='localhost',user='root',passwd='Bhuvan@12$',database='bankdb')
        cur = con.cursor()
        cur.execute('select userPW,balance from account where userName = %s',name)
        data = cur.fetchone()
        if data:
            if pw == data[0]:
                if data[1]>=amount:
                    update = data[1]-amount
                    cur.execute("update account set balance = %s where userName = %s",(update,name))
                    con.commit()
                    con.close()
                    tk.messagebox.showinfo("Success","operation was successful !")
                    self.clear_wd()

                else:
                    tk.messagebox.showerror("Error","Insufficent Balance !")
                    self.clear_wd()
            else:

                tk.messagebox.showerror("Error","Invalid password !")
                self.clear_wd()

        else:
            tk.messagebox.showerror("Error","Invalid Customer Name!")
            self.clear_wd()


    def close_wd(self):
        self.wd.destroy()
    def clear_wd(self):
        self.cNameIn.delete(0,tk.END)
        self.cPwIn.delete(0,tk.END)
        self.amountIn.delete(0,tk.END)
            

        







        


root=tk.Tk()
obj=bank(root)
root.mainloop()
