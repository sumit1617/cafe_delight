from tkinter import *


class Welcome:

    def __init__(self):
        self.welcome = Tk()
        self.welcome.title("Welcome to Coffee Maker")
        self.welcome.config(padx=50, pady=50, bg="#2B0F0E")

        # Welcome label
        self.welcome_label = Label(text="Welcome to Cafe Delight", font=("Comics", 25, "bold"), fg="#2B0F0E")
        self.welcome_label.place(x=100, y=-50)

        self.canvas = Canvas(width=700, height=575, bg="#ae7d5b", highlightthickness=0)
        self.welcome_logo = PhotoImage(file="Images/6-2-coffee-png-hd.png")
        self.canvas.create_image(400, 250, image=self.welcome_logo)
        self.canvas.grid(column=2, row=3)

        # next button
        self.next_button = Button(text="NEXT➡", font=("Times New Roman", 15, "bold"), highlightthickness=0, bg="#ae7d5b",
                             fg="#2B0F0E", width=15, command=self.next_page)
        self.next_button.grid(column=3, row=3)

        # Emoji
        self.coffee_emoji = Label(text="☕", font=("Times New Roman", 75, "bold"), fg="#ae7d5b", bg="#2B0F0E")
        self.coffee_emoji.place(x=725, y=75)
        self.cookie_emoji = Label(text="🍪", font=("Times New Roman", 75, "bold"), fg="#ae7d5b", bg="#2B0F0E")
        self.cookie_emoji.place(x=725, y=375)

        self.welcome.mainloop()

    def next_page(self):
        self.welcome.destroy()
        from user_details import UserDetails
        users_details = UserDetails()








# How to get the coordinates of x and y
# def motion(event):
#     x, y = event.x, event.y
#     print('{}, {}'.format(x, y))
#
#
# welcome.bind('<Motion>', motion)
