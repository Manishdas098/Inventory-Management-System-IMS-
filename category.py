from tkinter import *
from PIL import Image,ImageTk
from tkinter import ttk,messagebox
import sqlite3
import os
import PIL
from resizeimage import resizeimage
import qrcode 
class categoryClass:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1100x500+280+160")
        self.root.resizable(False, False)
        self.root.title("Inventory Manegment System | Devloped by Manish")
        self.root.config(bg="white")
        self.root.focus_force()
# ================================variables =============================#
        self.var_cid = StringVar()
        self.var_name = StringVar()
    
        
        
        
        
#################################################Start#####################################        
        lbl_title = Label(self.root , text="Manage Product Category" ,font=("Segoe UI" , 30) ,bd=3,relief=RIDGE, bg='#184a45' , fg="white" ).pack(side=TOP , fill=X, padx=10 ,pady=20)
        
        lbl_name = Label(self.root , text="Enter Category name" ,font=("Segoe UI" , 25)  )
        lbl_name.place(x=50 , y=100)
        
        lbl_Entry = Entry(self.root ,bg="lightyellow",textvariable=self.var_name,font=("Segoe UI" , 18))
        lbl_Entry.place(x=50 , y=170 , width=300)
        
        btn_add = Button(self.root,text="Add" ,command=self.add,bg="#4caf50" , fg="white" ,cursor="hand2", font=("Segoe UI" , 18))
        btn_add.place(x=360 , y=170 , height=30,width=150)

        btn_delete = Button(self.root,text="delete" ,bg="red" ,command=self.delete, fg="white" ,cursor="hand2", font=("Segoe UI" , 18))
        btn_delete.place(x=520 , y=170 , height=30,width=150)
        
        
# =======================================category frame======================================        
        cat_frame = Frame(self.root , bd=3, relief=RIDGE)
        cat_frame.place(x=700 , y=100, width=380,height=100)
        
        scrolly = Scrollbar(cat_frame,orient=VERTICAL)
        scrollx = Scrollbar(cat_frame,orient=HORIZONTAL)
        
        self.CategoryTable = ttk.Treeview(cat_frame,columns=("cid" , "name"),yscrollcommand=scrolly.set , xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM , fill=X)
        scrolly.pack(side=RIGHT , fill=Y)
        scrollx.config(command=self.CategoryTable.xview)
        scrolly.config(command=self.CategoryTable.yview)
        
        self.CategoryTable.heading("cid" , text="C Id")
        self.CategoryTable.heading("name" , text="Name")

        
        self.CategoryTable.column("cid" ,width="10")
        self.CategoryTable.column("name" ,width="130")

                
        self.CategoryTable.pack(fill=BOTH, expand=1)
        self.CategoryTable.bind("<ButtonRelease-1>",self.get_data)
        self.CategoryTable["show"]="headings"
        
        #=========================================image================================########
        
        self.im1=Image.open("images/cat.jpg") 
        self.im1= self.im1.resize((500,250),Image.ANTIALIAS)
        self.im1= ImageTk.PhotoImage(self.im1)


        self.lbl_im1 = Label(self.root, image=self.im1,bd=2, relief=RIDGE)
        self.lbl_im1.place(x=50 , y=220)
        
        
        self.im2=Image.open("images/category.jpg") 
        self.im2= self.im2.resize((500,250),Image.ANTIALIAS)
        self.im2= ImageTk.PhotoImage(self.im2)


        self.lbl_im2 = Label(self.root, image=self.im2,bd=2, relief=RIDGE)
        self.lbl_im2.place(x=580 , y=220)
        self.show()
    def add(self):
        con = sqlite3.connect(database=r"Database/ims.db")
        cur = con.cursor()
        try:
                if self.var_name.get()=="":
                    messagebox.showerror("Error","category name must be reqiure",parent=self.root)
                else:
                    cur.execute("Select * from category where name=?",(self.var_name.get(),))   
                    row=cur.fetchone()
                    if row!=None:
                            messagebox.showerror("Erorr" ,"This Category already present , try different",parent=self.root)
                    else:
                            cur.execute("Insert into category (name) values (?)",(self.var_name.get(),))
                            con.commit()
                            self.show()
                            messagebox.showinfo("Success" , "employee details has been added successfully")
                            self.clear()
        except Exception as ex:
                messagebox.showerror("Error",f"error due to : {str(ex)}",parent=self.root)
    def show(self):
                
                con = sqlite3.connect(database=r"Database/ims.db")
                cur = con.cursor()
                try:
                        cur.execute("select * from category") 
                        rows=cur.fetchall()
                        self.CategoryTable.delete(*self.CategoryTable.get_children())
                        for row in rows:
                                self.CategoryTable.insert('' , END , values =row)
                                
                except Exception as ex:
                        messagebox.showerror("Error",f"error due to : {str(ex)}",parent=self.root)  
                        
    def get_data(self ,ev):
            f = self.CategoryTable.focus()
            content = (self.CategoryTable.item(f))
            row = content['values']

            self.var_name.set(row[1])
            self.var_cid.set(row[0])
            
            
    def delete (self):
            
            con = sqlite3.connect(database=r"Database/ims.db")
            cur = con.cursor()
            try:
                if self.var_cid.get()=="":
                        messagebox.showerror("Error","Invice no. must be reqiure",parent=self.root)
                else:
                    cur.execute("Select * from category where name=?",(self.var_name.get(),))   
                    row=cur.fetchone()
                    if row==None:
                            messagebox.showerror("Erorr" ,"Invalid category Id , try different",parent=self.root)
                    else:
                            op = messagebox.askyesno("Confirm",'Do you realy want to delete' , parent=self.root)
                            if op==True:
                               cur.execute('Delete from category where name=?', (self.var_name.get(),))
                               con.commit()
                               messagebox.showinfo('delete' , "category deleted successfully", parent=self.root)
                               self.clear()
                               self.show()
                               
                    
            except Exception as ex: 
                    messagebox.showerror("Error",f"error due to : {str(ex)}",parent=self.root)       
                
    def clear(self):
                  
                   self.var_cid.set("")
                   self.var_name.set("")
                   
                #    self.txt_desc.insert(END ,row[9]),
  
                   self.show()            
        
                                       
################################################ends#####################################        
if __name__ == "__main__":
       
    root = Tk();
    obj = categoryClass(root);
    root.mainloop();                    