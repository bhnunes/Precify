from tkinter import *
from tkinter import ttk
import sqlite3
import re

class FunctionsProductsTab():
    def clear_fields(self):
        self.id_entry.delete(0, END)
        self.name_entry.delete(0, END)
        self.qty_entry.delete(0, END)
        self.unit_entry.delete(0, END)
        self.price_entry.delete(0, END)
    def connect_db(self):
        self.conn = sqlite3.connect("products.db")
        self.cursor = self.conn.cursor()
        print("Conecting to database")
    def disconnect_db(self):
        self.conn.close()
        print("Disconecting to database")
    def create_tables (self):
        self.connect_db()
        #STARTING TABLE
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS products (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                product_name CHAR(40) NOT NULL,
                qty INTEGER(20) NOT NULL,
                unit CHAR(40),
                price FLOAT(20) NOT NULL);
            """)
        self.conn.commit(); print ("Database created") 
        self.disconnect_db()   
    def variables(self):
        self.id = self.id_entry.get()
        self.product = self.name_entry.get()
        self.qty = self.qty_entry.get()
        self.unit = self.unit_entry.get()
        self.price = self.price_entry.get()
    def add_product(self):
        self.variables()
        self.connect_db()
        self.cursor.execute("""
            INSERT INTO products (product_name, qty, unit, price)
                VALUES (?, ?, ?, ?)""", (self.product, self.qty, self.unit, self.price))
        self.conn.commit()
        self.disconnect_db()
        self.select_list()
        self.clear_fields()
    def select_list(self):
        self.product_list.delete(*self.product_list.get_children())
        self.connect_db()
        list = self.cursor.execute(""" SELECT id, product_name, qty, unit, price FROM products
            ORDER BY product_name ASC; """)
        for i in list:
            self.product_list.insert("", END, values=i)
        self.disconnect_db()
        print(self.product_list)
    def onDoubleClick (self, event):
        self.clear_fields()
        self.product_list.selection()
        for i in self.product_list.selection():
            col1, col2, col3, col4, col5 = self.product_list.item(i, "values")
            self.id_entry.insert(END, col1)
            self.name_entry.insert(END, col2)
            self.qty_entry.insert(END, col3)
            self.unit_entry.insert(END, col4)
            self.price_entry.insert(END, col5)
    def delete_product(self):
        self.variables()
        self.connect_db()
        self.cursor.execute("""DELETE FROM products WHERE id = ?""", (self.id,))
        self.conn.commit()
        self.disconnect_db()
        self.clear_fields()
        self.select_list()
    def edit_products(self):
        self.variables()
        self.connect_db()
        self.cursor.execute("""UPDATE products SET product_name = ?, qty = ?, unit = ?, price = ?
                            WHERE id = ?""", (self.product, self.qty, self.unit, self.price, self.id))
        self.conn.commit()
        self.disconnect_db()
        self.clear_fields()
        self.select_list()
    def search_product(self):
        self.connect_db()
        self.product_list.delete(*self.product_list.get_children())
        self.name_entry.insert(END, "%")
        name = self.name_entry.get()
        self.cursor.execute("""SELECT id, product_name, qty, unit, price FROM products
                            WHERE product_name LIKE '%s' ORDER BY product_name ASC""" % name)
        searchingProduct = self.cursor.fetchall()
        for i in searchingProduct:
            self.product_list.insert("", END, values=i)
        
        self.clear_fields()
        self.disconnect_db()

class FunctionsRecipeTab ():
    def clear_recipefields(self):

        self.id_recipeentry.delete(0, END)
        self.name_recipeentry.delete(0, END)
        self.qty_recipeentry.delete(0, END)
        self.unit_recipeentry.delete(0, END)
        self.price_recipeentry.delete(0, END)
    def connect_db_recipetab(self):
        self.conn = sqlite3.connect("products.db")
        self.cursor = self.conn.cursor()
        print("Conecting to database")
    def disconnect_dbrecipetab(self):
        self.conn.close()
        print("Disconecting to database")
    def select_listofproducts(self):
        self.product_listofproducts.delete(*self.product_list.get_children())
        self.connect_db()
        list = self.cursor.execute(""" SELECT id, product_name, qty, unit, price FROM products
            ORDER BY product_name ASC; """)
        for i in list:
            self.product_listofproducts.insert("", END, values=i)
        self.disconnect_db()
        return list
    def searchrecipe_product(self):
        self.connect_db()
        self.ingredients_list.delete(*self.ingredients_list.get_children())
        self.name_recipeentry.insert(END, "%")
        name = self.name_recipeentry.get()
        self.cursor.execute("""SELECT id, product_name, qty, unit, price FROM products
                            WHERE product_name LIKE '%s' ORDER BY product_name ASC""" % name)
        searchingProduct = self.cursor.fetchall()
        for i in searchingProduct:
            self.ingredients_list.insert("", END, values=i)
        self.clear_recipefields()
        self.disconnect_db()
    def recipe_variables(self):
        self.ingredientid = self.id_recipeentry.get()
        self.ingredientproduct = self.name_recipeentry.get()
        self.ingredientqty = self.qty_recipeentry.get()
        self.ingredientunit = self.unit_recipeentry.get()
        #self.ingredientprice = self.price_recipeentry.get()
    def add_ingredient(self):
        self.recipe_variables()
        self.ingredients_list.insert("", END, values=(self.ingredientid, self.ingredientproduct, self.ingredientqty, self.ingredientunit))
        self.clear_recipefields()
    def onDoubleClick_recipetab (self, event):
        self.clear_fields()
        self.ingredients_list.selection()
        for i in self.ingredients_list.selection():
            col1, col2, col3, col4, col5 = self.ingredients_list.item(i, "values")
            self.id_recipeentry.insert(END, col1)
            self.name_recipeentry.insert(END, col2)
            self.qty_recipeentry.insert(END, col3)
            self.unit_recipeentry.insert(END, col4)
            #self.price_recipeentry.insert(END, col5)
        self.ingredients_list.delete(*self.ingredients_list.get_children())

class AutocompleteEntry(Entry,FunctionsProductsTab):
    def __init__(self, autocompleteList, *args, **kwargs):
        # Listbox length
        if 'listboxLength' in kwargs:
            self.listboxLength = kwargs['listboxLength']
            del kwargs['listboxLength']
        else:
            self.listboxLength = 8

        # Custom matches function
        if 'matchesFunction' in kwargs:
            self.matchesFunction = kwargs['matchesFunction']
            del kwargs['matchesFunction']
        else:
            def matches(fieldValue, acListEntry):
                pattern = re.compile('.*' + re.escape(fieldValue) + '.*', re.IGNORECASE)
                return re.match(pattern, acListEntry)

            self.matchesFunction = matches

        Entry.__init__(self, *args, **kwargs)
        self.focus()

        self.autocompleteList = autocompleteList

        self.var = self["textvariable"]
        if self.var == '':
            self.var = self["textvariable"] = StringVar()

        self.var.trace('w', self.changed)
        self.bind("<Right>", self.selection)
        self.bind("<Up>", self.moveUp)
        self.bind("<Down>", self.moveDown)

        self.listboxUp = False
        
        self.listcreation ()
    def changed(self, name, index, mode):
        if self.var.get() == '':
            if self.listboxUp:
                self.listbox.destroy()
                self.listboxUp = False
        else:
            words = self.comparison()
            if words:
                if not self.listboxUp:
                    self.listbox = Listbox(width=self["width"], height=self.listboxLength)
                    self.listbox.bind("<Button-1>", self.selection)
                    self.listbox.bind("<Right>", self.selection)
                    self.listbox.place(x=self.winfo_x(), y=self.winfo_y() + self.winfo_height())
                    self.listboxUp = True

                self.listbox.delete(0, END)
                for w in words:
                    self.listbox.insert(END, w)
            else:
                if self.listboxUp:
                    self.listbox.destroy()
                    self.listboxUp = False
    def selection(self, event):
        if self.listboxUp:
            self.var.set(self.listbox.get(ACTIVE))
            self.listbox.destroy()
            self.listboxUp = False
            self.icursor(END)
    def moveUp(self, event):
        if self.listboxUp:
            if self.listbox.curselection() == ():
                index = '0'
            else:
                index = self.listbox.curselection()[0]

            if index != '0':
                self.listbox.selection_clear(first=index)
                index = str(int(index) - 1)

                self.listbox.see(index)  # Scroll!
                self.listbox.selection_set(first=index)
                self.listbox.activate(index)
    def moveDown(self, event):
        if self.listboxUp:
            if self.listbox.curselection() == ():
                index = '0'
            else:
                index = self.listbox.curselection()[0]

            if index != END:
                self.listbox.selection_clear(first=index)
                index = str(int(index) + 1)

                self.listbox.see(index)  # Scroll!
                self.listbox.selection_set(first=index)
                self.listbox.activate(index)
    def comparison(self):
        return [w for w in self.autocompleteList if self.matchesFunction(self.var.get(), w)]
    def matches(fieldValue, acListEntry):
        pattern = re.compile(re.escape(fieldValue) + '.*', re.IGNORECASE)
        return re.match(pattern, acListEntry)
    def listcreation (self):
        self.listofproducts = []
        self.connect_db()
        list = self.cursor.execute(""" SELECT product_name FROM products
            ORDER BY product_name ASC; """)
        for i in list:
            self.listofproducts.append(i,)
        self.disconnect_db()
        return self.listofproducts



