import mysql.connector as sql
class Account:
    def __init__(self):
        self.conn=sql.MySQLConnection(user="root",password="shrikant2",database="bankdb",charset='utf8')
        print("Connected to Database...")
        
    def __del__(self):
        self.conn.close()
        print("Connection Closed..")
        
    def open(self,nm,bl):
        smt="insert into accmaster(name,balance) values(%s,%s)"
        cur=self.conn.cursor()
        lst=[nm,bl]
        cur.execute(smt,lst)
        smt="select max(accno) from accmaster"
        cur=self.conn.cursor()
        cur.execute(smt)
        row=cur.fetchone()
        accno=row[0]
        self.trans(accno,'d',bl)
        self.conn.commit()
        return accno
    
    def deposit(self,an,amt):
        smt="update accmaster set balance=balance + %s where accno=%s"
        lst=[amt,an]
        cur=self.conn.cursor()
        cur.execute(smt,lst)
        if cur.rowcount==1:
            self.trans(an,'d',amt)
            self.conn.commit()
            return True
        return False
    
    def withdraw(self,an,amt):
        smt="select balance from accmaster where accno="+an
        cur=self.conn.cursor()
        cur.execute(smt)
        row=cur.fetchone()
        if row==None:
            return -1
        bal=row[0]
        if int(amt)>bal:
            return 0
        smt="update accmaster set balance=balance - %s where accno=%s"
        cur=self.conn.cursor()
        params=[amt,an]
        cur.execute(smt,params)
        self.trans(an,'w',amt)
        self.conn.commit()
        return 1
    
    def search(self,an):
        smt="select * from accmaster where accno="+an
        cur=self.conn.cursor()
        cur.execute(smt)
        row=cur.fetchone()
        return row
    
    def gettrans(self,an):
        smt="select * from trans where accno="+an
        cur=self.conn.cursor()
        cur.execute(smt)
        rows=cur.fetchall()
        return rows

    def close(self,an):
        smt="delete from accmaster where accno="+an
        cur=self.conn.cursor()
        cur.execute(smt)
        smt="delete from trans where accno="+an
        cur=self.conn.cursor()
        cur.execute(smt)
        self.conn.commit()

    def listacc(self):
        smt="select * from accmaster"
        cur=self.conn.cursor()
        cur.execute(smt)
        rows=cur.fetchall()
        return rows

    def interest(self,r,n):
        rows=self.listacc()
        for row in rows:
            an=row[0]
            bal=row[2]
            si=bal*float(r)*float(n)/100
            self.deposit(an,si)
    
    def trans(self,an,ty,amt):
        smt="insert into trans(accno,transtype,amount) values(%s,%s,%s)"
        lst=[an,ty,amt]
        cur=self.conn.cursor()
        cur.execute(smt,lst)

acc=Account()
ch=0
while ch!=9:
    menu="1:Open Acc\n2:Depost\n3:Withdraw\n4:Search\n5:Transaction\n6:CloseAcc\n7:List\n8:Interest\n9:Exit"
    print(menu)
    ch=int(input("Enter Choice:"))
    if ch==1:
        nm=input("Enter Name:")
        bl=input("Enter Balance:")
        an=acc.open(nm,bl)
        print("Account Opened : AccNo:",an)
    if ch==2:
        an=input("Enter AccNo:")
        amt=input("Enter Amount to Deposit:")
        if(acc.deposit(an,amt)):
            print("Amount Deposited..")
        else:
            print("AccNo Not Found..")
    if ch==3:
        an=input("Enter AccNo:")
        amt=input("Enter Amount to Withdraw:")
        res=acc.withdraw(an,amt)
        if res==-1:
            print("AccNo Not Found..")
        elif res==0:
            print("Insufficient Balance")
        else:
            print("Amount Withdrawn Successfully..")
    if ch==4:
        an=input("Enter AccNo:")
        row=acc.search(an)
        if row==None:
            print("AccNo not Found..")
        else:
            print("Name:",row[1])
            print("Balance:",row[2])
    if ch==5:
        an=input("Enter AccNo:")
        row=acc.search(an)
        if row==None:
            print("AccNo not Found..")
        else:
            print("Name:",row[1])
            print("Balance:",row[2])
            rows=acc.gettrans(an)
            print("-"*37)
            for row in rows:
                print("|",row[1],"|",row[3],"|",str(row[4]).rjust(8),"|")
            print("-"*37)
    if ch==6:
        an=input("Enter AccNo:")
        row=acc.search(an)
        if row==None:
            print("AccNo not Found..")
        else:
            print("Name:",row[1])
            print("Balance:",row[2])
            res=input("Are you sure ? (y/n):")
            if res=="y":
                acc.close(an)
                print("A/C closed successfully..")
    if ch==7:
        rows=acc.listacc()
        print("-"*42)
        for row in rows:
              print("|",row[0],"|",row[1].ljust(20),"|",str(row[2]).rjust(8),"|")
        print("-"*42)
    if ch==8:
        r=input("Enter IRate:")
        n=input("Enter Period:")
        acc.interest(r,n)
        print("Calculated and added..")
del acc
