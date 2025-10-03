from tkinter import *
from tkinter import ttk
import pymysql

con = pymysql.connect(
    host="localhost",
    user="root",
    password="root",
    port=3306,
    database="riper"
)

cursor = con.cursor()

root = Tk()
root.geometry("1000x800")

def adduser():
    name = t1.get()
    model = t2.get()
    phone = t3.get()
    issue = t4.get()
    qry = "insert into customer values (%s,%s,%s,%s,%s)"
    val = (0,name,model,phone,issue)
    cursor.execute(qry,val)
    con.commit()

def show():
    cursor.execute("select * from customer")
    records = cursor.fetchall()
    for i,(id,name,model,phone,issue) in enumerate(records):
        table.insert("","end",values=(id,name,model,phone,issue))


l1 = Label(root,text="name").place(x=100,y=100)
l2 = Label(root,text="model").place(x=100,y=150)
l3 = Label(root,text="phone").place(x=100,y=200)
l4 = Label(root,text="issue").place(x=100,y=200)

t1 = Entry(root)
t1.place(x=200,y=100)
t2 = Entry(root)
t2.place(x=200,y=150)
t3 = Entry(root)
t3.place(x=200,y=200)
t4 = Entry(root)
t4.place(x=200,y=200)


b1  =Button(root,text="submit",width=15,command=adduser).place(x=200,y=250)
# b2  =Button(root,text="delete",width=15,command=deleteuser).place(x=300,y=250)
# b3  =Button(root,text="update",width=15,command=updateuser).place(x=400,y=250)
cols = ("id","name","model","phone","issue")
table = ttk.Treeview(root,columns=cols,show="headings")
for col in cols:
    table.heading(col,text= col)
    table.place(x=10,y=300)
show()
root.mainloop()