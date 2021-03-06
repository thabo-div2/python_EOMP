# End of Module Project
# Thabo Setsubi Class 2

from tkinter import *
from tkinter import messagebox
from datetime import datetime
import re
import smtplib
from playsound import playsound
import random

root = Tk()
root.geometry("650x650")
root.title("Lotto Login")
root.config(bg="#ffff00")


# Making a class for age verification page
class Login:

    def __init__(self, master):
        # Frame
        self.frame = Frame(master, bg="#ffffff")
        self.frame.place(x=10, y=10, width=500, height=500)
        # Labels
        self.name = Label(self.frame, text="Name: ")
        self.name.place(x=10, y=50)
        self.email = Label(self.frame, text="Email: ")
        self.email.place(x=10, y=85)
        self.ident = Label(self.frame, text="ID: ")
        self.ident.place(x=10, y=120)
        # Entries
        self.name_entry = Entry(self.frame)
        self.name_entry.place(x=80, y=50)
        self.email_entry = Entry(self.frame)
        self.email_entry.place(x=80, y=85)
        self.id_entry = Entry(self.frame)
        self.id_entry.place(x=80, y=120)
        # Buttons
        self.verify = Button(self.frame, text="Verify", command=self.player_id)
        self.verify.place(x=10, y=155)
        self.clear_btn = Button(self.frame, text="Clear", command=self.clear_func)
        self.clear_btn.place(x=80, y=155)
        self.exit_btn = Button(self.frame, text="Exit", command=self.exit_func)
        self.exit_btn.place(x=145, y=155)
        # Image
        self.canvas = Canvas(self.frame, width=600, height=400, bg="#ffff00")
        self.canvas.place(x=-10, y=200)
        self.img = PhotoImage(file="79b3c5f0-lotto-results.jpg.optimal-removebg-preview.png")
        self.canvas.create_image(10, 10, anchor=NW, image=self.img)

    # function verifying age and email of the user
    def player_id(self):
        dt = datetime.today()
        ex = "^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$"
        id_play = random.randint(0, 10000)
        try:
            for i in range(len(self.email_entry.get())):
                if re.search(ex, self.email_entry.get()):
                    with open("Emails.txt", "w+") as f:
                        f.write(self.email_entry.get())
                        f.write("\n")
                        f.write(str(self.name_entry.get()[0:3]) + str(self.id_entry.get()[0:2]) + str(id_play))
                        f.write("\n")
                        f.write(str(dt))
                        f.write("\n")
                        f.write(self.name_entry.get())
                        f.write("\n")
                        f.write(self.id_entry.get())
                        f.write("\n")
                else:
                    playsound("./Sound/erro.mp3")
                    messagebox.showerror("Error", "Invalid Email")
                    root.destroy()
            for x in range(int(self.id_entry.get())):
                res = int(self.id_entry.get()[0:2]) - int(dt.strftime("%y"))
                if res >= 18:
                    messagebox.showinfo("Status", "You are qualified to play Lotto")
                    root.destroy()
                    import lotto_page
                elif len(self.id_entry.get()) != 13:
                    messagebox.showerror("Error", "Not a valid ID number")
                    break
                else:
                    playsound("./Sound/erro.mp3")
                    messagebox.showerror("Error", "You are too young to play Lotto")
                    break
        except ValueError:
            if self.id_entry.get() != int:
                playsound("./Sound/erro.mp3")
                messagebox.showerror("Error", "The id number must be an integer")
            elif self.name_entry.get() != str:
                playsound("./Sound/erro.mp3")
                messagebox.showerror("Error", "Name must be a string or in letters")

    # function for clear button
    def clear_func(self):
        self.name_entry.delete(0, END)
        self.email_entry.delete(0, END)
        self.id_entry.delete(0, END)

    # function for exit button
    def exit_func(self):
        return root.destroy()


log = Login(root)
root.mainloop()
