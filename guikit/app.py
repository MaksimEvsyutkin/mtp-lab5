"""Main application window with Menu and Notebook layout (Tasks Medium 7 & Integration)."""

import tkinter as tk
from tkinter import messagebox, ttk

from guikit.canvas_draw import CanvasDrawFrame
from guikit.converter import ConverterFrame
from guikit.list_manager import ListManagerFrame


class MainWindow(tk.Tk):
    """Main window integrating all tasks of Lab 5."""

    def __init__(self) -> None:
        super().__init__()
        self.title("Лабораторная работа №5: GUI (Вариант 2) — Евсюткин М. С.")
        self.geometry("640x500")
        self.minsize(580, 440)

        self._build_menu()
        self._build_tabs()

    def _build_menu(self) -> None:
        """Create menu bar with File -> Exit (Task Medium 7)."""
        menu_bar = tk.Menu(self)

        # Меню "Файл" (Задание Средн. №7: File -> Exit)
        file_menu = tk.Menu(menu_bar, tearoff=0)
        file_menu.add_command(label="Очистить холст", command=self._clear_active_canvas)
        file_menu.add_separator()
        file_menu.add_command(
            label="Выход (Exit)",
            accelerator="Ctrl+Q",
            command=self.quit_app,
        )
        menu_bar.add_cascade(label="Файл (File)", menu=file_menu)

        # Меню "Справка"
        help_menu = tk.Menu(menu_bar, tearoff=0)
        help_menu.add_command(label="О программе", command=self._show_about)
        menu_bar.add_cascade(label="Справка", menu=help_menu)

        self.config(menu=menu_bar)
        self.bind_all("<Control-q>", lambda e: self.quit_app())

    def _build_tabs(self) -> None:
        """Assemble tabs using ttk.Notebook."""
        notebook = ttk.Notebook(self)
        notebook.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        self.converter_frame = ConverterFrame(notebook)
        self.list_frame = ListManagerFrame(notebook)
        self.canvas_frame = CanvasDrawFrame(notebook)

        notebook.add(self.converter_frame, text=" 💱 Конвертер валют ")
        notebook.add(self.list_frame, text=" 📋 Список (Listbox) ")
        notebook.add(self.canvas_frame, text=" 🎨 Рисование (Canvas) ")

    def _clear_active_canvas(self) -> None:
        """Clear canvas from menu action."""
        self.canvas_frame.clear_canvas()

    def _show_about(self) -> None:
        """Display about dialog."""
        messagebox.showinfo(
            "О программе",
            "Лабораторная работа №5: Визуальное программирование на Python\n"
            "Студент: Евсюткин Максим Сергеевич, группа 221141, вариант 2\n\n"
            "Задания:\n"
            "• Средн. 2: Текстовое поле и кнопка\n"
            "• Средн. 4: Listbox и выбор элемента\n"
            "• Средн. 7: Меню File -> Exit\n"
            "• Повыш. 2: Рисование фигур мышью\n"
            "• Повыш. 6: Конвертер валют",
        )

    def quit_app(self) -> None:
        """Exit application handler (Task Medium 7)."""
        self.destroy()
