# Thabo Setsubi Class 2
# Generate 6 numbers
from tkinter import *
from tkinter import messagebox
import random


# Tkinter window
window = Tk()
window.title("Lotto Draw!")
window.geometry("650x650")
window.config(bg="#ffff00")


# Class for Lotto Play
class LottoPage:
    label_text = StringVar()

    def __init__(self, master):
        # Frame
        self.frame = Frame(master, bg="#ffff00")
        self.frame.place(x=10, y=10, width=500, height=500)
        # Labels
        self.lotto_lab = Label(self.frame, text="LOTTO ", font="arial 20", bg="#ffff00")
        self.lotto_lab.place(x=10, y=10)
        self.answer1 = Label(self.frame, text="", bg="#ffff00")
        self.answer1.place(x=10, y=370)
        self.answer2 = Label(self.frame, text="", bg="#ffff00")
        self.answer2.place(x=10, y=410)
        self.answer3 = Label(self.frame, text="", bg="#ffff00")
        self.answer3.place(x=10, y=450)
        self.claim_lab = Label(self.frame, text="Prize(in rands): ")
        self.claim_lab.place(x=170, y=410)
        # Buttons
        self.first = Button(self.frame, text="1", command=lambda: self.play_num(1))
        self.first.place(x=10, y=50)
        self.second = Button(self.frame, text="2", command=lambda: self.play_num(2))
        self.second.place(x=50, y=50)
        self.third = Button(self.frame, text="3", command=lambda: self.play_num(3))
        self.third.place(x=90, y=50)
        self.fourth = Button(self.frame, text="4", command=lambda: self.play_num(4))
        self.fourth.place(x=130, y=50)
        self.fifth = Button(self.frame, text="5", command=lambda: self.play_num(5))
        self.fifth.place(x=170, y=50)
        self.sixth = Button(self.frame, text="6", command=lambda: self.play_num(6))
        self.sixth.place(x=210, y=50)
        self.seventh = Button(self.frame, text="7", command=lambda: self.play_num(7))
        self.seventh.place(x=250, y=50)
        self.eighth = Button(self.frame, text="8", command=lambda: self.play_num(8))
        self.eighth.place(x=10, y=90)
        self.ninth = Button(self.frame, text="9", command=lambda: self.play_num(9))
        self.ninth.place(x=50, y=90)
        self.tenth = Button(self.frame, text="10", width=1, command=lambda: self.play_num(10))
        self.tenth.place(x=90, y=90)
        self.eleven = Button(self.frame, text="11", width=1, command=lambda: self.play_num(11))
        self.eleven.place(x=130, y=90)
        self.twelve = Button(self.frame, text="12", width=1, command=lambda: self.play_num(12))
        self.twelve.place(x=170, y=90)
        self.thirteen = Button(self.frame, text="13", width=1, command=lambda: self.play_num(13))
        self.thirteen.place(x=210, y=90)
        self.fourteen = Button(self.frame, text="14", width=1, command=lambda: self.play_num(14))
        self.fourteen.place(x=250, y=90)
        self.fifteen = Button(self.frame, text="15", width=1, command=lambda: self.play_num(15))
        self.fifteen.place(x=10, y=130)
        self.sixteen = Button(self.frame, text="16", width=1, command=lambda: self.play_num(16))
        self.sixteen.place(x=50, y=130)
        self.seventeen = Button(self.frame, text="17", width=1, command=lambda: self.play_num(17))
        self.seventeen.place(x=90, y=130)
        self.eighteen = Button(self.frame, text="18", width=1, command=lambda: self.play_num(18))
        self.eighteen.place(x=130, y=130)
        self.nineteen = Button(self.frame, text="19", width=1, command=lambda: self.play_num(19))
        self.nineteen.place(x=170, y=130)
        self.twenty = Button(self.frame, text="20", width=1, command=lambda: self.play_num(20))
        self.twenty.place(x=210, y=130)
        self.twenty_1 = Button(self.frame, text="21", width=1, command=lambda: self.play_num(21))
        self.twenty_1.place(x=250, y=130)
        self.twenty_2 = Button(self.frame, text="22", width=1, command=lambda: self.play_num(22))
        self.twenty_2.place(x=10, y=170)
        self.twenty_3 = Button(self.frame, text="23", width=1, command=lambda: self.play_num(23))
        self.twenty_3.place(x=50, y=170)
        self.twenty_4 = Button(self.frame, text="24", width=1, command=lambda: self.play_num(24))
        self.twenty_4.place(x=90, y=170)
        self.twenty_5 = Button(self.frame, text="25", width=1, command=lambda: self.play_num(25))
        self.twenty_5.place(x=130, y=170)
        self.twenty_6 = Button(self.frame, text="26", width=1, command=lambda: self.play_num(26))
        self.twenty_6.place(x=170, y=170)
        self.twenty_7 = Button(self.frame, text="27", width=1, command=lambda: self.play_num(27))
        self.twenty_7.place(x=210, y=170)
        self.twenty_8 = Button(self.frame, text="28", width=1, command=lambda: self.play_num(28))
        self.twenty_8.place(x=250, y=170)
        self.twenty_9 = Button(self.frame, text="29", width=1, command=lambda: self.play_num(29))
        self.twenty_9.place(x=10, y=210)
        self.thirty = Button(self.frame, text="30", width=1, command=lambda: self.play_num(30))
        self.thirty.place(x=50, y=210)
        self.thirty_1 = Button(self.frame, text="31", width=1, command=lambda: self.play_num(31))
        self.thirty_1.place(x=90, y=210)
        self.thirty_2 = Button(self.frame, text="32", width=1, command=lambda: self.play_num(32))
        self.thirty_2.place(x=130, y=210)
        self.thirty_3 = Button(self.frame, text="33", width=1, command=lambda: self.play_num(33))
        self.thirty_3.place(x=170, y=210)
        self.thirty_4 = Button(self.frame, text="34", width=1, command=lambda: self.play_num(34))
        self.thirty_4.place(x=210, y=210)
        self.thirty_5 = Button(self.frame, text="35", width=1, command=lambda: self.play_num(35))
        self.thirty_5.place(x=250, y=210)
        self.thirty_6 = Button(self.frame, text="36", width=1, command=lambda: self.play_num(36))
        self.thirty_6.place(x=10, y=250)
        self.thirty_7 = Button(self.frame, text="37", width=1, command=lambda: self.play_num(37))
        self.thirty_7.place(x=50, y=250)
        self.thirty_8 = Button(self.frame, text="38", width=1, command=lambda: self.play_num(38))
        self.thirty_8.place(x=90, y=250)
        self.thirty_9 = Button(self.frame, text="39", width=1, command=lambda: self.play_num(39))
        self.thirty_9.place(x=130, y=250)
        self.forty = Button(self.frame, text="40", width=1, command=lambda: self.play_num(40))
        self.forty.place(x=170, y=250)
        self.forty_1 = Button(self.frame, text="41", width=1, command=lambda: self.play_num(41))
        self.forty_1.place(x=210, y=250)
        self.forty_2 = Button(self.frame, text="42", width=1, command=lambda: self.play_num(42))
        self.forty_2.place(x=250, y=250)
        self.forty_3 = Button(self.frame, text="43", width=1, command=lambda: self.play_num(43))
        self.forty_3.place(x=10, y=290)
        self.forty_4 = Button(self.frame, text="44", width=1, command=lambda: self.play_num(44))
        self.forty_4.place(x=50, y=290)
        self.forty_5 = Button(self.frame, text="45", width=1, command=lambda: self.play_num(45))
        self.forty_5.place(x=90, y=290)
        self.forty_6 = Button(self.frame, text="46", width=1, command=lambda: self.play_num(46))
        self.forty_6.place(x=130, y=290)
        self.forty_7 = Button(self.frame, text="47", width=1, command=lambda: self.play_num(47))
        self.forty_7.place(x=170, y=290)
        self.forty_8 = Button(self.frame, text="48", width=1, command=lambda: self.play_num(48))
        self.forty_8.place(x=210, y=290)
        self.forty_9 = Button(self.frame, text="49", width=1, command=lambda: self.play_num(49))
        self.forty_9.place(x=250, y=290)
        self.lotto_btn1 = Button(self.frame, text="Play Lotto!", command=self.lotto_draw3)
        self.lotto_btn1.place(x=10, y=330)
        self.clear_btn = Button(self.frame, text="Clear", command=self.clear_function)
        self.clear_btn.place(x=110, y=330)
        self.fin_btn = Button(self.frame, text="Exit", bg="red", fg="#ffffff", command=self.exit_func)
        self.fin_btn.place(x=280, y=330)
        self.claim_prize = Button(self.frame, text="Claim Prize", bg="green", fg="#ffffff", command=self.claim_prize_func)
        self.claim_prize.place(x=175, y=330)
        self.list1 = []
        self.list2 = []
        self.list3 = []

    # function to compare the lists to the lotto list
    def lotto_draw1(self):
        global prize
        y = 0
        lotto = random.sample(range(1, 50), 6)
        for x in range(0, 6):
            if self.list1[x] == lotto[x]:
                y += 1
        if y == 6:
            prize = 10000000
        elif y == 5:
            prize = 8584
        elif y == 4:
            prize = 2384
        elif y == 3:
            prize = 100.50
        elif y == 2:
            prize = 20
        elif y < 2:
            prize = 0
        messagebox.showinfo("Status", "Set had: " + str(y))
        messagebox.showinfo("Lotto", "Numbers are: " + str(lotto))
        messagebox.showinfo("Winnings", "You have won R" + str(prize))

    # function to compare list 2 to lotto list
    def lottery_draw2(self):
        global prize
        y = 0
        lotto = random.sample(range(1, 50), 6)
        for i in range(0, 6):
            if self.list2[i] == lotto[i]:
                y += 1
        if y == 6:
            prize = 10000000
        elif y == 5:
            prize = 8584
        elif y == 4:
            prize = 2384
        elif y == 3:
            prize = 100.50
        elif y == 2:
            prize = 20
        elif y < 2:
            prize = 0
        messagebox.showinfo("Status", "Set had: " + str(y))
        messagebox.showinfo("Lotto", "Numbers are: " + str(lotto))
        messagebox.showinfo("Winnings", "You have won R" + str(prize))

    # function comparing all the list to 3 separate lotto list
    def lotto_draw3(self):
        self.lotto_draw1()
        self.lottery_draw2()

        global prize
        y = 0
        lotto = random.sample(range(1, 50), 6)
        for j in range(0, 6):
            if self.list3[j] == lotto[j]:
                y += 1
        if y == 6:
            prize = 10000000
        elif y == 5:
            prize = 8584
        elif y == 4:
            prize = 2384
        elif y == 3:
            prize = 100.50
        elif y == 2:
            prize = 20
        elif y < 2:
            prize = 0
        messagebox.showinfo("Status", "Set had: " + str(y))
        messagebox.showinfo("Lotto", "Numbers are: " + str(lotto))
        messagebox.showinfo("Winnings", "You have won R" + str(prize))

    # function to put values to the button and add them to the empty list
    def play_num(self, num):
        if len(self.list1) <= 5 and num not in self.list1:
            self.list1.append(num)
            self.answer1.config(text=self.list1)

        elif len(self.list1) == 6 and len(self.list2) <= 5 and num not in self.list2:
            self.list2.append(num)
            self.answer2.config(text=self.list2)

        elif len(self.list2) == 6 and len(self.list3) <= 5 and num not in self.list3:
            self.list3.append(num)
            self.answer3.config(text=self.list3)

        else:
            messagebox.showerror("Error", "You can choose a number once")

    def claim_prize_func(self):
        window.destroy()
        import Currency

    def clear_function(self):
        self.answer1.config(text="")
        self.answer2.config(text="")
        self.answer3.config(text="")
        self.list1 = []
        self.list2 = []
        self.list3 = []

    # function to exit the program
    def exit_func(self):
        return window.destroy()


LottoPage(window)
window.mainloop()
