from ast import Lambda
from cgitb import text
from distutils.cmd import Command
from faulthandler import disable
from tkinter import *
from tkinter.font import BOLD
from PIL import Image,ImageTk
import datetime
from datetime import datetime, date
import time
import sqlite3
from time import strftime
from tkinter import ttk,messagebox
import sqlite3
import os
import PIL
from resizeimage import resizeimage
import qrcode 
import tempfile




class BillClass:
       

    def __init__(self, root):
        
        self.root = root
        self.root.geometry("1350x700+0+0")
        self.root.title("Inventory Manegment System | Devloped by Manish")
        self.root.config(bg="white")
    #   ======================variable===============================
        self.cart_list = [] 
        self.var_searchby = StringVar()
        self.var_searchtxt = StringVar()
        self.var_name = StringVar()
        self.var_contact = StringVar()

#title#
        self.icon_title= PhotoImage(file="images/logo1.png")
        title = Label(self.root, text="Inventory Manegement System",image=self.icon_title,compound=LEFT, font=("times new roman" , 40 , "bold"),bg="#010c48" ,fg="white",anchor="w" ,padx=20 ).place(x=0 ,y=0 ,relwidth=1,height=70)
    
    #=========================log out ===================================#
        btn_logout =Button(self.root,text="Logout" ,font=('times new roman' , 15 ,'bold') ,bg="yellow", cursor="hand2" ).place(x=1150 ,y=10, width=150,height=50)
    #========clock==================#
        self.lbl_clock = Label(self.root, text="Wellcome to Inventory Managment System\t\t Date:"+""+"\t\t Time:" , font=("times new roman" , 15 , "bold"),bg="#4d636d" ,fg="white")
        self.lbl_clock.place(x=0 ,y=70 ,relwidth=1,height=30)       
        
        lbl_footer = Label( text="BillClass-Inventory Manegement System | Devloped by Manish\n for any technical issue contact: 9833xxxx39 ", font=("times new roman" , 12 , "bold"),bg="#4d636d" ,fg="white",)
        lbl_footer.pack(fill=X ,side=BOTTOM)
        self.clock()
        
        
        productFrame = Frame(self.root, bd=4 , relief=RIDGE , bg="white")
        productFrame.place(x=10, y=106, width=410, height=550)
        
        p_title = Label(productFrame, text="All Product" , font=("times new roman" , 20 , "bold"),bg="#262626" ,fg="white").pack(fill=X ,side=TOP)
        
        productFrame2 = Frame(productFrame, bd=2 , relief=RIDGE , bg="white")
        productFrame2.place(x=2, y=42, width=398, height=90) 
        
        
        lbl_search = Label(productFrame2, text="Search product " ,bg="white",fg="green", font=("times new roman" , 15 ,"bold")).place(x=2, y=5)
        cmb_search=ttk.Combobox(productFrame2,textvariable=self.var_searchby,value=("Select","category", "supplier" ,"name") , state="readonly", justify=CENTER,font=("Segoe UI" ,15))
        cmb_search.place(x=140 ,y=5 , width=140)
        cmb_search.current(0)
        
        lbl_search = Label(productFrame2 ,text="Product Name",bg="white", font=("times new roman",15 ,"bold")).place(x=5 , y=45)
        txt_search = Entry(productFrame2 ,bg="lightyellow",textvariable=self.var_searchtxt, font=("times new roman" , 15 )).place(x=129 , y=47, height=22, width=150)
        btn_search = Button(productFrame2,text="Search" , bg="#2196f3" ,command=self.search,fg="white",cursor="hand2", font=("times new roman" , 15 , "bold")).place(x=285 , y=45,width=100,height=25)
        
        btn_Show_all = Button(productFrame2,text="Show All" ,command=self.show, bg="#083531" ,fg="white",cursor="hand2", font=("times new roman" , 15 , "bold")).place(x=285 , y=10,width=100,height=25)
   
# ================================= Treeview =====================================
        productFrame3 = Frame(productFrame , bd=3, relief=RIDGE)
        productFrame3.place(x=2 , y=140, width=398,height=385)
        
        scrolly = Scrollbar(productFrame3,orient=VERTICAL)
        scrollx = Scrollbar(productFrame3,orient=HORIZONTAL)
        
        self.productTable = ttk.Treeview(productFrame3,columns=("pid" , "name" , "price" , "qty" , "status" ),yscrollcommand=scrolly.set , xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM , fill=X)
        scrolly.pack(side=RIGHT , fill=Y)
        scrollx.config(command=self.productTable.xview)
        scrolly.config(command=self.productTable.yview)
        
        
        self.productTable.heading("pid" , text="PID")
        self.productTable.heading("name" , text="name")
        self.productTable.heading("price" , text="price")
        self.productTable.heading("qty" , text="QYT")
        self.productTable.heading("status" , text="Status")

        
        
       
        self.productTable.column("pid" ,width="40")        
        self.productTable.column("name" ,width="100")
        self.productTable.column("price",width="100")
        self.productTable.column("qty" ,width="50")
        self.productTable.column("status",width="100")


        
        self.productTable.pack(fill=BOTH, expand=1)
        self.productTable.bind("<ButtonRelease-1>",self.get_data)
        self.productTable["show"]="headings"
        self.show()
        
        
        
        customerFrame = Frame(self.root, bd=4 , relief=RIDGE , bg="white")
        customerFrame.place(x=420, y=110, width=530, height=70)
        
        p_title = Label(customerFrame, text="Customer Details" , font=("times new roman" , 15 , "bold"),bg="#262626" ,fg="lightgrey").pack(fill=X ,side=TOP)
        lbl_name = Label(customerFrame ,text="Name",bg="white", font=("times new roman",15 )).place(x=5 , y=35)
        txt_name = Entry(customerFrame ,bg="lightyellow",textvariable=self.var_name, font=("times new roman" , 12 )).place(x=80 , y=35 )
        # btn_search = Button(customerFrame,text="Search" , bg="#2196f3" ,command=self.search,fg="white",cursor="hand2", font=("times new roman" , 15 , "bold")).place(x=285 , y=45,width=100,height=25)
        
        
        
        lbl_Contact_no = Label(customerFrame ,text="Contact no.",bg="white", font=("times new roman",15 )).place(x=270 , y=35)
        txt_Contact_no = Entry(customerFrame ,bg="lightyellow",textvariable=self.var_contact, font=("times new roman" , 12 )).place(x=380 , y=35 , width=130)
    
     
        Cal_cart_Frame = Frame(self.root, bd=2, relief=RIDGE , bg="white")
        Cal_cart_Frame.place(x=420, y=190, width=530, height=360)
        
        # ==================== calculator frame ==========================#
        
        self.txt_cal_num = StringVar()     
        Cal_Frame = Frame(Cal_cart_Frame, bd=2, relief=RIDGE , bg="white")
        Cal_Frame.place(x=5, y=10, width=268, height=340)  
        
        self.txt_cal_input = Entry(Cal_Frame , textvariable=self.txt_cal_num ,state = "readonly", font=("times new roman" ,15, "bold") ,width=25 ,bd=10, relief=GROOVE, justify=RIGHT)
        self.txt_cal_input.grid(row=0,columnspan=4)
        
        btn_7 = Button(Cal_Frame  , font=("arial" , 15 , "bold"), text=7 , width=4, bd=5 , command=lambda:self.get_input(7),pady=10 ,cursor="hand2").grid(row=1 , column=0)
        btn_8 = Button(Cal_Frame  , font=("arial" , 15 , "bold"), text=8 , width=4, bd=5 , command=lambda:self.get_input(8) ,pady=10 ,cursor="hand2").grid(row=1 , column=1)
        btn_9 = Button(Cal_Frame  , font=("arial" , 15 , "bold"), text=9 , width=4, bd=5 , command=lambda:self.get_input(9) ,pady=10 ,cursor="hand2").grid(row=1 , column=2)
        btn_sum = Button(Cal_Frame  , font=("arial" , 15 , "bold"), text='+' , width=4, bd=5 , command=lambda:self.get_input('+') ,pady=10 ,cursor="hand2").grid(row=1 , column=3)
        
        btn_4 = Button(Cal_Frame  , font=("arial" , 15 , "bold"), text=4 , width=4, bd=5 , command=lambda:self.get_input(4) ,pady=10 ,cursor="hand2").grid(row=2 , column=0)
        btn_5 = Button(Cal_Frame  , font=("arial" , 15 , "bold"), text=5 , width=4, bd=5 , command=lambda:self.get_input(5) ,pady=10 ,cursor="hand2").grid(row=2 , column=1)
        btn_6 = Button(Cal_Frame  , font=("arial" , 15 , "bold"), text=6 , width=4, bd=5 , command=lambda:self.get_input(6) ,pady=10 ,cursor="hand2").grid(row=2 , column=2)
        btn_sub = Button(Cal_Frame  , font=("arial" , 15 , "bold"), text='-' , width=4, bd=5 , command=lambda:self.get_input('-') ,pady=10 ,cursor="hand2").grid(row=2 , column=3)
        
        btn_1 = Button(Cal_Frame  , font=("arial" , 15 , "bold"), text=1 , width=4, bd=5 , command=lambda:self.get_input(1) ,pady=15 ,cursor="hand2").grid(row=3 , column=0)
        btn_2 = Button(Cal_Frame  , font=("arial" , 15 , "bold"), text=2 , width=4, bd=5 , command=lambda:self.get_input(2) ,pady=15 ,cursor="hand2").grid(row=3 , column=1)
        btn_3 = Button(Cal_Frame  , font=("arial" , 15 , "bold"), text=3 , width=4, bd=5 , command=lambda:self.get_input(3) ,pady=15 ,cursor="hand2").grid(row=3 , column=2)
        btn_mul = Button(Cal_Frame  , font=("arial" , 15 , "bold"), text='*' , width=4, bd=5 , command=lambda:self.get_input('*') ,pady=15 ,cursor="hand2").grid(row=3 , column=3)
        
        btn_0 = Button(Cal_Frame  , font=("arial" , 15 , "bold"), text=0 , width=4, bd=5 , command=lambda:self.get_input(0) ,pady=15 ,cursor="hand2").grid(row=4 , column=0)
        btn_c = Button(Cal_Frame  , font=("arial" , 15 , "bold"), text='C' , width=4, bd=5 , command=self.clear_cal ,pady=15 ,cursor="hand2").grid(row=4 , column=1)
        btn_eq = Button(Cal_Frame  , font=("arial" , 15 , "bold"), text='=' , width=4, bd=5 , command=self.perform_cal ,pady=15 ,cursor="hand2").grid(row=4 , column=2)
        btn_div = Button(Cal_Frame  , font=("arial" , 15 , "bold"), text='/' , width=4, bd=5 , command=lambda:self.get_input('/') ,pady=15 ,cursor="hand2").grid(row=4 , column=3)
        
        
        # =============================All fungtion============================#         
        cart_Frame = Frame(Cal_cart_Frame , bd=3, relief=RIDGE)
        cart_Frame.place(x=280 , y=8, width=245,height=342)
        
        self.cart_titles = Label(cart_Frame , text=("cart \t Total items[0]"), font=("times new roman" , 15) ,bg="lightgrey")
        self.cart_titles.pack(side=TOP , fill=X)
     
        
        scrolly = Scrollbar(cart_Frame,orient=VERTICAL)
        scrollx = Scrollbar(cart_Frame,orient=HORIZONTAL)
        
        self.customer_Table = ttk.Treeview(cart_Frame,columns=("pid" ,"name" , "price" , "qty" ,"stock" ),yscrollcommand=scrolly.set , xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM , fill=X)
        scrolly.pack(side=RIGHT , fill=Y)
        scrollx.config(command=self.customer_Table.xview)
        scrolly.config(command=self.customer_Table.yview)
        
        
        self.customer_Table.heading("pid" , text="PID")
        self.customer_Table.heading("name" , text="name")
        self.customer_Table.heading("price" , text="price")
        self.customer_Table.heading("qty" , text="QYT")
        self.customer_Table.heading("stock" , text="Stock")
    
       
        self.customer_Table.column("pid" ,width="40")      
        self.customer_Table.column("name" ,width="90")
        self.customer_Table.column("price",width="60")
        self.customer_Table.column("qty" ,width="40")
        self.customer_Table.column("stock" ,width="40")
  


        
        self.customer_Table.pack(fill=BOTH, expand=1)
        self.customer_Table.bind("<ButtonRelease-1>",self.get_data_cart)
        self.customer_Table["show"]="headings"
      
     
     
    #  ======================Add cart button ========================#
        cart_btn_Frame = Frame(self.root, bd=4 , relief=RIDGE , bg="white")
        cart_btn_Frame.place(x=420, y=550, width=530, height=109)
        # variable
        
        self.var_pid = StringVar()
        self.pname = StringVar()
        self.price = StringVar()
        self.qty = StringVar()
        self.instock = StringVar()
        
        
        lbl_p_name = Label(cart_btn_Frame , text="Product Name" , font=("times new roman" , 15 ) , bg="white" ).place(x=5 ,y=5)
        txt_p_name = Entry(cart_btn_Frame , font=("times new roman" , 15 ) ,textvariable=self.pname, bg="lightyellow" ,state = "readonly").place(x=5 ,y=35 , width=190, height=22)
     
        lbl_p_price = Label(cart_btn_Frame , text="Price per qty" , font=("times new roman" , 15 ) , bg="white" ).place(x=230 ,y=5)
        txt_p_price = Entry(cart_btn_Frame , font=("times new roman" , 15 ) ,textvariable=self.price, bg="lightyellow" ,state = "readonly").place(x=230 ,y=35 , width=150, height=22)
     
        lbl_p_qty = Label(cart_btn_Frame , text="Qty" , font=("times new roman" , 15 ) , bg="white" ).place(x=390 ,y=5)
        txt_p_qty = Entry(cart_btn_Frame , font=("times new roman" , 15 ) ,textvariable=self.qty, bg="lightyellow" ,).place(x=390 ,y=35 , width=120, height=22)
        
        self.lbl_instock = Label(cart_btn_Frame , text="" , font=("times new roman" , 15 ) , bg="white" )
        self.lbl_instock.place(x=5 ,y=70)
   
     
        btn_clear = Button(cart_btn_Frame, text="Clear" ,command=self.clear_cal, font=("times new roman" ,15), bg="lightgrey" ).place(x=180,y=70,height=30, width=130)
          
        btn_update_cart = Button(cart_btn_Frame, text="update cart",command=self.add_update_cart,  font=("times new roman" ,15), bg="orange" ).place(x=340,y=70,height=30, width=180)
             
# =========================================== billing area =================================

        self.billFrame= Frame (self.root , bd=2 , relief=RIDGE , bg="white")
        self.billFrame.place(x=953,y=110,height=410, width=500)
        b_title = Label(self.billFrame, text="Bill Area" , font=("times new roman" , 20 , "bold"),bg="orange" ,fg="white").pack(fill=X ,side=TOP)
        
        scrolly = Scrollbar(self.billFrame ,orient=VERTICAL)
        scrolly.pack(side=RIGHT,fill=Y)
        self.txt_bill_area = Text(self.billFrame, yscrollcommand=scrolly )
        self.txt_bill_area.pack(fill=BOTH ,expand=1)
        scrolly.config(command=self.txt_bill_area.yview)
     
# =========================================== bill menu frame ===============================#
 

        self.billmenu= Frame(self.root , bd=2 , relief=RIDGE , bg="white")
        self.billmenu.place(x=953,y=520,height=140, width=410)
        
        self.lbl_amount = Label(self.billmenu ,text="Total Amount\n₹ 0", font=("times new roman" , 15,"bold") , bg="#3551b4", fg="white")
        self.lbl_amount.place(x=2,y=5,width=120 , height=70)
        
        
        self.lbl_discound = Label(self.billmenu ,text="Discount\n 5%", font=("times new roman" , 15,"bold") , bg="#8bc34a", fg="white")
        self.lbl_discound.place(x=124,y=5,width=120 , height=70)
        
        
        self.lbl_net_pay = Label(self.billmenu ,text="Net pay\n₹ 0", font=("times new roman" , 15,"bold") , bg="#607d8b", fg="white")
        self.lbl_net_pay.place(x=246,y=5,width=160 , height=70)
        
        
        btn_lbl_print = Button(self.billmenu ,bd=3,command=self.print_bill,relief=GROOVE,text="Print", font=("times new roman" , 15,"bold") , bg="lightgreen", fg="white")
        btn_lbl_print.place(x=124,y=75,width=120 , height=50)
        
        btn_lbl_clear_all = Button(self.billmenu ,command=self.clear_bill,bd=3,relief=GROOVE,text="clear all", font=("times new roman" , 15,"bold") , bg="grey", fg="white")
        btn_lbl_clear_all.place(x=2,y=75,width=120 , height=50)

        
        
        btn_lbl_genrate = Button(self.billmenu ,bd=3,relief=GROOVE , command=self.generate_bill,text="Generate", font=("times new roman" , 15,"bold") , bg="#009688", fg="white")
        btn_lbl_genrate.place(x=246,y=75,width=160 , height=50)
        
    def add_update_cart(self):
    
            if self.qty.get()=="" :
                messagebox.showerror("error" , "please enter a quantity")
            elif self.var_pid.get() == "":
                    messagebox.showerror("error" , "plese select a product")       
            else:
                # price_cal =(int(self.qty.get())*float(self.price.get()))
                # price_cal = float(price_cal)
                
                price_cal =self.price.get()
              
                self.cart_data =[self.var_pid.get(),self.pname.get(),price_cal,self.qty.get() , self.instock.get()]
            

                present ="no"
                index_=0
                for row in self.cart_list:
                        if self.var_pid.get()==row[0]:
                                present='yes'
                                break
                        index_+=1
                if  present == 'yes':
                     op = messagebox.askyesno('confirm' , "item atem is present \n do you want to update" , parent=self.root)
                     if op==True:
                        if self.qty.get() == "0":
                            self.cart_list.pop(index_)
                        else:
                                # self.cart_list[index_][2] = price_cal
                                self.cart_list[index_][3]= self.qty.get()
                                
                else:
                        self.cart_list.append(self.cart_data)
                self.show_cart()
                self.bill_update()
     
    def show_cart(self):
        try:    
                
                
                
                self.customer_Table.delete(*self.customer_Table.get_children())
                for row in self.cart_list:
                        self.customer_Table.insert('' , END , values =row)
                        col = len(self.cart_list)
                               
                                                 
                                                            
        except Exception as ex:
                messagebox.showerror("Error",f"error due to : {str(ex)}",parent=self.root)
    
    
    
        
    def clear_cal(self):
            self.txt_cal_num.set('')
            
    def perform_cal(self):
            result=self.txt_cal_num.get()
            self.txt_cal_num.set(eval(result))

    def show(self):
                
                con = sqlite3.connect(database=r"Database/ims.db")
                cur = con.cursor()
                try:
                        cur.execute("select pid , name , price , qty , status from product")
                        rows=cur.fetchall()
                        self.productTable.delete(*self.productTable.get_children())
                        for row in rows:
                                self.productTable.insert('' ,END, values =row)
                                col = len(rows)
                               
                                                 
                                                            
                except Exception as ex:
                        messagebox.showerror("Error",f"error due to : {str(ex)}",parent=self.root)
    
    
    
    def get_data(self ,ev):
               f = self.productTable.focus()
               content = (self.productTable.item(f))
               row = content['values']       
               self.var_pid.set(row[0])
               self.pname.set(row[1])
               self.price.set(row[2])
        #        self.qty.set(row[0])
               self.lbl_instock.config(text=f"In Stock[{row[3]}]")
               self.instock.set(row[3])
               self.qty.set('1')
               
               
    def get_data_cart(self ,ev):
               f = self.customer_Table.focus()
               content = (self.customer_Table.item(f))
               row = content['values']       
               self.var_pid.set(row[0])
               self.pname.set(row[1])
               self.price.set(row[2])
        #        self.qty.set(row[0])
               self.lbl_instock.config(text=f"In Stock[{row[3]}]")
               self.instock.set(row[3])
               self.qty.set('1')
               
               
    def bill_update(self):
            self.bill_amt =0
            self.net_pay =0
            for row in self.cart_list:
                    self.bill_amt = self.bill_amt+(float(row[2])*int(row[3]))     
            
            self.net_pay = self.bill_amt - (self.bill_amt*5)/100
            self.discount =(self.bill_amt*5)/100
            self.lbl_amount.config(text=f"Bill Ammt\n ₹{str(self.bill_amt)}")
            self.lbl_net_pay.config(text=f"Net pay\n ₹{str(self.net_pay)}")
            self.cart_titles.config(text=f"cart \t Total items[{str(len(self.cart_list))}]")
            
                   
    def search(self):    
              con = sqlite3.connect(database=r"Database/ims.db")
              cur = con.cursor()
              try:
                        if self.var_searchby.get() =="Select":
                                messagebox.showerror("error" , "select search by option" , parent=self.root)
                        elif self.var_searchtxt.get() =="":
                                messagebox.showerror("error" , "search input must be reqiure" , parent=self.root)
                        else:               
                                cur.execute("select pid , name , price , qty , status from product where "+self.var_searchby.get()+" LIKE '%"+self.var_searchtxt.get()+"%'")
                                rows=cur.fetchall()
                                if len(rows)!= 0:                                        
                                     self.productTable.delete(*self.productTable.get_children())
                                     for row in rows:
                                       self.productTable.insert('' , END , values =row)
                                else:
                                        messagebox.showerror("error" , "No record found")
              except Exception as ex:
                        messagebox.showerror("Error",f"error due to : {str(ex)}",parent=self.root) 
                        
                        
                        
                        
    def generate_bill(self):
            if self.var_name.get() =="" or self.var_contact.get()=="":
                    messagebox.showerror("error" , "please enter mobile number")  
            elif len(self.var_contact.get()) < 10:
                    messagebox.showerror("error" , "invalid mobile number")
            else:        
                self.bill_top()
                self.bill_middle() 
                self.bill_bottom()
                self.bill_tax()
                fp =open(f"Bills/{str(self.invoice)}.txt" , "w", encoding='utf-8') 
                # fp.write(self.txt_bill_area.get('1.0',END))
                fp.write((self.txt_bill_area.get('1.0',END)))
                fp.close()
               
                    
    def bill_top(self):
        self.invoice=int(time.strftime("%H%M%S"))+int(time.strftime("%d%m%Y"))

        bill_top_temp=f'''

\t\t      
\t\t      𓂀 India Mart 𓂀 
\t\t    
 Phone No. 98725*** ,\t\t\t\tMumbai-125001
{str("="*59)}
Customer Name: {self.var_name.get()}
Ph no. :{self.var_contact.get()}
Bill No. {str(self.invoice)}\t\t\t\t\tDate: {str(time.strftime("%d/%m/%Y"))}
{str("="*59)}
Product\t\t   QTY\tM.R.P\tRate\t\tTotal
{str("="*59)}
        ''' 
        self.txt_bill_area.delete('1.0',END)
        self.txt_bill_area.insert('1.0',bill_top_temp)

    def bill_bottom(self):
        bill_bottom_temp=f'''
{str("="*59)}
Total Bill Amount\t\t\t\t\t\t₹{float(self.bill_amt)}
Total Discount\t\t\t\t\t\t₹{self.discount}
Net Pay\t\t\t\t\t\t₹{float(self.net_pay)}
{str("="*59)}
\t\t\t\t      Total ₹{self.net_pay}

Name\t\tTaxable\t\tTax\t\tNet Amount
{str("="*59)}
        ''' 
        # Total CGST\t\t\t\t\t₹{self.tax}
        # Total SGST\t\t\t\t\t₹{self.tax}

        self.txt_bill_area.insert(END,bill_bottom_temp)   
    
               
        print
    def bill_tax(self):
        for row in self.cart_list:    
           name=row[1]
           rate = float(row[2])-float(row[2])*5/100
           rate = "{:.2f}".format(rate)
           rate = str(rate)
           tax_perc ="18%"
           tax= float(row[2])*18/100
           tax = str(tax)
           taxable = float(row[2])-float(tax)
           taxable = str(taxable)
           cgst = float(tax)/2
           cgst = "{:.2f}".format(cgst)
           cgst = str(cgst)
           sgst = float(tax)/2
           sgst = "{:.2f}".format(sgst)
           sgst = str(sgst)
           price= float(taxable)+float(cgst)+float(sgst)
           price = "{:.2f}".format(price)
           price = str(price)
           print (price, tax_perc)
           thx_for_vist =f'''

{str("="*59)}           
\t      ***🙂Thanks for Visiting Us🙂***\t\t
        '''    
           self.txt_bill_area.insert(END,'\n'+name+"\t\t"+taxable+"\t"'\t₹'+tax+"\t\t"+price+"\t") 
        self.txt_bill_area.insert(END,thx_for_vist) 
    def bill_middle(self):
        for row in self.cart_list:
            name=row[1]
            qty=row[3]
            ogprice= row[2]
            rate = float(row[2])-float(row[2])*5/100
            rate = "{:.2f}".format(rate)
            rate = str(rate)
            price=float(rate)*float(row[3])
            price=str(price)
            self.tax = float(price)*9/100
            self.txt_bill_area.insert(END,"\n"+name+"\t\t   "+qty+"\t₹"+ogprice+'\t₹'+rate+"\t\t₹"+price)
            print(rate)
            
            
            

        # self.txt_bill_area.insert(END,bill_bottom_temp)
        # self.txt_bill_area.insert(END,bill_bottom_temp)
    
    def clear_bill(self):
            self.txt_bill_area.delete('1.0', END)
    
    
            
    def clock(self):
        self.time= time.strftime(" %I:%M:%S")    
        self.year = time.strftime(" %d:%m:%Y")    
        self.lbl_clock.config(text="Wellcome to Inventory Managment System\t\t Date "+self.year  +"\t\t Time"+self.time+"", font=("times new roman" , 15 , "bold"),bg="#4d636d" ,fg="white")
        self.lbl_clock.after(200,self.clock)
        
    def print_bill (self):
            new_file =tempfile.mktemp('.txt')
            open(new_file, "w",encoding="utf-8").write(self.txt_bill_area.get('1.0' , END))
            os.startfile(new_file,"print","man")
    def get_input(self,num):
            xnum= self.txt_cal_num.get()+str(num)
            self.txt_cal_num.set(xnum)

if __name__ == "__main__":
    root = Tk();
    obj = BillClass(root);
    root.mainloop();  