from tkinter import messagebox

def create_list(dfc_name_entry, spinbox_amount, check_top, check_bot):
    dfc_list = []
    surface = ""
    dfc_name = dfc_name_entry.get()
    if len(dfc_name) != 0:
        pass
    else:
        messagebox.showerror("DFC Name", "Please Enter First DFC name")
        return
    try:
        dfc_number = int(dfc_name.split("-")[1])
        dfc_amount = int(spinbox_amount.get())
        if check_top.get() == 1 and check_bot.get() == 0:
            surface = "T"
        elif check_bot.get() == 1 and check_top.get() == 0:
            surface = "B"
        else:
            messagebox.showerror("Warning", "Please select one CheckButton")
            return
    except Exception as e:
        messagebox.showerror("Error", f"Something went wrong: {e}")
        return
    try:
        for i in range(dfc_amount):
            dfc_list.append(
                "{}{}{}".format(
                    dfc_name[:-1].strip().capitalize(),
                    dfc_number,
                    surface,
                )
            )
            dfc_number += 1
        return dfc_list
    except:
        messagebox.showerror(
            "List Creation Error", "There was an error while creating list"
        )    