from tkinter import *
from PIL import Image,ImageTk
import datetime
from datetime import datetime, date
import time
import sqlite3
from time import strftime
from employee import employeeClass
from supplier import supplierClass
from category import categoryClass
from product import productClass
from sales import salesClass
def create_db():
    con= sqlite3.connect(database=r"./Database/ims.db")
    cur=con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS employee(eid INTEGER PRIMARY KEY AUTOINCREMENT , name TEXT, email TEXT, gender TEXT, contact TEXT, dob TEXT, doj TEXT, pass TEXT,utype TEXT, address TEXT, salary TEXT)")
    con.commit()
    
create_db()   
def create_db():
        con= sqlite3.connect(database=r"./Database/ims.db")
        cur=con.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS supplier(invoice INTEGER PRIMARY KEY AUTOINCREMENT , name TEXT, contact TEXT, desc Text)")
        con.commit()
      
create_db()



class IMS:
       

    def __init__(self, root):
        
        self.root = root
        self.root.geometry("1350x700+0+0")
        self.root.title("Inventory Manegment System | Devloped by Manish")
        self.root.config(bg="white")
    #   ======================variable===============================
    
    
        self.var_cat_num = StringVar()
        self.var_supp_num = StringVar()
        self.var_emp_num = StringVar()
        self.total_sales = StringVar()
        self.var_ttl_pro_num = StringVar()
        self.show()
        
        # self.update_time()
#title#
        self.icon_title= PhotoImage(file="images/logo1.png")
        title = Label(self.root, text="Inventory Manegement System",image=self.icon_title,compound=LEFT, font=("times new roman" , 40 , "bold"),bg="#010c48" ,fg="white",anchor="w" ,padx=20 ).place(x=0 ,y=0 ,relwidth=1,height=70)
    
    #=========================log out ===================================#
        btn_logout =Button(self.root,text="Logout" ,font=('times new roman' , 15 ,'bold') ,bg="yellow", cursor="hand2" ).place(x=1150 ,y=10, width=150,height=50)
    #========clock==================#
        self.lbl_clock = Label(self.root, text="Wellcome to Inventory Managment System\t\t Date:"+""+"\t\t Time:", font=("times new roman" , 15 , "bold"),bg="#4d636d" ,fg="white")
        self.lbl_clock.place(x=0 ,y=70 ,relwidth=1,height=30) 
        
      
    #=================left menu=======================#
        self.menuLogo = Image.open("images/menu_im.png")
        self.menuLogo = self.menuLogo.resize((200,270) ,Image.ANTIALIAS)
        self.menuLogo = ImageTk.PhotoImage(self.menuLogo)
        
        leftMenu = Frame(self.root, bd=2, relief=RIDGE, bg="white")
        leftMenu.place(x=0,y=100,width=250, height=700  )
    
        
        lbl_menuLogo=Label(leftMenu,image=self.menuLogo)
        lbl_menuLogo.pack(side=TOP, fill=X)
        
        self.icon_side= PhotoImage(file="images/side.png")
        
        lbl_menu = Label(leftMenu, text="Menu" ,font=("times new roman", 20 ),bg="#009688").pack(side=TOP , fill=X )
        

        btn_employee = Button(leftMenu, text="Employee" ,command=self.employee,font=("times new roman", 25,"bold" ),image=self.icon_side,compound=LEFT,padx=5,anchor="w",bg="#fff",cursor="hand2" ,bd=3).pack(side=TOP , fill=X)
        btn_supplier = Button(leftMenu, text="Supplier" ,command=self.supplier,font=("times new roman", 25,"bold" ),image=self.icon_side,compound=LEFT,padx=5,anchor="w",bg="#fff",cursor="hand2" ,bd=3).pack(side=TOP , fill=X)  
        btn_category = Button(leftMenu, text="Category" ,command=self.category,font=("times new roman", 25,"bold" ),image=self.icon_side,compound=LEFT,padx=5,anchor="w",bg="#fff",cursor="hand2" ,bd=3).pack(side=TOP , fill=X)  
        btn_product = Button(leftMenu, text="Product" ,command=self.product,font=("times new roman", 25,"bold" ),image=self.icon_side,compound=LEFT,padx=5,anchor="w",bg="#fff",cursor="hand2" ,bd=3).pack(side=TOP , fill=X)
        btn_sales = Button(leftMenu, text="Sales" ,command=self.sales,font=("times new roman", 25,"bold" ),image=self.icon_side,compound=LEFT,padx=5,anchor="w",bg="#fff",cursor="hand2" ,bd=3).pack(side=TOP , fill=X)           
        btn_exit = Button(leftMenu, text="Exit", command=self.exit ,font=("times new roman", 25,"bold" ),image=self.icon_side,compound=LEFT,padx=5,anchor="w",bg="#fff",cursor="hand2" ,bd=3).pack(side=TOP , fill=X)             

#====================================================content====================================================#
        self.lbl_employee = Label(self.root ,bd=5, relief=GROOVE, text="Total Employee\n ["+str(self.var_emp_num)+"]",bg="#33bbf9", fg="white", font=("goudy old style", 20 ,"bold"))
        self.lbl_employee.place(x=350 ,y=120 ,height=200 ,width=300)
   
        self.lbl_supplier = Label(self.root ,bd=5, relief=GROOVE, text="Total supplier\n ["+str(self.var_supp_num)+"]",bg="#ff5722", fg="white", font=("goudy old style", 20 ,"bold"))
        self.lbl_supplier.place(x=700 ,y=120 ,height=200 ,width=300)
        
        self.lbl_category = Label(self.root ,bd=5, relief=GROOVE, text="Total category\n [" +str(self.var_cat_num) +"]",bg="#009688", fg="white", font=("goudy old style", 20 ,"bold"))
        self.lbl_category.place(x=1050 ,y=120 ,height=200 ,width=300)
        
        self.lbl_product = Label(self.root ,bd=5, relief=GROOVE, text="Total product\n ["+str(self.var_ttl_pro_num)+" ]",bg="#607d8b", fg="white", font=("goudy old style", 20 ,"bold"))
        self.lbl_product.place(x=350 ,y=350 ,height=200 ,width=300)

        self.lbl_sales = Label(self.root ,bd=5, relief=GROOVE, text="Total sales\n [ "+str(self.total_sales)+" ]",bg="#ffc107", fg="white", font=("goudy old style", 20 ,"bold"))
        self.lbl_sales.place(x=700 ,y=350 ,height=200 ,width=300)

        # self.update_label()
     

#====================================footer================================#

        lbl_footer = Label( text="IMS-Inventory Manegement System | Devloped by Manish\n for any technical issue contact: 9833xxxx39 ", font=("times new roman" , 12 , "bold"),bg="#4d636d" ,fg="white",)
        lbl_footer.pack(fill=X ,side=BOTTOM)
        
        self.clock()
 
#=======================================exit=================================#
    def exit(self):
        root.destroy()    


        
    


  
       
#=====================================#


    def employee(self):
        self.new_win=Toplevel(self.root)
        self.new_obj =employeeClass(self.new_win)
    
        

    def supplier(self):
        self.new_win=Toplevel(self.root)
        self.new_obj =supplierClass(self.new_win)
        self.show()
        
    def category(self):
        self.new_win=Toplevel(self.root)
        self.new_obj =categoryClass(self.new_win)   
        self.show()
        
    def product(self):
        self.new_win=Toplevel(self.root)
        self.new_obj =productClass(self.new_win)  
        self.show()
        
    def sales(self):
        self.new_win=Toplevel(self.root)
        self.new_obj =salesClass(self.new_win) 
        self.show() 


        
            
    def show(self):
                
            con = sqlite3.connect(database=r"Database/ims.db")
            cur = con.cursor()
            cur.execute("select * from category")
            rows=cur.fetchall()
              
            self.var_cat_num= len(rows)
            print(self.var_cat_num)
            
            
            con = sqlite3.connect(database=r"Database/ims.db")
            cur = con.cursor()
            cur.execute("select * from employee")
            rows=cur.fetchall()
              
            self.var_emp_num= len(rows)
            print(self.var_emp_num)
            
            
            con = sqlite3.connect(database=r"Database/ims.db")
            cur = con.cursor()
            cur.execute("select * from employee")
            rows=cur.fetchall()
              
            self.var_supp_num= len(rows)
            print(self.var_supp_num)
            
            
            con = sqlite3.connect(database=r"Database/ims.db")
            cur = con.cursor()
            cur.execute("select * from employee")
            rows=cur.fetchall()
              
            self.total_sales= len(rows)
            print(self.total_sales)
            
            
            con = sqlite3.connect(database=r"Database/ims.db")
            cur = con.cursor()
            cur.execute("select * from employee")
            rows=cur.fetchall()
              
            self.var_ttl_pro_num= len(rows)
            print(self.var_ttl_pro_num)
                                                

    def clock(self):
        self.time= time.strftime(" %I:%M:%S")    
        self.year = time.strftime(" %d:%m:%Y")    
        self.lbl_clock.config(text="Wellcome to Inventory Managment System\t\t Date "+self.year+"\t\t Time"+self.time+"", font=("times new roman" , 15 , "bold"),bg="#4d636d" ,fg="white")
        self.lbl_clock.after(200,self.clock)
            
            
#Update the Time
    # def updateTime(self):
    #        self.lbl_clock.config(text= "New Text")

    

if __name__ == "__main__":
    root = Tk();
    obj = IMS(root);
    root.mainloop();    
    
    