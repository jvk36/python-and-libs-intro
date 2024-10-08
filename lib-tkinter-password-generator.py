from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = [random.choice(letters) for _ in range(nr_letters)]
    password_list += [random.choice(symbols) for _ in range(nr_symbols)]
    password_list += [random.choice(numbers) for _ in range(nr_numbers)]

    random.shuffle(password_list)

    password = "".join(password_list)

    # print(f"Your password is: {password}")
    password_entry.delete(0, "end")
    password_entry.insert(0, password)
    pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }

    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please don't leave any fields empty")
    else:
        try:
            with open("./data/password-data.json", "r") as file:
                data = json.load(file)
        except FileNotFoundError:
            with open("./data/password-data.json", "w") as file:
                json.dump(new_data, file, indent=4)
        else:
            data.update(new_data)
            with open("./data/password-data.json", "w") as file:
                json.dump(data, file, indent=4)
        finally:
            website_entry.delete(0, "end")
            password_entry.delete(0, "end")
            website_entry.focus()
            # file.write(f"{website} | {email} | {password}\n")


# ---------------------------- SEARCH ------------------------------- #


def search_entry():
    website = website_entry.get()
    try:
        with open("./data/password-data.json", "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        messagebox.showinfo("Error", "No Data File Found.")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(website, f"Email: {email}\nPassword: {password}")
        else:
            messagebox.showinfo("Error", "No details for the website exists.")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
logo = PhotoImage(file="./images/password-logo.png")
canvas.create_image(100, 95, image=logo)
canvas.grid(row=0, column=1)

label = Label(text="Website:")
label.grid(row=1, column=0)

website_entry = Entry(width=30)
website_entry.grid(row=1, column=1)
website_entry.focus()

search_button = Button(text="Search", width=15, command=search_entry)
search_button.grid(row=1, column=2)

label = Label(text="Email/Username:")
label.grid(row=2, column=0)

email_entry = Entry(width=50)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0, "JohnKonnayilVincent@gmail.com")

label = Label(text="Password:")
label.grid(row=3, column=0)

password_entry = Entry(width=30)
password_entry.grid(row=3, column=1)

generate_button = Button(text="Generate Password", width=15, command=generate_password)
generate_button.grid(row=3, column=2)

add_button = Button(text="Add", width=45, command=save)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
