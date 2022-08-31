from tkinter import *
from PIL import Image,ImageTk
from tkinter import ttk,messagebox
import sqlite3

class productClass:
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
        
        self.var_pid = StringVar()
        self.var_cat = StringVar()
        self.var_sup = StringVar()
        self.cat_list=[]
        self.sup_list=[]
        self.fetch_cat_sup()        
        
        self.var_name = StringVar()       
        self.var_price = StringVar()
        self.var_qty = StringVar()
        self.var_status = StringVar() 
        
        
        product_frame = Frame(self.root ,bd=3, relief=RIDGE)
        product_frame.place(x=10, y=10 ,height=480 , width=450)
        
        
        
        title =Label(product_frame , text="Product Details" ,font=("Segoe UI" , 18,"bold") , bg="#0f4d7d" , fg="white").pack(side=TOP,fill=X)

        lbl_category =Label(product_frame , text="Category" ,font=("Segoe UI" , 18)).place(x=30,y=60)
        lbl_supplier =Label(product_frame , text="supplier" ,font=("Segoe UI" , 18)).place(x=30,y=110)
        lbl_product_name =Label(product_frame , text="product" ,font=("Segoe UI" , 18)).place(x=30,y=170)
        lbl_price =Label(product_frame , text="price" ,font=("Segoe UI" , 18)).place(x=30,y=230)
        lbl_qyt =Label(product_frame , text="quantity" ,font=("Segoe UI" , 18)).place(x=30,y=290)                        
        lbl_status =Label(product_frame , text="status" ,font=("Segoe UI" , 18)).place(x=30,y=350)

        

       
        txt_category=ttk.Combobox(product_frame ,textvariable=self.var_cat,values=(self.cat_list) , state="readonly", justify=CENTER,font=("Segoe UI" ,18))
        txt_category.place(x=150 ,y=60,width=200)
        # txt_category.current(0) 
        
        txt_supplier=ttk.Combobox(product_frame ,textvariable=self.var_sup,value=(self.sup_list), state="readonly", justify=CENTER,font=("Segoe UI" ,18))
        txt_supplier.place(x=150 ,y=110,width=200)
        # txt_supplier.current(0)         
        
        txt_name = Entry(product_frame  ,bg="lightyellow", bd=3, relief=RIDGE ,textvariable=self.var_name,font=("Segoe UI" , 15)).place(x=150,y=166 ,width=200) 
        txt_price = Entry(product_frame  ,bg="lightyellow", bd=3, relief=RIDGE ,textvariable=self.var_price,font=("Segoe UI" , 15)).place(x=150,y=226 ,width=200)        
        txt_qyt = Entry(product_frame  ,bg="lightyellow", bd=3, relief=RIDGE ,textvariable=self.var_qty,font=("Segoe UI" , 15)).place(x=150,y=282 ,width=200)        
  
        cmb_status=ttk.Combobox(product_frame ,textvariable=self.var_status,values=("Select","Active" ,"Inactive") , state="readonly", justify=CENTER,font=("Segoe UI" ,18))
        cmb_status.place(x=150 ,y=339,width=200)
        # cmb_status.current(0) 
        
        
        btn_add = Button(product_frame ,command=self.add,text="Save" ,font=("Segoe UI" , 15,"normal"),bg="#2196f3",fg="white" ,cursor="hand2").place(x=10,y=400, height=40,width=100)
        btn_update = Button(product_frame ,command=self.update,text="update" ,font=("Segoe UI" , 15,"normal"),bg="#4caf50",fg="white" ,cursor="hand2").place(x=120,y=400, height=40,width=100)
        btn_del = Button(product_frame ,text="Delete",command=self.delete ,font=("Segoe UI" , 15,"normal"),bg="#f44336",fg="white" ,cursor="hand2").place(x=230,y=400, height=40,width=100)
        btn_clear = Button(product_frame ,text="Clear" ,command=self.clear,font=("Segoe UI" , 15,"normal"),bg="#607d8b",fg="white" ,cursor="hand2").place(x=340,y=400, height=40,width=100)




        searchFrame = LabelFrame (self.root,bd=2,relief=RIDGE,font=("goudy old style" ,12 ,"bold"),text="search employee" , bg="white")
        searchFrame.place(x=480, y=10 , width=600,height=80)

#==============option++++++++++++++++++++++++#

        cmb_search=ttk.Combobox(searchFrame,textvariable=self.var_searchby,value=("Select","category", "supplier" ,"name") , state="readonly", justify=CENTER,font=("Segoe UI" ,15))
        cmb_search.place(x=10 ,y=10 , width=180)
        # cmb_search.current(0)


        txt_search = Entry(searchFrame,textvariable=self.var_searchtxt, font=("Segoe UI" ,15,"bold"),bg="lightyellow")
        txt_search.place(x=200,y=10)
        
        btn_search = Button(searchFrame ,text=("Search"),command=self.search ,font=("goudy old style" ,15,"normal"),bg="#4caf50",fg="white" ,cursor="hand2").place(x=410,y=9, width=150, height=30)


# =====================================product details
        P_frame = Frame(self.root , bd=3, relief=RIDGE)
        P_frame.place(x=480 , y=100, width=600,height=390)
        
        scrolly = Scrollbar(P_frame,orient=VERTICAL)
        scrollx = Scrollbar(P_frame,orient=HORIZONTAL)
        
        self.productTable = ttk.Treeview(P_frame,columns=("pid" , "category" , "supplier" , "name" , "price" , "qty" , "status" ),yscrollcommand=scrolly.set , xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM , fill=X)
        scrolly.pack(side=RIGHT , fill=Y)
        scrollx.config(command=self.productTable.xview)
        scrolly.config(command=self.productTable.yview)
        
        
        self.productTable.heading("pid" , text="PID")
        self.productTable.heading("supplier" , text="supplier")  
        self.productTable.heading("category" , text="category")

        self.productTable.heading("name" , text="name")
        self.productTable.heading("price" , text="price")
        self.productTable.heading("qty" , text="QYT")
        self.productTable.heading("status" , text="Status")

        
        
       
        self.productTable.column("pid" ,width="90")
        self.productTable.column("supplier" ,width="100")
        self.productTable.column("category" ,width="100")
        
        self.productTable.column("name" ,width="100")
        self.productTable.column("price",width="100")
        self.productTable.column("qty" ,width="100")
        self.productTable.column("status",width="100")


        
        self.productTable.pack(fill=BOTH, expand=1)
        self.productTable.bind("<ButtonRelease-1>",self.get_data)
        self.productTable["show"]="headings"
        
        
        
        self.show() 


    def fetch_cat_sup(self):
        con = sqlite3.connect(database=r"Database/ims.db")
        cur = con.cursor()
        try:
                    cur.execute("Select name from category")   
                    cat=cur.fetchall()
                    self.cat_list.append("select")
                    # if len(cat)>0:
                    #     del self.cat_list.append[:]
                    # #     self.cat_list.append("select")
                    for i in cat:
                            self.cat_list.append(i[0])
                                                   
                    cur.execute("Select name from supplier")   
                    sup=cur.fetchall()
                    self.sup_list.append("select")
                    # if len(cat)>0:
                    #     del self.cat_list.append[:]
                    # #     self.cat_list.append("select")
                    for i in sup:
                            self.sup_list.append(i[0])
                                     
                    
        except Exception as ex:
                messagebox.showerror("Error",f"error due to : {str(ex)}",parent=self.root)  
                      
        
    def add(self):
        con = sqlite3.connect(database=r"Database/ims.db")
        cur = con.cursor()
        try:
                if self.var_cat.get()=="select" or self.var_sup.get()=="select" or self.var_name.get()=="":
                    messagebox.showerror("Error","All field are reqiure",parent=self.root)
                else:
                    cur.execute("Select * from product where name=?",(self.var_name.get(),))   
                    row=cur.fetchone()
                    if row!=None:
                            messagebox.showerror("Erorr" ,"This product is ID already assigned , try different",parent=self.root)
                    else:
                            cur.execute("Insert into product (category , supplier , name , price , qty , status) values (?,?,?,?,?,?)",(
                            self.var_cat.get(),
                            self.var_sup.get(),
                            self.var_name.get(),       
                            self.var_price.get(),
                            self.var_qty.get(),
                            self.var_status.get()
                            ))
                            con.commit() 
                            self.show()
                            self.clear()
                            messagebox.showinfo("Success" , "employee details has been added successfully")
        except Exception as ex:
                messagebox.showerror("Error",f"error due to : {str(ex)}",parent=self.root)
                
                
        
       
    def show(self):
                
                con = sqlite3.connect(database=r"Database/ims.db")
                cur = con.cursor()
                try:
                        cur.execute("select * from product")
                        rows=cur.fetchall()
                        self.productTable.delete(*self.productTable.get_children())
                        for row in rows:
                                self.productTable.insert('' , END , values =row)
                                col = len(rows)
                                                            
                except Exception as ex:
                        messagebox.showerror("Error",f"error due to : {str(ex)}",parent=self.root)
    def get_data(self ,ev):
            f = self.productTable.focus()
            content = (self.productTable.item(f))
            row = content['values']
            self.var_pid.set(row[0])
            self.var_cat.set(row[1])
            self.var_sup.set(row[2])
            self.var_name.set(row[3])       
            self.var_price.set(row[4])
            self.var_qty.set(row[5])
            self.var_status.set(row[6]) 
                
    def update(self):
        con = sqlite3.connect(database=r"Database/ims.db")
        cur = con.cursor()
        try:
                if self.var_pid.get()=="":
                    messagebox.showerror("Error","Employee ID must be reqiure",parent=self.root)
                else:
                    cur.execute("Select * from product where pid=?",(self.var_pid.get(),))   
                    row=cur.fetchone()
                    if row==None:
                            messagebox.showerror("Erorr" ,"Invalid product ID , try different",parent=self.root)
                    else:
                            cur.execute("Update product set category=? , supplier=? , name=? , price=? , qty=? , status=? where pid=?",(
                               
                            self.var_cat.get(),
                            self.var_sup.get(),
                            self.var_name.get(),       
                            self.var_price.get(),
                            self.var_qty.get(),
                            self.var_status.get(),
                            self.var_pid.get()
                            ))
                            con.commit()
                            self.show()
                            self.clear()
                            messagebox.showinfo("Success" , "product details has been updated successfully")
        except Exception as ex:
                messagebox.showerror("Error",f"error due to : {str(ex)}",parent=self.root)        
    def delete (self):
            
            con = sqlite3.connect(database=r"Database/ims.db")
            cur = con.cursor()
            try:
                if self.var_pid.get()=="":
                        messagebox.showerror("Error","Employee ID must be reqiure",parent=self.root)
                else:
                    cur.execute("Select * from product where pid=?",(self.var_pid.get(),))   
                    row=cur.fetchone()
                    if row==None:
                            messagebox.showerror("Erorr" ,"Invalid product ID , try different",parent=self.root)
                    else:
                            op = messagebox.askyesno("Confirm",'Do you realy want to delete' , parent=self.root)
                            if op==True:
                               cur.execute('Delete from product where pid=?', (self.var_pid.get(),))
                               con.commit()
                               messagebox.showinfo('delete' , "product deleted successfully", parent=self.root)
                               self.clear()
                               self.show()
                    
            except Exception as ex: 
                    messagebox.showerror("Error",f"error due to : {str(ex)}",parent=self.root)       
    
    def clear(self):
        self.var_pid.set(""),
        self.var_cat.set(""),
        self.var_sup.set(""),
        # self.cat_list.set(""),
        # self.sup_list.set(""),     
        self.var_name.set(""),      
        self.var_price.set(""),
        self.var_qty.set(""),
        self.var_status.set("") 
                  

          
    def search(self):    
              con = sqlite3.connect(database=r"Database/ims.db")
              cur = con.cursor()
              try:
                        if self.var_searchby.get() =="Select":
                                messagebox.showerror("error" , "select search by option" , parent=self.root)
                        elif self.var_searchtxt.get() =="":
                                messagebox.showerror("error" , "search input must be reqiure" , parent=self.root)
                        else:               
                                cur.execute("select * from product where "+self.var_searchby.get()+" LIKE '%"+self.var_searchtxt.get()+"%'")
                                rows=cur.fetchall()
                                if len(rows)!= 0:                                        
                                     self.productTable.delete(*self.productTable.get_children())
                                     for row in rows:
                                       self.productTable.insert('' , END , values =row)
                                else:
                                        messagebox.showerror("error" , "No record found")
              except Exception as ex:
                        messagebox.showerror("Error",f"error due to : {str(ex)}",parent=self.root)   
                              
if __name__ == "__main__":
       
    root = Tk();
    obj = productClass(root);
    root.mainloop();                  
        