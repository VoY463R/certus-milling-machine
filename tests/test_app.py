import pytest
import tkinter as tk
from app import MyApp


@pytest.fixture
def app():
    app_instance = MyApp()
    app_instance.root.update()
    return app_instance


def test_window_creation(app):
    assert isinstance(app.root, tk.Tk)
    assert app.root.title() == "Certus milling machine App"
    assert app.root.geometry() == "300x200+100+100"


def test_frame_existence(app):
    assert isinstance(app.dfc_name_frame, tk.Frame)
    assert isinstance(app.amount_of_dfc, tk.Frame)
    assert isinstance(app.top_bot, tk.Frame)
    assert isinstance(app.buttons, tk.Frame)


def test_widgets_existence(app):
    assert isinstance(app.dfc_name_label, tk.Label)
    assert isinstance(app.dfc_name_entry, tk.Entry)

    assert isinstance(app.dfc_amount_label, tk.Label)
    assert isinstance(app.spinbox_amount, tk.Spinbox)

    assert isinstance(app.top, tk.Checkbutton)
    assert isinstance(app.bot, tk.Checkbutton)

    assert isinstance(app.dfc_list_button, tk.Button)
    assert isinstance(app.map, tk.Button)
    assert isinstance(app.milling, tk.Button)
    assert isinstance(app.position, tk.Button)


def test_create_list_top(app):
    app.dfc_name_entry.insert(0, "a8-1")
    app.spinbox_amount.delete(0, "end")
    app.spinbox_amount.insert(0, "3")
    app.check_top.set(1)
    app.check_bot.set(0)
    app.dfc_list_button.invoke()
    assert app.check_top.get() == 1
    assert len(app.dfc_list) == 3
    assert app.dfc_list[0] == "A8-1T"


def test_create_list_bot(app):
    app.dfc_name_entry.insert(0, "a8-3")
    app.spinbox_amount.delete(0, "end")
    app.spinbox_amount.insert(0, "5")
    app.check_top.set(0)
    app.check_bot.set(1)
    app.dfc_list_button.invoke()
    assert app.check_bot.get() == 1
    assert len(app.dfc_list) == 5
    assert app.dfc_list[1] == "A8-4B"
