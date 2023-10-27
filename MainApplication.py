from tkinter import *
from tkinter import ttk
import sqlite3

from Products import Products
from Recipe import NewRecipe


root = Tk()
       
class Application(Products, NewRecipe):
    def __init__(self): 
        self.root = root
        self.window()
        self.window_frame()
        self.widgets_producttab()
        self.list_products()
        self.widgets_newrecipe()
        self.list_recipeingredients()
        self.create_tables()
        self.select_list()
        self.menus()

        root.mainloop()  #manter a janela aberta 
    def window (self):
        self.root.title("Cadastro de Produtos")
        self.root.configure(background="#FEC2D6")
        self.root.geometry("799x588")
        self.root.resizable(True, True)
        #self.root.maxsize(width = 988, height= 788)
        self.root.minsize(width=788, height=588)
    def window_frame (self):

        self.frame_1 = Frame(self.root, bd = 4, bg="#F5F5F4",
                             highlightbackground="#EBE8E2", highlightthickness=2)
        self.frame_1.place(relx=0.01, rely=0.01, relwidth=0.98, relheight=0.98)
        
        #self.frame_2 = Frame(self.root, bd=4, bg="#F5F5F4",
        #                     highlightbackground="#EBE8E2", highlightthickness=2)
        #self.frame_2.place(relx=0.02, rely=0.23, relwidth=0.96, relheight=0.70)

        self.tabs = ttk.Notebook(self.frame_1)
        self.products_tab = Frame(self.tabs)
        self.recipe_tab = Frame(self.tabs)
        self.pricechart_tab = Frame(self.tabs)

        self.products_tab.configure(bd = 4, bg="#F5F5F4", highlightbackground="#EBE8E2", highlightthickness=2,)
        self.recipe_tab.configure(bd = 4, bg="#F5F5F4", highlightbackground="#EBE8E2", highlightthickness=2)
        self.pricechart_tab.configure(bd = 4, bg="#F5F5F4", highlightbackground="#EBE8E2", highlightthickness=2)

        self.tabs.add(self.products_tab, text="Products")
        self.tabs.add(self.recipe_tab, text="New Recipe")
        self.tabs.add(self.pricechart_tab, text="Price Chart")

        self.tabs.place(relx=0.01, rely=0.01, relwidth=0.98, relheight=0.98)
    def menus (self):
        menubar = Menu(self.root)
        self.root.config(menu=menubar)
        filemenu = Menu(menubar)
        
        def quit():
            self.root.destroy()        
        
        menubar.add_cascade(label="Options", menu=filemenu)
        filemenu.add_command(label="Quit", command=quit)
        filemenu.add_command(label="Clear", command=self.clear_fields)
        filemenu.add_command(label="Products")
        filemenu.add_command(label="Recipes")
        filemenu.add_command(label="Price Chart")
        filemenu.add_command(label="Dark Mode", command=self.dark_mode)
    def dark_mode (self):
        self.root.configure(background="#000000")
        self.frame_1 = Frame(self.root, bd = 4, bg="#232429",
                             highlightbackground="#232429", highlightthickness=2)
        
        self.products_tab.configure(bd = 4, bg="#232429", highlightbackground="#232429", highlightthickness=2,)
        self.recipe_tab.configure(bd = 4, bg="#232429", highlightbackground="#232429", highlightthickness=2)
        self.pricechart_tab.configure(bd = 4, bg="#232429", highlightbackground="#232429", highlightthickness=2)

        #PRODUCTS VIEW
        self.bt_clear = Button(self.products_tab, text="Clear", bd=2, bg = "#000000", fg= "#f5f5f4",
                               activebackground="#000000", activeforeground="#f5f5f4",
                               font = ("Caviar Dreams", 9, "bold"), command=self.clear_fields)
 
        #SEARCH BUTTON
        self.bt_search = Button(self.products_tab, text="Search", bd=2, bg = "#000000", 
                               fg= "#f5f5f4", font = ("Caviar Dreams", 9, "bold"), command=self.search_product)

        #NEW BUTTON
        self.bt_new = Button(self.products_tab, text="New", bd=2, bg = "#000000", 
                               fg= "#f5f5f4", font = ("Caviar Dreams", 9, "bold"), command=self.add_product)
         
        #EDIT BUTTON
        self.bt_edit = Button(self.products_tab, text="Edit", bd=2, bg = "#000000", 
                               fg= "#f5f5f4", font = ("Caviar Dreams", 9, "bold"), command = self.edit_products)

        #DELETE BUTTON
        self.bt_delete = Button(self.products_tab, text="Delete", bd=2, bg = "#000000", 
                               fg= "#f5f5f4", font = ("Caviar Dreams", 9, "bold"), command=self.delete_product)

        #ADD INGREDIENT BUTTON
        self.bt_new = Button(self.products_tab, text="Add to Recipe", bd=2, bg = "#000000", 
                               fg= "#f5f5f4", font = ("Caviar Dreams", 9, "bold"), command=self.add_ingredient)
        
        style = ttk.Style(self.root)  
        style.theme_use('clam')
        style.configure("Treeview", background="#232429", fieldbackground="#232429", foreground="#000000")
        style.configure('Treeview.Heading', background="#000000", fg= "#F5F5F4", font = ("Caviar Dreams", 9, "bold"))

Application()

