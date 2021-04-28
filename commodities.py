from tkinter import *
from tkinter import ttk
import mysql.connector
import tkinter.messagebox
from PIL import ImageTk, Image

#Establishing a connection with database
conn = mysql.connector.connect(host="localhost", user="root", password="root", database="grocerystore")
mycursor = conn.cursor()
class Commodities():
    """This class is to perform operations on the commodities table of our database"""
    def __init__(self, window):
        self.window = window
        self.left = Frame(window, width=2000, height=1600, bg="white")
        self.left.pack(side = LEFT)

        self.right = Frame(window, width = 10, height = 1600, bg = "white")
        self.right.pack(side = RIGHT)

        self.back_img = Image.open('commodities_in1.png')
        self.back_img = self.back_img.resize((700, 500), Image.ANTIALIAS)
        self.back_img1 = ImageTk.PhotoImage(self.back_img)
        self.background_label = Label(self.left, image=self.back_img1, compound = "right", bg = "white", fg = None)
        self.background_label.pack(side = "top", fill ="both")
        self.background_label.place(x=250, y=-100, relwidth = 1, relheight = 1)

        self.heading = Label(self.left, text ="Commodities Information", font=('arial 30 bold'), fg = 'HotPink4', bg = "white")
        self.heading.place(x = 200, y = 0)

        self.heading = Label(self.left, text ="Product_No", font=('arial 10 bold'), fg = 'black',bg = "white")
        self.heading.place(x = 0, y = 100)

        self.heading = Label(self.left, text ="Product_Name", font=('arial 10 bold'), fg = 'black', bg = "white")
        self.heading.place(x = 0, y = 140)

        self.heading = Label(self.left, text ="Prod_Quantity", font=('arial 10 bold'), fg = 'black', bg = "white")
        self.heading.place(x = 0, y = 180)

        self.heading = Label(self.left, text ="Prod_Price", font=('arial 10 bold'), fg = 'black', bg = "white")
        self.heading.place(x = 0, y = 220)

        # Entries for all Labels
        self.product_No = Entry(self.left, width = 30,bg = "ghost white")
        self.product_No.place(x = 210, y = 100)

        self.Product_Name = Entry(self.left, width = 30,bg = "ghost white")
        self.Product_Name.place(x = 210, y = 140)

        self.Prod_Quantity = Entry(self.left, width = 30,bg = "ghost white")
        self.Prod_Quantity.place(x = 210, y = 180)

        self.Prod_Price = Entry(self.left, width = 30,bg = "ghost white")
        self.Prod_Price.place(x = 210, y = 220)

        # Submit Button
        self.submit = Button(self.left, text = "Add product", width = 15, height = 2, font=('arial 10 bold'),bg = "light gray", command = self.add_product)
        self.submit.place(x=100, y = 400)
        # Search Button
        self.search = Button(self.left, text = "Click to search", width = 15, height = 2,font=('arial 10 bold'),bg = "light gray", command = self.searchproduct)
        self.search.place(x = 250, y = 400)
        self.exit_now = Button(self.left, text = "Close", width = 15, height = 2,font=('arial 10 bold'),bg = "light gray", command = self.window.destroy)
        self.exit_now.place(x = 390, y = 400)
        self.clear_now2 = Button(self.left, text ="Clear", width = 15, height = 2,font=('arial 10 bold'),bg = "light gray", command = self.clear2)
        self.clear_now2.place(x = 550, y = 400)

    # Function to call when add product is clicked
    def add_product(self):
        """This function is used add new product into the commodities table of our Grocery Store Management system"""
        self.val1 = self.Product_No.get()
        self.val2 = self.Product_Name.get()
        self.val3 = self.Prod_Quantity.get()
        self.val4 = self.Prod_Price.get()

        if self.val1 == '' or self.val2 == '' or self.val3 =='' or self.val4 =='' :
            tkinter.messagebox.showinfo("Error", "Fill in all fields")
        else:
            query_Comm = "INSERT INTO Commodities(Product_No,Product_Name,Prod_Quantity,Prod_Price) values(%s, %s, %s, %s) "
            values = (self.val1, self.val2, self.val3, self.val4)
            mycursor.execute(query_Comm, values)
            conn.commit()
            self.clear2()
            tkinter.messagebox.showinfo("Success", "Successfully added", parent = self.left)
    def searchproduct(self):
        """This function opens a new window, when the user clicks on the search button in the main window. It provides other options like edit as well."""
        self.search_product = Tk()
        self.search_product.title("Search product")
        self.search_product.geometry("1600x1000")
        self.drop = ttk.Combobox(self.search_product, value = ["Product_No", "Product_Name", "Prod_Quantity", "Prod_Price"])
        self.drop.current(0)
        self.drop.place(x = 0, y = 50)
        self.search_box = Entry(self.search_product)
        self.search_box.place(x = 150, y = 50)

        # Search button
        self.search_now = Button(self.search_product, text = "Search product", width = 15, height = 2,font=('arial 10 bold'),bg = "light gray", command = self.searchNow)
        self.search_now.place(x = 100, y = 100)
        #Close button
        self.exit_now = Button(self.search_product, text = "Close", width = 15, height = 2,font=('arial 10 bold'),bg = "light gray", command = self.search_product.destroy)
        self.exit_now.place(x = 250, y = 100)
        #Edit button
        self.edit_now = Button(self.search_product, text = "Change", width = 15, height = 2,font=('arial 10 bold'),bg = "light gray", command = self.editNow)
        self.edit_now.place(x = 400, y = 100)
        #Clear Button
        self.clear_now = Button(self.search_product, text ="Clear", width = 15, height = 2,font=('arial 10 bold'),bg = "light gray", command = self.clear)
        self.clear_now.place(x = 550, y = 100)

    def searchNow(self):
        """This function helps us to search for any data in Commodities table"""
        selected = self.drop.get()
        if selected == "Product_No":
            sql_query = "SELECT * FROM Commodities WHERE Product_No=%s"
        elif selected == "Product_Name":
            sql_query = "SELECT * FROM Commodities WHERE Product_Name=%s"
        elif selected == "Prod_Quantity":
            sql_query = "SELECT * FROM Commodities WHERE Prod_Quantity=%s"
        elif selected == "Prod_Price":
            sql_query = "SELECT * FROM Commodities WHERE Prod_Price=%s"

        searched = self.search_box.get()
        name = (searched,)
        mycursor.execute(sql_query, name)
        searchResult = mycursor.fetchall()
        cols = ('Serial No', 'Product_No' , 'Product_Name', 'Prod_Quantity' , 'Prod_Price')
        self.listBox = ttk.Treeview(self.search_product, columns=cols, show = 'headings' )
        # set column headings
        for col in cols:
            self.listBox.heading(col, text=col)
        for i, (Product_No, Product_Name, Prod_Quantity, Prod_Price) in enumerate(searchResult, start=1):
            self.listBox.insert("", "end", values=(i, Product_No, Product_Name, Prod_Quantity, Prod_Price))
        self.listBox.place(x = 0, y = 200)
        if searchResult:
            child_id = self.listBox.get_children()[-1]
            val1 = self.listBox.focus(child_id)
            #print("val1 is ", val1)
            id = self.listBox.focus()
            self.id_item = self.listBox.item(id)
        self.listBox.bind("<<TreeviewSelect>>", self.onSelect)
        if not searchResult:
            searchResult = "Product not found"
            searched_label = Label(self.search_product, text = searchResult)
            searched_label.place(x = 0, y = 160)
    def editNow(self):
        """This function is called when we click on change button.We need to select the product and then click on edit button.
            This function then provides us the option to update or delete"""
        try:
            if self.item_text:
                self.cProduct_No = Label(self.search_product, text ="Product_No",
                             font=('arial 10 bold'), fg = 'black')
                self.cProduct_No.place(x = 0, y = 450)
                self.Product_No2 = Entry(self.search_product, width = 30)
                self.Product_No2.place(x = 210, y = 450)
                self.Product_No2.insert(0, self.item_text[1])
                self.Product_No2.config(state=DISABLED)
                self.cProduct_Name = Label(self.search_product, text ="Product_Name",font=('arial 10 bold'), fg = 'black')
                self.cProduct_Name.place(x = 0, y = 480)
                self.Product_Name2 = Entry(self.search_product, width = 30)
                self.Product_Name2.place(x = 210, y = 480)
                self.Product_Name2.insert(0, self.item_text[2])

                self.cProd_Quantity = Label(self.search_product ,text ="Prod_Quantity",
                             font=('arial 10 bold'), fg = 'black')
                self.cProd_Quantity.place(x = 0, y = 510)

                self.Prod_Quantity2 = Entry(self.search_product, width = 30)
                self.Prod_Quantity2.place(x = 210, y = 510)
                self.Prod_Quantity2.insert(0, self.item_text[3])

                self.cProd_Price = Label(self.search_product, text ="Prod_Price",
                             font=('arial 10 bold'), fg = 'black')
                self.cProd_Price.place(x = 0, y = 540)
                self.Prod_Price2 = Entry(self.search_product, width = 30)
                self.Prod_Price2.place(x = 210, y = 540)
                self.Prod_Price2.insert(0, self.item_text[4])

                self.update_now = Button(self.search_product, text = "Update", width = 15, height = 2,font=('arial 10 bold'),bg = "light gray", command = self.updateNow)
                self.update_now.place(x = 70, y = 690)

                self.delete_now = Button(self.search_product, text = "Delete", width = 15, height = 2,font=('arial 10 bold'),bg = "light gray", command = self.deleteNow)
                self.delete_now.place(x = 180, y = 690)

        except:
            tkinter.messagebox.showinfo("Warning", "Please select a product to edit", parent = self.search_product)

    def onSelect(self,event):
        """This function is used to get the selected item from the displayed list"""
        for item in self.listBox.selection():
            self.item_text = self.listBox.item(item,"values")

    def updateNow(self):
        """Used to update the Commodities table"""
        update_query = "Update commodities set Product_Name = %s, Prod_Quantity = %s, Prod_Price = %s where Product_No = %s"
        Pro_No = self.Product_No2.get()
        Pro_Name = self.Product_Name2.get()
        Pro_Quantity = self.Prod_Quantity2.get()
        Pro_Price = self.Prod_Price2.get()

        inputs = (Pro_Name, Pro_Quantity, Pro_Price,Pro_No)
        mycursor.execute(update_query, inputs)
        conn.commit()
        self.clear()
        tkinter.messagebox.showinfo("Success", "Successfully Updated", parent = self.search_product)

    def deleteNow(self):
        """Used to delete data from Commodities table only if there are no products in that location"""
        Pro_NO = self.Product_No2.get()

        my_var=tkinter.messagebox.askyesnocancel("Delete ?","Delete id:"+str(Pro_NO),icon='warning',default='no', parent = self.search_product)
        try:
            if my_var: # True if yes button is clicked
                mycursor.execute("DELETE FROM commodities WHERE Product_No= "+ Pro_NO )
                conn.commit()
                self.clear()
                tkinter.messagebox.showinfo("Success", "Successfully Deleted", parent = self.search_product)
        except:
            tkinter.messagebox.showinfo("Warning", "Products exists in this Store", parent = self.search_product)


    def clear(self):
        """Refresh the search Product window"""
        self.search_product.destroy()
        self.searchproduct()

    def clear2(self):
        """Refresh the main window"""
        self.left.destroy()
        self.right.destroy()
        self.__init__(self.window)

# root = Tk()
# root.title("Commodity Details")
# b = Commodities(root)
# root.geometry("1200x1200+0+0")
# root.mainloop()

