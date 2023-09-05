# -*- coding: utf-8 -*-
"""
Created on Sun Sep  3 10:59:01 2023

@author: Timot
"""

import customtkinter
import sqlite3
import hashlib

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

root = customtkinter.CTk()
root.title("DataNexus GUI")
root.geometry("500x350")


def login ():
    global Username
    global Password
    Username = entry1.get()
    Password = entry2.get()
    print(Username)
    if Username != "Timothy" and Password != "Williams":
        #if label2 == "":
        label2 = customtkinter.CTkLabel(master=frame, text = "Incorrect Login Information", font=("Roboto",12),text_color = "red")
        label2.pack()
        label2.after(2000, lambda: label2.destroy)
    if Username == "Timothy" and Password == "Williams":
        root.destroy()


        
frame = customtkinter.CTkFrame(master=root)
frame.pack(pady=20,padx=60,fill="both",expand=True)

label = customtkinter.CTkLabel(master=frame, text="Login System", font = ("Roboto", 24))
label.pack(pady=12,padx=10)



entry1 = customtkinter.CTkEntry(master=frame, placeholder_text = "Username")
entry1.pack(pady=12,padx=10)

entry2 = customtkinter.CTkEntry(master=frame, placeholder_text = "Password", show="*")
entry2.pack(pady=12,padx=10)

button = customtkinter.CTkButton(master=frame, text ="Login", command=login)
button.pack(pady=12,padx=10)

checkbox = customtkinter.CTkCheckBox(master=frame, text = "Remember Me")

root.mainloop()