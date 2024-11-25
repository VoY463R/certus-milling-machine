import time
from tkinter import messagebox
import pyautogui


class PositionControl:
    def __init__(self) -> None:
        self.change_sheet = 195

    def mouse_position(self):
        """
        Determine the position of the mouse cursor.
        """
        self.mouse_position_set = pyautogui.position()
        print(self.mouse_position_set[0], self.mouse_position_set[1])
        return self.mouse_position_set

    def mapping(self, dfc_list):
        """
        The function responsible for carrying out the mapping of fuel cell tiles based on the uploaded list of cells and the position of the cursor.
        """
        x_cor = [155, 255, 255, 155, 55]
        y_cor = [26, 26, 96, 96, 96]
        self.mapping_dfc_list = dfc_list[1:]
        try:
            for i in range(len(self.mapping_dfc_list)):
                pyautogui.click(self.mouse_position_set[0], self.mouse_position_set[1])
                pyautogui.move(-96, -58)
                pyautogui.click()
                pyautogui.move(19, 55)
                pyautogui.doubleClick()
                pyautogui.write(str(x_cor[i]))
                pyautogui.move(0, 33)
                pyautogui.doubleClick()
                pyautogui.write(str(y_cor[i]))
                pyautogui.move(-64, -91)
                pyautogui.click()
                pyautogui.move(26, 55)
                pyautogui.click()
                time.sleep(28)
                pyautogui.move(247, 27)
                pyautogui.click()
                pyautogui.write(dfc_list[i])
                pyautogui.press("enter")

        except Exception as e:
            messagebox.showerror(
                "Milling error",
                f"There was a problem with the milling of fuel cells: {e}",
            )
            return

        messagebox.showinfo("Mapping Finised", "Mapping process complete")

    def milling(self, dfc_list):
        """
        The function responsible for carrying out the milling of fuel cell plates based on the uploaded list of cells and the position of the cursor.
        """
        try:
            for i in range(len(dfc_list)):
                pyautogui.click(self.mouse_position_set[0], self.mouse_position_set[1])
                pyautogui.move(153, -21)
                pyautogui.click()
                pyautogui.write(dfc_list[i])
                pyautogui.press("enter")
                pyautogui.move(-321, 721)
                pyautogui.click()
                pyautogui.moveTo(self.change_sheet, 913)
                pyautogui.click()
                pyautogui.move(-150, -745)
                pyautogui.click()
                with pyautogui.hold("ctrlleft"):
                    pyautogui.press("c")
                pyautogui.moveTo(268, 1004)
                pyautogui.click()
                pyautogui.move(665, -188)
                pyautogui.click()
                pyautogui.move(-390, 82)
                pyautogui.click()
                pyautogui.move(19, -553)
                pyautogui.click()
                with pyautogui.hold("ctrlleft"):
                    pyautogui.press("a")
                with pyautogui.hold("ctrlleft"):
                    pyautogui.press("v")
                pyautogui.move(-156, -196)
                pyautogui.click()
                pyautogui.move(426, -28)
                pyautogui.click()
                pyautogui.move(-277, 693)
                pyautogui.click()
                pyautogui.move(-192, 96)
                pyautogui.click()
                self.change_sheet += 40
                time.sleep(215)
        except Exception as e:
            messagebox.showerror(
                "Milling error",
                f"There was a problem with the milling of fuel cells: {e}",
            )
            return

        messagebox.showinfo("Milling Finised", "Milling process complete")
        self.change_sheet = 195
