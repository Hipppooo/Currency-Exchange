from tkinter import *
from tkinter import messagebox
from CurrencyModule import *
from Currency import *
from NonPositiveError import NonPositiveError
from locale import atof, LC_NUMERIC, setlocale


class MainView(object):
    def __init__(self):
        self.app_window = Tk()
        self.app_window.title("Przelicznik Walut")
        self.app_window.geometry("320x320")

        # self.app_frame(self.app_window)

        self.currencies = CurrencyModule().get_currencies()
        self.create_widgets()

        self.app_window.mainloop()

    def create_widgets(self):
        self.detault_currency_label = Label()
        self.detault_currency_label["text"] = "Polski złoty"
        self.detault_currency_label.grid(row=0, column=0, sticky=W, pady=5)

        self.default_currency_field = Text(width=25, height=1, background="#ddedfd")
        self.default_currency_field.grid(row=0, column=1, sticky=W, pady=5)

        self.convert_button = Button(text="Konwertuj")
        self.convert_button.grid(row=1, column=0, sticky=W, pady=5, padx=5)
        self.convert_button["command"] = self.convert

        self.clear_button = Button(text="Wyczyść")
        self.clear_button.grid(row=1, column=1, sticky=W, pady=5, padx=5)
        self.clear_button["command"] = self.clear

        self.currency_labels = list()
        self.currency_fields = list()

        for i in range(8):
            self.currency_labels.append(Label())
            self.currency_labels[i]["text"] = self.currencies[i].get_name()
            self.currency_labels[i].grid(row=i + 2, column=0, sticky=W, pady=5)

            self.currency_fields.append(Text(width=25, height=1, state='disabled', background="#ddedfd"))
            self.currency_fields[i].grid(row=i + 2, column=1, sticky=W, pady=5)

    def convert(self):
        self.clear_output()

        try:
            setlocale(LC_NUMERIC, '')
            self.default_currency_value = atof(self.default_currency_field.get(1.0, "end-1c"))
            self.default_currency_value = float(self.default_currency_value)
            if (self.default_currency_value < 0):
                raise NonPositiveError
        except NonPositiveError:
            messagebox.showerror("ERROR", "Liczba nie może być mniejsza od 0")
        except:
            messagebox.showerror("ERROR", "To nie jest liczba!")
            self.clear
        else:
            for i in range(len(self.currency_fields)):
                self.currency_fields[i].configure(state='normal')

                converted_value = self.default_currency_value * self.currencies[i].get_exchange_rate()
                self.currency_fields[i].insert(0.0, round(converted_value, 2))

                self.currency_fields[i].configure(state='disabled')

    def clear(self):
        self.default_currency_field.delete(0.0, END)
        self.clear_output()

    def clear_output(self):
        for i in range(len(self.currency_fields)):
            self.currency_fields[i].configure(state='normal')
            self.currency_fields[i].delete(0.0, END)
            self.currency_fields[i].configure(state='disabled')
