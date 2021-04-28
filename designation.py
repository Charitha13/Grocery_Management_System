from tkinter import *
from tkinter import ttk
import mysql.connector
import tkinter.messagebox
from PIL import ImageTk, Image

#Establishing a connection with database
conn = mysql.connector.connect(host="localhost", user="root", password="root", database="grocerystore")
mycursor = conn.cursor()
class Designation():
    """This class is to perform operations on the designation table of our database"""
    def __init__(self, window):
        self.window = window
        self.left = Frame(window, width=2000, height=1600, bg="white")
        self.left.pack(side = LEFT)

        self.right = Frame(window, width = 10, height = 1600, bg = "white")
        self.right.pack(side = RIGHT)

        self.back_img = Image.open('roles_in1.png')
        self.back_img = self.back_img.resize((750, 400), Image.ANTIALIAS)
        self.back_img1 = ImageTk.PhotoImage(self.back_img)
        self.background_label = Label(self.left, image=self.back_img1, compound = "right", bg = "white", fg = None)
        self.background_label.pack(side = "top", fill ="both")
        self.background_label.place(x=280, y=-40, relwidth = 1, relheight = 1)

        self.heading = Label(self.left, text ="Employees Designation Details", font=('arial 30 bold'), fg = 'HotPink4', bg = "white")
        self.heading.place(x = 200, y = 0)

        self.heading = Label(self.left, text ="Designation ID", font=('arial 10 bold'), fg = 'black',bg = "white")
        self.heading.place(x = 0, y = 100)

        self.heading = Label(self.left, text ="Designation", font=('arial 10 bold'), fg = 'black', bg = "white")
        self.heading.place(x = 0, y = 140)

        self.heading = Label(self.left, text ="Salary", font=('arial 10 bold'), fg = 'black', bg = "white")
        self.heading.place(x = 0, y = 180)

        # Entries for all Labels
        self.dsgn_id = Entry(self.left, width = 30, bg = "ghost white")
        self.dsgn_id.place(x = 210, y = 100)

        self.dsgn = Entry(self.left, width = 30, bg = "ghost white")
        self.dsgn.place(x = 210, y = 140)

        self.salary = Entry(self.left, width = 30, bg = "ghost white")
        self.salary.place(x = 210, y = 180)

        # Submit Button
        self.submit = Button(self.left, text = "Add Designation", width = 15, height = 2, font=('arial 10 bold'),bg = "MistyRose3",fg = 'dark slate blue', command = self.add_designation)
        self.submit.place(x=100, y = 400)
        # Search Button
        self.search = Button(self.left, text = "Click to search", width = 15, height = 2,font=('arial 10 bold'),bg = "MistyRose3",fg = 'dark slate blue', command = self.searchDesignation)
        self.search.place(x = 250, y = 400)
        self.exit_now = Button(self.left, text = "Close", width = 15, height = 2,font=('arial 10 bold'),bg = "MistyRose3",fg = 'dark slate blue', command = self.window.destroy)
        self.exit_now.place(x = 390, y = 400)
        self.clear_now2 = Button(self.left, text ="Clear", width = 15, height = 2,font=('arial 10 bold'),bg = "MistyRose3",fg = 'dark slate blue', command = self.clear2)
        self.clear_now2.place(x = 550, y = 400)

    # Function to call when add new designation is clicked
    def add_designation(self):
        """This function is usedto add new designation into the designation table of our Grocery Store Management system"""
        self.val1 = self.dsgn_id.get()
        self.val2 = self.dsgn.get()
        self.val3 = self.salary.get()

        if self.val1 == '' or self.val2 == '' or self.val3 =='' :
            tkinter.messagebox.showinfo("Error", "Fill in all fields")
        else:
            query_loc = "INSERT INTO designation(Dsgn_Id, Designation, Salary) values(%s, %s, %s) "
            values = (self.val1, self.val2, self.val3)
            mycursor.execute(query_loc, values)
            conn.commit()
            self.clear2()
            tkinter.messagebox.showinfo("Success", "Successfully added", parent = self.left)
    def searchDesignation(self):
        """This function opens a new window, when the user clicks on the search button in the main window. It provides other options like edit as well."""
        self.search_designation = Tk()
        self.search_designation.title("Search Designation")
        self.search_designation.geometry("1600x1000")
        self.drop = ttk.Combobox(self.search_designation, value = ["Designation ID", "Designation"])
        self.drop.current(1)
        self.drop.place(x = 0, y = 50)
        self.search_box = Entry(self.search_designation)
        self.search_box.place(x = 150, y = 50)

        # Search button
        self.search_now = Button(self.search_designation, text = "Search Designation", width = 15, height = 2,font=('arial 10 bold'),bg = "light gray", command = self.searchNow)
        self.search_now.place(x = 100, y = 100)
        #Close button
        self.exit_now = Button(self.search_designation, text = "Close", width = 15, height = 2,font=('arial 10 bold'),bg = "light gray", command = self.search_designation.destroy)
        self.exit_now.place(x = 250, y = 100)
        #Edit button
        self.edit_now = Button(self.search_designation, text = "Change", width = 15, height = 2,font=('arial 10 bold'),bg = "light gray", command = self.editNow)
        self.edit_now.place(x = 400, y = 100)
        #Clear Button
        self.clear_now = Button(self.search_designation, text ="Clear", width = 15, height = 2,font=('arial 10 bold'),bg = "light gray", command = self.clear)
        self.clear_now.place(x = 550, y = 100)

    def searchNow(self):
        """This function helps us to search for any data in Designation table"""
        selected = self.drop.get()
        if selected == "Designation ID":
            sql_query = "SELECT * FROM designation WHERE Dsgn_Id=%s"
        elif selected == "Designation":
            sql_query = "SELECT * FROM designation WHERE Designation=%s"


        searched = self.search_box.get()
        name = (searched,)
        mycursor.execute(sql_query, name)
        searchResult = mycursor.fetchall()
        cols = ('Serial No', 'Designation_Id' , 'Designation', 'Salary')
        self.listBox = ttk.Treeview(self.search_designation, columns=cols, show = 'headings' )
        # set column headings
        for col in cols:
            self.listBox.heading(col, text=col)
        for i, (Dsgn_Id, Designation, Salary) in enumerate(searchResult, start=1):
            self.listBox.insert("", "end", values=(i, Dsgn_Id, Designation, Salary))
        self.listBox.place(x = 0, y = 200)
        if searchResult:
            child_id = self.listBox.get_children()[-1]
            val1 = self.listBox.focus(child_id)
            id = self.listBox.focus()
            self.id_item = self.listBox.item(id)
        self.listBox.bind("<<TreeviewSelect>>", self.onSelect)
        if not searchResult:
            searchResult = "Designation not found"
            searched_label = Label(self.search_designation, text = searchResult)
            searched_label.place(x = 0, y = 160)
    def editNow(self):
        """This function is called when we click on change button.We need to select the designation and then click on edit button.
            This function then provides us the option to update or delete"""
        try:
            if self.item_text:
                self.ldsgn_Id = Label(self.search_designation, text ="Designation_Id",
                             font=('arial 10 bold'), fg = 'black')
                self.ldsgn_Id.place(x = 0, y = 450)
                self.dsgn_Id2 = Entry(self.search_designation, width = 30)
                self.dsgn_Id2.place(x = 210, y = 450)
                self.dsgn_Id2.insert(0, self.item_text[1])
                self.dsgn_Id2.config(state=DISABLED)
                self.ldesignation = Label(self.search_designation, text ="Designation",font=('arial 10 bold'), fg = 'black')
                self.ldesignation.place(x = 0, y = 480)
                self.designation2 = Entry(self.search_designation, width = 30)
                self.designation2 .place(x = 210, y = 480)
                self.designation2 .insert(0, self.item_text[2])

                self.lsalary = Label(self.search_designation ,text ="Salary",
                             font=('arial 10 bold'), fg = 'black')
                self.lsalary.place(x = 0, y = 510)

                self.salary2 = Entry(self.search_designation, width = 30)
                self.salary2.place(x = 210, y = 510)
                self.salary2.insert(0, self.item_text[3])



                self.update_now = Button(self.search_designation, text = "Update", width = 15, height = 2,font=('arial 10 bold'),bg = "light gray", command = self.updateNow)
                self.update_now.place(x = 70, y = 690)

                self.delete_now = Button(self.search_designation, text = "Delete", width = 15, height = 2,font=('arial 10 bold'),bg = "light gray", command = self.deleteNow)
                self.delete_now.place(x = 180, y = 690)

        except:
            tkinter.messagebox.showinfo("Warning", "Please select a designation to edit", parent = self.search_designation)

    def onSelect(self,event):
        """This function is used to get the selected item from the displayed list"""
        for item in self.listBox.selection():
            self.item_text = self.listBox.item(item,"values")

    def updateNow(self):
        """Used to update the Designation table"""
        update_query = "Update designation set Designation = %s, Salary = %s where Dsgn_Id = %s"
        d_id = self.dsgn_Id2.get()
        dsg = self.designation2.get()
        sal = self.salary2.get()

        inputs = (dsg, sal, d_id)
        mycursor.execute(update_query, inputs)
        conn.commit()
        tkinter.messagebox.showinfo("Success", "Successfully Updated", parent = self.search_designation)

    def deleteNow(self):
        """Used to delete data from Designation table only if there are no employees under that designation"""
        d_id = self.dsgn_Id2.get()

        my_var=tkinter.messagebox.askyesnocancel("Delete ?","Delete id:"+str(d_id),icon='warning',default='no', parent = self.search_designation)
        try:
            if my_var: # True if yes button is clicked
                mycursor.execute("DELETE FROM designation WHERE Dsgn_Id= " + "\"" + d_id + "\"" )
                conn.commit()
                self.clear()
                tkinter.messagebox.showinfo("Success", "Successfully Deleted", parent = self.search_designation)
        except:
            tkinter.messagebox.showinfo("Warning", "Designation is still assigned to some Employees", parent = self.search_designation)


    def clear(self):
        """Refresh the search Designation window"""
        self.search_designation.destroy()
        self.searchDesignation()

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

