from tkinter import *
from tkinter import ttk
import sqlite3
from Functions import FunctionsRecipeTab, AutocompleteEntry


class NewRecipe (FunctionsRecipeTab, AutocompleteEntry):
    def widgets_newrecipe(self):
        #CLEAR BUTTON
        self.bt_clear = Button(self.recipe_tab, text="Clear", bd=2, bg = "#F99DBC", fg= "#f5f5f4",
                               activebackground="#FEC2D6", activeforeground="#f5f5f4",
                               font = ("Caviar Dreams", 9, "bold"), command=self.clear_recipefields)
        self.bt_clear.place(relx=0.12, rely=0.045, relwidth=0.1, relheight=0.04)

        #SEARCH BUTTON
        self.bt_search = Button(self.recipe_tab, text="Search", bd=2, bg = "#F99DBC", 
                               fg= "#f5f5f4", font = ("Caviar Dreams", 9, "bold"), command=self.searchrecipe_product)
        self.bt_search.place(relx = 0.23, rely=0.045, relwidth=0.1, relheight=0.04)

        #NEW BUTTON
        self.bt_new = Button(self.recipe_tab, text="Add", bd=2, bg = "#F99DBC", 
                               fg= "#f5f5f4", font = ("Caviar Dreams", 9, "bold"), command=self.add_ingredient)
        self.bt_new.place(relx = 0.66, rely=0.045, relwidth=0.1, relheight=0.04)
        
        #EDIT BUTTON
        self.bt_edit = Button(self.recipe_tab, text="Edit", bd=2, bg = "#F99DBC", 
                               fg= "#f5f5f4", font = ("Caviar Dreams", 9, "bold"), command = self.edit_products)
        self.bt_edit.place(relx = 0.77, rely=0.045, relwidth=0.1, relheight=0.04)

        #DELETE BUTTON
        self.bt_delete = Button(self.recipe_tab, text="Delete", bd=2, bg = "#F99DBC", 
                               fg= "#f5f5f4", font = ("Caviar Dreams", 9, "bold"), command=self.delete_product)
        self.bt_delete.place(relx = 0.88, rely=0.045, relwidth=0.1, relheight=0.04)

        #===================================================================================

        #LABELS AND ENTRIES
        #ID
        self.lb_id = Label(self.recipe_tab, text="Product ID", background="#F5F5F4",
                           fg= "#F99DBC", font = ("Caviar Dreams", 9, "bold"))
        self.lb_id.place(relx=0.01, rely=0.01, relwidth=0.1, relheight=0.04)
        self.id_recipeentry = Entry(self.recipe_tab)
        #self.id_entry.insert(0, "000")
        self.id_recipeentry.place(relx=0.01, rely=0.045, relwidth=0.1, relheight=0.04)

        #PRODUCT NAME
        self.lbrecipe_name = Label(self.recipe_tab, text="Product Name", background="#F5F5F4",
                           fg= "#F99DBC", font = ("Caviar Dreams", 9, "bold"))
        self.lbrecipe_name.place(relx=0.01, rely=0.11, relwidth=0.12, relheight=0.04)
        self.name_recipeentry = Entry(self.recipe_tab)
        
        #self.name_recipeentry = AutocompleteEntry(self.listcreation, self.recipe_tab,
        #                        listboxLength=6, width=32)
        self.name_recipeentry.place(relx=0.01, rely=0.15, relwidth=0.55, relheight=0.04)

        #UNIT
        self.lbrecipe_qty = Label(self.recipe_tab, text="Quantity", background="#F5F5F4",
                           fg= "#F99DBC", font = ("Caviar Dreams", 9, "bold"))
        self.lbrecipe_qty.place(relx=0.57, rely=0.11, relwidth=0.08, relheight=0.04)
        self.qty_recipeentry = Entry(self.recipe_tab)
        self.qty_recipeentry.place(relx=0.57, rely=0.15, relwidth=0.12, relheight=0.04)

        #QUANTITY
        self.lbrecipe_unit = Label(self.recipe_tab, text="Unit", background="#F5F5F4",
                           fg= "#F99DBC", font = ("Caviar Dreams", 9, "bold"))
        self.lbrecipe_unit.place(relx=0.70, rely=0.11, relwidth=0.05, relheight=0.04)
        self.unit_recipeentry = Entry(self.recipe_tab)
        self.unit_recipeentry.place(relx=0.70, rely=0.15, relwidth=0.12, relheight=0.04)

        #PRICE
        #self.lbrecipe_price = Label(self.recipe_tab, text="Price", background="#F5F5F4",
        #                   fg= "#F99DBC", font = ("Caviar Dreams", 9, "bold"))
        #self.lbrecipe_price.place(relx=0.83, rely=0.11, relwidth=0.05, relheight=0.04)
        #self.price_recipeentry = Entry(self.recipe_tab)
        #self.price_recipeentry.place(relx=0.83, rely=0.15, relwidth=0.15, relheight=0.04)        
    def list_recipeingredients(self):
        style = ttk.Style(self.root)  
        style.theme_use('clam')
        style.configure("Treeview", background="#F5F5F4", fieldbackground="#F5F5F4", foreground="#F99DBC")
        style.configure('Treeview.Heading', background="#F99DBC", fg= "#F99DBC", font = ("Caviar Dreams", 9, "bold"))
        self.ingredients_list = ttk.Treeview(self.recipe_tab, height=3, columns=("col1","col2","col3","col4","col5"))
        self.ingredients_list.heading("#0", text="")
        self.ingredients_list.heading("#1", text="ID")
        self.ingredients_list.heading("#2", text="Product")
        self.ingredients_list.heading("#3", text="Qty")
        self.ingredients_list.heading("#4", text="Unit")
        self.ingredients_list.heading("#5", text="Price")

        self.ingredients_list.column("#0", width=1)
        self.ingredients_list.column("#1", width=10)
        self.ingredients_list.column("#2", width=220)
        self.ingredients_list.column("#3", width=90)
        self.ingredients_list.column("#4", width=90)
        self.ingredients_list.column("#5", width=90)

        self.ingredients_list.place(relx=0.01, rely=0.22, relwidth=0.97, relheight=0.75)

        self.scrolli_list = Scrollbar(self.recipe_tab, orient="vertical")
        self.ingredients_list.configure(yscroll=self.scrolli_list.set)
        self.scrolli_list.place(relx=0.98, rely=0.22, relwidth=0.02, relheight=0.75)

        self.ingredients_list.bind("<Double-1>", self.onDoubleClick_recipetab)    