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
        
        
        
        
        
        
        
# ============================== End ===============================#
        
        
if __name__ == "__main__":
       
    root = Tk();
    obj = supplierClass(root);
    root.mainloop();      