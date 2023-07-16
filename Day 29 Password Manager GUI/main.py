from tkinter import *
from tkinter import messagebox
import pyperclip
import random
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate():
    password_entry.delete(0,END)
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list=[random.choice(letters) for _ in range(nr_letters)]
    password_list += [random.choice(symbols) for char in range(nr_symbols)]
    password_list += [random.choice(numbers) for char in range(nr_numbers)]

    random.shuffle(password_list)

    password="".join(password_list)
    password_entry.insert(0,password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get()
    email=email_entry.get()
    password=password_entry.get()
    if len(website)==0 or len(password)==0:
        messagebox.showinfo(title="Oops", message="Please don't leave any fields empty!")
    else:
        is_ok=messagebox.askokcancel(title=website,message=f"These are the details entered: \nEmail: {email} \nPassword: {password} \nIs it ok to save?")
        if is_ok:
            with open("passwords.txt", "a") as file:
                file.write(website +"|"+email+"|"+password+"\n")
            website_entry.delete(0, END)
            password_entry.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)
canvas = Canvas(width=200, height=200)
photo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=photo)
canvas.grid(column=1, row=0)

website_label = Label(window, text="Website:")
website_label.grid(column=0, row=1)
website_entry = Entry(window, width=35)
website_entry.grid(column=1, row=1,columnspan=2)
website_entry.focus()

email_label = Label(window, text="Email/Username:")
email_label.grid(column=0, row=2)
email_entry = Entry(window, width=35)
email_entry.grid(column=1, row=2,columnspan=2)
email_entry.insert(0,"jaisonemathew@tech")

password_label = Label(window, text="Password:")
password_label.grid(column=0, row=3)
password_entry = Entry(width=19)
password_entry.grid(column=1, row=3)

generate_button = Button(text="Generate password",command=generate)
generate_button.grid(column=2, row=3)

add_button = Button(window, text="Add",width=36,command=save)
add_button.grid(column=1, row=4,columnspan=2)

window.mainloop()