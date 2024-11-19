import tkinter as tk


class MyApp:
    def __init__(self) -> None:
        self.root = tk.Tk()
        self.root.title("Certus milling machine App")
        self.root.geometry("500x300+100+100")

        self.dfc_name = tk.Frame(self.root)
        self.dfc_name.grid(row=0, column=0, sticky="nsew")

        self.amount_of_dfc = tk.Frame(self.root)
        self.amount_of_dfc.grid(row=1, column=0, sticky="nsew")
        
        self.top_bot = tk.Frame(self.root)
        self.top_bot.grid(row=2, column=0, sticky="nsew")

        self.buttons = tk.Frame(self.root)
        self.buttons.grid(row=2, column=0, sticky="nsew")
        
    def run(self):
        self.root.mainloop()


if __name__ == "__main__":
    app = MyApp()
    app.run()
