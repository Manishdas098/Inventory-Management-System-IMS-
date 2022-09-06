from struct import pack
from tkinter import *
from PIL import Image,ImageTk
from tkinter import ttk,messagebox
import sqlite3
import os
import PIL
from resizeimage import resizeimage
import qrcode 
class salesClass:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1100x500+280+160")
        self.root.resizable(False, False)
        self.root.title("Inventory Manegment System | Devloped by Manish")
        self.root.config(bg="white")
        self.root.focus_force()
# ============================== Start =============================#


# ============================== Variable =================================#


        self.var_invoice = StringVar()
        self.bill_list = []












        title =Label(self.root , text="View Customer Bills" ,font=("goudy old style" , 30) , bg="#184a45" , fg="white").pack(side=TOP,fill=X,pady=20,padx=10)      
        
        lbl_invoice = Label(self.root , font=("times new roman"  , 15),text=("Invoice no.") , bg="white").place(x=50,y=100)
    
        txt_invoice = Entry(self.root , font=("times new roman"  , 15),textvariable=self.var_invoice, bg="lightyellow").place(x=160,y=100,width=180, height=28)
        
        
        btn_search = Button(self.root ,text="Search" ,command=self.search,font=("times new roman" , 15,"bold"),bg="#2196f3",fg="white" ,cursor="hand2").place(x=360,y=100, height=28,width=120)
        
        btn_clear = Button(self.root ,text="Clear" ,command=self.clear,font=("times new roman" , 15,"bold"),bg="lightgrey",fg="black" ,cursor="hand2").place(x=490,y=100, height=28,width=120)

        sales_frame = Frame(self.root , bd=3 , relief=RIDGE)
        sales_frame.place(x=50,y=140,width=200,height=330)

        scrolly = Scrollbar(sales_frame,orient=VERTICAL)
        self.Sales_List = Listbox(sales_frame ,font=("times new roman"  , 15) ,bg="white",yscrollcommand=scrolly.set)
        scrolly.pack(side=RIGHT,fill=Y)
        scrolly.config(command=self.Sales_List.yview)
        self.Sales_List.pack(fill=BOTH,expand=1)
     
    #  =============================Bill area ============================
        bill_list = Frame(self.root , bd=3 , relief=RIDGE)
        bill_list.place(x=280,y=140,width=500,height=330)

        bill_title =Label(bill_list, text="Customer Bills Area" ,font=("goudy old style" , 20) , bg="orange").pack(side=TOP,fill=X) 


        scrolly2 = Scrollbar(bill_list,orient=VERTICAL)
        self.txt_bill_area =Text(bill_list,bg="white",yscrollcommand=scrolly2.set)
        scrolly2.pack(side=RIGHT,fill=Y)
        scrolly2.config(command=self.txt_bill_area.yview)
        self.txt_bill_area.pack(fill=BOTH,expand=1)
     



# =======================images=========================#
        self.menuLogo = Image.open("images/cat2.jpg")
        self.menuLogo = self.menuLogo.resize((300,300) ,Image.ANTIALIAS)
        self.menuLogo = ImageTk.PhotoImage(self.menuLogo)

        lbl_image = Label(self.root , image=self.menuLogo,bd=0)
        lbl_image.place(x=800, y=110)
        self.Sales_List.bind("<ButtonRelease-1>" , self.get_data)
        self.show()
# ======================================================================================

    def show(self):
        self.bill_list[:]
        # self.Sales_List.delete(0,END)
        # print(os.listdir('Q:\Inventory Manegment System\Bills'))
        for i in os.listdir("Q:\Inventory Manegment System\Bills"):
            # print(i.split('.'),i.split('.')[-1])
            if i.split('.')[-1] == "txt":
                self.Sales_List.insert(END,i)
                self.bill_list.append(i.split('.')[0])
     

    def get_data(self,ev):
        index_ = self.Sales_List.curselection()
        file_name = self.Sales_List.get(index_)
        self.txt_bill_area.delete("1.0",END)
        fp = open(f"Bills/{file_name}" , "r")
        for i in fp :
            self.txt_bill_area.insert(END,i)
        fp.close()    
        
        
    def search(self):
        if self.var_invoice.get() == "":
            messagebox.showerror("Error" , "Invalid invoice number")
            
        else:
            if self.var_invoice.get() in self.bill_list:
             fp = open(f"Bills/{self.var_invoice.get()}.txt" , "r")
             self.txt_bill_area.delete("1.0" ,END)
             for i in fp :
               self.txt_bill_area.insert(END,i)
             fp.close()
             
             
             
    def clear(self):
                  
            self.txt_bill_area.delete("1.0",END)
            self.bill_list.delete("1.0",END)
            self.show()  

    def exit(self):
            self.root.destroy()  
                           

# ============================== End ===============================#
        
        
if __name__ == "__main__":
       
    root = Tk();
    obj = salesClass(root);
    root.mainloop();      