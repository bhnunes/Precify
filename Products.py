from tkinter import *
from tkinter import ttk
import sqlite3
from Functions import FunctionsProductsTab, FunctionsRecipeTab, AutocompleteEntry

class Products(FunctionsProductsTab):
    def widgets_producttab (self):
        #CLEAR BUTTON
        self.bt_clear = Button(self.products_tab, text="Clear", bd=2, bg = "#F99DBC", fg= "#f5f5f4",
                               activebackground="#FEC2D6", activeforeground="#f5f5f4",
                               font = ("Caviar Dreams", 9, "bold"), command=self.clear_fields)
        #relx = Da esquerda pra direito (0.1 = 10%)
        #relx = de cima pra baixo (0.1 = 10%)
        self.bt_clear.place(relx=0.12, rely=0.045, relwidth=0.1, relheight=0.04)

        #SEARCH BUTTON
        self.bt_search = Button(self.products_tab, text="Search", bd=2, bg = "#F99DBC", 
                               fg= "#f5f5f4", font = ("Caviar Dreams", 9, "bold"), command=self.search_product)
        self.bt_search.place(relx = 0.23, rely=0.045, relwidth=0.1, relheight=0.04)

        #NEW BUTTON
        self.bt_new = Button(self.products_tab, text="New", bd=2, bg = "#F99DBC", 
                               fg= "#f5f5f4", font = ("Caviar Dreams", 9, "bold"), command=self.add_product)
        self.bt_new.place(relx = 0.66, rely=0.045, relwidth=0.1, relheight=0.04)
        
        #EDIT BUTTON
        self.bt_edit = Button(self.products_tab, text="Edit", bd=2, bg = "#F99DBC", 
                               fg= "#f5f5f4", font = ("Caviar Dreams", 9, "bold"), command = self.edit_products)
        self.bt_edit.place(relx = 0.77, rely=0.045, relwidth=0.1, relheight=0.04)

        #DELETE BUTTON
        self.bt_delete = Button(self.products_tab, text="Delete", bd=2, bg = "#F99DBC", 
                               fg= "#f5f5f4", font = ("Caviar Dreams", 9, "bold"), command=self.delete_product)
        self.bt_delete.place(relx = 0.88, rely=0.045, relwidth=0.1, relheight=0.04)

        #ADD INGREDIENT BUTTON
        self.bt_new = Button(self.products_tab, text="Add to Recipe", bd=2, bg = "#F99DBC", 
                               fg= "#f5f5f4", font = ("Caviar Dreams", 9, "bold"), command=self.add_ingredient)
        self.bt_new.place(relx = 0.5, rely=0.045, relwidth=0.15, relheight=0.04)
        #===================================================================================

        #LABELS AND ENTRIES
        #ID
        self.lb_id = Label(self.products_tab, text="Product ID", background="#F5F5F4",
                           fg= "#F99DBC", font = ("Caviar Dreams", 9, "bold"))
        self.lb_id.place(relx=0.01, rely=0.01, relwidth=0.1, relheight=0.04)
        self.id_entry = Entry(self.products_tab)
        #self.id_entry.insert(0, "000")
        self.id_entry.place(relx=0.01, rely=0.045, relwidth=0.1, relheight=0.04)

        #PRODUCT NAME
        self.lb_name = Label(self.products_tab, text="Product Name", background="#F5F5F4",
                           fg= "#F99DBC", font = ("Caviar Dreams", 9, "bold"))
        self.lb_name.place(relx=0.01, rely=0.11, relwidth=0.12, relheight=0.04)
        self.name_entry = Entry(self.products_tab)
        self.name_entry.place(relx=0.01, rely=0.15, relwidth=0.55, relheight=0.04)

        #UNIT
        self.lb_qty = Label(self.products_tab, text="Quantity", background="#F5F5F4",
                           fg= "#F99DBC", font = ("Caviar Dreams", 9, "bold"))
        self.lb_qty.place(relx=0.57, rely=0.11, relwidth=0.08, relheight=0.04)
        self.qty_entry = Entry(self.products_tab)
        self.qty_entry.place(relx=0.57, rely=0.15, relwidth=0.12, relheight=0.04)

        #QUANTITY
        self.lb_unit = Label(self.products_tab, text="Unit", background="#F5F5F4",
                           fg= "#F99DBC", font = ("Caviar Dreams", 9, "bold"))
        self.lb_unit.place(relx=0.70, rely=0.11, relwidth=0.05, relheight=0.04)
        #self.unit_entry = Entry(self.products_tab)
        units = ["Gramas", "Mililitros", "Unidade"]
        self.unit_entry = AutocompleteEntry(units, self.products_tab, listboxLength=3, width=20)
        self.unit_entry.place(relx=0.70, rely=0.15, relwidth=0.12, relheight=0.04)

        #PRICE
        self.lb_price = Label(self.products_tab, text="Price", background="#F5F5F4",
                           fg= "#F99DBC", font = ("Caviar Dreams", 9, "bold"))
        self.lb_price.place(relx=0.83, rely=0.11, relwidth=0.05, relheight=0.04)
        self.price_entry = Entry(self.products_tab)
        self.price_entry.place(relx=0.83, rely=0.15, relwidth=0.15, relheight=0.04) 
    def list_products(self):
        style = ttk.Style(self.root)  
        style.theme_use('clam')
        style.configure("Treeview", background="#F5F5F4", fieldbackground="#F5F5F4", foreground="#F99DBC")
        style.configure('Treeview.Heading', background="#F99DBC", fg= "#F99DBC", font = ("Caviar Dreams", 9, "bold"))
        self.product_list = ttk.Treeview(self.products_tab, height=3, columns=("col1","col2","col3","col4","col5"))
        self.product_list.heading("#0", text="")
        self.product_list.heading("#1", text="ID")
        self.product_list.heading("#2", text="Product")
        self.product_list.heading("#3", text="Qty")
        self.product_list.heading("#4", text="Unit")
        self.product_list.heading("#5", text="Price")

        self.product_list.column("#0", width=1)
        self.product_list.column("#1", width=10)
        self.product_list.column("#2", width=220)
        self.product_list.column("#3", width=90)
        self.product_list.column("#4", width=90)
        self.product_list.column("#5", width=90)

        self.product_list.place(relx=0.01, rely=0.22, relwidth=0.97, relheight=0.75)

        self.scroll_list = Scrollbar(self.products_tab, orient="vertical")
        self.product_list.configure(yscroll=self.scroll_list.set)
        self.scroll_list.place(relx=0.98, rely=0.22, relwidth=0.02, relheight=0.75)

        self.product_list.bind("<Double-1>", self.onDoubleClick)