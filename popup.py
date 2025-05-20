import os
import tkinter as tk
from tkinter import messagebox

def gui_popup():
    try:
        root = tk.Tk()
        root.withdraw()  # Hide the root window

        response = messagebox.askyesno("Question", "Do you want to continue?")
        if response:
            messagebox.showinfo("Result", "You clicked YES!")
        else:
            messagebox.showinfo("Result", "You clicked NO!")
        root.destroy()
        return True
    except tk.TclError:
        return False  # GUI failed

def cli_fallback():
    while True:
        answer = input("Do you want to continue? (yes/no): ").strip().lower()
        if answer in ['yes', 'y']:
            print("You clicked YES!")
            break
        elif answer in ['no', 'n']:
            print("You clicked NO!")
            break
        else:
            print("Please answer yes or no.")

if not gui_popup():
    print("(GUI not available — switching to text mode)")
    cli_fallback()
