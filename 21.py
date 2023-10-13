from tkinter import *
root=Tk()
root.title("Adition")
root.geometry("600x600")
input_box = Entry(root)
input_box.pack()

def addition():
    number = 5
    get_input = input_box.get()
    try:
        print(number + get_input)
    except(TypeError):
            messagebox.showinfo("Error", "Cannot add two different data types: integer and string")

button = Button(root , text= "addition", command = addition)
button.pack()
root.mainloop()