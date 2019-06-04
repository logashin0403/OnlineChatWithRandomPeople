from tkinter import *
import socket
import os
from tkinter import messagebox as mb

class Window:

    def __init__(self):

        self.lbl1 = Label(tk, height = 3, width = 71, bg = "#8e7acd")
        self.lbl1.place(x=0, y=0)
        self.lbl2 = Label(tk, text = "EDOR", height = 1, width = 5, font = "arial 15 bold", bg = "#8e7acd")
        self.lbl2.place(x = 5, y = 5)
        self.lbl3 = Label(tk, height=3, width=1, bg="#332758")
        self.lbl3.place(x=90, y=0)

        self.btn1 = Button(tk, text = "Rules", height = 2, width = 10, bg = "#7a68b4", fg = "white", command = self.rules)
        self.btn1.place(x = 220, y = 5)
        self.btn2 = Button(tk, text = "Clear", height = 2, width = 10, bg = "#7a68b4", fg = "white", command = self.clear)
        self.btn2.place(x = 120, y = 5)
        self.btn3 = Button(tk, text = "Exit", height = 2, width = 10, bg = "#7a68b4", fg = "white", command = tk.destroy)
        self.btn3.place(x = 320, y = 5)
        self.btn4 = Button(tk, text = "Send", height = 1, width = 7, bg = "#1c162f", fg = "white", command = self.sendlet)
        self.btn4.place(x = 305, y = 597)
        self.btn5 = Button(tk, text = "D", height = 1, width = 3, bg = "#1c162f", fg = "white", command = self.dark)
        self.btn5.place(x = 0, y = 52)
        self.btn6 = Button(tk, text = "L", height = 1, width = 3, bg = "#f2e977", fg = "black", command = self.light)
        self.btn6.place(x = 31, y = 52)
        

        self.ent1 = Entry(tk, bg = "#1c162f", width = 35, fg = "white", font = "arial 10 bold")
        self.ent1.place(x = 30, y = 600)

        self.txt1 = Text(tk, width = 47, height = 30, bg = "#1c162f", fg = "white", wrap = WORD, font = "arial 10 bold", state = "disabled")
        self.txt1.place(x = 30, y = 90)
        self.text = ""
        self.namepc = os.environ.get('USERNAME')

        tk.bind('<KeyPress>', self.onKeyPress)

        try:
            self.sock = socket.socket()
            self.sock.connect(('localhost', 9090))
            print("Server is activated")
        except:
            print("Server is not work")
            tk.destroy()
        self.serv()

    def serv(self):
        self.sock.send(f"{self.namepc}  connected".encode('UTF-8'))
        while True:
            self.sock.settimeout(0.01)
            if self.text == "":
                pass
            else:
                self.sock.send(f"{self.namepc}: {self.text}".encode('UTF-8'))
                self.text = ""
            try:
                data = self.sock.recv(1024)
            except:
                data = ""
            if not data:
                pass
            else:
                data = data.decode('UTF-8')
                self.txt1["state"] = "normal"
                self.txt1.insert(1.0, data +'\n')
                self.txt1["state"] = "disabled"
                data = ""
            try:
                tk.update()
            except:
                pass   

    def onKeyPress(self, event):
        if event.keycode == 13:
            self.sendlet()

    def dark(self):
        tk["bg"] = "#332758"
        self.lbl1["bg"] = "#8e7acd"
        self.lbl2["bg"] = "#8e7acd"
        self.lbl3["bg"] = "#332758"
        self.btn1["bg"] = "#7a68b4"
        self.btn2["bg"] = "#7a68b4"
        self.btn3["bg"] = "#7a68b4"
        self.btn4["bg"] = "#1c162f"
        self.ent1["bg"] = "#1c162f"
        self.txt1["bg"] = "#1c162f"
        self.btn1["fg"] = "white"
        self.btn2["fg"] = "white"
        self.btn3["fg"] = "white"
        self.btn4["fg"] = "white"
        self.ent1["fg"] = "white"
        self.txt1["fg"] = "white"

    def light(self):
        tk["bg"] = "#e1d20e"
        self.lbl1["bg"] = "#aeefa2"
        self.lbl2["bg"] = "#aeefa2"
        self.lbl3["bg"] = "#e1d20e"
        self.btn1["bg"] = "#9ed994"
        self.btn2["bg"] = "#9ed994"
        self.btn3["bg"] = "#9ed994"
        self.btn4["bg"] = "#f4cb86"
        self.ent1["bg"] = "#f4cb86"
        self.txt1["bg"] = "#f4cb86"
        self.btn1["fg"] = "black"
        self.btn2["fg"] = "black"
        self.btn3["fg"] = "black"
        self.btn4["fg"] = "black"
        self.ent1["fg"] = "black"
        self.txt1["fg"] = "black" 

    def sendlet(self):
        self.text = self.ent1.get()
        self.ent1.delete(0, END)

    def clear(self):
        self.txt1["state"] = "normal"
        self.txt1.delete(1.0, END)
        self.txt1["state"] = "disabled"

    def rules(self):
        mb.showerror("Rules", "1.You cant say bad words\n2.Be friendly)")

tk = Tk()
tk.geometry("405x650+390+15")
tk["bg"] = "#332758"
tk.title("Chat from EDOR")
tk.resizable(False, False)
wn = Window()
tk.mainloop()

            


