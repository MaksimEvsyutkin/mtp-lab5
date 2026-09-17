"""Currency converter module (Tasks Advanced 6 & Medium 2)."""

import tkinter as tk
from tkinter import ttk
from typing import Dict


class CurrencyEngine:
    """Core logic for currency conversion."""

    BASE_RATES_TO_USD: Dict[str, float] = {
        "USD": 1.0,
        "EUR": 0.92,
        "RUB": 92.50,
        "CNY": 7.24,
        "KZT": 478.0,
    }

    @classmethod
    def convert(cls, amount: float, from_curr: str, to_curr: str) -> float:
        """
        Convert amount from from_curr to to_curr.

        Args:
            amount: Non-negative monetary amount.
            from_curr: Source currency code (e.g. 'USD').
            to_curr: Target currency code (e.g. 'RUB').

        Returns:
            Converted amount.

        Raises:
            ValueError: If amount is negative or currencies are invalid.
        """
        if amount < 0:
            raise ValueError("Сумма не может быть отрицательной.")

        from_c = from_curr.upper().strip()
        to_c = to_curr.upper().strip()

        if from_c not in cls.BASE_RATES_TO_USD:
            raise ValueError(f"Неизвестная валюта отправления: {from_curr}")
        if to_c not in cls.BASE_RATES_TO_USD:
            raise ValueError(f"Неизвестная валюта назначения: {to_curr}")

        amount_in_usd = amount / cls.BASE_RATES_TO_USD[from_c]
        result = amount_in_usd * cls.BASE_RATES_TO_USD[to_c]
        return round(result, 2)


class ConverterFrame(ttk.Frame):
    """GUI Frame for Currency Converter (Task Advanced 6 with Entry & Button from Medium 2)."""

    def __init__(self, parent: tk.Widget) -> None:
        super().__init__(parent, padding=15)
        self._build_ui()

    def _build_ui(self) -> None:
        currencies = list(CurrencyEngine.BASE_RATES_TO_USD.keys())

        # Title
        title_label = ttk.Label(self, text="Конвертер валют", font=("Helvetica", 14, "bold"))
        title_label.grid(row=0, column=0, columnspan=2, pady=(0, 15), sticky="w")

        # 1. Текстовое поле ввода суммы (Задание Средн. №2)
        ttk.Label(self, text="Сумма для перевода:").grid(row=1, column=0, sticky="w", pady=5)
        self.amount_entry = ttk.Entry(self, width=22)
        self.amount_entry.grid(row=1, column=1, sticky="ew", pady=5)
        self.amount_entry.insert(0, "100")

        # Валюта из
        ttk.Label(self, text="Из валюты:").grid(row=2, column=0, sticky="w", pady=5)
        self.from_combo = ttk.Combobox(self, values=currencies, state="readonly", width=20)
        self.from_combo.grid(row=2, column=1, sticky="ew", pady=5)
        self.from_combo.set("USD")

        # Валюта в
        ttk.Label(self, text="В валюту:").grid(row=3, column=0, sticky="w", pady=5)
        self.to_combo = ttk.Combobox(self, values=currencies, state="readonly", width=20)
        self.to_combo.grid(row=3, column=1, sticky="ew", pady=5)
        self.to_combo.set("RUB")

        # 2. Кнопка, запускающая обработку и вывод (Задание Средн. №2)
        self.convert_button = ttk.Button(self, text="Конвертировать", command=self.perform_conversion)
        self.convert_button.grid(row=4, column=0, columnspan=2, pady=15, sticky="ew")

        # 3. Метка для вывода результата (Задание Средн. №2)
        self.result_label = ttk.Label(
            self,
            text="Результат: нажмите кнопку для расчёта",
            font=("Helvetica", 11),
            foreground="#1a5276",
        )
        self.result_label.grid(row=5, column=0, columnspan=2, pady=5, sticky="w")

    def perform_conversion(self) -> None:
        """Handle convert button click and update result label."""
        raw_amount = self.amount_entry.get().strip()
        try:
            amount = float(raw_amount)
            res = CurrencyEngine.convert(amount, self.from_combo.get(), self.to_combo.get())
            text = f"Результат: {amount:.2f} {self.from_combo.get()} = {res:.2f} {self.to_combo.get()}"
            self.result_label.config(text=text, foreground="#196f3d")
        except ValueError as err:
            self.result_label.config(text=f"Ошибка: {err}", foreground="#c0392b")
