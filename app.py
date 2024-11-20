import tkinter as tk


class MyApp:
    def __init__(self) -> None:
        self.root = tk.Tk()
        self.root.title("Certus milling machine App")
        self.root.geometry("300x200+100+100")

        for i in range(0,4):
            self.root.rowconfigure(i, weight=1)
        self.root.columnconfigure(0, weight=1)

        self.dfc_name_frame = tk.Frame(self.root)
        self.dfc_name_frame.grid(row=0, column=0, sticky="nsew")
        self.dfc_name_frame.columnconfigure(0, weight=1)
        self.dfc_name_frame.columnconfigure(1, weight=1)
        self.dfc_name_frame.rowconfigure(0, weight=1)

        self.amount_of_dfc = tk.Frame(self.root)
        self.amount_of_dfc.grid(row=1, column=0, sticky="nsew")
        self.amount_of_dfc.columnconfigure(0, weight=1)
        self.amount_of_dfc.columnconfigure(1, weight=1)
        self.amount_of_dfc.rowconfigure(0, weight=1)

        self.top_bot = tk.Frame(self.root)
        self.top_bot.grid(row=2, column=0, sticky="nsew")
        self.top_bot.columnconfigure(0, weight=1)
        self.top_bot.columnconfigure(1, weight=1)
        self.top_bot.rowconfigure(0, weight=1)
        
        self.buttons = tk.Frame(self.root)
        self.buttons.grid(row=3, column=0, sticky="nsew")
        self.buttons.columnconfigure(0, weight=1)
        self.buttons.columnconfigure(1, weight=1)
        self.buttons.columnconfigure(2, weight=1)
        self.buttons.rowconfigure(0, weight=1)
        
        self.check_top = tk.IntVar()
        self.check_bot = tk.IntVar()

        self.create_widgets()

    def create_widgets(self):
        self.dfc_name_label = tk.Label(self.dfc_name_frame, text="First DFC name:")
        self.dfc_name_label.grid(column=0, row=0, padx=5, pady=5, sticky="nw")
        self.dfc_name_entry = tk.Entry(self.dfc_name_frame, width=30)
        self.dfc_name_entry.grid(column=1, row=0, padx=5, pady=5, sticky="ne")

        self.dfc_amount_label = tk.Label(self.amount_of_dfc, text="DFC Amount:")
        self.dfc_amount_label.grid(column=0, row=0, padx=5, pady=5, sticky="nw")
        self.spinbox_amount = tk.Spinbox(self.amount_of_dfc, from_=0, to=10)
        self.spinbox_amount.grid(column=1, row=0, padx=5, pady=5, sticky="ne")

        self.top = tk.Checkbutton(self.top_bot, text="Top", variable=self.check_top)
        self.top.grid(column=0, row=0, padx=5, pady=5, sticky="nsew")
        self.bot = tk.Checkbutton(self.top_bot, text="Bot", variable=self.check_bot)
        self.bot.grid(column=1, row=0, padx=5, pady=5, sticky="nsew")

        self.map = tk.Button(self.buttons, text="Map", command=self.start_map)
        self.map.grid(column=0, row=0, padx=5, pady=5, sticky="nsew")
        self.milling = tk.Button(self.buttons, text="Milling")
        self.milling.grid(column=1, row=0, padx=5, pady=5, sticky="nsew")
        self.position = tk.Button(self.buttons, text="Set Position")
        self.position.grid(column=2, row=0, padx=5, pady=5, sticky="nsew")

    def start_map(self):
        self.dfc_name = self.dfc_name_entry.get()
        self.dfc_amount = self.spinbox_amount.get()
        if self.dfc_name and self.dfc_amount:
            pass
        

    def run(self):
        self.root.mainloop()


if __name__ == "__main__":
    app = MyApp()
    app.run()
