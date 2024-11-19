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
    assert app.root.geometry() == "500x300+100+100"
    
def test_frame_existence(app):
    assert isinstance(app.dfc_name, tk.Frame)
    assert isinstance(app.amount_of_dfc, tk.Frame)
    assert isinstance(app.top_bot, tk.Frame)
    assert isinstance(app.buttons, tk.Frame)