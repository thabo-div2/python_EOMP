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
        self.currency_lab1.place(x=10, y=100)
        self.banking_lab = Label(master, text="Account Name: ")
        self.banking_lab.place(x=10, y=150)
        self.winnings = Label(master, text="Enter your winnings: ")
        self.winnings.place(x=10, y=200)
        self.convert_lab1 = Label(master, text="Convert to your countries currency: ")
        self.convert_lab1.place(x=10, y=250)
        self.bank_local = Label(master, text="Please pick your bank: ")
        self.bank_local.place(x=10, y=300)

        # Entries
        self.bank_name = Entry(master)
        self.bank_name.place(x=150, y=100)
        self.bank_account = Entry(master)
        self.bank_account.place(x=150, y=150)
        self.prize = Entry(master)
        self.prize.place(x=170, y=200)

        # Combobox
        self.url = 'https://v6.exchangerate-api.com/v6/86ad406dd027a7f9eb86121b/latest/ZAR'
        self.response = requests.get(self.url)
        self.data = self.response.json()
        self.rates = self.data['conversion_rates']
        self.currency_list = []
        for i in self.rates.keys():
            self.currency_list.append(i)
        self.rates_cb = ttk.Combobox(master)
        self.rates_cb['values'] = self.currency_list
        self.rates_cb['state'] = 'readonly'
        self.rates_cb.set("Select Currency")
        self.rates_cb.place(x=170, y=250)
        self.bank_list = ["FNB", "Standard Bank", "Nedbank", "ABSA"]
        self.bank_cb = ttk.Combobox(master)
        self.bank_cb['values'] = self.bank_list
        self.bank_cb['state'] = 'readonly'
        self.bank_cb.set("Select your bank")
        self.bank_cb.place(x=170, y=300)

        # Buttons
        self.convert_btn = Button(master, text="Convert Currency")
        self.convert_btn.place(x=350, y=250)
        self.submit_info = Button(master, text="Submit Info")
        self.submit_info.place(x=10, y=450)

    # function to submit information and winnings
    def convert_func(self):
        pass



CurrencyConverter(currency)
currency.mainloop()
