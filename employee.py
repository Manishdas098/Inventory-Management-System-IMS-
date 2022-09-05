from tkinter import *
from PIL import Image,ImageTk
from tkinter import ttk,messagebox
import sqlite3
class employeeClass:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1100x500+280+160")
        self.root.resizable(False, False)
        self.root.title("Inventory Manegment System | Devloped by Manish")
        self.root.config(bg="white")
        self.root.focus_force()
        
#===============================All Variable=====================================================================#
        self.var_searchby = StringVar()
        self.var_searchtxt= StringVar()
 
        self.var_emp_id = StringVar()
        self.var_gender = StringVar()
        self.var_contact= StringVar()
        self.var_name = StringVar()
        self.var_dob = StringVar()
        self.var_doj = StringVar()
        self.var_email = StringVar()
        self.var_pass = StringVar()
        self.var_utype = StringVar()
        self.var_salary = StringVar()

        
#======================================search frmae===============================================================#

        searchFrame = LabelFrame (self.root,bd=2,relief=RIDGE,font=("goudy old style" ,12 ,"bold"),text="search employee" , bg="white")
        searchFrame.place(x=250, y=20 , width=600,height=70)
   

#==============option++++++++++++++++++++++++#

        cmb_search=ttk.Combobox(searchFrame,textvariable=self.var_searchby,value=("Select","Email", "Name", "Contact") , state="readonly", justify=CENTER,font=("Segoe UI" ,15))
        cmb_search.place(x=10 ,y=10 , width=180)
        cmb_search.current(0)


        txt_search = Entry(searchFrame,textvariable=self.var_searchtxt, font=("times new roman" ,15,"bold"),bg="lightyellow")
        txt_search.place(x=200,y=10)
        
        btn_search = Button(searchFrame ,text=("Search"),command=self.search ,font=("goudy old style" ,15,"normal"),bg="#4caf50",fg="white" ,cursor="hand2").place(x=410,y=9, width=150, height=30)

#==============title################################################################

        title =Label(self.root , text="Employee Details" ,font=("Segoe UI" , 15,"bold") , bg="#0f4d7d" , fg="white").place(x=50,y=100, width=1000)

#==============content==========================#
#====================row1=========================================#
        lbl_empid =Label(self.root , text="Emp ID" ,font=("Segoe UI" , 15,"normal") , bg="white").place(x=50,y=150)       
        lbl_gender =Label(self.root , text="Gender" ,font=("Segoe UI" , 15,"normal") , bg="white").place(x=350,y=150)  
        lbl_contact =Label(self.root , text="Contact" ,font=("Segoe UI" , 15,"normal") , bg="white").place(x=750,y=150)  

        txt_empid =Entry(self.root ,bd=2,relief=GROOVE,textvariable=self.var_emp_id ,font=("times new roman" , 15,"normal") , bg="lightyellow").place(x=150,y=150,width=180)       
        txt_gender =Entry(self.root ,bd=2,relief=GROOVE, textvariable=self.var_gender  ,font=("times new roman" , 15,"normal") , bg="lightyellow").place(x=500,y=150,width=180)  
        cmb_gender=ttk.Combobox(self.root ,textvariable=self.var_gender,value=("Select","Male", "Female", "Other") , state="readonly", justify=CENTER,font=("times new roman" ,15))
        cmb_gender.place(x=500 ,y=150,width=180)
        cmb_gender.current(0)     
        txt_contact =Entry(self.root ,bd=2,relief=GROOVE,textvariable=self.var_contact,font=("times new roman" , 15,"normal") , bg="lightyellow").place(x=850,y=150,width=180)  


#====================row2=========================================#
        lbl_name =Label(self.root , text="Name" ,font=("Segoe UI" , 15,"normal") , bg="white").place(x=50,y=190)       
        lbl_dob =Label(self.root , text="D.O.B" ,font=("Segoe UI" , 15,"normal") , bg="white").place(x=350,y=190)  
        lbl_doj =Label(self.root , text="D.O.J" ,font=("Segoe UI" , 15,"normal") , bg="white").place(x=750,y=190)  

        txt_name =Entry(self.root ,bd=2,relief=GROOVE,textvariable=self.var_name ,font=("times new roman" , 15,"normal") , bg="lightyellow").place(x=150 ,y=190,width=180)      
        txt_dob =Entry(self.root ,bd=2,relief=GROOVE, textvariable=self.var_dob  ,font=("times new roman" , 15,"normal") , bg="lightyellow").place(x=500 ,y=190,width=180)     
        txt_doj =Entry(self.root ,bd=2,relief=GROOVE,textvariable=self.var_doj ,font=("times new roman" , 15,"normal") , bg="lightyellow").place(x=850,y=190,width=180)  


#====================row3=========================================#
        lbl_email =Label(self.root , text="email" ,font=("Segoe UI" , 15,"normal") , bg="white").place(x=50,y=230)       
        lbl_pass =Label(self.root , text="Password" ,font=("Segoe UI" , 15,"normal") , bg="white").place(x=350,y=230)  
        lbl_utype =Label(self.root , text="User Type" ,font=("Segoe UI" , 15,"normal") , bg="white").place(x=750,y=230)  

        txt_email =Entry(self.root ,bd=2,relief=GROOVE,textvariable=self.var_email ,font=("times new roman" , 15,"normal") , bg="lightyellow").place(x=150 ,y=230,width=180)      
        txt_pass =Entry(self.root ,bd=2,relief=GROOVE, textvariable=self.var_pass  ,font=("times new roman" , 15,"normal") , bg="lightyellow").place(x=500 ,y=230,width=180)     
        cmb_utype=ttk.Combobox(self.root ,textvariable=self.var_utype,value=("Admin","Employee") , state="readonly", justify=CENTER,font=("times new roman" ,15))
        cmb_utype.place(x=850,y=230,width=180)
        cmb_utype.current(0)  



#====================row3=========================================#
        lbl_address =Label(self.root , text="address" ,font=("Segoe UI" , 15,"normal") , bg="white").place(x=50,y=270)       
        lbl_salary =Label(self.root , text="salary" ,font=("Segoe UI" , 15,"normal") , bg="white").place(x=500,y=270)  
    

        self.txt_address =Text(self.root ,bd=2,relief=GROOVE ,font=("times new roman" , 15,"normal") , bg="lightyellow")
        self.txt_address.place(x=150 ,y=270,width=300,height=60)      
        txt_salary =Entry(self.root ,bd=2,relief=GROOVE, textvariable=self.var_salary  ,font=("times new roman" , 15,"normal") , bg="lightyellow").place(x=600,y=270,width=180)     

#================================buttons==============================#

        btn_add = Button(self.root ,command=self.add,text="Save" ,font=("Segoe UI" , 15,"normal"),bg="#2196f3",fg="white" ,cursor="hand2").place(x=500,y=310, height=28,width=110)
        btn_update = Button(self.root ,command=self.update,text="update" ,font=("Segoe UI" , 15,"normal"),bg="#4caf50",fg="white" ,cursor="hand2").place(x=620,y=310, height=28,width=110)
        btn_del = Button(self.root ,text="Delete",command=self.delete ,font=("Segoe UI" , 15,"normal"),bg="#f44336",fg="white" ,cursor="hand2").place(x=740,y=310, height=28,width=110)
        btn_clear = Button(self.root ,text="Clear" ,command=self.clear,font=("Segoe UI" , 15,"normal"),bg="#607d8b",fg="white" ,cursor="hand2").place(x=860,y=310, height=28,width=110)

#==============================Employee details==================================#  
        emp_frame = Frame(self.root , bd=3, relief=RIDGE)
        emp_frame.place(x=0 , y=350, relwidth=1,height=150)
        
        scrolly = Scrollbar(emp_frame,orient=VERTICAL)
        scrollx = Scrollbar(emp_frame,orient=HORIZONTAL)
        
        self.employeeTable = ttk.Treeview(emp_frame,columns=("eid" , "name" , "email" , "gender" , "contact" , "dob" , "doj" , "pass" ,"utype" , "address" , "salary"),yscrollcommand=scrolly.set , xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM , fill=X)
        scrolly.pack(side=RIGHT , fill=Y)
        scrollx.config(command=self.employeeTable.xview)
        scrolly.config(command=self.employeeTable.yview)
        
        
        self.employeeTable.heading("eid" , text="Emp ID")
        self.employeeTable.heading("name" , text="Name")
        self.employeeTable.heading("email" , text="Email")
        self.employeeTable.heading("gender" , text="Gender")
        self.employeeTable.heading("contact" , text="Contact")
        self.employeeTable.heading("dob" , text="D.O.B")
        self.employeeTable.heading("doj" , text="D.O.J")
        self.employeeTable.heading("pass" , text="Password")
        self.employeeTable.heading("utype" , text="User Type")
        self.employeeTable.heading("address" , text="Address")
        self.employeeTable.heading("salary" , text="Salary")
        
        
       
        self.employeeTable.column("eid" ,width="90")
        self.employeeTable.column("name" ,width="100")
        self.employeeTable.column("email" ,width="100")
        self.employeeTable.column("gender" ,width="100")
        self.employeeTable.column("contact",width="100")
        self.employeeTable.column("dob" ,width="100")
        self.employeeTable.column("doj",width="100")
        self.employeeTable.column("pass",width="100")
        self.employeeTable.column("utype" ,width="100")
        self.employeeTable.column("address" ,width="100")
        self.employeeTable.column("salary" ,width="100")

        
        self.employeeTable.pack(fill=BOTH, expand=1)
        self.employeeTable.bind("<ButtonRelease-1>",self.get_data)
        self.employeeTable["show"]="headings"
        
        
        
        self.show() 
#=================================================fungtion===========================================#        
    def add(self):
        con = sqlite3.connect(database=r"Database/ims.db")
        cur = con.cursor()
        try:
                if self.var_emp_id.get()=="":
                    messagebox.showerror("Error","Employee ID must be reqiure",parent=self.root)
                else:
                    cur.execute("Select * from employee where eid=?",(self.var_emp_id.get(),))   
                    row=cur.fetchone()
                    if row!=None:
                            messagebox.showerror("Erorr" ,"This employee is ID already assigned , try different",parent=self.root)
                    else:
                            cur.execute("Insert into employee (eid , name , email , gender , contact , dob , doj , pass ,utype , address , salary) values (?,?,?,?,?,?,?,?,?,?,?)",(
                                      self.var_emp_id.get(),
                                      self.var_name.get(),
                                      self.var_email.get(),
                                      self.var_gender.get(),
                                      self.var_contact.get(),
                                      self.var_dob.get(),
                                      self.var_doj.get(),
                                      self.var_pass.get(),
                                      self.var_utype.get(),
                                      self.txt_address.get("1.0" ,END),
                                      self.var_salary.get()
                            ))
                            con.commit()
                            self.show()
                            self.exit()
                            messagebox.showinfo("Success" , "employee details has been added successfully")
        except Exception as ex:
                messagebox.showerror("Error",f"error due to : {str(ex)}",parent=self.root)
                
                
        
       
    def show(self):
                
                con = sqlite3.connect(database=r"Database/ims.db")
                cur = con.cursor()
                try:
                        cur.execute("select * from employee")
                        rows=cur.fetchall()
                        self.employeeTable.delete(*self.employeeTable.get_children())
                        for row in rows:
                                self.employeeTable.insert('' , END , values =row)
                                col = len(rows)
                                print (col)
                                
                except Exception as ex:
                        messagebox.showerror("Error",f"error due to : {str(ex)}",parent=self.root)
    def get_data(self ,ev):
            f = self.employeeTable.focus()
            content = (self.employeeTable.item(f))
            row = content['values']
            self.var_emp_id.set(row[0])
            self.var_name.set(row[1])
            self.var_email.set(row[2])
            self.var_gender.set(row[3])
            self.var_contact.set(row[4])
            self.var_dob.set(row[5])
            self.var_doj.set(row[6])
            self.var_pass.set(row[7])
            self.var_utype.set(row[8])
            self.txt_address.delete("1.0" ,END),
            self.txt_address.insert(END ,row[9]),
            self.var_salary.set(row[10])               
    def update(self):
        con = sqlite3.connect(database=r"Database/ims.db")
        cur = con.cursor()
        try:
                if self.var_emp_id.get()=="":
                    messagebox.showerror("Error","Employee ID must be reqiure",parent=self.root)
                else:
                    cur.execute("Select * from employee where eid=?",(self.var_emp_id.get(),))   
                    row=cur.fetchone()
                    if row==None:
                            messagebox.showerror("Erorr" ,"Invalid employee ID , try different",parent=self.root)
                    else:
                            cur.execute("Update employee set name=? , email=? , gender=? , contact=? , dob=? , doj=? , pass=? ,utype=? , address=? , salary=? where eid=?",(
                               
                                      self.var_name.get(),
                                      self.var_email.get(),
                                      self.var_gender.get(),
                                      self.var_contact.get(),
                                      self.var_dob.get(),
                                      self.var_doj.get(),
                                      self.var_pass.get(),
                                      self.var_utype.get(),
                                      self.txt_address.get("1.0" ,END),
                                      self.var_salary.get(),
                                      self.var_emp_id.get()
                            ))
                            con.commit()
                            self.show()
                            self.exit()
                            messagebox.showinfo("Success" , "employee details has been added successfully")
        except Exception as ex:
                messagebox.showerror("Error",f"error due to : {str(ex)}",parent=self.root)        
    def delete (self):
            
            con = sqlite3.connect(database=r"Database/ims.db")
            cur = con.cursor()
            try:
                if self.var_emp_id.get()=="":
                        messagebox.showerror("Error","Employee ID must be reqiure",parent=self.root)
                else:
                    cur.execute("Select * from employee where eid=?",(self.var_emp_id.get(),))   
                    row=cur.fetchone()
                    if row==None:
                            messagebox.showerror("Erorr" ,"Invalid employee ID , try different",parent=self.root)
                    else:
                            op = messagebox.askyesno("Confirm",'Do you realy want to delete' , parent=self.root)
                            if op==True:
                               cur.execute('Delete from employee where eid=?', (self.var_emp_id.get(),))
                               con.commit()
                               messagebox.showinfo('delete' , "employee deleted successfully", parent=self.root)
                               self.clear()
                               self.exit()
                    
            except Exception as ex: 
                    messagebox.showerror("Error",f"error due to : {str(ex)}",parent=self.root)       
    
    def clear(self):
                  
                   self.var_emp_id.set("")
                   self.var_name.set("")
                   self.var_email.set("")
                   self.var_gender.set("Select")
                   self.var_contact.set("")
                   self.var_dob.set("")
                   self.var_doj.set("")
                   self.var_pass.set("")
                   self.var_utype.set("Admin")
                   self.txt_address.delete("1.0" ,END)
                #    self.txt_address.insert(END ,row[9]),
                   self.var_salary.set("")
                   self.show()            
                   
          
    def search(self):    
              con = sqlite3.connect(database=r"Database/ims.db")
              cur = con.cursor()
              try:
                        if self.var_searchby.get() =="Select":
                                messagebox.showerror("error" , "select search by option" , parent=self.root)
                        elif self.var_searchtxt.get() =="":
                                messagebox.showerror("error" , "search input must be reqiure" , parent=self.root)
                        else:               
                                cur.execute("select * from employee where "+self.var_searchby.get()+" LIKE '%"+self.var_searchtxt.get()+"%'")
                                rows=cur.fetchall()
                                if len(rows)!= 0:                                        
                                     self.employeeTable.delete(*self.employeeTable.get_children())
                                     for row in rows:
                                       self.employeeTable.insert('' , END , values =row)
                                else:
                                        messagebox.showerror("error" , "No record found")
              except Exception as ex:
                        messagebox.showerror("Error",f"error due to : {str(ex)}",parent=self.root)   
                        
                        
    def exit(self):
            self.root.destroy()                      
                                  
if __name__ == "__main__":
       
    root = Tk();
    obj = employeeClass(root);
    root.mainloop();            