import tkinter as tk
from tkinter import messagebox
import os
import base64

window = tk.Tk()
window.geometry("500x500")
window.resizable(False, False)
window.configure(bg="skyblue")

def decrypt(data):

    decode_message = data.encode("utf-8")
    base64_bytes = base64.b64decode(decode_message)
    decrypted_message = base64_bytes.decode("utf-8")
    
    inputtxt3.insert(1.0, decrypted_message)

def encrypt(text):

    encode_message = text.encode("utf-8")
    base64_bytes = base64.b64encode(encode_message)
    encrypted_message = base64_bytes.decode("utf-8")
    
    return encrypted_message

def clear():
    inputtxt1.delete(1.0, 'end')
    inputtxt2.delete(1.0, 'end')
    inputtxt3.delete(1.0, 'end')

def savepass():
    web = inputtxt1.get(1.0, "end-1c").strip()
    email = inputtxt2.get(1.0, "end-1c").strip()
    pasw = inputtxt3.get(1.0, "end-1c").strip()

    pas = encrypt(pasw)
    resr = []
    if os.path.exists("SavedPassword.txt"):
        with open("SavedPassword.txt", "r") as file:
            res = file.readlines()
  
    resr = [line.strip() for line in res]
    
    i = 0
    stat = 0
    leng = len(res)
    while i < leng:
        if web == resr[i] and email == resr[i + 1]:
            listofline = res
            listofline[i + 2] = pas + "\n"
            with open("SavedPassword.txt", "w") as file:
                file.writelines(listofline)
            stat = 1
            messagebox.showinfo("Alert", "Password Updated")
            break
        i += 3
    
    if stat == 0:
        with open("SavedPassword.txt", "a") as file:
            file.write(f"{web}\n{email}\n{pas}\n")
        messagebox.showinfo("Success", "Password Saved")
    
    clear()

def openpass():
    web = inputtxt1.get(1.0, "end-1c").strip()
    email = inputtxt2.get(1.0, "end-1c").strip()
    res = []
    if os.path.exists("SavedPassword.txt"):
        with open("SavedPassword.txt", "r") as file:
            res = file.readlines()
    
    resr = [line.strip() for line in res]
    
    i = 0
    stat = 0
    leng = len(res)
    while i < leng:
        if web == resr[i] and email == resr[i + 1]:
            inputtxt3.delete(1.0, 'end')
            decrypt(resr[i + 2])
            stat = 1
            break
        i += 3
    if stat == 0:
        inputtxt3.delete(1.0, 'end')
        inputtxt3.insert(1.0, 'No record found')

b_savepass = tk.Button(window, text="Save Password", height=2, width=20, bg="brown", fg="green", command=savepass)
b_savepass.place(relx=0.5, rely=0.65, anchor=tk.CENTER)

b_openpass = tk.Button(window, text="Open Saved Password", height=2, width=20, bg="brown", fg="green", command=openpass)
b_openpass.place(relx=0.5, rely=0.8, anchor=tk.CENTER)

b_clear = tk.Button(window, text="Clear All", height=2, width=10, bg="brown", fg="green", command=clear)
b_clear.place(relx=0.5, rely=0.95, anchor=tk.CENTER)

l2 = tk.Label(window, text="Password Manager", font=("arial", 20, "bold"))
l2.config(bg="lightpink")
l2.place(relx=0.5, rely=0.1, anchor=tk.CENTER)

inputtxt1 = tk.Text(window, height=1, width=20)
inputtxt1.place(relx=0.7, rely=0.3, anchor=tk.E)

lbl1 = tk.Label(window, text="Website", bg="lightpink", font=("arial", 10, "bold"))
lbl1.place(relx=0.1, rely=0.3, anchor=tk.W)

inputtxt2 = tk.Text(window, height=1, width=20)
inputtxt2.place(relx=0.7, rely=0.4, anchor=tk.E)

lbl2 = tk.Label(window, text="E-Mail", bg="lightpink", font=("arial", 10, "bold"))
lbl2.place(relx=0.1, rely=0.4, anchor=tk.W)

inputtxt3 = tk.Text(window, height=1, width=20)
inputtxt3.place(relx=0.7, rely=0.5, anchor=tk.E)

lbl3 = tk.Label(window, text="Password", bg="lightpink", font=("arial", 10, "bold"))
lbl3.place(relx=0.1, rely=0.5, anchor=tk.W)

window.mainloop()
