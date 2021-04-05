# Main module to call all the other Grocery Store Management related GUI's
from tkinter import *
import employees as ee
import location as loc
import designation as dg
import cutomers as cust


class mainWindow():
    def __init__(self, window1):
        self.window = window1
        self.window = Frame(self.window, width=2000, height=1600, bg="snow2")
        self.window.pack()
        self.heading = Label(self.window, text="Grocery Store Management", font=('arial 40 bold'), fg='HotPink4', bg="snow2")
        self.heading.place(x=350, y=50)

        self.employees_button = Button(self.window, text = "Employee Information", width = 25, height = 2,font=('arial 10 bold'),bg = "MistyRose3",fg = 'dark slate blue', command = self. mainEmployees)
        self.employees_button.place(x = 550, y = 170)
        self.location_button = Button(self.window, text = "Location Information", width = 25, height = 2,font=('arial 10 bold'),bg = "MistyRose3",fg = 'dark slate blue', command = self.mainLocation)
        self.location_button.place(x = 550, y = 250)
        self.designation_button = Button(self.window, text = "EE Designation Information", width = 25, height = 2,font=('arial 10 bold'),bg = "MistyRose3",fg = 'dark slate blue', command = self.mainDesignation)
        self.designation_button.place(x = 550, y = 320)
        self.customers_button = Button(self.window, text = "Customers Information", width = 25, height = 2,font=('arial 10 bold'),bg = "MistyRose3",fg = 'dark slate blue', command = self.mainCustomer)
        self.customers_button.place(x = 550, y = 390)


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


root = Tk()
root.title("Grocery Store Management")
obj = mainWindow(root)
root.geometry("1600x1600+0+0")
root.mainloop()
