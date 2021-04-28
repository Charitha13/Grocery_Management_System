from tkinter import *
from tkinter import ttk
import mysql.connector
from PIL import ImageTk, Image
import tkinter.messagebox

#Establishing a connection with database
conn = mysql.connector.connect(host="localhost", user="root", password="root", database="grocerystore")
mycursor = conn.cursor()
class Categories():
    """This class is to perform operations on the categories table of our database"""
    def __init__(self, window):
        self.window = window
        self.left = Frame(window, width=2000, height=1600, bg="white")
        self.left.pack(side = LEFT)

        self.right = Frame(window, width = 10, height = 1600, bg = "white")
        self.right.pack(side = RIGHT)

        self.back_img = Image.open('category_in1.png')
        # self.back_img = self.back_img.resize((1000, 1000), Image.ANTIALIAS)
        self.back_img1 = ImageTk.PhotoImage(self.back_img)
        self.background_label = Label(self.left, image=self.back_img1, compound = "right", bg = "white", fg = None)
        self.background_label.pack(side = "top", fill ="both")
        self.background_label.place(x=250, y=-100, relwidth = 1, relheight = 1)

        self.heading = Label(self.left, text ="Category Details", font=('arial 30 bold'), fg = 'HotPink4', bg = "white")
        self.heading.place(x = 200, y = 0)

        self.heading = Label(self.left, text ="Category ID", font=('arial 10 bold'), fg = 'HotPink4',bg = "white")
        self.heading.place(x = 0, y = 100)

        self.heading = Label(self.left, text ="Category Name", font=('arial 10 bold'), fg = 'HotPink4', bg = "white")
        self.heading.place(x = 0, y = 140)

        self.heading = Label(self.left, text ="Product ID", font=('arial 10 bold'), fg = 'HotPink4', bg = "white")
        self.heading.place(x = 0, y = 180)

        # Entries for all Labels
        self. Category_Id= Entry(self.left, width = 30,bg = "ghost white")
        self.Category_Id.place(x = 210, y = 100)

        self.Category_Name = Entry(self.left, width = 30,bg = "ghost white")
        self.Category_Name.place(x = 210, y = 140)

        self.Product_No = Entry(self.left, width = 30,bg = "ghost white")
        self.Product_No.place(x = 210, y = 180)

        # Submit Button
        self.submit = Button(self.left, text = "Add Category", width = 15, height = 2, font=('arial 10 bold'),bg = "MistyRose3",fg = 'dark slate blue', command = self.add_Category)
        self.submit.place(x=100, y = 400)
        # Search Button
        self.search = Button(self.left, text = "Click to search", width = 15, height = 2,font=('arial 10 bold'),bg = "MistyRose3",fg = 'dark slate blue', command = self.searchCategory)
        self.search.place(x = 250, y = 400)
        self.exit_now = Button(self.left, text = "Close", width = 15, height = 2,font=('arial 10 bold'),bg = "MistyRose3",fg = 'dark slate blue', command = self.window.destroy)
        self.exit_now.place(x = 390, y = 400)
        self.clear_now2 = Button(self.left, text ="Clear", width = 15, height = 2,font=('arial 10 bold'),bg = "MistyRose3",fg = 'dark slate blue', command = self.clear2)
        self.clear_now2.place(x = 550, y = 400)

    # Function to call when add new Category is clicked
    def add_Category(self):
        """This function is usedto add new Category into the Category table of our Grocery Store Management system"""
        self.val1 = self.Category_Id.get()
        self.val2 = self.Category_Name.get()
        self.val3 = self.Product_No.get()

        if self.val1 == '' or self.val2 == '' or self.val3 =='' :
            tkinter.messagebox.showinfo("Error", "Fill in all fields")
        else:
            query_loc = "INSERT INTO Categories(Category_Id, Category_Name, Product_No) values(%s, %s, %s) "
            values = (self.val1, self.val2, self.val3)
            mycursor.execute(query_loc, values)
            conn.commit()
            self.clear2()
            tkinter.messagebox.showinfo("Success", "Successfully added", parent = self.left)
    def searchCategory(self):
        """This function opens a new window, when the user clicks on the search button in the main window. It provides other options like edit as well."""
        self.search_Category = Tk()
        self.search_Category.title("Search Category")
        self.search_Category.geometry("1600x1000")
        self.drop = ttk.Combobox(self.search_Category, value = ["Category ID", "Category Name"])
        self.drop.current(1)
        self.drop.place(x = 0, y = 50)
        self.search_box = Entry(self.search_Category)
        self.search_box.place(x = 150, y = 50)

        # Search button
        self.search_now = Button(self.search_Category, text = "Search Category", width = 15, height = 2,font=('arial 10 bold'),bg = "light gray", command = self.searchNow)
        self.search_now.place(x = 100, y = 100)
        #Close button
        self.exit_now = Button(self.search_Category, text = "Close", width = 15, height = 2,font=('arial 10 bold'),bg = "light gray", command = self.search_Category.destroy)
        self.exit_now.place(x = 250, y = 100)
        #Edit button
        self.edit_now = Button(self.search_Category, text = "Change", width = 15, height = 2,font=('arial 10 bold'),bg = "light gray", command = self.editNow)
        self.edit_now.place(x = 400, y = 100)
        #Clear Button
        self.clear_now = Button(self.search_Category, text ="Clear", width = 15, height = 2,font=('arial 10 bold'),bg = "light gray", command = self.clear)
        self.clear_now.place(x = 550, y = 100)

    def searchNow(self):
        """This function helps us to search for any data in Category table"""
        selected = self.drop.get()
        if selected == "Category ID":
            sql_query = "SELECT * FROM Categories WHERE Category_Id=%s"
        elif selected == "Category Name":
            sql_query = "SELECT * FROM Categories WHERE Category_Name=%s"


        searched = self.search_box.get()
        name = (searched,)
        mycursor.execute(sql_query, name)
        searchResult = mycursor.fetchall()
        cols = ('Serial No', 'Category_ID', 'Category_Name','Product_No')
        self.listBox = ttk.Treeview(self.search_Category, columns=cols, show = 'headings' )
        # set column headings
        for col in cols:
            self.listBox.heading(col, text=col)
        for i, (Category_Id, Category_Name, Product_No) in enumerate(searchResult, start=1):
            self.listBox.insert("", "end", values=(i, Category_Id, Category_Name, Product_No))
        self.listBox.place(x = 40, y = 200)
        if searchResult:
            #child_Id = self.listBox.get_children()[-1]
            #val1 = self.listBox.focus(child_Id)
            id = self.listBox.focus()
            self.id_item = self.listBox.item(id)
        self.listBox.bind("<<TreeviewSelect>>", self.onSelect)
        if not searchResult:
            searchResult = "Category not found"
            searched_label = Label(self.search_Category, text = searchResult)
            searched_label.place(x = 0, y = 160)
    def editNow(self):
        """This function is called when we click on change button.We need to select the Category and then click on edit button.
            This function then provides us the option to update or delete"""
        try:
            if self.item_text:
                self.lCategory_Id = Label(self.search_Category, text ="category_Id",
                             font=('arial 10 bold'), fg = 'black')
                self.lCategory_Id.place(x = 0, y = 450)
                self.Category_Id2 = Entry(self.search_Category, width = 30)
                self.Category_Id2.place(x = 210, y = 450)
                self.Category_Id2.insert(0, self.item_text[1])

                self.lCategory_Name = Label(self.search_Category, text ="Category Name",font=('arial 10 bold'), fg = 'black')
                self.lCategory_Name.place(x = 0, y = 480)
                self.Category_Name2 = Entry(self.search_Category, width = 30)
                self.Category_Name2 .place(x = 210, y = 480)
                self.Category_Name2.insert(0, self.item_text[2])

                self.lProduct_No = Label(self.search_Category ,text ="product number",
                             font=('arial 10 bold'), fg = 'black')
                self.lProduct_No.place(x = 0, y = 510)

                self.Product_No2 = Entry(self.search_Category, width = 30)
                self.Product_No2.place(x = 210, y = 510)
                self.Product_No2.insert(0, self.item_text[3])
                self.Product_No2.config(state=DISABLED)



                self.update_now = Button(self.search_Category, text = "Update", width = 15, height = 2,font=('arial 10 bold'),bg = "light gray", command = self.updateNow)
                self.update_now.place(x = 70, y = 690)

                self.delete_now = Button(self.search_Category, text = "Delete", width = 15, height = 2,font=('arial 10 bold'),bg = "light gray", command = self.deleteNow)
                self.delete_now.place(x = 180, y = 690)

        except:
            tkinter.messagebox.showinfo("Warning", "Please select a category to edit", parent = self.search_Category)

    def onSelect(self,event):
        """This function is used to get the selected item from the displayed list"""
        for item in self.listBox.selection():
            self.item_text = self.listBox.item(item,"values")

    def updateNow(self):
        """Used to update the Category table"""
        update_query = "Update categories set Category_Id = %s, Category_Name= %s where Product_No = %s"
        Category_Id = self.Category_Id2.get()
        Category_Name = self.Category_Name2.get()
        Product_No= self.Product_No2.get()
        #print(Category_Id, Category_Name, Product_No)

        inputs = ( Category_Id, Category_Name, Product_No)
        mycursor.execute(update_query, inputs)
        conn.commit()
        tkinter.messagebox.showinfo("Success", "Successfully Updated", parent = self.search_Category)

    def deleteNow(self):
        """Used to delete data from Category table only if there are no employees under that Category"""
        Category_Id = self.Category_Id2.get()
        Product_No= self.Product_No2.get()

        my_var=tkinter.messagebox.askyesnocancel("Delete ?","Delete id:"+str(Product_No),icon='warning',default='no', parent = self.search_Category)
        try:
            if my_var: # True if yes button is clicked
                mycursor.execute("DELETE FROM Categories WHERE Product_No = " + Product_No)
                conn.commit()
                self.clear()
                tkinter.messagebox.showinfo("Success", "Successfully Deleted", parent = self.search_Category)
        except:
            tkinter.messagebox.showinfo("Warning", "Category is still assigned to some Products", parent = self.search_Category)


    def clear(self):
        """Refresh the search category window"""
        self.search_Category.destroy()
        self.searchCategory()

    def clear2(self):
        """Refresh the main window"""
        self.left.destroy()
        self.right.destroy()
        self.__init__(self.window)

# root = Tk()
# root.title("Location Details")
# b = Categories(root)
# root.geometry("1200x1200+0+0")
# root.mainloop()

