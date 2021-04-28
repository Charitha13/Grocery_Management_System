from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
import mysql.connector

#Establishing a connection with database
conn = mysql.connector.connect(host = "localhost", user = "root", password = "root", database = "grocerystore")
mycursor = conn.cursor()
class Manager:
    """This class is to perform operations on the manager table of our database"""
    def __init__(self, window):
        self.window = window
        self.left = Frame(window, width = 2000, height = 1200, bg = "white")
        self.left.pack(side = LEFT)

        self.right = Frame(window, width = 10, height = 1200, bg = "white")
        self.right.pack(side = RIGHT)

        self.back_img = Image.open('manager_in1.png')
        # self.back_img = self.back_img.resize((1000, 1000), Image.ANTIALIAS)
        self.back_img1 = ImageTk.PhotoImage(self.back_img)
        self.background_label = Label(self.left, image=self.back_img1, compound = "right", bg = "white", fg = None)
        self.background_label.pack(side = "right", fill ="both")
        self.background_label.place(x=250, y=-100, relwidth = 1, relheight = 1)

        self.heading = Label(self.left, text ="Managers Information",
                             font=('arial 30 bold'), fg = 'HotPink4',
                             bg = "white")
        self.heading.place(x = 200, y = 0)




        self.drop = ttk.Combobox(self.left, value = ["Employee ID", "Email", "All"])
        self.drop.current(0)
        self.drop.place(x = 0, y = 100)
        self.search_box = Entry(self.left, bg = "ghost white")
        self.search_box.place(x = 150, y = 100)
        # Search button
        self.search_now = Button(self.left, text = "Search Manager", width = 15, height = 2,font=('arial 10 bold'),bg = "light gray", command = self.searchNow)
        self.search_now.place(x = 100, y = 200)

        self.exit_now = Button(self.left, text = "Close", width = 15, height = 2,font=('arial 10 bold'),bg = "light gray", command = self.window.destroy)
        self.exit_now.place(x = 250, y = 200)
        self.clear_now2 = Button(self.left, text ="Clear", width = 15, height = 2,font=('arial 10 bold'),bg = "light gray", command = self.clear2)
        self.clear_now2.place(x = 390, y = 200)

        self.view_manager = Button(self.left, text ="Branch-Manager", width = 20, height = 2,font=('arial 10 bold'),bg = "light gray", command = self.viewManager)
        self.view_manager.place(x = 550, y = 200)



    def searchNow(self):
        """This function helps us to search for any data in table"""
        selected = self.drop.get()
        if selected == "Employee ID":
            sql_query = "SELECT * FROM manager WHERE E_Id=%s"
            searched = self.search_box.get()
            name = (searched,)
            mycursor.execute(sql_query, name)
        elif selected == "Email":
            sql_query = "SELECT * FROM manager WHERE Email=%s"
            searched = self.search_box.get()
            name = (searched,)
            mycursor.execute(sql_query, name)
        elif selected == "All":
            sql_query = "SELECT * FROM manager"
            mycursor.execute(sql_query)

        searchResult = mycursor.fetchall()
        #searchResult.sort(key=lambda e: e[1], reverse=True)
        cols = ('Serial No', 'E_Id', 'Mobile', 'Email')
        self.listBox = ttk.Treeview(self.left, columns=cols, show = 'headings' )
        # set column headings
        for col in cols:
            self.listBox.heading(col, text=col)
        for i, (EID, Mobile, Email) in enumerate(searchResult, start=1):
            self.listBox.insert("", "end", values=(i, EID, Mobile, Email))
        self.listBox.place(x = 0, y = 300)
        if searchResult:
            child_id = self.listBox.get_children()[-1]
            val1 = self.listBox.focus(child_id)
            id = self.listBox.focus()
            self.id_item = self.listBox.item(id)
        if not searchResult:
            searchResult = "Manager not found"
            searched_label = Label(self.left, text = searchResult)
            searched_label.place(x = 0, y = 260)


    def clear2(self):
        """Refresh the main window"""
        self.left.destroy()
        self.right.destroy()
        self.__init__(self.window)

    def viewManager(self):
        view_win = Tk()
        view_win.geometry("1250x300")
        # conn = mysql.connector.connect(host="localhost", user="root", password="root", database="grocerystore")
        # mycursor = conn.cursor()
        view_query = "SELECT * from Branch_Manager"
        mycursor.execute(view_query)
        view_result = mycursor.fetchall()

        view_cols = ('Serial No', 'First Name', 'Last Name', 'Street', 'City', 'Zipcode')
        self.listBox2 = ttk.Treeview(view_win, columns=view_cols, show = 'headings' )
        # set column headings
        for col in view_cols:
            self.listBox2.heading(col, text=col)
        for i, (First_Name, Last_Name, Street, City, Zipcode) in enumerate(view_result, start=1):
            self.listBox2.insert("", "end", values=(i, First_Name, Last_Name, Street, City, Zipcode))

        self.listBox2.place(x = 10, y = 50)

        view_win.mainloop()

# root = Tk()
# root.title("Manager Details")
# b = Manager(root)
# root.geometry("1200x1200+0+0")
# root.mainloop()

