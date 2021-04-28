from tkinter import *
from tkinter import ttk
import mysql.connector
import tkinter.messagebox
from PIL import ImageTk, Image

#Establishing a connection with database
conn = mysql.connector.connect(host = "localhost", user = "root", password = "root", database = "grocerystore")
mycursor = conn.cursor()
class Employees:
    """This class is to perform operations on the employees table of our database"""
    def __init__(self, window):
        self.window = window
        self.left = Frame(window, width = 2000, height = 1200, bg = "white")
        self.left.pack(side = LEFT)

        self.right = Frame(window, width = 10, height = 1200, bg = "white")
        self.right.pack(side = RIGHT)

        self.back_img = Image.open('employees_in1.png')
        # self.back_img = self.back_img.resize((810, 429), Image.ANTIALIAS)
        self.back_img1 = ImageTk.PhotoImage(self.back_img)
        self.background_label = Label(self.left, image=self.back_img1, compound = "right", bg = "white", fg = None)
        self.background_label.pack(side = "top", fill ="both")
        self.background_label.place(x=250, y=-50, relwidth = 1, relheight = 1)

        self.heading = Label(self.left, text ="Store Employees Information",
                             font=('arial 35 bold italic'), fg = 'HotPink4',
                             bg = "white")
        self.heading.place(x = 300, y = 0)

        self.heading = Label(self.left, text ="Employee First Name",
                             font=('arial 10 bold'), fg = 'black',
                             bg = "white")
        self.heading.place(x = 0, y = 100)

        self.heading = Label(self.left, text ="Employee Last Name",
                             font=('arial 10 bold'), fg = 'black',
                             bg = "white")
        self.heading.place(x = 0, y = 140)

        self.heading = Label(self.left, text ="Location ID",
                             font=('arial 10 bold'), fg = 'black',
                             bg = "white")
        self.heading.place(x = 0, y = 180)

        self.heading = Label(self.left, text ="Email",
                             font=('arial 10 bold'), fg = 'black',
                             bg = "white")
        self.heading.place(x = 0, y = 220)

        self.heading = Label(self.left, text ="Mobile",
                             font=('arial 10 bold'), fg = 'black',
                             bg = "white")
        self.heading.place(x = 0, y = 260)

        self.heading = Label(self.left, text ="Employee ID",font=('arial 10 bold'), fg = 'black',bg = "white")
        self.heading.place(x = 0, y = 300)
        self.heading = Label(self.left, text ="Designation ID",font=('arial 10 bold'), fg = 'black',bg = "white")
        self.heading.place(x = 0, y = 340)

        # Entries for all Labels
        self.first_name = Entry(self.left, width = 30,bg = "ghost white")
        self.first_name.place(x = 210, y = 100)

        self.last_name = Entry(self.left, width = 30, bg = "ghost white")
        self.last_name.place(x = 210, y = 140)

        self.loc_id = Entry(self.left, width = 30, bg = "ghost white")
        self.loc_id.place(x = 210, y = 180)

        self.email = Entry(self.left, width = 30, bg = "ghost white")
        self.email.place(x = 210, y = 220)

        self.mobile = Entry(self.left, width = 30, bg = "ghost white")
        self.mobile.place(x = 210, y = 260)

        self.e_id = Entry(self.left, width = 30, bg = "ghost white")
        self.e_id.place(x = 210, y = 300)

        self.dsgn_id = Entry(self.left, width = 30, bg = "ghost white")
        self.dsgn_id.place(x = 210, y = 340)

        # Submit Button
        self.submit = Button(self.left, text = "Add Employee", width = 15, height = 2, font=('arial 10 bold'),bg = "light gray", command = self.add_employee)
        self.submit.place(x=100, y = 400)
        # Search Button
        self.search = Button(self.left, text = "Click to search", width = 15, height = 2,font=('arial 10 bold'),bg = "light gray", command = self.searchEmployee)
        self.search.place(x = 250, y = 400)
        self.exit_now = Button(self.left, text = "Close", width = 15, height = 2,font=('arial 10 bold'),bg = "light gray", command = self.window.destroy)
        self.exit_now.place(x = 390, y = 400)
        self.clear_now2 = Button(self.left, text ="Clear", width = 15, height = 2,font=('arial 10 bold'),bg = "light gray", command = self.clear2)
        self.clear_now2.place(x = 550, y = 400)
    # Function to call when add employee is clicked
    def add_employee(self):
        """This function is used add employees into the Employees table of our Grocery Store Management system"""
        self.val1 = self.first_name.get()
        self.val2 = self.last_name.get()
        self.val3 = self.loc_id.get()
        self.val4 = self.email.get()
        self.val5 = self.mobile.get()
        self.val6 = self.e_id.get()
        self.val7 = self.dsgn_id.get()

        if self.val1 == '' or self.val2 == '' or self.val3 =='' or self.val4 =='' or self.val5 =='' or self.val6 =='' or self.val7 =='':
            tkinter.messagebox.showinfo("Error", "Fill in all fields")
        else:
            query = "INSERT INTO employees(Location_ID , Email, Mobile , First_Name , Last_Name , E_Id , Dsgn_Id ) values(%s, %s, %s, %s, %s, %s, %s) "
            values = (self.val3, self.val4, self.val5, self.val1, self.val2, self.val6, self.val7)
            mycursor.execute(query, values)
            conn.commit()
            self.clear2()
            tkinter.messagebox.showinfo("Success", "Successfully added", parent = self.left)
    def searchEmployee(self):
        """This function opens a new window, when the user clicks on the search button in the main window. It provides other options like edit as well."""
        self.search_employees = Tk()
        self.search_employees.title("Search Employees")
        self.search_employees.geometry("1600x1000")
        #self.search_label = Label(self.search_employees, text = "Employee Last Name",font=('arial 10 bold'))
        #self.search_label.place(x = 0, y = 50)
        self.drop = ttk.Combobox(self.search_employees, value = ["Last Name", "First Name", "Employee ID","Dsgn ID", "Loc ID"])
        self.drop.current(0)
        self.drop.place(x = 0, y = 50)
        self.search_box = Entry(self.search_employees)
        self.search_box.place(x = 150, y = 50)
        # Search button
        self.search_now = Button(self.search_employees, text = "Search Employee", width = 15, height = 2,font=('arial 10 bold'),bg = "light gray", command = self.searchNow)
        self.search_now.place(x = 100, y = 100)
        #close button
        self.exit_now = Button(self.search_employees, text = "Close", width = 15, height = 2,font=('arial 10 bold'),bg = "light gray", command = self.search_employees.destroy)
        self.exit_now.place(x = 250, y = 100)
        #Edit button
        self.edit_now = Button(self.search_employees, text = "Change", width = 15, height = 2,font=('arial 10 bold'),bg = "light gray", command = self.editNow)
        self.edit_now.place(x = 400, y = 100)
        #Clear button
        self.clear_now = Button(self.search_employees, text ="Clear", width = 15, height = 2,font=('arial 10 bold'),bg = "light gray", command = self.clear)
        self.clear_now.place(x = 550, y = 100)

    def searchNow(self):
        """This function helps us to search for any data in Employees table"""
        selected = self.drop.get()
        if selected == "Last Name":
            sql_query = "SELECT * FROM employees WHERE Last_Name=%s"
        elif selected == "First Name":
            sql_query = "SELECT * FROM employees WHERE First_Name=%s"
        elif selected == "Employee ID":
            sql_query = "SELECT * FROM employees WHERE E_Id=%s"
        elif selected == "Dsgn ID":
            sql_query = "SELECT * FROM employees WHERE Dsgn_Id=%s"
        elif selected == "Loc ID":
            sql_query = "SELECT * FROM employees WHERE Location_ID=%s"

        searched = self.search_box.get()
        name = (searched,)
        mycursor.execute(sql_query, name)
        searchResult = mycursor.fetchall()
        #searchResult.sort(key=lambda e: e[1], reverse=True)
        cols = ('Serial No', 'Location_Id', 'Email', 'Mobile', 'First Name', 'Last Name', 'E_Id', 'Dsgn_Id')
        self.listBox = ttk.Treeview(self.search_employees, columns=cols, show = 'headings' )
        # set column headings
        for col in cols:
            self.listBox.heading(col, text=col)
        for i, (location, Email, Mobile, LName, FName, EID, DsID) in enumerate(searchResult, start=1):
            self.listBox.insert("", "end", values=(i, location, Email, Mobile, LName, FName, EID, DsID))
        self.listBox.place(x = 0, y = 200)
        if searchResult:
            #child_id = self.listBox.get_children()[-1]
            #val1 = self.listBox.focus(child_id)
            id = self.listBox.focus()
            self.id_item = self.listBox.item(id)
        self.listBox.bind("<<TreeviewSelect>>", self.onSelect)
        if not searchResult:
            searchResult = "Employee not found"
            searched_label = Label(self.search_employees, text = searchResult)
            searched_label.place(x = 0, y = 160)
    def editNow(self):
        """This function is called when we click on change button.We need to select the employee and click on edit button.
        This function then provides us the option to update or delete"""
        try:
            if self.item_text:
                self.lfirst_name2 = Label(self.search_employees, text ="First name",
                             font=('arial 10 bold'), fg = 'black')
                self.lfirst_name2.place(x = 0, y = 450)
                self.first_name2 = Entry(self.search_employees, width = 30)
                self.first_name2.place(x = 210, y = 450)
                self.first_name2.insert(0, self.item_text[4])
                self.llast_name2 = Label(self.search_employees, text ="Last name",
                             font=('arial 10 bold'), fg = 'black')
                self.llast_name2.place(x = 0, y = 480)
                self.last_name2 = Entry(self.search_employees, width = 30)
                self.last_name2.place(x = 210, y = 480)
                self.last_name2.insert(0, self.item_text[5])

                self.lloc_id2 = Label(self.search_employees, text ="Location ID",
                             font=('arial 10 bold'), fg = 'black')
                self.lloc_id2.place(x = 0, y = 510)

                self.loc_id2 = Entry(self.search_employees, width = 30)
                self.loc_id2.place(x = 210, y = 510)
                self.loc_id2.insert(0, self.item_text[1])

                self.lemail2 = Label(self.search_employees, text ="Email",
                             font=('arial 10 bold'), fg = 'black')
                self.lemail2.place(x = 0, y = 540)
                self.email2 = Entry(self.search_employees, width = 30)
                self.email2.place(x = 210, y = 540)
                self.email2.insert(0, self.item_text[2])

                self.lmobile2 = Label(self.search_employees, text ="Mobile",
                             font=('arial 10 bold'), fg = 'black')
                self.lmobile2.place(x = 0, y = 570)
                self.mobile2 = Entry(self.search_employees, width = 30)
                self.mobile2.place(x = 210, y = 570)
                self.mobile2.insert(0, self.item_text[3])
                self.le_id2 = Label(self.search_employees, text ="Employee ID",
                             font=('arial 10 bold'), fg = 'black')
                self.le_id2.place(x = 0, y = 600)

                self.e_id2 = Entry(self.search_employees, width = 30)
                self.e_id2.place(x = 210, y = 600)
                self.e_id2.insert(0, self.item_text[6])
                self.e_id2.config(state=DISABLED)

                self.ldsgn_id2 = Label(self.search_employees, text ="Designation ID",
                             font=('arial 10 bold'), fg = 'black')
                self.ldsgn_id2.place(x = 0, y = 630)
                self.dsgn_id2 = Entry(self.search_employees, width = 30)
                self.dsgn_id2.place(x = 210, y = 630)
                self.dsgn_id2.insert(0, self.item_text[7])

                self.update_now = Button(self.search_employees, text = "Update", width = 15, height = 2,font=('arial 10 bold'),bg = "light gray", command = self.updateNow)
                self.update_now.place(x = 70, y = 690)

                self.delete_now = Button(self.search_employees, text = "Delete", width = 15, height = 2,font=('arial 10 bold'),bg = "light gray", command = self.deleteNow)
                self.delete_now.place(x = 180, y = 690)

        except:
            tkinter.messagebox.showinfo("Warning", "Please select an Employee to edit", parent = self.search_employees)

    def onSelect(self,event):
        """This function is used to get the selected item from the displayed list"""
        for item in self.listBox.selection():
            self.item_text = self.listBox.item(item,"values")

    def updateNow(self):
        """Used to update the Employees table"""
        update_query = "Update employees set Location_ID = %s, Email = %s, Mobile = %s, First_Name = %s, Last_Name = %s, Dsgn_Id = %s WHERE E_Id = %s"
        FN = self.first_name2.get()
        LN = self.last_name2.get()
        LOC = self.loc_id2.get()
        Email1 = self.email2.get()
        Mob = self.mobile2.get()
        eid = self.e_id2.get()
        dsgn = self.dsgn_id2.get()
        inputs = (LOC, Email1, Mob, FN, LN, dsgn, eid)
        mycursor.execute(update_query, inputs)
        conn.commit()
        self.clear()
        tkinter.messagebox.showinfo("Success", "Successfully Updated", parent = self.search_employees)

    def deleteNow(self):
        """Used to delete data from employees table"""
        eid = self.e_id2.get()
        my_var=tkinter.messagebox.askyesnocancel("Delete ?","Delete id:"+str(eid),icon='warning',default='no', parent = self.search_employees)
        if my_var: # True if, yes button is clicked
            #print("delete")
            mycursor.execute("DELETE FROM employees WHERE E_id=" + eid )
            conn.commit()
            self.clear()
            tkinter.messagebox.showinfo("Success", "Successfully Deleted", parent = self.search_employees)

    def clear(self):
        """Refresh the search Employees window"""
        self.search_employees.destroy()
        self.searchEmployee()

    def clear2(self):
        """Refresh the main window"""
        self.left.destroy()
        self.right.destroy()
        self.__init__(self.window)

#root = Tk()
#root.title("Employee Details")
#b = Employees(root)
#root.geometry("1200x1200+0+0")
#root.mainloop()

