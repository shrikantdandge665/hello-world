import mysql.connector as sql
from tkinter import *
class myopen(Toplevel):
    def __init__(self):
        Toplevel.__init__(self)
        self.la=Label(self,text="name")
        self.la.grid(row=0,column=0)
        self.name=StringVar()
        self.tn=Entry(self,textvariable=self.name)
        self.tn.grid(row=0,column=1,columnspan=2)
        self.lb=Label(self,text="balance")
        self.lb.grid(row=1,column=0)
        self.balance=StringVar()
        self.t1=Entry(self,textvariable=self.balance)
        self.t1.grid(row=1,column=1,columnspan=2)
        self.btn=Button(self,text="ok",command=self.close)
        self.btn.grid(row=2,column=0,columnspan=2)
        self.grab_set()
    def close(self):
        self.destroy()

class mydeposit(Toplevel):
    def __init__(self):
        Toplevel.__init__(self)
        self.la=Label(self,text="Enter accno")
        self.la.grid(row=0,column=0)
        self.accno=StringVar()
        self.ta=Entry(self,textvariable=self.accno)
        self.ta.grid(row=0,column=1,columnspan=2)
        self.lb=Label(self,text="Enter amount to deposit")
        self.lb.grid(row=1,column=0)
        self.amount=StringVar()
        self.t1=Entry(self,textvariable=self.amount)
        self.t1.grid(row=1,column=1,columnspan=2)
        self.btn=Button(self,text="ok",command=self.close)
        self.btn.grid(row=2,column=0,columnspan=2)
        self.grab_set()
    def close(self):
        self.destroy()

class mywithdraw(Toplevel):
    def __init__(self):
        Toplevel.__init__(self)
        self.la=Label(self,text="Enter accno")
        self.la.grid(row=0,column=0)
        self.accno=StringVar()
        self.ta=Entry(self,textvariable=self.accno)
        self.ta.grid(row=0,column=1,columnspan=2)
        self.lb=Label(self,text="Enter amount to withdraw")
        self.lb.grid(row=1,column=0)
        self.amount=StringVar()
        self.t1=Entry(self,textvariable=self.amount)
        self.t1.grid(row=1,column=1,columnspan=2)
        self.btn=Button(self,text="ok",command=self.close)
        self.btn.grid(row=2,column=0,columnspan=2)
        self.grab_set()
    def close(self):
        self.destroy()

class mysearch(Toplevel):
    def __init__(self):
        Toplevel.__init__(self)
        self.la=Label(self,text="Enter accno")
        self.la.grid(row=0,column=0)
        self.accno=StringVar()
        self.ta=Entry(self,textvariable=self.accno)
        self.ta.grid(row=0,column=1,columnspan=2)
        self.btn=Button(self,text="ok",command=self.close)
        self.btn.grid(row=2,column=0,columnspan=2)
        self.grab_set()
    def close(self):
        self.destroy()

class mytrans(Toplevel):
    def __init__(self):
        Toplevel.__init__(self)
        self.la=Label(self,text="Enter accno")
        self.la.grid(row=0,column=0)
        self.accno=StringVar()
        self.ta=Entry(self,textvariable=self.accno)
        self.ta.grid(row=0,column=1,columnspan=2)
        self.btn=Button(self,text="ok",command=self.close)
        self.btn.grid(row=2,column=0,columnspan=2)
        self.grab_set()
    def close(self):
        self.destroy()

class myclose(Toplevel):
    def __init__(self):
        Toplevel.__init__(self)
        self.la=Label(self,text="Enter accno")
        self.la.grid(row=0,column=0)
        self.accno=StringVar()
        self.ta=Entry(self,textvariable=self.accno)
        self.ta.grid(row=0,column=1,columnspan=2)
        self.lb=Label(self,text="Do you want to delete acc (y/n)")
        self.lb.grid(row=1,column=0)
        self.response=StringVar()
        self.tr=Entry(self,textvariable=self.response)
        self.tr.grid(row=1,column=1)
        self.btn=Button(self,text="ok",command=self.close)
        self.btn.grid(row=2,column=0,columnspan=2)
        self.grab_set()
    def close(self):
        self.destroy()

class myinterest(Toplevel):
    def __init__(self):
        Toplevel.__init__(self)
        self.la=Label(self,text="Enter Rate:")
        self.la.grid(row=0,column=0)
        self.rate=StringVar()
        self.tr=Entry(self,textvariable=self.rate)
        self.tr.grid(row=0,column=1,columnspan=2)
        self.lb=Label(self,text="Enter Period:")
        self.lb.grid(row=1,column=0)
        self.period=StringVar()
        self.tr=Entry(self,textvariable=self.period)
        self.tr.grid(row=1,column=1,columnspan=2)
        self.btn=Button(self,text="ok",command=self.close)
        self.btn.grid(row=2,column=0,columnspan=2)
        self.grab_set()
    def close(self):
        self.destroy()





class myframe(Tk):
    def __init__(self):
        self.conn=sql.MySQLConnection(user="root",password="shrikant2",database="bankdb",charset='utf8')
        print("Connected to Database...")   
        Tk.__init__(self)
        self.geometry("900x600")
        self.b1=Button(self,text="open",command=self.open)
        self.b2=Button(self,text="deposit",command=self.deposit)
        self.b3=Button(self,text="withdraw",command=self.withdraw)
        self.b4=Button(self,text="search",command=self.search)
        self.b5=Button(self,text="gettrans",command=self.gettrans)
        self.b6=Button(self,text="close",command=self.close)
        self.b7=Button(self,text="listacc",command=self.listacc)
        self.b8=Button(self,text="interest",command=self.interest)
        self.b9=Button(self,text="clear",command=self.clear)
        self.b1.pack(side=TOP,fill=X)
        self.b2.pack(side=TOP,fill=X)
        self.b3.pack(side=TOP,fill=X)
        self.b4.pack(side=TOP,fill=X)
        self.b5.pack(side=TOP,fill=X)
        self.b6.pack(side=TOP,fill=X)
        self.b7.pack(side=TOP,fill=X)
        self.b8.pack(side=TOP,fill=X)
        self.b9.pack(side=TOP,fill=X)
        self.info=StringVar()
        self.lbl=Label(self,bg="yellow",textvariable=self.info)
        self.lbl.pack(side=TOP,fill=BOTH,expand=True)
        self.lst=Listbox(self,bg="yellow")
        self.lst.pack(side=BOTTOM,fill=BOTH,expand=True)
    def __del__(self):
        self.conn.close()
        print("Connection Closed..")
    def open(self):
        dlg=myopen()
        self.wait_window(dlg)
        self.name=str(dlg.name.get())
        self.balance=str(dlg.balance.get())
        smt="insert into accmaster(name,balance) values(%s,%s)"
        cur=self.conn.cursor()
        lst=[self.name,self.balance]
        cur.execute(smt,lst)
        smt="select max(accno) from accmaster"
        cur=self.conn.cursor()
        cur.execute(smt)
        row=cur.fetchone()
        self.accno=row[0]
        self.accno=str(self.accno)
        self.info.set("account is created \n account no is"+" "+self.accno)
        smt="insert into trans(accno,transtype,amount) values(%s,%s,%s)"
        lst=[self.accno,'d',self.balance]
        cur=self.conn.cursor()
        cur.execute(smt,lst)
        self.conn.commit()
        
        
    def deposit(self):
        dlg=mydeposit()
        self.wait_window(dlg)
        self.accno=str(dlg.accno.get())
        self.amount=str(dlg.amount.get())
        smt="update accmaster set balance=balance + %s where accno=%s"
        lst=[self.amount,self.accno]
        cur=self.conn.cursor()
        cur.execute(smt,lst)
        if cur.rowcount==1:
            self.info.set("Amount Deposited")
            smt="insert into trans(accno,transtype,amount) values(%s,%s,%s)"
            lst=[self.accno,'d',self.amount]
            cur=self.conn.cursor()
            cur.execute(smt,lst)
            self.conn.commit()
        else:
            self.info.set("Accno not found")

    def withdraw(self):
        dlg=mywithdraw()
        self.wait_window(dlg)
        self.accno=str(dlg.accno.get())
        self.amount=str(dlg.amount.get())
        smt="select balance from accmaster where accno="+self.accno
        cur=self.conn.cursor()
        cur.execute(smt)
        self.row=cur.fetchone()
        if self.row==None:
            self.info.set("Accno not found")

        self.bal=self.row[0]
        print(self.bal)
        if int(self.amount)>int(self.bal):
            self.info.set("Insufficient balance")
        else:    
            smt="update accmaster set balance=balance - %s where accno=%s"
            cur=self.conn.cursor()
            params=[self.amount,self.accno]
            cur.execute(smt,params)
            if cur.rowcount==1:
                self.info.set("Amount withdraw")
                smt="insert into trans(accno,transtype,amount) values(%s,%s,%s)"
                lst=[self.accno,'w',self.amount]
                cur=self.conn.cursor()
                cur.execute(smt,lst)
                self.conn.commit()


    def search(self):
        dlg=mysearch()
        self.wait_window(dlg)
        self.accno=str(dlg.accno.get())
        smt="select * from accmaster where accno="+self.accno
        cur=self.conn.cursor()
        cur.execute(smt)
        row=cur.fetchone()
        if row==None:
            self.info.set("Account not found")
        else:    
            self.info.set("name is:"+" "+str(row[1])+"\n"+"balance is:"+" "+str(row[2]))

    def gettrans(self):
        dlg=mytrans()
        self.wait_window(dlg)
        self.accno=str(dlg.accno.get())
        smt="select * from accmaster where accno="+self.accno
        cur=self.conn.cursor()
        cur.execute(smt)
        row=cur.fetchone()
        if row==None:
            self.info.set("Account not found")
        else:    
            smt="select * from trans where accno="+self.accno
            cur=self.conn.cursor()
            cur.execute(smt)
            self.rows=cur.fetchall()
            for self.row in self.rows:
                self.lst.insert(1,"date"+"                            "+"\ttype\t"+"                    "+"\tamount\t"+"     ")
                self.lst.insert(1,"----\t-------\t\t------\t---------------------------")
                self.lst.insert(1,"|"+str(self.row[1])+"|"+str(self.row[3]).ljust(8)+"|"+"             "+str(self.row[4]).rjust(8)+"|")
                self.lst.insert(1,"....\t.......\t\t......\t...........................................................")
              
    def close(self):
        dlg=myclose()
        self.wait_window(dlg)
        self.accno=str(dlg.accno.get())
        smt="select * from accmaster where accno="+self.accno
        cur=self.conn.cursor()
        cur.execute(smt)
        row=cur.fetchone()
        if row==None:
            self.info.set("Account not found")
        else:
            self.res=str(dlg.response.get())
            if self.res=="y":
                smt="delete from accmaster where accno="+self.accno
                cur=self.conn.cursor()
                cur.execute(smt)
                smt="delete from trans where accno="+self.accno
                cur=self.conn.cursor()
                cur.execute(smt)
                self.conn.commit()    
                self.info.set("Account deleted sucessfully")

    def listacc(self):
        smt="select * from accmaster"
        cur=self.conn.cursor()
        cur.execute(smt)
        self.rows=cur.fetchall()
        print(self.rows)
        for self.row in self.rows:
        	#self.info.set(self.rows)
        	#self.info.set(self.row)
            self.lst.insert(1,"  "+"Accno"+"       "+"\tNAME.\t"+"                    "+"\tBALANCE\t"+"     ")
            self.lst.insert(1,"----\t-------\t\t------\t---------------------------")
            self.lst.insert(1,"  "+str(self.row[0]) +"         "+ "\t%s" %str(self.row[1]).ljust(8) +"              "+ "\t\t%s" %str(self.row[2]).rjust(8) )
            self.lst.insert(1,"....\t.......\t\t......\t........................................................")
    def interest(self):
        dlg=myinterest()
        self.wait_window(dlg)
        self.r=str(dlg.rate.get())
        self.n=str(dlg.period.get())
        smt="select * from accmaster"
        cur=self.conn.cursor()
        cur.execute(smt)
        self.rows=cur.fetchall()
        for self.row in self.rows:
            self.accno=self.row[0]
            self.balance=self.row[2]
            self.si=self.balance*float(self.r)*float(self.n)/100
        smt="update accmaster set balance=balance + %s where accno=%s"
        lst=[self.si,self.accno]
        cur=self.conn.cursor()
        cur.execute(smt,lst)
        if cur.rowcount==1:
            self.info.set("Interest Added")
            smt="insert into trans(accno,transtype,amount) values(%s,%s,%s)"
            lst=[self.accno,'d',self.si]
            cur=self.conn.cursor()
            cur.execute(smt,lst)
            self.conn.commit()
        else:
            self.info.set("Accno not found")    
    
       
    def clear(self):
        self.lst.delete(0,END)
        self.info.set(" ")

win=myframe()
win.title("BANKDB")
win.mainloop()
        
