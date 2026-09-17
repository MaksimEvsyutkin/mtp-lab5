"""Interactive canvas drawing module with mouse events (Task Advanced 2)."""

import tkinter as tk
from tkinter import ttk


class CanvasDrawFrame(ttk.Frame):
    """GUI Frame for drawing shapes using mouse events on Canvas (Task Advanced 2)."""

    def __init__(self, parent: tk.Widget) -> None:
        super().__init__(parent, padding=15)
        self.shape_type = tk.StringVar(value="rectangle")
        self.color_choice = tk.StringVar(value="blue")
        self.start_x = 0
        self.start_y = 0
        self.current_shape_id: int | None = None
        self.shapes_count = 0
        self._build_ui()

    def _build_ui(self) -> None:
        title_label = ttk.Label(self, text="Рисование фигур мышью (Canvas)", font=("Helvetica", 14, "bold"))
        title_label.grid(row=0, column=0, columnspan=4, pady=(0, 10), sticky="w")

        # Controls panel
        ctrl_frame = ttk.Frame(self)
        ctrl_frame.grid(row=1, column=0, columnspan=4, pady=5, sticky="ew")

        ttk.Label(ctrl_frame, text="Фигура:").pack(side=tk.LEFT, padx=(0, 5))
        for s_type, label in [("rectangle", "Прямоугольник"), ("oval", "Овал/Круг"), ("line", "Линия")]:
            ttk.Radiobutton(ctrl_frame, text=label, value=s_type, variable=self.shape_type).pack(side=tk.LEFT, padx=5)

        ttk.Label(ctrl_frame, text="Цвет:").pack(side=tk.LEFT, padx=(15, 5))
        color_combo = ttk.Combobox(
            ctrl_frame,
            values=["blue", "red", "green", "black", "orange", "purple"],
            textvariable=self.color_choice,
            state="readonly",
            width=10,
        )
        color_combo.pack(side=tk.LEFT, padx=5)

        clear_btn = ttk.Button(ctrl_frame, text="Очистить холст", command=self.clear_canvas)
        clear_btn.pack(side=tk.RIGHT, padx=5)

        self.canvas = tk.Canvas(
            self, width=500, height=280, bg="#ffffff",
            highlightthickness=1, highlightbackground="#bdc3c7"
        )
        self.canvas.grid(row=2, column=0, columnspan=4, pady=10, sticky="nsew")

        # Bind mouse events
        self.canvas.bind("<Button-1>", self.on_mouse_down)
        self.canvas.bind("<B1-Motion>", self.on_mouse_drag)
        self.canvas.bind("<ButtonRelease-1>", self.on_mouse_up)

        # Status
        self.info_label = ttk.Label(
            self,
            text="Зажмите ЛКМ на белом холсте и потяните мышь для рисования фигуры.",
            foreground="#555555",
        )
        self.info_label.grid(row=3, column=0, columnspan=4, sticky="w")

    def on_mouse_down(self, event: tk.Event) -> None:
        """Mouse button pressed: save starting coordinates and create initial shape."""
        self.start_x = event.x
        self.start_y = event.y
        stype = self.shape_type.get()
        color = self.color_choice.get()

        if stype == "rectangle":
            self.current_shape_id = self.canvas.create_rectangle(
                self.start_x, self.start_y, self.start_x, self.start_y,
                outline=color, fill="", width=2
            )
        elif stype == "oval":
            self.current_shape_id = self.canvas.create_oval(
                self.start_x, self.start_y, self.start_x, self.start_y,
                outline=color, fill="", width=2
            )
        else:  # line
            self.current_shape_id = self.canvas.create_line(
                self.start_x, self.start_y, self.start_x, self.start_y,
                fill=color, width=2
            )

    def on_mouse_drag(self, event: tk.Event) -> None:
        """Mouse dragged with button held: dynamically resize current shape."""
        if self.current_shape_id is not None:
            self.canvas.coords(self.current_shape_id, self.start_x, self.start_y, event.x, event.y)
            self.info_label.config(
                text=f"Рисование: ({self.start_x}, {self.start_y}) -> ({event.x}, {event.y})"
            )

    def on_mouse_up(self, event: tk.Event) -> None:
        """Mouse button released: finalize shape."""
        if self.current_shape_id is not None:
            self.shapes_count += 1
            stype = self.shape_type.get()
            msg = (
                f"Нарисовано фигур: {self.shapes_count} | "
                f"Последняя: {stype} от ({self.start_x}, {self.start_y}) до ({event.x}, {event.y})"
            )
            self.info_label.config(text=msg)
            self.current_shape_id = None

    def clear_canvas(self) -> None:
        """Clear all drawn objects from canvas."""
        self.canvas.delete("all")
        self.shapes_count = 0
        self.info_label.config(text="Холст очищен. Нарисуйте новую фигуру мышью.")
