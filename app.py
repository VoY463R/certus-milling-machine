import tkinter as tk
from tkinter import messagebox
import time
from app_func import create_list
from actions import PositionControl


class MyApp:
    def __init__(self) -> None:
        """
        Initialization of the application window with the configuration of frames.
        """
        self.root = tk.Tk()
        self.root.title("Certus milling machine App")
        self.root.geometry("300x200+100+100")

        for i in range(0, 4):
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
        self.buttons.rowconfigure(1, weight=1)

        self.check_top = tk.IntVar()
        self.check_bot = tk.IntVar()
        
        self.mouse_controlling = PositionControl()

        self.create_widgets()

    def create_widgets(self):
        """
        Creation of widgets responsible for providing the necessary data for milling machine processing.
        """
        self.dfc_name_label = tk.Label(self.dfc_name_frame, text="First DFC name:")
        self.dfc_name_label.grid(column=0, row=0, padx=5, pady=5, sticky="nw")
        self.dfc_name_entry = tk.Entry(self.dfc_name_frame, width=30)
        self.dfc_name_entry.grid(column=1, row=0, padx=5, pady=5, sticky="ne")

        self.dfc_amount_label = tk.Label(self.amount_of_dfc, text="DFC Amount:")
        self.dfc_amount_label.grid(column=0, row=0, padx=5, pady=5, sticky="nw")
        self.spinbox_amount = tk.Spinbox(self.amount_of_dfc, from_=1, to=10)
        self.spinbox_amount.grid(column=1, row=0, padx=5, pady=5, sticky="ne")

        self.top = tk.Checkbutton(self.top_bot, text="Top", variable=self.check_top)
        self.top.grid(column=0, row=0, padx=5, pady=5, sticky="nsew")
        self.bot = tk.Checkbutton(self.top_bot, text="Bot", variable=self.check_bot)
        self.bot.grid(column=1, row=0, padx=5, pady=5, sticky="nsew")

        self.position_timer = tk.Label(self.buttons, text="")
        self.position_timer.grid(columnspan=3, row=0, padx=5, pady=5, sticky="nsew")
        
        self.dfc_list_button = tk.Button(
            self.buttons, text="Generate DFC list", command=self.create_list
        )
        self.dfc_list_button.grid(columnspan=3, row=1, padx=5, pady=5, sticky="nsew")
        self.map = tk.Button(self.buttons, text="Map", command=self.mapping_proccess)
        self.map.grid(column=0, row=2, padx=5, pady=5, sticky="nsew")
        self.milling = tk.Button(self.buttons, text="Milling")
        self.milling.grid(column=1, row=2, padx=5, pady=5, sticky="nsew")
        self.position = tk.Button(self.buttons, text="Set Position", command=self.position_getter)
        self.position.grid(column=2, row=2, padx=5, pady=5, sticky="nsew")

    def position_getter(self):
        """
        Determine the position of the mouse cursor. Returns the value of x and y coordinates and writes to the variable mouse_position_x, mouse_position_y.
        """
        for i in range(5,0,-1):
            self.position_timer.config(text=f"Determining the position for {i} sec")
            self.root.update()
            time.sleep(1)
        self.mouse_position_x, self.mouse_position_y  = self.mouse_controlling.mouse_position()
        messagebox.showinfo("Mouse Position", f"Position established: (x={self.mouse_position_x}, y={self.mouse_position_y})")
        self.position_timer.config(text="")
        
    def mapping_proccess(self):
        """
        Call function for fuel cells mapping
        """
        try:
            self.dfc_list
            pass
        except Exception as e:
            messagebox.showerror("List error", f"There was a problem with the list of fuel cells: {e}")
            return
        self.mouse_controlling.mapping(self.dfc_list)
            
    def milling_proccess(self):
        """
        Call function for fuel cells milling
        """
        try:
            self.dfc_list
            pass
        except Exception as e:
            messagebox.showerror("List error", f"There was a problem with the list of fuel cells: {e}")
            return
        self.mouse_controlling.milling(self.dfc_list)
            
    def create_list(self):
        """
        Create a list of dfc cells based on the options selected in the application.
        """
        self.dfc_list = create_list(self.dfc_name_entry, self.spinbox_amount, self.check_top, self.check_bot)

    def run(self):
        """
        Launching the Application GUI.
        """
        self.root.mainloop()


if __name__ == "__main__":
    app = MyApp()
    app.run()
