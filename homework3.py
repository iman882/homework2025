import tkinter as tk
class Model(object):
    def __init__(self,celsius,fahrenheit):
        self.celsius=celsius
        self.fahrenheit=fahrenheit
    def fahrenheit_to_celsius(self, fahrenheit):
        return (float(fahrenheit) - 32) * 5 / 9
class View:
    def __init__(self, window):
        self.frame_fahrenheit = tk.Frame(master=window)
        self.frame_fahrenheit.grid(row=0, column=0, padx=15)

        self.label_temp = tk.Label(master=self.frame_fahrenheit, text="Fahrenheit:")
        self.label_temp.grid(row=0, column=0, padx=10, pady=15)

        self.entry_temp = tk.Entry(master=self.frame_fahrenheit)
        self.entry_temp.grid(row=0, column=1, padx=15, pady=15)

        self.button_conv = tk.Button(master=self.frame_fahrenheit, text="Convert to Celsius")
        self.button_conv.grid(row=0, column=2, padx=10)

        self.label_result = tk.Label(master=self.frame_fahrenheit, text="\N{DEGREE FAHRENHEIT}")
        self.label_result.grid(row=0, column=3, padx=15)
class Controller:
    def __init__(self, window):
        self.window = window
        self.model = Model()
        self.view = View(window)
        self.view.button_conv.bind("<Button-1>", self.handle_convert)
    def run(self):
        self.window.mainloop()
    def handle_convert(self, event):
        fahrenheit = self.view.entry_temp.get()
        celsius = self.model.fahrenheit_to_celsius(float(fahrenheit))
        self.view.label_result["text"] = "RESULT={:.2f}C".format(celsius)     
if __name__=="__main__":
    window=tk.Tk()
    window.title("Fahrenheit to Celsius converter")
    c=Controller
    window.mainloop()