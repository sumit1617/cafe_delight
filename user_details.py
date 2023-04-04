from tkinter import *
from tkinter import messagebox
import json


class UserDetails:

    def __init__(self):
        self.user_details = Tk()
        self.user_details.title("User Details")
        self.user_details.config(bg="#2B0F0E")
        self.user_details.minsize(1000, 600)

        # Logo
        self.users = Canvas(width=300, height=300, highlightthickness=0, bg="#2B0F0E")
        self.user_logo = PhotoImage(file="Images/285645_user_icon (1).png")
        self.users.create_image(150, 150, image=self.user_logo)
        self.users.place(x=350, y=0)

        # Name
        self.name_label = Label(text="Name : ", font=("Times New Roman", 25, "bold"), fg="#ae7d5b", bg="#2B0F0E")
        self.name_label.place(x=34, y=350)
        self.name_input = Entry(width=50, fg="#2B0F0E", bg="#ae7d5b", font=("Times New Roman", 12, "bold"))
        self.name_input.focus()
        self.name_input.place(x=150, y=365)

        # Mobile
        self.mobile_label = Label(text="Mobile No : ", font=("Times New Roman", 25, "bold"), fg="#ae7d5b", bg="#2B0F0E")
        self.mobile_label.place(x=34, y=425)
        self.mobile_input = Entry(width=25, fg="#2B0F0E", bg="#ae7d5b", font=("Times New Roman", 12, "bold"))
        self.mobile_input.place(x=212, y=438)

        # Address
        self.address_label = Label(text="Address : ", font=("Times New Roman", 25, "bold"), fg="#ae7d5b", bg="#2B0F0E")
        self.address_label.place(x=525, y=400)
        self.address_input = Text(height=5, width=35, fg="#2B0F0E", bg="#ae7d5b", font=("Times New Roman", 12, "bold"))
        self.address_input.place(x=670, y=375)

        # Next
        self.next_button = Button(text="Login", width=15, font=("Times New Roman", 15, "bold"), fg="#2B0F0E",
                                  bg="#ae7d5b", command=self.save)
        self.next_button.place(x=775, y=520)

        # Search
        self.search_button = Button(text="Search", width=15, font=("Times New Roman", 15, "bold"), fg="#2B0F0E",
                                    bg="#ae7d5b", command=self.find_user)
        self.search_button.place(x=600, y=520)
        self.user_details.mainloop()

    def save(self):
        name = self.name_input.get().title()
        mobile_no = self.mobile_input.get()
        address = self.address_input.get("1.0", 'end-1c')
        new_data = {
            mobile_no: {
                "name": name,
                "address": address,
            }
        }

        if len(name) == 0 or len(mobile_no) == 0 or len(address) == 0:
            messagebox.showinfo(title="Oops", message="Please make sure you haven't left anys fields empty.")
        elif any(ch.isdigit() for ch in name):
            messagebox.showinfo(title="Oops", message=f"Please make sure that {name} can't have numbers.")
        elif len(name) <= 2:
            messagebox.showinfo(title="Oops", message=f"Please make sure that {name} is too short.")
        elif len(name) > 20:
            messagebox.showinfo(title="Oops", message=f"Please make sure that {name} is too long.")

        elif len(mobile_no) > 10 or len(mobile_no) < 10:
            messagebox.showinfo(title="Oops", message="Please make sure you haven't fill more or less than 10 digit "
                                                      "in Mobile No")
        elif any(n.isalpha() for n in mobile_no):
            messagebox.showinfo(title="Oops", message=f"Please make sure that your Contact Number {mobile_no} can't have Alphabet.")

        else:
            try:
                with open("Users_Data/data.json", "r") as data_file:
                    # Reading the old data
                    data = json.load(data_file)
            except FileNotFoundError:
                with open("Users_Data/data.json", "w") as data_file:
                    json.dump(new_data, data_file, indent=4)
            else:
                # Updating the Old data with new data
                data.update(new_data)

                with open("Users_Data/data.json", "w") as data_file:
                    # Saving the updated data
                    json.dump(data, data_file, indent=4)
            finally:
                self.name_input.delete(0, END)
                self.mobile_input.delete(0, END)
                self.address_input.delete("1.0", 'end-1c')
                self.user_details.destroy()
                from menu import Menu
                menu_page = Menu()

    def find_user(self):
        phone_no = self.mobile_input.get().title()
        try:
            with open("Users_Data/data.json", "r") as data_file:
                data = json.load(data_file)

        except FileNotFoundError:
            messagebox.showinfo(title="Error", message="No Data File Found.")
        else:
            if phone_no in data:
                name = data[phone_no]["name"]
                address = data[phone_no]["address"]
                self.name_input.insert(0, name)
                self.address_input.insert("1.0", address)
            else:
                messagebox.showinfo(title="Error", message=f"details for phone no {phone_no} doesn't exists.")





# How to get the coordinates of x and y
# def motion(event):
#     x, y = event.x, event.y
#     print('{}, {}'.format(x, y))
# window.bind('<Motion>', motion)