from tkinter import *
from tkinter import messagebox # This module provide to create a standart dialogue
import random
import json
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

#---------------------------------SEARCH WEBSITE_---------------------------------#

def search():
    website = wb_entry.get()
    try:
        with open("data.json") as data_file:
            data = json.load(data_file)
            if website in data:
                email = data[website]['e-mail']
                password = data[website]['password']
                messagebox.showinfo(title=website, message=f"email: {email}\npassword: {password}")
            elif website=="":
                messagebox.showinfo(title="Ooops", message="Enter a website for search")
            else:
                messagebox.showinfo(title="Ooops", message="website not found")

    except FileNotFoundError:
        messagebox.showinfo(title="Warning", message="There is no data.")

    except KeyError:
        messagebox.showinfo(title="Warning", message=f"There is no website.")













# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    global letters, numbers, symbols
    password = ""
    nr_letters = random.randint(8, 10)
    nr_numbers = random.randint(2, 4)
    nr_symbols = random.randint(2, 4)


    password_letters = [random.choice(letters) for letter in  range(nr_letters)]
    password_numbers = [random.choice(numbers) for number in range(nr_numbers)]
    password_symbols = [random.choice(symbols) for symbol in range(nr_symbols)]
    password_list = password_letters + password_numbers + password_symbols
    "".join(password_list)
    for char in password_list:
        password += char
    password_entry.insert(END, password)





# ---------------------------- SAVE PASSWORD ------------------------------- #
def add():
    new_data = {
        wb_entry.get(): {
            "e-mail": username_entry.get(),
            "password": password_entry.get()
        }
    }
    if wb_entry.get() == "" or username_entry.get() == "" or password_entry.get() == "":
        messagebox.showwarning(title="Oops", message="Somthing empty")
    else:
        is_ok = messagebox.askokcancel(title="warning",
                                       message=f"WEBSİTE: {wb_entry.get()}\nUSERNAME: {username_entry.get()}\nPASSWORD: {password_entry.get()}")
        if is_ok:
            try:
                with open("data.json", "r") as data_file:
                    # Reading old data
                    data = json.load(data_file)
            except FileNotFoundError:
                with open("data.json", "w") as data_file:
                    json.dump(new_data, data_file)
            else:
                # updating old data with new data
                data.update(new_data)

                with open("data.json", "w") as data_file:
                    # To save new date as json structure
                    json.dump(data, data_file, indent=4)
            finally:
                wb_entry.delete(0, END)
                username_entry.delete(0, END)
                password_entry.delete(0, END)
                wb_entry.focus()








# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.minsize(width=550, height=500)
window.maxsize(width=550, height=500)
window.config(padx=50, pady=50, )

#create a canvas for logo
canvas = Canvas(width=200, height=200)
logo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo)
canvas.pack()
# Create to labels for UI
wb_label = Label(text="Website:", font=("Arial",12, "bold"))
wb_label.place(x=30, y=250)

username_label = Label(text="Email/Username:", font=("Arial", 12, "bold"))
username_label.place(x=30, y=280)

password_label = Label(text="Password:", font=("Arial", 12, "bold"))
password_label.place(x=30, y=310)

# create entries for UI
wb_entry = Entry(width=33)
wb_entry.focus()
wb_entry.place(x=108, y=253)


username_entry = Entry(width=43)
username_entry.place(x=170, y=283)

password_entry = Entry(width=30)
password_entry.place(x=123, y=313)


search_entry = Entry(width=43)


# Create buttons for UI
generate_button = Button(text="Generate", width=15, height=-8, command=generate_password)
generate_button.place(x=327, y=311)

add_button = Button(text="Add", width=56, command=add)
add_button.place(x=40, y=355)


search_button = Button(text="Search", width=15, height=1, command=search)
search_button.place(x=320, y=251, height = 20)

window.mainloop()