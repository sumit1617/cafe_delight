import json
from tkinter import *
from tkinter import messagebox
from user_details import *

rupees = "₹"

# Latte
latte_price = 0
l_quantity = 0


def latte_plus_price():
    global latte_price, l_quantity
    l_quantity += 1
    latte_price += 250


def latte_minus_price():
    global latte_price, l_quantity
    if latte_price <= 0 and l_quantity <= 0:

        pass
    else:
        l_quantity -= 1
        latte_price -= 250


# Colf Coffee
cold_coffee = 0
cc_quantity = 0


def cold_coffee_plus_price():
    global cold_coffee, cc_quantity
    cc_quantity += 1
    cold_coffee += 200


def cold_coffee_minus_price():
    global cold_coffee, cc_quantity
    if cold_coffee <= 0 and cc_quantity <= 0:
        pass
    else:
        cc_quantity -= 1
        cold_coffee -= 200


# Cappuccino
cappuccino = 0
cp_quantity = 0


def cappuccino_plus_price():
    global cappuccino, cp_quantity
    cp_quantity += 1
    cappuccino += 300


def cappuccino_minus_price():
    global cappuccino, cp_quantity
    if cappuccino <= 0 and cp_quantity <= 0:
        pass
    else:
        cp_quantity -= 1
        cappuccino -= 300


# Cookies
cookies = 0
co_quantity = 0


def cookies_plus_price():
    global cookies, co_quantity
    co_quantity += 1
    cookies += 150


def cookies_minus_price():
    global cookies, co_quantity
    if cookies <= 0 and co_quantity <= 0:
        pass
    else:
        co_quantity -= 1
        cookies -= 150


# Pizza
pizza = 0
p_quantity = 0


def pizza_plus_price():
    global pizza, p_quantity
    p_quantity += 1
    pizza += 400


def pizza_minus_price():
    global pizza, p_quantity
    if pizza <= 0 and p_quantity <= 0:
        pass
    else:
        p_quantity -= 1
        pizza -= 400


# Sandwich
sandwich = 0
s_quantity = 0


def sandwich_plus_price():
    global sandwich, s_quantity
    s_quantity += 1
    sandwich += 200


def sandwich_minus_price():
    global sandwich, s_quantity
    if sandwich <= 0 and s_quantity <= 0:
        pass
    else:
        s_quantity -= 1
        sandwich -= 200


# Total Price
total = 0


def total_price():
    global latte_price, cold_coffee, cappuccino, cookies, pizza, sandwich, total, rupees
    total = latte_price + cold_coffee + cappuccino + cookies + pizza + sandwich
    total_label = Label(text=f"Total Price = {rupees}{total}", font=("Times New Roman", 30, "bold"),
                        fg="#ae7d5b", bg="#2B0F0E")
    total_label.place(x=550, y=500)


class Cart:

    def __init__(self):
        self.latte = 0
        self.cart = Tk()
        self.cart.title("Cart")
        self.cart.minsize(width=1000, height=600)
        self.cart.config(padx=10, pady=10, bg="#ae7d5b")
        self.cart_label = Label(text="Your Food Cart 🛒😊", font=("Times New Roman", 45, "bold"), highlightthickness=0,
                                bg="#ae7d5b", fg="#2B0F0E")
        self.cart_label.place(x=250, y=0)

        def menu():
            self.cart.destroy()
            from menu import Menu
            menu_page = Menu()

        self.menu_button = Button(text="Go back To Menu", font=("Times New Roman", 15, "bold"), highlightthickness=0,
                                  bg="#2B0F0E",
                                  fg="white", command=menu)
        self.menu_button.place(x=50, y=100)

        # Latte
        self.latte = Label(text=f"latte = {l_quantity} x {rupees}250 = {rupees}{latte_price}",
                           font=("Times New Roman", 25, "bold"), highlightthickness=0, bg="#2B0F0E", fg="white")
        if latte_price <= 0 and l_quantity <= 0:
            self.latte.destroy()
        else:
            self.latte.place(x=125, y=150)

        # Cold Coffee
        self.cold_coffee = Label(text=f"Cold Coffee = {cc_quantity} x {rupees}200 = {rupees}{cold_coffee}",
                                 font=("Times New Roman", 30, "bold"), highlightthickness=0, bg="#2B0F0E", fg="white")
        if cold_coffee <= 0 and cc_quantity <= 0:
            self.cold_coffee.destroy()
        else:
            self.cold_coffee.place(x=125, y=200)

        # Cappuccino
        self.cappuccino = Label(text=f"Cappuccino = {cp_quantity} x {rupees}300 = {rupees}{cappuccino}",
                                font=("Times New Roman", 30, "bold"), highlightthickness=0, bg="#2B0F0E", fg="white")
        if cappuccino <= 0 and cp_quantity <= 0:
            self.cappuccino.destroy()
        else:
            self.cappuccino.place(x=125, y=260)

        # Cookies
        self.cookies = Label(text=f"Choco Cookies = {co_quantity} x {rupees}150 = {rupees}{cookies}",
                             font=("Times New Roman", 30, "bold"), highlightthickness=0, bg="#2B0F0E", fg="white")
        if cookies <= 0 and co_quantity <= 0:
            self.cookies.destroy()
        else:
            self.cookies.place(x=125, y=320)

        # Pizza
        self.pizza = Label(text=f"Pizza = {p_quantity} x {rupees}400 = {rupees}{pizza}",
                           font=("Times New Roman", 30, "bold"), highlightthickness=0, bg="#2B0F0E", fg="white")
        if pizza <= 0 and p_quantity <= 0:
            self.pizza.destroy()
        else:
            self.pizza.place(x=125, y=380)

        # Sandwich
        self.sandwich = Label(text=f"Sandwich = {s_quantity} x {rupees}200 = {rupees}{sandwich}",
                              font=("Times New Roman", 30, "bold"), highlightthickness=0, bg="#2B0F0E", fg="white")
        if sandwich <= 0 and s_quantity <= 0:
            self.sandwich.destroy()
        else:
            self.sandwich.place(x=125, y=440)

        # Total
        self.total_button = Button(text="Total", font=("Times New Roman", 15, "bold"), highlightthickness=0,
                                   bg="#2B0F0E", fg="white", command=total_price)
        self.total_button.place(x=800, y=100)

        # Deliver
        def deliver():
            if total == 0:
                messagebox.showinfo(title="Oops", message=f"Make sure that you cart is doesn't empty ")
            else:
                self.cart.destroy()
                import delivery

        self.delivery = Button(text="Place the Order", font=("Times New Roman", 15, "bold"), highlightthickness=0,
                               bg="#2B0F0E", fg="white", command=deliver)
        self.delivery.place(x=800, y=350)

        self.cart.mainloop()
