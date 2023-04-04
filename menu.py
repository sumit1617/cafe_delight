from cart import *
from tkinter import *


rupees = "₹"

class Menu:

    def __init__(self):
        self.menu = Tk()
        self.menu.title("Menu")
        self.menu.config(padx=5, pady=5, bg="#ae7d5b")


        # Coffee 1
        self.coffee_1 = Canvas(width=250, height=275, bg="#ae7d5b", highlightthickness=0)
        self.menu1_logo = PhotoImage(file="Images/coffee_1.png")
        self.coffee_1.create_image(150, 100, image=self.menu1_logo)
        self.coffee_1.grid(column=0, row=0)
        self.latte_label = Label(text=f"Latte = {rupees}250", font=("Times New Roman", 15, "bold"),
                                 highlightthickness=0, bg="#2B0F0E", fg="white")
        self.latte_label.place(x=175, y=210)


        self.add1_button = Button(text="➕", font=("Times New Roman", 15, "bold"), highlightthickness=0, bg="#2B0F0E",
                                  fg="white", command=latte_plus_price)
        self.add1_button.place(x=125, y=150)
        self.minus1_button = Button(text="➖", font=("Times New Roman", 15, "bold"), highlightthickness=0, bg="#2B0F0E",
                                    fg="white", command=latte_minus_price)
        self.minus1_button.place(x=300, y=150)


        # Coffee 2
        self.coffee_2 = Canvas(width=325, height=275, bg="#ae7d5b", highlightthickness=0)
        self.menu2_logo = PhotoImage(file="Images/coffee_2.png")
        self.coffee_2.create_image(150, 100, image=self.menu2_logo)
        self.coffee_2.grid(column=1, row=0)
        self.cold_coffee = Label(text=f"Cold Coffee = {rupees}200", font=("Times New Roman", 15, "bold"),
                                 highlightthickness=0, bg="#2B0F0E", fg="white")
        self.cold_coffee.place(x=570, y=210)
        self.add2_button = Button(text="➕", font=("Times New Roman", 15, "bold"), highlightthickness=0, bg="#2B0F0E",
                                  fg="white", command=cold_coffee_plus_price)
        self.add2_button.place(x=535, y=150)
        self.minus2_button = Button(text="➖", font=("Times New Roman", 15, "bold"), highlightthickness=0, bg="#2B0F0E",
                                    fg="white", command=cold_coffee_minus_price)
        self.minus2_button.place(x=720, y=150)



        # Coffee 3
        self.coffee_3 = Canvas(width=325, height=275, bg="#ae7d5b", highlightthickness=0)
        self.menu3_logo = PhotoImage(file="Images/coffee_3.png")
        self.coffee_3.create_image(150, 100, image=self.menu3_logo)
        self.coffee_3.grid(column=2, row=0)
        self.cappuccino_label = Label(text=f"Cappuccino = {rupees}300", font=("Times New Roman", 15, "bold"),
                                      highlightthickness=0, bg="#2B0F0E", fg="white")
        self.cappuccino_label.place(x=1000, y=210)
        self.add3_button = Button(text="➕", font=("Times New Roman", 15, "bold"), highlightthickness=0, bg="#2B0F0E",
                                  fg="white", command=cappuccino_plus_price)
        self.add3_button.place(x=925, y=150)
        self.minus3_button = Button(text="➖", font=("Times New Roman", 15, "bold"), highlightthickness=0, bg="#2B0F0E",
                                    fg="white", command=cappuccino_minus_price)
        self.minus3_button.place(x=1200, y=150)


        # Cookies
        self.cookies = Canvas(width=425, height=250, bg="#ae7d5b", highlightthickness=0)
        self.menu4_logo = PhotoImage(file="Images/cookies_1.png")
        self.cookies.create_image(150, 100, image=self.menu4_logo)
        self.cookies.grid(column=0, row=2)
        self.cookies_label = Label(text=f"Choco Cookies = {rupees}150", font=("Times New Roman", 15, "bold"),
                                   highlightthickness=0, bg="#2B0F0E", fg="white")
        self.cookies_label.place(x=55, y=490)
        self.add4_button = Button(text="➕", font=("Times New Roman", 15, "bold"), highlightthickness=0, bg="#2B0F0E",
                                  fg="white", command=cookies_plus_price)
        self.add4_button.place(x=0, y=440)
        self.minus4_button = Button(text="➖", font=("Times New Roman", 15, "bold"), highlightthickness=0, bg="#2B0F0E",
                                    fg="white", command=cookies_minus_price)
        self.minus4_button.place(x=260, y=440)


        # Pizza
        self.pizza = Canvas(width=475, height=250, bg="#ae7d5b", highlightthickness=0)
        self.menu5_logo = PhotoImage(file="Images/pizza.png")
        self.pizza.create_image(150, 100, image=self.menu5_logo)
        self.pizza.grid(column=1, row=2)
        self.pizza_label = Label(text=f"Pizza = {rupees}400", font=("Times New Roman", 15, "bold"),
                                 highlightthickness=0, bg="#2B0F0E", fg="white")
        self.pizza_label.place(x=500, y=490)
        self.add5_button = Button(text="➕", font=("Times New Roman", 15, "bold"), highlightthickness=0, bg="#2B0F0E",
                                  fg="white", command=pizza_plus_price)
        self.add5_button.place(x=378, y=440)
        self.minus5_button = Button(text="➖", font=("Times New Roman", 15, "bold"), highlightthickness=0, bg="#2B0F0E",
                                    fg="white", command=pizza_minus_price)
        self.minus5_button.place(x=732, y=440)


        # Sandwich
        self.sandwich = Canvas(width=400, height=250, bg="#ae7d5b", highlightthickness=0)
        self.menu6_logo = PhotoImage(file="Images/sandwich.png")
        self.sandwich.create_image(150, 100, image=self.menu6_logo)
        self.sandwich.grid(column=2, row=2)
        self.sandwich_label = Label(text=f"Sandwich = {rupees}200", font=("Times New Roman", 15, "bold"),
                                    highlightthickness=0, bg="#2B0F0E", fg="white")
        self.sandwich_label.place(x=975, y=485)
        self.add5_button = Button(text="➕", font=("Times New Roman", 15, "bold"), highlightthickness=0, bg="#2B0F0E",
                                  fg="white", command=sandwich_plus_price)
        self.add5_button.place(x=855, y=440)
        self.minus5_button = Button(text="➖", font=("Times New Roman", 15, "bold"), highlightthickness=0, bg="#2B0F0E",
                                    fg="white", command=sandwich_minus_price)
        self.minus5_button.place(x=1202, y=435)

        def cart():
            self.menu.destroy()
            from cart import Cart
            cart_page = Cart()



        # Cart
        cart_button = Button(text="🛒", font=("Times New Roman", 15, "bold"), highlightthickness=0, bg="#2B0F0E",
                             fg="white", command=cart)
        cart_button.place(x=1260, y=490)




        self.menu.mainloop()











# # How to get the coordinates of x and y
# def motion(event):
#     x, y = event.x, event.y
#     print('{}, {}'.format(x, y))
#
#
# window.bind('<Motion>', motion)