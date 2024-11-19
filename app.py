import tkinter as tk

class MyApp:
    def __init__(self) -> None:
        self.root = tk.Tk()
        self.root.title("Certus milling machine App")
        
    def run(self):
        self.root.mainloop()
        
if __name__ == "__main__":
    app = MyApp()
    app.run()