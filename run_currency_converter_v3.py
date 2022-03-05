# OOP project
# GUI version


import requests
from tkinter import *
from tkinter import ttk
import tkinter.messagebox


class Converter:
    def __init__(self):
        self.text_result_amount = None
        self.base_currency = None
        self.base_amount = None
        self.converted_currency = None
        self.result_amount = None
        self.f_base_currency = None
        self.f_base_amount = None
        self.f_converted_currency = None
        self.url = None
        self.e3 = None
        self.currencies = sorted(list(requests.get('https://api.exchangerate-api.com/v4/latest/BOB').json()['rates'].keys()))

    def generate_gui(self):
        master = Tk(className=" Your Currency Converter")
        master.option_add("*Font", "Calibri")
        bg_color = '#202040'
        fg_color = '#FFBD69'
        master.configure(background=bg_color)
        # master.configure(font=(family='Helvetica', size=14, weight='', fg='#0059b3'))
        canvas = Canvas(master, height=250, width=700, highlightthickness=0, relief='ridge')
        canvas.pack()
        canvas.configure(background=bg_color)

        amount_rel_x = 0.03
        amount_rel_height = 0.1
        amount_rel_width = 0.25

        Label(master, text='Amount', bg=bg_color, fg=fg_color).place(relx=amount_rel_x, rely=0.1,
                                                                     relheight=amount_rel_height,
                                                                     anchor='nw')
        self.base_currency = StringVar(master)
        self.base_currency.set(self.currencies[self.currencies.index('USD')])
        self.base_amount = StringVar(master)
        self.e3 = Entry(master, textvariable=self.base_amount, justify='center')
        self.e3.insert(END, 1)  # default value
        self.e3.place(relx=amount_rel_x, rely=0.1 + amount_rel_height, relwidth=amount_rel_width)

        from_rel_x = (amount_rel_x + amount_rel_width) * 1.05
        from_rel_height = 0.1
        from_rel_width = 0.25

        Label(master, text='From', bg=bg_color, fg=fg_color).place(relx=from_rel_x, rely=0.1, relheight=from_rel_height,
                                                                   anchor='nw')
        e1 = ttk.Combobox(master, textvariable=self.base_currency, values=self.currencies)
        e1.place(relx=from_rel_x, rely=0.1 + from_rel_height, relwidth=from_rel_width,
                 anchor='nw')

        to_rel_x = (from_rel_x + from_rel_width) * 1.05
        to_rel_height = 0.1
        to_rel_width = 0.25

        Label(master, text='To', bg=bg_color, fg=fg_color).place(relx=to_rel_x, rely=0.1, relheight=to_rel_height,
                                                                 anchor='nw')
        self.converted_currency = StringVar(master)
        self.converted_currency.set(self.currencies[self.currencies.index('BRL')])
        e2 = ttk.Combobox(master, textvariable=self.converted_currency, values=self.currencies)
        e2.place(relx=to_rel_x, rely=0.1 + to_rel_height, relwidth=to_rel_width,
                 anchor='nw')

        button_rel_x = (to_rel_x + to_rel_width) * 1.02
        button_rel_height = 32
        button_rel_width = 0.15

        button = Button(master, text="Convert", command=self.button_click, width=20, bg='#543864', fg=fg_color)
        button.place(relx=button_rel_x, rely=0.1 + to_rel_height, relwidth=button_rel_width,
                     height=button_rel_height, anchor='nw')

        self.text_result_amount = StringVar(master)
        Label(master, text='', textvariable=self.text_result_amount, justify='center', bg=bg_color, fg=fg_color).place(
            relx=amount_rel_x,
            rely=0.5,
            relheight=amount_rel_height,
            anchor='nw')
        self.result_amount = StringVar(master)
        Label(master, text='', textvariable=self.result_amount, justify='center', bg=bg_color, fg=fg_color,
              font=("Calibri", 30)).place(relx=amount_rel_x,
                                          rely=0.5 + amount_rel_height,
                                          relheight=amount_rel_height * 2,
                                          anchor='nw')
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
        result_top = f'{float(self.f_base_amount):,.2f} {self.f_base_currency} ='
        result_bottom = f'{float(self.f_base_amount) * rate:,.2f} {self.f_converted_currency}'
        #         e4.delete(0, 'end')
        #         e4.insert(0, result)
        #         result_amount.delete(0, 'end')
        self.text_result_amount.set(result_top)
        self.result_amount.set(result_bottom)

    def input_warning(self):
        tkinter.messagebox.showerror(title="Error!", message="Invalid input")
        self.e3.delete(0, 'end')
        self.e3.insert(END, 1)


if __name__ == "__main__":
    c = Converter()
    c.generate_gui()
