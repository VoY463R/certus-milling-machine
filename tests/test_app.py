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

    assert isinstance(app.map, tk.Button)
    assert isinstance(app.milling, tk.Button)
    assert isinstance(app.position, tk.Button)