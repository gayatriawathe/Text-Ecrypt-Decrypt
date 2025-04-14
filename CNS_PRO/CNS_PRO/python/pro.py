from tkinter import *
from tkinter import messagebox
import base64



def decrypt():
    password = code.get()

    if password == "1234":
        screen2 = Toplevel(screen)
        screen2.title("Decryption")
        screen2.geometry("400x200")
        screen2.configure(bg="#00bd56")

        message = text1.get(1.0, END).strip()
        try:
            base64_bytes = base64.b64decode(message.encode("ascii"))
            decrypted_message = base64_bytes.decode("ascii")

            Label(screen2, text="DECRYPTED TEXT", font="Arial 12 bold", fg="white", bg="#00bd56").place(x=10, y=0)
            text2 = Text(screen2, font="Roboto 10", bg="white", relief=GROOVE, wrap=WORD, bd=2)
            text2.place(x=10, y=40, width=380, height=150)
            text2.insert(END, decrypted_message)
        except:
            messagebox.showerror("Decryption Error", "Invalid encrypted text!")

    elif password == "":
        messagebox.showerror("Error", "Input Password")

    else:
        messagebox.showerror("Error", "Invalid Password")

def encrypt():
    password = code.get()

    if password == "1234":
        screen1 = Toplevel(screen)
        screen1.title("Encryption")
        screen1.geometry("400x200")
        screen1.configure(bg="#ed3833")

        message = text1.get(1.0, END).strip()
        encoded_message = base64.b64encode(message.encode("ascii")).decode("ascii")

        Label(screen1, text="ENCRYPTED TEXT", font="Arial 12 bold", fg="white", bg="#ed3833").place(x=10, y=0)
        text2 = Text(screen1, font="Roboto 10", bg="white", relief=GROOVE, wrap=WORD, bd=2)
        text2.place(x=10, y=40, width=380, height=150)
        text2.insert(END, encoded_message)

    elif password == "":
        messagebox.showerror("Error", "Input Password")

    else:
        messagebox.showerror("Error", "Invalid Password")

def reset():
    text1.delete(1.0, END)
    code.set("")

def main_screen():
    global screen, text1, code
    screen = Tk()
    screen.geometry("375x398")
    screen.title("Text Encryption & Decryption")

    # Icon (ensure 'keys.png' is in the same directory)
    # try:
    #     image_icon = PhotoImage(file="Keys.PNG")
    #     screen.iconphoto(False, image_icon)
    # except:
    #     messagebox.showwarning("Warning", "Icon file not found!")

    Label(screen, text="Enter text for encryption and decryption", fg="black", font=("Calibri", 13)).place(x=10, y=10)
    text1 = Text(screen, font="Roboto 12", bg="white", relief=GROOVE, wrap=WORD, bd=2)
    text1.place(x=10, y=50, width=355, height=100)

    Label(screen, text="Enter secret key for encryption and decryption", fg="black", font=("Calibri", 12)).place(x=10, y=160)

    code = StringVar()
    Entry(screen, textvariable=code, width=19, bd=2, font=("Arial", 18), show="*").place(x=10, y=190)

    Button(screen, text="ENCRYPT", height=2, width=23, bg="#ed3833", fg="white", bd=0, command=encrypt).place(x=10, y=250)
    Button(screen, text="DECRYPT", height=2, width=23, bg="#00bd56", fg="white", bd=0, command=decrypt).place(x=200, y=250)
    Button(screen, text="RESET", height=2, width=50, bg="#1089ff", fg="white", bd=0, command=reset).place(x=10, y=300)

    screen.mainloop()

main_screen()
