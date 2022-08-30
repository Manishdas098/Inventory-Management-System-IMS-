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
        
        
        
        
        
        product_frame = Frame(self.root ,bd=3, relief=RIDGE)
        product_frame.place(x=10, y=10 ,height=480 , width=450)
        
        
        
        title =Label(product_frame , text="Product Details" ,font=("Segoe UI" , 18,"bold") , bg="#0f4d7d" , fg="white").pack(side=TOP,fill=X)

        lbl_category =Label(product_frame , text="Category" ,font=("Segoe UI" , 18)).place(x=30,y=60)
        lbl_supplier =Label(product_frame , text="supplier" ,font=("Segoe UI" , 18)).place(x=30,y=110)
        lbl_product_name =Label(product_frame , text="product" ,font=("Segoe UI" , 18)).place(x=30,y=170)
        lbl_price =Label(product_frame , text="price" ,font=("Segoe UI" , 18)).place(x=30,y=230)
        lbl_qyt =Label(product_frame , text="quantity" ,font=("Segoe UI" , 18)).place(x=30,y=290)                        
        lbl_status =Label(product_frame , text="status" ,font=("Segoe UI" , 18)).place(x=30,y=350)

        

        txt_category = Label(product_frame , text="Category" ,font=("Segoe UI" , 18)).place(x=30,y=60)        
        txt_category=ttk.Combobox(self.root ,value=("Select","Male", "Female", "Other") , state="readonly", justify=CENTER,font=("Segoe UI" ,15))
        txt_category.place(x=150 ,y=80,width=180)
        txt_category.current(0) 
        
        
        
        
if __name__ == "__main__":
       
    root = Tk();
    obj = productClass(root);
    root.mainloop();                  
        