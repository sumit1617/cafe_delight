from cart import *
from tkinter import *
from datetime import *
import random

delivery_boy = random.choice(["Harshikesh", "Rohan", "Sachin", "Salim"])


delivery = Tk()
delivery.title("Deliver the Food")
delivery.minsize(width=1500, height=750)
delivery.config(padx=10, pady=10, bg="#ae7d5b")

payment = Label(text=f"Pay {rupees}{total} Cash. When you get your food delivered",
                font=("Times New Roman", 40, "bold"), fg="#ae7d5b", bg="#2B0F0E")
payment.place(x=100, y=15)

def order_received():
    order_taken = Label(text=f"At {datetime.now().hour}:{datetime.now().minute} Your order has been received📃.",
                        font=("Times New Roman", 40, "bold"), fg="#ae7d5b", bg="#2B0F0E")
    order_taken.place(x=100, y=200)


def order_prepare():
    order_prepared = Label(text=f"At {datetime.now().hour}:{datetime.now().minute} Your order is being Prepared✔.",
                           font=("Times New Roman", 40, "bold"), fg="#ae7d5b", bg="#2B0F0E")
    order_prepared.place(x=100, y=300)

def order_dispatched():
    order_routed = Label(text=f"At {datetime.now().hour}:{datetime.now().minute} Your order is being "
                              f"Dispatched by {delivery_boy}👦.",
                         font=("Times New Roman", 40, "bold"), fg="#ae7d5b", bg="#2B0F0E")
    order_routed.place(x=100, y=400)

def order_delivered():
    order_deliver = Label(text=f"At {datetime.now().hour}:{datetime.now().minute} Your order is being Delivered😊☺.",
                          font=("Times New Roman", 40, "bold"), fg="#ae7d5b", bg="#2B0F0E")
    order_deliver.place(x=100, y=500)


delivery.after(10000, order_received)
delivery.after(60000, order_prepare)
delivery.after(120000, order_dispatched)
delivery.after(180000, order_delivered)



delivery.mainloop()
