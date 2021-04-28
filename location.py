from tkinter import *
from tkinter import ttk
import mysql.connector
import tkinter.messagebox
from PIL import ImageTk, Image

#Establishing a connection with database
conn = mysql.connector.connect(host="localhost", user="root", password="root", database="grocerystore")
mycursor = conn.cursor()
class Location():
    """This class is to perform operations on the location table of our database"""
    def __init__(self, window):
        self.window = window
        self.left = Frame(window, width=2000, height=1600, bg="white")
        self.left.pack(side = LEFT)

        self.right = Frame(window, width = 10, height = 1600, bg = "white")
        self.right.pack(side = RIGHT)

        self.back_img = Image.open('locations_in1.png')
        self.back_img = self.back_img.resize((640, 500), Image.ANTIALIAS)
        self.back_img1 = ImageTk.PhotoImage(self.back_img)
        self.background_label = Label(self.left, image=self.back_img1, compound = "right", bg = "white", fg = None)
        self.background_label.pack(side = "top", fill ="both")
        self.background_label.place(x=250, y=-40, relwidth = 1, relheight = 1)

        self.heading = Label(self.left, text ="Store Location Information", font=('arial 30 bold'), fg = 'HotPink4', bg = "white")
        self.heading.place(x = 200, y = 0)

        self.heading = Label(self.left, text ="Location ID", font=('arial 10 bold'), fg = 'black',bg = "white")
        self.heading.place(x = 0, y = 100)

        self.heading = Label(self.left, text ="Zipcode", font=('arial 10 bold'), fg = 'black', bg = "white")
        self.heading.place(x = 0, y = 140)

        self.heading = Label(self.left, text ="City", font=('arial 10 bold'), fg = 'black', bg = "white")
        self.heading.place(x = 0, y = 180)

        self.heading = Label(self.left, text ="Street", font=('arial 10 bold'), fg = 'black', bg = "white")
        self.heading.place(x = 0, y = 220)

        # Entries for all Labels
        self.location_id = Entry(self.left, width = 30, bg = "ghost white")
        self.location_id.place(x = 210, y = 100)

        self.zipcode = Entry(self.left, width = 30, bg = "ghost white")
        self.zipcode.place(x = 210, y = 140)

        self.city = Entry(self.left, width = 30, bg = "ghost white")
        self.city.place(x = 210, y = 180)

        self.street = Entry(self.left, width = 30, bg = "ghost white")
        self.street.place(x = 210, y = 220)

        # Submit Button
        self.submit = Button(self.left, text = "Add Location", width = 15, height = 2, font=('arial 10 bold'),bg = "light gray", command = self.add_location)
        self.submit.place(x=100, y = 400)
        # Search Button
        self.search = Button(self.left, text = "Click to search", width = 15, height = 2,font=('arial 10 bold'),bg = "light gray", command = self.searchLocation)
        self.search.place(x = 250, y = 400)
        self.exit_now = Button(self.left, text = "Close", width = 15, height = 2,font=('arial 10 bold'),bg = "light gray", command = self.window.destroy)
        self.exit_now.place(x = 390, y = 400)
        self.clear_now2 = Button(self.left, text ="Clear", width = 15, height = 2,font=('arial 10 bold'),bg = "light gray", command = self.clear2)
        self.clear_now2.place(x = 550, y = 400)

    # Function to call when add location is clicked
    def add_location(self):
        """This function is used add new location into the Location table of our Grocery Store Management system"""
        self.val1 = self.location_id.get()
        self.val2 = self.zipcode.get()
        self.val3 = self.city.get()
        self.val4 = self.street.get()

        if self.val1 == '' or self.val2 == '' or self.val3 =='' or self.val4 =='' :
            tkinter.messagebox.showinfo("Error", "Fill in all fields")
        else:
            query_loc = "INSERT INTO location(Location_Id , Zipcode, City , Street) values(%s, %s, %s, %s) "
            values = (self.val1, self.val2, self.val3, self.val4)
            mycursor.execute(query_loc, values)
            conn.commit()
            self.clear2()
            tkinter.messagebox.showinfo("Success", "Successfully added", parent = self.left)
    def searchLocation(self):
        """This function opens a new window, when the user clicks on the search button in the main window. It provides other options like edit as well."""
        self.search_location = Tk()
        self.search_location.title("Search Location")
        self.search_location.geometry("1600x1000")
        self.drop = ttk.Combobox(self.search_location, value = ["Location ID", "Zipcode", "City", "Street"])
        self.drop.current(0)
        self.drop.place(x = 0, y = 50)
        self.search_box = Entry(self.search_location)
        self.search_box.place(x = 150, y = 50)

        # Search button
        self.search_now = Button(self.search_location, text = "Search Location", width = 15, height = 2,font=('arial 10 bold'),bg = "light gray", command = self.searchNow)
        self.search_now.place(x = 100, y = 100)
        #Close button
        self.exit_now = Button(self.search_location, text = "Close", width = 15, height = 2,font=('arial 10 bold'),bg = "light gray", command = self.search_location.destroy)
        self.exit_now.place(x = 250, y = 100)
        #Edit button
        self.edit_now = Button(self.search_location, text = "Change", width = 15, height = 2,font=('arial 10 bold'),bg = "light gray", command = self.editNow)
        self.edit_now.place(x = 400, y = 100)
        #Clear Button
        self.clear_now = Button(self.search_location, text ="Clear", width = 15, height = 2,font=('arial 10 bold'),bg = "light gray", command = self.clear)
        self.clear_now.place(x = 550, y = 100)

    def searchNow(self):
        """This function helps us to search for any data in Location table"""
        selected = self.drop.get()
        if selected == "Location ID":
            sql_query = "SELECT * FROM location WHERE Location_Id=%s"
        elif selected == "Zipcode":
            sql_query = "SELECT * FROM location WHERE Zipcode=%s"
        elif selected == "City":
            sql_query = "SELECT * FROM location WHERE City=%s"
        elif selected == "Street":
            sql_query = "SELECT * FROM location WHERE Street=%s"

        searched = self.search_box.get()
        name = (searched,)
        mycursor.execute(sql_query, name)
        searchResult = mycursor.fetchall()

        #searchResult.sort(key=lambda e: e[1], reverse=True)
        cols = ('Serial No', 'Location_Id' , 'Zipcode', 'City' , 'Street')
        self.listBox = ttk.Treeview(self.search_location, columns=cols, show = 'headings' )
        # set column headings
        for col in cols:
            self.listBox.heading(col, text=col)
        for i, (Location_Id, Zipcode, City, Street) in enumerate(searchResult, start=1):
            self.listBox.insert("", "end", values=(i, Location_Id, Zipcode, City, Street))
        self.listBox.place(x = 0, y = 200)
        if searchResult:
            child_id = self.listBox.get_children()[-1]
            val1 = self.listBox.focus(child_id)
            #print("val1 is ", val1)
            id = self.listBox.focus()
            self.id_item = self.listBox.item(id)
        self.listBox.bind("<<TreeviewSelect>>", self.onSelect)
        if not searchResult:
            searchResult = "Location not found"
            searched_label = Label(self.search_location, text = searchResult)
            searched_label.place(x = 0, y = 160)
    def editNow(self):
        """This function is called when we click on change button.We need to select the location and then click on edit button.
            This function then provides us the option to update or delete"""
        try:
            if self.item_text:
                self.llocation = Label(self.search_location, text ="Location_Id", font=('arial 10 bold'), fg = 'black')
                self.llocation.place(x = 0, y = 450)
                self.location2 = Entry(self.search_location, width = 30)
                self.location2.place(x = 210, y = 450)
                self.location2.insert(0, self.item_text[1])
                self.location2.config(state=DISABLED)
                self.lzipcode = Label(self.search_location, text ="Zipcode",font=('arial 10 bold'), fg = 'black')
                self.lzipcode.place(x = 0, y = 480)
                self.zipcode2 = Entry(self.search_location, width = 30)
                self.zipcode2.place(x = 210, y = 480)
                self.zipcode2.insert(0, self.item_text[2])

                self.lcity = Label(self.search_location ,text ="City",
                             font=('arial 10 bold'), fg = 'black')
                self.lcity.place(x = 0, y = 510)

                self.city2 = Entry(self.search_location, width = 30)
                self.city2.place(x = 210, y = 510)
                self.city2.insert(0, self.item_text[3])

                self.lstreet = Label(self.search_location, text ="Street",
                             font=('arial 10 bold'), fg = 'black')
                self.lstreet.place(x = 0, y = 540)
                self.street2 = Entry(self.search_location, width = 30)
                self.street2.place(x = 210, y = 540)
                self.street2.insert(0, self.item_text[4])

                self.update_now = Button(self.search_location, text = "Update", width = 15, height = 2,font=('arial 10 bold'),bg = "light gray", command = self.updateNow)
                self.update_now.place(x = 70, y = 690)

                self.delete_now = Button(self.search_location, text = "Delete", width = 15, height = 2,font=('arial 10 bold'),bg = "light gray", command = self.deleteNow)
                self.delete_now.place(x = 180, y = 690)

        except:
            tkinter.messagebox.showinfo("Warning", "Please select a Location to edit", parent = self.search_location)

    def onSelect(self,event):
        """This function is used to get the selected item from the displayed list"""

        for item in self.listBox.selection():
            self.item_text = self.listBox.item(item,"values")

    def updateNow(self):
        """Used to update the Location table"""
        update_query = "Update location set Zipcode = %s, City = %s, Street = %s where Location_Id = %s"
        loc = self.location2.get()
        zip = self.zipcode2.get()
        city = self.city2.get()
        street = self.street2.get()

        inputs = (zip, city, street,loc)
        mycursor.execute(update_query, inputs)
        conn.commit()
        self.clear()
        tkinter.messagebox.showinfo("Success", "Successfully Updated", parent = self.search_location)

    def deleteNow(self):
        """Used to delete data from Location table only if there are no employees working in that location"""
        loc_id = self.location2.get()

        my_var=tkinter.messagebox.askyesnocancel("Delete ?","Delete id:"+str(loc_id),icon='warning',default='no', parent = self.search_location)
        try:
            if my_var: # True if yes button is clicked
                mycursor.execute("DELETE FROM location WHERE Location_Id= " + "\"" + loc_id + "\"" )
                conn.commit()
                self.clear()
                tkinter.messagebox.showinfo("Success", "Successfully Deleted", parent = self.search_location)
        except:
            tkinter.messagebox.showinfo("Warning", "Employees are still working in this location", parent = self.search_location)


    def clear(self):
        """Refresh the search Location window"""
        self.search_location.destroy()
        self.searchLocation()

    def clear2(self):
        """Refresh the main window"""
        self.left.destroy()
        self.right.destroy()
        self.__init__(self.window)

# root = Tk()
# root.title("Location Details")
# b = Location(root)
# root.geometry("1200x1200+0+0")
# root.mainloop()

