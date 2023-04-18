
import tkinter as tk
import requests
from datetime import datetime, timedelta


API_BASE_URL = "https://openexchangerates.org/api/latest.json?app_id=fcc4802daebf4c2d8b2c021296492d91"


def convert_currency():
    # Get users input
    amount = float(amount_entry.get())
    from_currency = str(from_currency_var.get())
    to_currency = str(to_currency_var.get())

    # Fetch currencies from API
    response = requests.get(API_BASE_URL)
    data = response.json()

    # Extract converted amount from API response
    converted_amount = data["rates"][from_currency]
    amt = data["rates"][to_currency]
    print(converted_amount)
    print(amt)

    # Update result label
    result_label.config(text=f"Converted Amount: {(amt / converted_amount) * amount}")


def reset():
    amount_entry.delete(0, tk.END)
    from_currency_var.set("")
    to_currency_var.set("")
    result_label.config(text="")






# Create main window
root = tk.Tk()
root.title("Currency Converter")
root.geometry("500x600")
root.configure(bg="gray")

# Create input fields
label = tk.Label(root, text="Currency Converter", font=("Arial", 32), bg="#404040", fg="white")
label.place(x=20, y=20)
amount_label = tk.Label(root, text="Amount:", font=("Arial", 25))
amount_label.place(x=20, y=80)
amount_entry = tk.Entry(root, font=("Arial", 18))
amount_entry.place(x=20, y=120)

from_currency_label = tk.Label(root, text="From Currency:", font=("Arial", 18))
from_currency_label.place(x=20, y=200)
from_currency_var = tk.StringVar(root)
from_currency_var.set("Choose")
from_currency_dropdown = tk.OptionMenu(root, from_currency_var, "USD", "EUR", "GBP", "JPY", "CAD", "PKR")
from_currency_dropdown.config(width=5)
from_currency_dropdown.place(x=20, y=230)

to_currency_label = tk.Label(root, text="To  Currency:", font=("Arial", 18))
to_currency_label.place(x=20, y=280)
to_currency_var = tk.StringVar(root)
to_currency_var.set("Choose")
to_currency_dropdown = tk.OptionMenu(root, to_currency_var, "USD", "EUR", "GBP", "JPY", "CAD", "PKR")
to_currency_dropdown.config(width=5)
to_currency_dropdown.place(x=20, y=310)

# Create buttons
convert_button = tk.Button(root, text="Convert", font=("Arial", 24), bg="orange red", command=convert_currency)
convert_button.place(x=320, y=310)

reset_button = tk.Button(root, text="Reset", font=("Arial", 20), bg="orange red", command=reset)
reset_button.place(x=320, y=360)


result_label = tk.Label(root, text="",font=("Arial",16),bg="Gray50")
result_label.place(x=20, y=360)

# GUI event loop
root.mainloop()