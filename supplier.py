from tkinter import *
from PIL import Image,ImageTk
from tkinter import ttk,messagebox
import sqlite3
import os
import PIL
from resizeimage import resizeimage
import qrcode 
class supplierClass:
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

        self.invoice = StringVar()
        self.var_name = StringVar()
        self.var_contact= StringVar()
        self.var_email = StringVar()







        
#======================================search frmae===============================================================#

        # searchFrame = LabelFrame (self.root,bd=2,relief=RIDGE,font=("goudy old style" ,12 ,"bold"),text="search employee" , bg="white")
        # # searchFrame.place(x=250, y=20 , width=600,height=70)
   
   
   
#==============option++++++++++++++++++++++++#
        lbl_search = Label(self.root,text="Invoice no.", font=("Segoe UI" ,15,"bold"))
        lbl_search.place(x=680 ,y=80 )
        
        # cmb_search=ttk.Combobox(self.root,textvariable=self.var_searchby,value=("Select","Email", "Name", "Contact") , state="readonly", justify=CENTER,font=("Segoe UI" ,15))
        # cmb_search.place(x=10 ,y=80 , width=180)
        # cmb_search.current(0)


        txt_search = Entry(self.root,textvariable=self.var_searchtxt, font=("Segoe UI" ,15,"bold"),bg="lightyellow")
        txt_search.place(x=800 ,y=80, width=180 )
        
        btn_search = Button(self.root ,text=("Search"),command=self.search ,font=("goudy old style" ,15,"normal"),bg="#4caf50",fg="white" ,borderwidth = 0,cursor="hand2").place(x=970,y=79, width=100, height=29)



#==============title################################################################

        title =Label(self.root , text="Supplier Details" ,font=("Segoe UI" , 15,"bold") , bg="#0f4d7d" , fg="white").place(x=50,y=10, width=1000 , height=40)

#==============content==========================#
#====================row1=========================================#
        lbl_supplier_invoice =Label(self.root , text="invoice no" ,font=("Segoe UI" , 15,"normal") , bg="white").place(x=50,y=60)       
        
        txt_supplier_invoice =Entry(self.root ,bd=2,relief=GROOVE,textvariable=self.invoice ,font=("Segoe UI" , 15,"normal") , bg="lightyellow").place(x=170,y=60,width=180)       
        


#====================row2=========================================#
        lbl_name =Label(self.root , text="Name" ,font=("Segoe UI" , 15,"normal") , bg="white").place(x=50,y=100)       
       

        txt_name =Entry(self.root ,bd=2,relief=GROOVE,textvariable=self.var_name ,font=("Segoe UI" , 15,"normal") , bg="lightyellow").place(x=170 ,y=100,width=180)      
        


#====================row3=========================================#
        lbl_contact =Label(self.root , text="Contact" ,font=("Segoe UI" , 15,"normal") , bg="white").place(x=50,y=140)       
      
        txt_contact =Entry(self.root ,bd=2,relief=GROOVE,textvariable=self.var_contact ,font=("Segoe UI" , 15,"normal") , bg="lightyellow").place(x=170 ,y=140,width=180)  
   
       
#====================row3=========================================#
        lbl_txt_desc =Label(self.root , text="Description" ,font=("Segoe UI" , 15,"normal") , bg="white").place(x=50,y=180)       
        lbl_salary =Label(self.root  ,font=("Segoe UI" , 15,"normal") , bg="white").place(x=500,y=180)  
    

        self.txt_desc =Text(self.root ,bd=2,relief=GROOVE ,font=("Segoe UI" , 15,"normal") , bg="lightyellow")
        self.txt_desc.place(x=170 ,y=180,width=330,height=120)      
     

#================================buttons==============================#

        btn_add = Button(self.root ,command=self.add,text="Save" ,font=("Segoe UI" , 15,"normal"),bg="#2196f3",fg="white" ,cursor="hand2").place(x=50,y=320, height=35,width=110)
        btn_update = Button(self.root ,command=self.update,text="update" ,font=("Segoe UI" , 15,"normal"),bg="#4caf50",fg="white" ,cursor="hand2").place(x=170,y=320, height=35,width=110)
        btn_del = Button(self.root ,text="Delete",command=self.delete ,font=("Segoe UI" , 15,"normal"),bg="#f44336",fg="white" ,cursor="hand2").place(x=290,y=320, height=35,width=110)
        btn_clear = Button(self.root ,text="Clear" ,command=self.clear,font=("Segoe UI" , 15,"normal"),bg="#607d8b",fg="white" ,cursor="hand2").place(x=410,y=320, height=35,width=110)
        btn_gen = Button(self.root ,text="Genrate" ,command=self.genrate,font=("Segoe UI" , 15,"normal"),bg="#2196f3",fg="white" ,cursor="hand2").place(x=530,y=320, height=35,width=110)

#==============================Employee details==================================#  
        emp_frame = Frame(self.root , bd=3, relief=RIDGE)
        emp_frame.place(x=680 , y=120, width=380,height=350)
        
        scrolly = Scrollbar(emp_frame,orient=VERTICAL)
        scrollx = Scrollbar(emp_frame,orient=HORIZONTAL)
        
        self.employeeTable = ttk.Treeview(emp_frame,columns=("invoice" , "name", "contact" ,"desc"),yscrollcommand=scrolly.set , xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM , fill=X)
        scrolly.pack(side=RIGHT , fill=Y)
        scrollx.config(command=self.employeeTable.xview)
        scrolly.config(command=self.employeeTable.yview)
        
        
        self.employeeTable.heading("invoice" , text="Emp ID")
        self.employeeTable.heading("name" , text="Name")
        self.employeeTable.heading("contact" , text="Contact")
        self.employeeTable.heading("desc" , text ="Description")
        
        
       
        self.employeeTable.column("invoice" ,width="90")
        self.employeeTable.column("name" ,width="100")
        self.employeeTable.column("contact",width="100")
        self.employeeTable.column("desc" ,width="100")
      
        
        
        
        
        
        
        
        
        
        
        
        
        
        self.employeeTable.pack(fill=BOTH, expand=1)
        self.employeeTable.bind("<ButtonRelease-1>",self.get_data)
        self.employeeTable["show"]="headings"
        
        
        
        self.show() 
#=================================================fungtion===========================================#   

     
    def add(self):
        con = sqlite3.connect(database=r"Database/ims.db")
        cur = con.cursor()
        try:
                if self.invoice.get()=="":
                    messagebox.showerror("Error","Employee ID must be reqiure",parent=self.root)
                else:
                    cur.execute("Select * from supplier where invoice=?",(self.invoice.get(),))   
                    row=cur.fetchone()
                    if row!=None:
                            messagebox.showerror("Erorr" ,"This employee is ID already assigned , try different",parent=self.root)
                    else:
                            cur.execute("Insert into supplier (invoice , name , contact ,desc) values (?,?,?,?)",(
                                      self.invoice.get(),
                                      self.var_name.get(),
                                      self.var_contact.get(),
                                      self.txt_desc.get("1.0" ,END)
                                     
                            ))
                            con.commit()
                            self.show()
                            self.clear()
                            messagebox.showinfo("Success" , "employee details has been added successfully")
                            self.exit()
        except Exception as ex:
                messagebox.showerror("Error",f"error due to : {str(ex)}",parent=self.root)
                
    def genrate(self):
     
        if self.invoice.get()=="":
            messagebox.showinfo("Error","plese ender a fleld") 
        else:
            qr_data =(f"Invoice no: {self.invoice.get()}\n Name: {self.var_name.get()}\n Contact: {self.var_contact.get()}\n Description:{self.var_email.get()}")
            qr_code = qrcode.make(qr_data)
            # print(qr_code)

            qr_code = resizeimage.resize_cover(qr_code,[200,200])
            QR =  qr_code.save("Invoice/invoice no. "+str(self.invoice.get())+'.png')
            
            file ="Invoice"
           
            path = os.path.abspath(file)
            path1 = path+"\Invoice no. "+str(self.invoice.get())+'.png'
            print (path1)
            messagebox.showinfo("Qr saved","Roll no "+str(self.invoice.get())+" has been Genrated and saved at " +path1)    
           
            self.clear()
            sub = Toplevel(root)
            sub.title("Qr-Code")
            sub.geometry("225x220+390+500")
            sub.resizable(False, False)
     
            img = ImageTk.PhotoImage(Image.open(path1))
            panel = Label(sub, image = img, bd=4 , relief=GROOVE ,  bg="#0f4d7d")
            panel.pack( fill = "none", expand = "no" )
            self.sales()
            self.exit()
            

          
          
                        
        
       
    def show(self):
                
                con = sqlite3.connect(database=r"Database/ims.db")
                cur = con.cursor()
                try:
                        cur.execute("select * from supplier") 
                        rows=cur.fetchall()
                        self.employeeTable.delete(*self.employeeTable.get_children())
                        for row in rows:
                                self.employeeTable.insert('' , END , values =row)
                                
                except Exception as ex:
                        messagebox.showerror("Error",f"error due to : {str(ex)}",parent=self.root)
    def get_data(self ,ev):
            f = self.employeeTable.focus()
            content = (self.employeeTable.item(f))
            row = content['values']
            self.invoice.set(row[0])
            self.var_name.set(row[1])
            self.var_contact.set(row[2])
            self.txt_desc.delete("1.0" ,END),
            self.txt_desc.insert(END ,row[3])
                         
    def update(self):
        con = sqlite3.connect(database=r"Database/ims.db")
        cur = con.cursor()
        try:
                if self.invoice.get()=="":
                    messagebox.showerror("Error","Invoice no must be reqiure",parent=self.root)
                else:
                    cur.execute("Select * from supplier where invoice=?",(self.invoice.get(),))   
                    row=cur.fetchone()
                    if row==None:
                            messagebox.showerror("Erorr" ,"Invalid invoice no. , try different",parent=self.root)
                    else:
                            cur.execute("Update supplier set name=?, contact=? , desc=? where invoice=?",(
                               
                                      self.var_name.get(),
                                      self.var_contact.get(),
                                      self.txt_desc.get("1.0" ,END),
                                      self.invoice.get()
                            ))
                            con.commit()
                            self.show()
                            
                            messagebox.showinfo("Success" , "supplier details has been added successfully")
                            self.exit()
        except Exception as ex:
                messagebox.showerror("Error",f"error due to : {str(ex)}",parent=self.root)        
    def delete (self):
            
            con = sqlite3.connect(database=r"Database/ims.db")
            cur = con.cursor()
            try:
                if self.invoice.get()=="":
                        messagebox.showerror("Error","Invice no. must be reqiure",parent=self.root)
                else:
                    cur.execute("Select * from supplier where invoice=?",(self.invoice.get(),))   
                    row=cur.fetchone()
                    if row==None:
                            messagebox.showerror("Erorr" ,"Invalid supplier Id , try different",parent=self.root)
                    else:
                            op = messagebox.askyesno("Confirm",'Do you realy want to delete' , parent=self.root)
                            if op==True:
                               cur.execute('Delete from supplier where invoice=?', (self.invoice.get(),))
                               con.commit()
                               messagebox.showinfo('delete' , "supplier deleted successfully", parent=self.root)
                               self.clear()
                               self.exit()
                    
            except Exception as ex: 
                    messagebox.showerror("Error",f"error due to : {str(ex)}",parent=self.root)       
    
    def clear(self):
                  
                   self.invoice.set("")
                   self.var_name.set("")
                   self.var_contact.set("")
                   self.txt_desc.delete("1.0" ,END)
                #    self.txt_desc.insert(END ,row[9]),
  
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
                                cur.execute("select * from supplier where invoice=?" , (self.var_searchtxt.get(), ))
                                rows=cur.fetchone()
                                if rows != None:                                        
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
    obj = supplierClass(root);
    root.mainloop();            