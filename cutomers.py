from tkinter import *
from tkinter import ttk
import mysql.connector
import tkinter.messagebox
from PIL import ImageTk, Image

#Establishing a connection with database
conn = mysql.connector.connect(host="localhost", user="root", password="root", database="grocerystore")
mycursor = conn.cursor()
class Customers():
    """This class is to perform operations on the customers table of our database"""
    def __init__(self, window):
        self.window = window
        self.left = Frame(window, width=2000, height=1600, bg="white")
        self.left.pack(side = LEFT)

        self.right = Frame(window, width = 10, height = 1600, bg = "white")
        self.right.pack(side = RIGHT)

        self.back_img = Image.open('customers_in1.png')
        # self.back_img = self.back_img.resize((1000, 1000), Image.ANTIALIAS)
        self.back_img1 = ImageTk.PhotoImage(self.back_img)
        self.background_label = Label(self.left, image=self.back_img1, compound = "right", bg = "white", fg = None)
        self.background_label.pack(side = "top", fill ="both")
        self.background_label.place(x=0, y=40, relwidth = 1, relheight = 1)

        self.heading = Label(self.left, text ="Customer Details", font=('arial 30 bold'), fg = 'HotPink4', bg = "white")
        self.heading.place(x = 200, y = 0)

        self.heading = Label(self.left, text ="Customer ID", font=('arial 10 bold'), fg = 'black',bg = "white")
        self.heading.place(x = 0, y = 100)

        self.heading = Label(self.left, text ="First Name", font=('arial 10 bold'), fg = 'black', bg = "white")
        self.heading.place(x = 0, y = 140)

        self.heading = Label(self.left, text ="Last Name", font=('arial 10 bold'), fg = 'black', bg = "white")
        self.heading.place(x = 0, y = 180)

        self.heading = Label(self.left, text ="Mobile", font=('arial 10 bold'), fg = 'black', bg = "white")
        self.heading.place(x = 0, y = 220)

        self.heading = Label(self.left, text ="Email", font=('arial 10 bold'), fg = 'black', bg = "white")
        self.heading.place(x = 0, y = 260)

        self.heading = Label(self.left, text ="Location ID", font=('arial 10 bold'), fg = 'black',bg = "white")
        self.heading.place(x = 0, y = 300)

        # Entries for all Labels
        self.cust_id = Entry(self.left, width = 30, bg = "ghost white")
        self.cust_id.place(x = 210, y = 100)

        self.FN = Entry(self.left, width = 30, bg = "ghost white")
        self.FN.place(x = 210, y = 140)

        self.LN = Entry(self.left, width = 30, bg = "ghost white")
        self.LN.place(x = 210, y = 180)

        self.phone = Entry(self.left, width = 30, bg = "ghost white")
        self.phone.place(x = 210, y = 220)

        self.email = Entry(self.left, width = 30, bg = "ghost white")
        self.email.place(x = 210, y = 260)

        self.loc_id = Entry(self.left, width = 30, bg = "ghost white")
        self.loc_id.place(x = 210, y = 300)

        # Submit Button
        self.submit = Button(self.left, text = "Add Customer", width = 15, height = 2, font=('arial 10 bold'),bg = "MistyRose3",fg = 'dark slate blue', command = self.add_customer)
        self.submit.place(x=100, y = 400)
        # Search Button
        self.search = Button(self.left, text = "Click to search", width = 15, height = 2,font=('arial 10 bold'),bg = "MistyRose3",fg = 'dark slate blue', command = self.searchCustomer)
        self.search.place(x = 250, y = 400)
        self.exit_now = Button(self.left, text = "Close", width = 15, height = 2,font=('arial 10 bold'),bg = "MistyRose3",fg = 'dark slate blue', command = self.window.destroy)
        self.exit_now.place(x = 390, y = 400)
        self.clear_now2 = Button(self.left, text ="Clear", width = 15, height = 2,font=('arial 10 bold'),bg = "MistyRose3",fg = 'dark slate blue', command = self.clear2)
        self.clear_now2.place(x = 550, y = 400)

    # Function to call when add new customer is clicked
    def add_customer(self):
        """This function is used to add new customer into the customer table of our Grocery Store Management system"""
        self.val1 = self.cust_id.get()
        self.val2 = self.FN.get()
        self.val3 = self.LN.get()
        self.val4 = self.phone.get()
        self.val5 = self.email.get()
        self.val6 = self.loc_id.get()

        if self.val1 == '' or self.val2 == '' or self.val3 =='' or self.val4 =='' or self.val5 =='' or self.val6 =='' :
            tkinter.messagebox.showinfo("Error", "Fill in all fields")
        else:
            query_loc = "INSERT INTO customers(Cust_ID, First_Name,Last_Name, Phone, Email, Location_Id) values(%s, %s, %s, %s, %s, %s) "
            values = (self.val1, self.val2, self.val3, self.val4, self.val5, self.val6)
            mycursor.execute(query_loc, values)
            conn.commit()
            self.clear2()
            tkinter.messagebox.showinfo("Success", "Successfully added", parent = self.left)
    def searchCustomer(self):
        """This function opens a new window, when the user clicks on the search button in the main window. It provides other options like edit as well."""
        self.search_customer = Tk()
        self.search_customer.title("Search Customer")
        self.search_customer.geometry("1600x1000")
        self.drop = ttk.Combobox(self.search_customer, value = ["Customer ID", "First Name", "Last Name", "Mobile", "Email", "Location ID"])
        self.drop.current(1)
        self.drop.place(x = 0, y = 50)
        self.search_box = Entry(self.search_customer)
        self.search_box.place(x = 150, y = 50)

        # Search button
        self.search_now = Button(self.search_customer, text = "Search Customer", width = 15, height = 2,font=('arial 10 bold'),bg = "light gray", command = self.searchNow)
        self.search_now.place(x = 100, y = 100)
        #Close button
        self.exit_now = Button(self.search_customer, text = "Close", width = 15, height = 2,font=('arial 10 bold'),bg = "light gray", command = self.search_customer.destroy)
        self.exit_now.place(x = 250, y = 100)
        #Edit button
        self.edit_now = Button(self.search_customer, text = "Change", width = 15, height = 2,font=('arial 10 bold'),bg = "light gray", command = self.editNow)
        self.edit_now.place(x = 400, y = 100)
        #Clear Button
        self.clear_now = Button(self.search_customer, text ="Clear", width = 15, height = 2,font=('arial 10 bold'),bg = "light gray", command = self.clear)
        self.clear_now.place(x = 550, y = 100)

    def searchNow(self):
        """This function helps us to search for any data in Customers table"""
        selected = self.drop.get()
        if selected == "DCustomer ID":
            sql_query = "SELECT * FROM customers WHERE Cust_ID=%s"
        elif selected == "First Name":
            sql_query = "SELECT * FROM customers WHERE First_Name=%s"
        elif selected == "Last Name":
            sql_query = "SELECT * FROM customers WHERE Last_Name=%s"
        elif selected == "Mobile":
            sql_query = "SELECT * FROM customers WHERE Phone=%s"
        elif selected == "Email":
            sql_query = "SELECT * FROM customers WHERE Email=%s"
        elif selected == "Location ID":
            sql_query = "SELECT * FROM customers WHERE Location_Id=%s"


        searched = self.search_box.get()
        name = (searched,)
        mycursor.execute(sql_query, name)
        searchResult = mycursor.fetchall()
        cols = ('Serial No', 'Customer Id' , 'First Name', 'Last Name', "Mobile", "Email", "Location ID")
        self.listBox = ttk.Treeview(self.search_customer, columns=cols, show = 'headings' )
        # set column headings
        for col in cols:
            self.listBox.heading(col, text=col)
        for i, (Cust_ID, First_Name, Last_Name, Phone, Email, Location_Id) in enumerate(searchResult, start=1):
            self.listBox.insert("", "end", values=(i, Cust_ID, First_Name, Last_Name, Phone, Email, Location_Id))
        self.listBox.place(x = 0, y = 200)
        if searchResult:
            child_id = self.listBox.get_children()[-1]
            val1 = self.listBox.focus(child_id)
            id = self.listBox.focus()
            self.id_item = self.listBox.item(id)
        self.listBox.bind("<<TreeviewSelect>>", self.onSelect)
        if not searchResult:
            searchResult = "Customer not found"
            searched_label = Label(self.search_customer, text = searchResult)
            searched_label.place(x = 0, y = 160)
    def editNow(self):
        """This function is called when we click on change button.We need to select the designation and then click on edit button.
            This function then provides us the option to update or delete"""
        try:
            if self.item_text:
                self.lcust_Id = Label(self.search_customer, text ="Customer Id", font=('arial 10 bold'), fg = 'black')
                self.lcust_Id.place(x = 0, y = 450)

                self.cust_Id2 = Entry(self.search_customer, width = 30)
                self.cust_Id2.place(x = 210, y = 450)
                self.cust_Id2.insert(0, self.item_text[1])
                self.cust_Id2.config(state=DISABLED)

                self.lFN = Label(self.search_customer, text ="First Name",font=('arial 10 bold'), fg = 'black')
                self.lFN.place(x = 0, y = 480)
                self.FN2 = Entry(self.search_customer, width = 30)
                self.FN2 .place(x = 210, y = 480)
                self.FN2 .insert(0, self.item_text[2])

                self.lLN = Label(self.search_customer ,text ="Last Name", font=('arial 10 bold'), fg = 'black')
                self.lLN.place(x = 0, y = 510)
                self.LN2 = Entry(self.search_customer, width = 30)
                self.LN2.place(x = 210, y = 510)
                self.LN2.insert(0, self.item_text[3])

                self.lmob = Label(self.search_customer ,text ="Mobile", font=('arial 10 bold'), fg = 'black')
                self.lmob.place(x = 0, y = 540)
                self.mob2 = Entry(self.search_customer, width = 30)
                self.mob2.place(x = 210, y = 540)
                self.mob2.insert(0, self.item_text[4])

                self.lemail = Label(self.search_customer ,text ="Email", font=('arial 10 bold'), fg = 'black')
                self.lemail.place(x = 0, y = 570)
                self.email2 = Entry(self.search_customer, width = 30)
                self.email2.place(x = 210, y = 570)
                self.email2.insert(0, self.item_text[5])

                self.lloc = Label(self.search_customer ,text ="Location ID", font=('arial 10 bold'), fg = 'black')
                self.lloc.place(x = 0, y = 600)
                self.loc2 = Entry(self.search_customer, width = 30)
                self.loc2.place(x = 210, y = 600)
                self.loc2.insert(0, self.item_text[6])


                self.update_now = Button(self.search_customer, text = "Update", width = 15, height = 2,font=('arial 10 bold'),bg = "light gray", command = self.updateNow)
                self.update_now.place(x = 70, y = 690)

                self.delete_now = Button(self.search_customer, text = "Delete", width = 15, height = 2,font=('arial 10 bold'),bg = "light gray", command = self.deleteNow)
                self.delete_now.place(x = 180, y = 690)

        except:
            tkinter.messagebox.showinfo("Warning", "Please select a customer to edit", parent = self.search_customer)

    def onSelect(self,event):
        """This function is used to get the selected item from the displayed list"""
        for item in self.listBox.selection():
            self.item_text = self.listBox.item(item,"values")

    def updateNow(self):
        """Used to update the customers table"""
        update_query = "Update customers set First_Name = %s, Last_Name = %s , Phone = %s, Email = %s, Location_Id = %s where Cust_ID = %s"
        cid = self.cust_Id2.get()
        F_N = self.FN2.get()
        L_N = self.LN2.get()
        mob = self.mob2.get()
        eml = self.email2.get()
        loc = self.loc2.get()

        inputs = (F_N, L_N, mob, eml, loc, cid)
        mycursor.execute(update_query, inputs)
        conn.commit()
        self.clear()
        tkinter.messagebox.showinfo("Success", "Successfully Updated", parent = self.search_customer)

    def deleteNow(self):
        """Used to delete data from customers table."""
        cid = self.cust_Id2.get()

        my_var=tkinter.messagebox.askyesnocancel("Delete ?","Delete id:"+str(cid),icon='warning',default='no', parent = self.search_customer)

        if my_var: # True if yes button is clicked
            mycursor.execute("DELETE FROM customers WHERE Cust_ID= " + cid )
            conn.commit()
            self.clear()
            tkinter.messagebox.showinfo("Success", "Successfully Deleted", parent = self.search_customer)



    def clear(self):
        """Refresh the search Designation window"""
        self.search_customer.destroy()
        self.searchCustomer()

    def clear2(self):
        """Refresh the main window"""
        self.left.destroy()
        self.right.destroy()
        self.__init__(self.window)

#root = Tk()
#root.title("Location Details")
#b = Location(root)
#root.geometry("1200x1200+0+0")
#root.mainloop()

