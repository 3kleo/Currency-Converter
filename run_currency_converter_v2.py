# OOP project
# GUI version


import requests
from tkinter import *
from tkinter import ttk
import tkinter.messagebox


class Converter:
    def __init__(self):
        self.base_currency = None
        self.base_amount = None
        self.converted_currency = None
        self.result_amount = None
        self.f_base_currency = None
        self.f_base_amount = None
        self.f_converted_currency = None
        self.url = None
        self.e3 = None
        with open('currencies.txt', 'r') as a:
            self.currencies = a.read().replace('\n', '').split(',')

    def generate_gui(self):
        master = Tk(className=" Your Currency Converter")
        master.option_add("*Font", "Calibri")
        bg_color = '#dff9fb'
        master.configure(background=bg_color)
        master.geometry("700x250")

        Label(master, text='Base Currency', bg=bg_color).grid(row=0)
        self.base_currency = StringVar(master)
        self.base_currency.set(self.currencies[self.currencies.index('USD')])

        Label(master, text='Converted Currency', bg=bg_color).grid(row=1)
        self.converted_currency = StringVar(master)
        self.converted_currency.set(self.currencies[self.currencies.index('BRL')])

        Label(master, text='Value', bg=bg_color).grid(row=0, column=2)
        Label(master, text='Value', bg=bg_color).grid(row=1, column=2)
        e1 = ttk.Combobox(master, textvariable=self.base_currency, values=self.currencies)
        e2 = ttk.Combobox(master, textvariable=self.converted_currency, values=self.currencies)
        self.base_amount = StringVar(master)
        self.e3 = Entry(master, textvariable=self.base_amount, justify='center')
        self.e3.insert(END, 1)  # default value
        # e4 = Entry(master, justify='center')
        self.result_amount = StringVar(master)
        Label(master, text='a', textvariable=self.result_amount, justify='center', bg=bg_color).grid(row=1, column=3)

        e1.grid(row=0, column=1)
        e2.grid(row=1, column=1)
        self.e3.grid(row=0, column=3)

        button = Button(master, text="Convert", command=self.button_click, width=20, bg=bg_color)
        button.place(x=250, y=100)
        mainloop()

    def button_click(self):
        if self.validate_values():
            self.convert_values()
        else:
            self.input_warning()

    def validate_values(self):
        self.f_base_currency = self.base_currency.get()
        self.f_base_amount = self.base_amount.get()
        self.f_converted_currency = self.converted_currency.get()
        try:
            int(self.f_base_amount)
            if int(self.f_base_amount) == 0:
                return False
            else:
                return True
        except ValueError:
            try:
                float(self.f_base_amount.replace(',', '.'))
                self.f_base_amount = self.f_base_amount.replace(',', '.')
                return True
            except ValueError:
                return False

    def convert_values(self):
        r = requests.get(f'https://api.exchangerate-api.com/v4/latest/{self.f_base_currency}').json()
        rate = r['rates'][self.f_converted_currency]
        result = f'{float(self.f_base_amount) * rate:.2f}'
        #         e4.delete(0, 'end')
        #         e4.insert(0, result)
        #         result_amount.delete(0, 'end')
        self.result_amount.set(result)

    def input_warning(self):
        tkinter.messagebox.showerror(title="Error!", message="Invalid input")
        self.e3.delete(0, 'end')
        self.e3.insert(END, 1)


if __name__ == "__main__":
    c = Converter()
    c.generate_gui()
