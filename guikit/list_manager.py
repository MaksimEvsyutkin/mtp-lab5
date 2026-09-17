"""List manager module with Listbox and item selection (Task Medium 4)."""

import tkinter as tk
from tkinter import ttk


class ListManagerFrame(ttk.Frame):
    """GUI Frame demonstrating Listbox widget and item selection (Task Medium 4)."""

    def __init__(self, parent: tk.Widget) -> None:
        super().__init__(parent, padding=15)
        self._build_ui()

    def _build_ui(self) -> None:
        title_label = ttk.Label(self, text="Управление элементами (Listbox)", font=("Helvetica", 14, "bold"))
        title_label.grid(row=0, column=0, columnspan=3, pady=(0, 15), sticky="w")

        # Entry for new element
        ttk.Label(self, text="Новый элемент:").grid(row=1, column=0, sticky="w", pady=5)
        self.item_entry = ttk.Entry(self, width=25)
        self.item_entry.grid(row=1, column=1, sticky="ew", pady=5)
        self.item_entry.insert(0, "Элемент списка")

        add_btn = ttk.Button(self, text="Добавить", command=self.add_item)
        add_btn.grid(row=1, column=2, padx=5, pady=5)

        # 1. Список Listbox (Задание Средн. №4)
        list_container = ttk.Frame(self)
        list_container.grid(row=2, column=0, columnspan=3, pady=10, sticky="nsew")

        self.listbox = tk.Listbox(list_container, height=7, width=45, selectmode=tk.SINGLE)
        scrollbar = ttk.Scrollbar(list_container, orient=tk.VERTICAL, command=self.listbox.yview)
        self.listbox.config(yscrollcommand=scrollbar.set)

        self.listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        # Pre-populate sample items
        initial_items = ["Python 3.12", "Tkinter GUI", "PyQt5 Framework", "FastAPI Service", "PostgreSQL DB"]
        for it in initial_items:
            self.listbox.insert(tk.END, it)

        # 2. Обработчик события выбора элемента <<ListboxSelect>>
        self.listbox.bind("<<ListboxSelect>>", self.on_item_select)

        # Buttons to delete or clear
        btn_frame = ttk.Frame(self)
        btn_frame.grid(row=3, column=0, columnspan=3, pady=5, sticky="ew")

        del_btn = ttk.Button(btn_frame, text="Удалить выбранный", command=self.delete_selected)
        del_btn.pack(side=tk.LEFT, padx=(0, 5))

        clear_btn = ttk.Button(btn_frame, text="Очистить список", command=self.clear_all)
        clear_btn.pack(side=tk.LEFT)

        # 3. Метка с информацией о выбранном элементе
        self.status_label = ttk.Label(
            self,
            text="Выбранный элемент: (выберите строку в списке выше)",
            font=("Helvetica", 11),
            foreground="#2e4053",
        )
        self.status_label.grid(row=4, column=0, columnspan=3, pady=10, sticky="w")

    def add_item(self) -> None:
        """Add item from entry to listbox."""
        val = self.item_entry.get().strip()
        if val:
            self.listbox.insert(tk.END, val)
            self.item_entry.delete(0, tk.END)
            self.status_label.config(text=f"Добавлен элемент: '{val}'")

    def on_item_select(self, event=None) -> None:
        """Handle <<ListboxSelect>> event and update status label."""
        selection = self.listbox.curselection()
        if selection:
            index = selection[0]
            value = self.listbox.get(index)
            self.status_label.config(
                text=f"Выбран элемент: '{value}' (индекс: {index})",
                foreground="#1b4f72",
            )

    def delete_selected(self) -> None:
        """Delete selected item from listbox."""
        selection = self.listbox.curselection()
        if selection:
            index = selection[0]
            val = self.listbox.get(index)
            self.listbox.delete(index)
            self.status_label.config(text=f"Удалён элемент: '{val}'")

    def clear_all(self) -> None:
        """Clear all items from listbox."""
        self.listbox.delete(0, tk.END)
        self.status_label.config(text="Список полностью очищен.")
