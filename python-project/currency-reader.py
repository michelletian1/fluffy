from tkinter import*
from tkinter import messagebox
from tkinter import ttk

root = Tk()
root.title("Currency")

def button() :
    if country.get() == "United States" :
        messagebox.showinfo("Title" , "Dollar")
    elif country.get() == "Indonesia" :
        messagebox.showinfo("Currency" , "Rupiah")
    elif country.get() == "Japan" :
        messagebox.showinfo("Title" , "Yen")
    elif country.get() == "India" :
        messagebox.showinfo("Title", "Rupees")
    else :
        messagebox.showinfo("Title", "Not on the list")

text_country = Label(root, text = "Choose a country")
country = ttk.Combobox(root, values = ["United States", "Indonesia", "Japan", "India"])
button = Button(root, text = "Show Currency", command = button)

text_country.grid(row = 1, column = 1)
country.grid(row = 1, column = 2)
button.grid(row = 1, column = 3)

root = mainloop()
