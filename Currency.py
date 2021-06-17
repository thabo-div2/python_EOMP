# Thabo Setsubi Class 2
from tkinter import *
from tkinter import ttk
import requests


# tkinter window
currency = Tk()
currency.geometry("650x650")
currency.title("Currency Converter")
currency.config(bg="green")


class CurrencyConverter:
    def __init__(self, master):
        # Labels
        self.currency_lab1 = Label(master, text="Banking Details: ")
        self.currency_lab1.place(x=10, y=10)
        self.banking_lab = Label(master, text="Account Name: ")
        self.banking_lab.place(x=10, y=50)

        # Entries
        self.bank_name = Entry(master)
        self.bank_name.place(x=150, y=10)
        self.bank_account = Entry(master)
        self.bank_account.place(x=150, y=50)


CurrencyConverter(currency)
currency.mainloop()
