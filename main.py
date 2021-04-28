# Main module to call all the other Grocery Store Management related GUI's
from tkinter import *
import employees as ee
import location as loc
import designation as dg
import cutomers as cust
import commodities as comm
import Categories as cat
import suppliers as suppl
import manager as mg
from PIL import ImageTk, Image
import mysql.connector
import tkinter.messagebox

__copyright__ = "University of New Haven"
__author__ = "Charitha Sree Jayaramireddy, Madhavi Kuchipudi, Ganesh Putta, Pranitha Challa, Monika Veerati"

class mainWindow():
    def __init__(self, window1):
        self.window = window1
        self.window = Frame(self.window, width=2000, height=1600, bg="white")
        self.window.pack()
        #Considering the image to be displayed as icon of our Store Title
        self.logo = Image.open('orange.png')
        self.logo = self.logo.resize((100, 100), Image.ANTIALIAS)
        self.logo1 = ImageTk.PhotoImage(self.logo)
        # Initializing menu on the main screen
        my_menu = Menu(root)
        root.config(menu = my_menu)


        text_aboutus1 = "Copyright - 2021, University of New Haven."
        text_aboutus2 = "We, Team Datadive, as part of our Database course, has developed a Grocery Store Management System"
        text_aboutus3 = "You can reach out to us through Emails provided in the Contact Us menu on the main screen."

        #Creating multiple menus and their options
        file_menu = Menu(my_menu, tearoff = 0)
        my_menu.add_cascade(label="About us", menu = file_menu)
        file_menu.add_command(label=text_aboutus1)
        file_menu.add_command(label=text_aboutus2)
        file_menu.add_command(label=text_aboutus3)


        contact_menu = Menu(my_menu, tearoff = 0)
        my_menu.add_cascade(label="Contact us", menu = contact_menu)
        contact_menu.add_command(label="cjaya1@unh.newhaven.edu")
        contact_menu.add_separator()
        contact_menu.add_command(label="mkuch2@unh.newhaven.edu")
        contact_menu.add_separator()
        contact_menu.add_command(label="gputta1@unh.newhaven.edu")
        contact_menu.add_separator()
        contact_menu.add_command(label="pchal4@unh.newhaven.eduu")
        contact_menu.add_separator()
        contact_menu.add_command(label="mveer3@unh.newhaven.edu")

        help_menu = Menu(my_menu, tearoff = 0)
        my_menu.add_cascade(label="Help/Exit", menu = help_menu)

        help_menu2 = Menu(help_menu, tearoff = 0)
        # help_menu.add_command(label="Help")
        help_menu.add_cascade(label = "Help", menu = help_menu2)
        help_menu2.add_command(label="cjaya1@unh.newhaven.edu")
        help_menu.add_command(label="Exit", command = root.destroy)


        # self.back_img = Image.open('image.png')
        # self.back_img = self.back_img.resize((1500, 1000), Image.ANTIALIAS)
        # self.back_img1 = ImageTk.PhotoImage(self.back_img)
        # self.background_label = Label(self.window, image=self.back_img1, compound = "left", bg = "white", fg = None)
        # self.background_label.pack(side = "top", fill ="both")
        # self.background_label.place(x=0, y=0, relwidth = 1, relheight = 1)

        # Store Title displayed on the screen
        self.heading = Label(self.window, text="Orange Stores", font=('arial 60 bold italic'),image = self.logo1,compound = "left", fg='DarkOrange3', bg="white")
        self.heading.pack(side="top", fill = "both")
        self.heading.place(x=400, y=50)


        #Images that are used on buttons
        self.image = Image.open('EEs3.png')
        self.image = self.image.resize((350, 210), Image.ANTIALIAS)
        self.EE_image = ImageTk.PhotoImage(self.image)

        self.loc_img = Image.open('branches.png')
        self.loc_img = self.loc_img.resize((270, 210), Image.ANTIALIAS)
        self.loc_img1 = ImageTk.PhotoImage(self.loc_img)

        self.des_img = Image.open('designation2.png')
        self.des_img = self.des_img.resize((270, 210), Image.ANTIALIAS)
        self.des_img1 = ImageTk.PhotoImage(self.des_img)

        self.cus_img = Image.open('customer2.png')
        self.cus_img = self.cus_img.resize((270, 210), Image.ANTIALIAS)
        self.cus_img1 = ImageTk.PhotoImage(self.cus_img)

        self.cat_img = Image.open('category2.png')
        self.cat_img = self.cat_img.resize((270, 210), Image.ANTIALIAS)
        self.cat_img1 = ImageTk.PhotoImage(self.cat_img)

        self.comm_img = Image.open('comm1.png')
        self.comm_img = self.comm_img.resize((270, 210), Image.ANTIALIAS)
        self.comm_img1 = ImageTk.PhotoImage(self.comm_img)

        self.supl_img = Image.open('supplier1.png')
        self.supl_img = self.supl_img.resize((270, 210), Image.ANTIALIAS)
        self.supl_img1 = ImageTk.PhotoImage(self.supl_img)

        self.mgr_img = Image.open('manager2.png')
        self.mgr_img = self.mgr_img.resize((270, 210), Image.ANTIALIAS)
        self.mgr_img1 = ImageTk.PhotoImage(self.mgr_img)

        #Buttons with images on the screen
        self.employees_button = Button(self.window, image = self.EE_image, compound = "center", width = 250, height = 200,font=('arial 15 bold'),bg = "MistyRose3",highlightbackground = "yellow", fg = 'RoyalBlue4', command = self. mainEmployees)

        self.employees_button.pack(side="top", fill = "both")
        self.employees_button.place(x = 50, y = 250)
        self.location_button = Button(self.window, image = self.loc_img1,compound = "center", width = 250, height = 200,font=('arial 20 bold'),bg = "MistyRose3",fg = 'RoyalBlue4', command = self.mainLocation)
        self.location_button.pack(side="top", fill = "both")
        self.location_button.place(x = 400, y = 250)
        self.designation_button = Button(self.window,  image = self.des_img1,compound = "center", width = 250, height = 200,font=('arial 20 bold'),bg = "MistyRose3",fg = 'RoyalBlue4', command = self.mainDesignation)
        self.designation_button.place(x = 750, y = 250)
        self.customers_button = Button(self.window,  image = self.cus_img1,compound = "center", width = 250, height = 200,font=('arial 15 bold'),bg = "MistyRose3",fg = 'RoyalBlue4', command = self.mainCustomer)
        self.customers_button.place(x = 1100, y = 250)
        self.categories_button = Button(self.window,  image = self.cat_img1,compound = "center", width = 250, height = 200,font=('arial 15 bold'),bg = "MistyRose3",fg = 'RoyalBlue4', command = self.mainCategory)
        self.categories_button.place(x = 50, y = 550)
        self.comm_button = Button(self.window,  image = self.comm_img1,compound = "center", width = 250, height = 200,font=('arial 15 bold'),bg = "MistyRose3",fg = 'RoyalBlue4', command = self.mainCommodities)
        self.comm_button.place(x = 400, y = 550)
        self.supplier_button = Button(self.window,  image = self.supl_img1,compound = "center", width = 250, height = 200,font=('arial 15 bold'),bg = "MistyRose3",fg = 'RoyalBlue4', command = self.mainSupplier)
        self.supplier_button.place(x = 750, y = 550)

        self.manager_button = Button(self.window,  image = self.mgr_img1,compound = "center", width = 250, height = 200,font=('arial 15 bold'),bg = "MistyRose3",fg = 'RoyalBlue4', command = self.mainManager)
        self.manager_button.place(x = 1100, y = 550)

    # Functions that will be called on a respective button click.
    def mainEmployees(self):
        ee.Employees(self.window)
        if ee.Employees(self.window).exit_now:
            self.__init__(root)

    def mainLocation(self):
        loc.Location(self.window)
        if loc.Location(self.window).exit_now:
            self.__init__(root)

    def mainDesignation(self):
        dg.Designation(self.window)
        if dg.Designation(self.window).exit_now:
            self.__init__(root)

    def mainCustomer(self):
        cust.Customers(self.window)
        if cust.Customers(self.window).exit_now:
            self.__init__(root)

    def mainCategory(self):
        cat.Categories(self.window)
        if cat.Categories(self.window).exit_now:
            self.__init__(root)

    def mainCommodities(self):
        comm.Commodities(self.window)
        if comm.Commodities(self.window).exit_now:
            self.__init__(root)

    def mainSupplier(self):
        suppl.Suppliers(self.window)
        if suppl.Suppliers(self.window).exit_now:
            self.__init__(root)

    def mainManager(self):
        mg.Manager(self.window)
        if mg.Manager(self.window).exit_now:
            self.__init__(root)

# Function that will get us into main screen, on a successful login
def mainFun():
    global root
    if password == actual:
        login.withdraw()
        root = Toplevel()
        root.title("Grocery Store Management")
        mainWindow(root)
        root.geometry("1600x1600+0+0")
        root.mainloop()
    else:
        tkinter.messagebox.showinfo("Error", "Please enter correct password", parent = login)

# Creating a login screen
login = Tk()
login.title("Login")
login.geometry("300x200+0+0")
login.configure(bg = "snow2")

# Database connection - To access the username and password from a table
conn = mysql.connector.connect(host="localhost", user="root", password="root", database="grocerystore")
mycursor = conn.cursor()

# labels and text boxes displayed on the login screen
usernameLabel = Label(login, text = "Username", bg = "snow2")
usernameLabel.place(x = 0, y = 10)
usernameBox = Entry(login)
usernameBox.place(x = 100, y = 10)

passwordLabel = Label(login, text = "Password", bg = "snow2")
passwordLabel.place(x = 0, y = 60)
passwordBox = Entry(login, show = "*")
passwordBox.place(x = 100, y = 60)
username = ""
password = ""
actualPassword = ""

# Function for login button on the login screen
def submit():
    global username, password, actual
    username = usernameBox.get()
    password = passwordBox.get()
    query = "SELECT Password from dbusers where Username = %s"
    values = (username,)
    mycursor.execute(query, values)
    actualPassword = mycursor.fetchall()
    try:
        actual = actualPassword[0][0]
        mainFun()
    except:
        tkinter.messagebox.showinfo("Error", "Invalid Username", parent = login)


#Placing the login button on the login screen
submit_button = Button(login, text = "Login", width = 10, font = "Arial 10 bold",fg = "HotPink4", command = submit)
submit_button.place(x = 90, y = 100)
login.mainloop()




