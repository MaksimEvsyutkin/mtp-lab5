"""Comprehensive tests for GUI and business logic (Lab 5, Variant 2)."""

import tkinter as tk
import unittest

from guikit import CurrencyEngine, MainWindow


class TestCurrencyEngine(unittest.TestCase):
    def test_direct_conversion(self):
        # 100 USD -> 9250.00 RUB (92.5 rate)
        res = CurrencyEngine.convert(100.0, "USD", "RUB")
        self.assertEqual(res, 9250.0)

    def test_cross_conversion(self):
        # 92 EUR -> 100 USD -> 9250 RUB
        res = CurrencyEngine.convert(92.0, "EUR", "USD")
        self.assertEqual(res, 100.0)

    def test_zero_amount(self):
        self.assertEqual(CurrencyEngine.convert(0.0, "USD", "EUR"), 0.0)

    def test_negative_amount_raises(self):
        with self.assertRaises(ValueError):
            CurrencyEngine.convert(-10.0, "USD", "RUB")

    def test_unknown_currency_raises(self):
        with self.assertRaises(ValueError):
            CurrencyEngine.convert(50.0, "XYZ", "USD")
        with self.assertRaises(ValueError):
            CurrencyEngine.convert(50.0, "USD", "ABC")


class TestGUIWidgetsAndEvents(unittest.TestCase):
    def setUp(self):
        self.app = MainWindow()
        self.app.withdraw()  # hide window during automated tests

    def tearDown(self):
        self.app.destroy()

    def test_converter_tab_logic_and_widgets(self):
        frame = self.app.converter_frame
        frame.amount_entry.delete(0, tk.END)
        frame.amount_entry.insert(0, "50")
        frame.from_combo.set("USD")
        frame.to_combo.set("RUB")

        frame.perform_conversion()
        res_text = frame.result_label.cget("text")
        self.assertIn("50.00 USD", res_text)
        self.assertIn("4625.00 RUB", res_text)

    def test_converter_invalid_input(self):
        frame = self.app.converter_frame
        frame.amount_entry.delete(0, tk.END)
        frame.amount_entry.insert(0, "не_число")

        frame.perform_conversion()
        res_text = frame.result_label.cget("text")
        self.assertIn("Ошибка", res_text)

    def test_listbox_tab_operations_and_selection(self):
        frame = self.app.list_frame
        initial_count = frame.listbox.size()

        # Add item
        frame.item_entry.delete(0, tk.END)
        frame.item_entry.insert(0, "Новый тест")
        frame.add_item()
        self.assertEqual(frame.listbox.size(), initial_count + 1)

        # Select item
        frame.listbox.selection_clear(0, tk.END)
        frame.listbox.selection_set(0)
        frame.on_item_select()
        self.assertIn("Выбран элемент", frame.status_label.cget("text"))

        # Clear
        frame.clear_all()
        self.assertEqual(frame.listbox.size(), 0)

    def test_canvas_drawing_events(self):
        frame = self.app.canvas_frame
        self.assertEqual(frame.shapes_count, 0)

        # Simulate Mouse Down
        event_down = tk.Event()
        event_down.x = 20
        event_down.y = 30
        frame.on_mouse_down(event_down)
        self.assertIsNotNone(frame.current_shape_id)

        # Simulate Drag
        event_drag = tk.Event()
        event_drag.x = 100
        event_drag.y = 120
        frame.on_mouse_drag(event_drag)

        # Simulate Release
        event_up = tk.Event()
        event_up.x = 100
        event_up.y = 120
        frame.on_mouse_up(event_up)

        self.assertEqual(frame.shapes_count, 1)
        self.assertIn("Нарисовано фигур: 1", frame.info_label.cget("text"))

        # Clear
        frame.clear_canvas()
        self.assertEqual(frame.shapes_count, 0)

    def test_menubar_has_exit_command(self):
        menubar = self.app.nametowidget(self.app.cget("menu"))
        self.assertIsNotNone(menubar)
        # 0 is the first cascade: "Файл (File)"
        file_menu_name = menubar.entrycget(0, "menu")
        file_menu = self.app.nametowidget(file_menu_name)
        labels = [
            file_menu.entrycget(i, "label")
            for i in range(file_menu.index(tk.END) + 1)
            if file_menu.type(i) != "separator"
        ]
        self.assertTrue(any("Выход" in lbl for lbl in labels))


if __name__ == "__main__":
    unittest.main()
