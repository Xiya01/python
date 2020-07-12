import tkinter
import keyboard


class connection():
    def __init__(self):
        import socket
        self.socket = socket.socket()

    def server(self,port):
        self.port = port
        self.socket.bind(('',self.port))
        self.socket.listen(5)
        self.connection, self.clientIP = self.socket.accept()
        return self

    def client(self,IP,port):
        self.IP = IP
        self.port = port
        self.connection = self.socket
        self.connection.connect((self.IP, self.port))
        return self
        
    def send(self,message):
        self.connection.send(message.encode())

    def recieve(self):
        self.connection.settimeout(0.1)
        try:
            msg = self.connection.recv(1024).decode()
        except:
            msg = False
        self.connection.settimeout(None)
        return msg
        
class gui():
    

    def menu(self):

        self.window = tkinter.Tk()
        self.window.title("Czat")

        self.photofile = tkinter.PhotoImage(file = "C:\\Users\\Xiya\\Desktop\\dio.gif")
        self.foto = tkinter.Label(self.window, image = self.photofile)
        self.foto.grid(row=7, column=1)

        self.checkbox = tkinter.BooleanVar()
        self.serwer = tkinter.Checkbutton(self.window, text="serwer", variable=self.checkbox, cursor = "heart", bg ="Lavenderblush1" )
        self.serwer.grid(row=6, column=0)

        self.nazwa = tkinter.Label(self.window, text = "Wpisz swój nick")
        self.nazwa.grid(row = 0, column = 0)

        self.wpisznick = tkinter.Entry(self.window, width = "40")
        self.wpisznick.grid(row=1, column=1)
        
        self.nazwaip = tkinter.Label(self.window, text = "Podaj IP:")
        self.nazwaip.grid(row = 2, column = 0)

        self.IP = tkinter.Entry(self.window, width = "40")
        self.IP.grid(row=2, column =1)

        self.podajport = tkinter.Label(self.window, text = "Podaj numer portu: ")
        self.podajport.grid(row =4, column=0)

        self.Numerportu = tkinter.Entry(self.window, width = "40")
        self.Numerportu.grid(row=4, column=1)


        self.zatwierdz = tkinter.Button(self.window, text= "Wyślij", command=self.przycisk, bg = "Lavenderblush1")
        self.zatwierdz.grid(row=1, column=2)
        
        self.window.mainloop()

    def przycisk(self):
        self.nick = self.wpisznick.get()
        self.IP = self.IP.get()
        self.Numerportu = int(self.Numerportu.get())
        self.serwer = self.checkbox.get()
        self.window.destroy()

        if self.serwer:
            self.polaczenie = connection().server(self.Numerportu)

        else:
            self.polaczenie = connection().client(self.IP,self.Numerportu)
        
        self.start()

    def start(self):
        self.chat_window = tkinter.Tk()


        self.tytul = tkinter.Label(self.chat_window, text="CZAT")
        self.tytul.grid(row=0, column=0)

        self.oknoczatu = tkinter.Label(self.chat_window, text= "")
        self.oknoczatu.grid(row=0, column=1)
        
        self.poledopisania = tkinter.Entry(self.chat_window, width = "40")
        self.poledopisania.grid(row=1, column=1)


        self.send = tkinter.Button(self.chat_window, text= "Wyślij", command=self.button, bg = "Lavenderblush1")
        self.send.grid(row=1, column=2)
      
        self.wyjscie = tkinter.Button(self.chat_window, text= "Wyjście", command=self.chat_window.destroy, bg = "Lavenderblush1")
        self.wyjscie.grid(row=2, column=2)

        self.odbieranie()

        self.chat_window.mainloop()

    def odbieranie(self):
        self.odebrana_wiadomosc = self.polaczenie.recieve()
        print(self.odebrana_wiadomosc)
        
        if self.odebrana_wiadomosc:
            self.oknoczatu["text"] = self.oknoczatu["text"] + self.odebrana_wiadomosc + "\n"
        self.chat_window.after(1000,self.odbieranie)


    def button(self):
        self.oknoczatu["text"] = self.oknoczatu["text"] + self.nick + ": " + self.poledopisania.get() + "\n"
        self.polaczenie.send(self.nick + ": " + self.poledopisania.get())
        self.poledopisania.delete(0,tkinter.END)
   
gui().menu()