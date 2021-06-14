# Thabo Setsubi Class 2
from tkinter import *

window = Tk()
window.title("Lotto Draw!")
window.geometry("650x650")
window.config(bg="#ffff00")

class LottoPage:
    def __init__(self,master):
        self.frame = Frame(master, bg="#ffffff")
        self.frame.place(x=10, y=10, width=500, height=500)




LottoPage(window)
window.mainloop()
