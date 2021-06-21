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
currency.config(bg="#ffff00")


class CurrencyConverter:
    def __init__(self, master):
        # Labels
        self.claim_label = Label(master, text="Claim Your Prize!", font="Arial 20", bg="#ffff00")
        self.claim_label.place(x=10, y=10)
        self.currency_lab1 = Label(master, text="Account Name: ", bg="#ffff00")
        self.currency_lab1.place(x=10, y=100)
        self.banking_lab = Label(master, text="Account Number: ", bg="#ffff00")
        self.banking_lab.place(x=10, y=150)
        self.winnings = Label(master, text="Your winnings(in rands): ", bg="#ffff00")
        self.winnings.place(x=10, y=200)
        self.convert_lab1 = Label(master, text="Convert to your countries currency: ", bg="#ffff00")
        self.convert_lab1.place(x=10, y=250)
        self.bank_local = Label(master, text="Please pick your bank: ", bg="#ffff00")
        self.bank_local.place(x=10, y=300)
        self.prize = Label(master, text="", bg="#ffff00")
        self.prize.place(x=170, y=200)
        self.foreign = Label(master, text="", bg="#ffff00")
        self.foreign.place(x=10, y=500)

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
        self.convert_btn = Button(master, text="Convert Currency", command=self.convert_func, bg="#CD7F32", fg="#ffffff")
        self.convert_btn.place(x=350, y=250)
        self.submit_info = Button(master, text="Submit Info", command=self.submit_line, bg="green", fg="#ffffff")
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
            playsound("./Sound/erro.mp3")
            messagebox.showerror("Error", "No internet connection")

    def submit_line(self):
        email_line = []
        try:
            with open("Emails.txt", "+a") as w:
                w.write("Bank Account Name: " + str(self.bank_name.get()))
                w.write("\n")
                w.write("Bank Account Number: " + str(int(self.bank_account.get())))
                w.write("\n")
                w.write("Bank: " + str(self.bank_cb.get()))
            with open("Emails.txt", "+r") as f:
                line = f.readline()
                email_line.append(line)
                line2 = f.read()
            s = smtplib.SMTP('smtp.gmail.com', 587)
            sender = 'lifechoiceslotto147@gmail.com'
            receive = str(email_line[0])
            password = 'lifechoices2021'
            s.starttls()
            s.login(sender, password)
            message = str(line2)
            s.sendmail(sender, receive, message)
            s.quit()
        except ValueError:
            if self.bank_name.get() != str:
                playsound("./Sound/erro.mp3")
                messagebox.showerror("Error", "Must be in letters or characters or strings")
            if self.bank_account.get() != int:
                playsound("./Sound/erro.mp3")
                messagebox.showerror("Error", "Must be in numbers")

        except smtplib.SMTPException:
            playsound("./Sound/erro.mp3")


CurrencyConverter(currency)
currency.mainloop()
