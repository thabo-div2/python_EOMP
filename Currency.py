# Thabo Setsubi Class 2
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import requests
import smtplib
from playsound import playsound


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
        self.winnings = Label(master, text="Your winnings(in rands): ")
        self.winnings.place(x=10, y=200)
        self.convert_lab1 = Label(master, text="Convert to your countries currency: ")
        self.convert_lab1.place(x=10, y=250)
        self.bank_local = Label(master, text="Please pick your bank: ")
        self.bank_local.place(x=10, y=300)
        self.prize = Label(master, text="")
        self.prize.place(x=170, y=200)
        self.foreign = Label(master, text="")
        self.foreign.place(x=10, y=500)
        self.example = Label(master, text="")
        self.example.place(x=10, y=700)

        # Entries
        self.bank_name = Entry(master)
        self.bank_name.place(x=150, y=100)
        self.bank_account = Entry(master)
        self.bank_account.place(x=150, y=150)

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
        self.convert_btn = Button(master, text="Convert Currency", command=self.convert_func)
        self.convert_btn.place(x=350, y=250)
        self.submit_info = Button(master, text="Submit Info", command=self.submit_line)
        self.submit_info.place(x=10, y=450)

    # function to submit information and winnings
    def convert_func(self):
        try:
            x = self.data['conversion_rates'][self.rates_cb.get()]
            mywinnings = []
            with open("Prizes.txt", "rt") as myfile:
                for myline in myfile:
                    mywinnings.append(int(myline))
                    self.prize.config(text=mywinnings[0])
            new_currency = x * float(mywinnings[0])
            self.foreign.config(text=new_currency)
        except requests.exceptions.ConnectionError:
            messagebox.showerror("Error", "No internet connection")

    def submit_line(self):
        email_line = []
        try:
            with open("Emails.txt", "+r") as f:
                line = f.readline()
                email_line.append(line)
            s = smtplib.SMTP('smtp.gmail.com', 587)
            sender = '3981212@myuwc.ac.za'
            receive = str(email_line[0])
            password = '9903156253086'
            s.starttls()
            s.login(sender, password)
            message = str(email_line[0:])
            s.sendmail(sender, receive, message)
            s.quit()
        except smtplib.SMTPException:
            pass


CurrencyConverter(currency)
currency.mainloop()
