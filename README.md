# Лабораторная работа №5

Евсюткин Максим Сергеевич, группа 221141, вариант 2, лабораторная №5

## Тема
Визуальное программирование на Python (виджеты Tkinter: Entry, Button, Label, Listbox, Menu, Canvas, обработка событий мыши и клавиатуры, компоновка интерфейса).

Репозиторий: https://github.com/MaksimEvsyutkin/mtp-lab5

---

## Выполненные задания

По таблице методических указаний (стр. 10) для **варианта 2**:

| Сложность | № | Задание по методичке | Модуль / Реализация |
|:---|:---:|:---|:---|
| **Средняя** | **2** | Окно с текстовым полем и кнопкой, выводящей текст | [`guikit/converter.py`](guikit/converter.py) — текстовое поле ввода суммы (`ttk.Entry`), кнопка расчёта (`ttk.Button`) и вывод результата в форматированную метку (`ttk.Label`) |
| **Средняя** | **4** | Список (Listbox) и выбор элемента | [`guikit/list_manager.py`](guikit/list_manager.py) — список `tk.Listbox` с вертикальным скроллбаром, обработчик события выбора `<<ListboxSelect>>`, добавление и удаление элементов |
| **Средняя** | **7** | Окно с меню (File $\rightarrow$ Exit) | [`guikit/app.py`](guikit/app.py) — верхняя строка меню `tk.Menu` с пунктами `Файл (File)` $\rightarrow$ `Выход (Exit)`, диалогом «О программе» и горячей клавишей `Ctrl+Q` |
| **Повышенная** | **2** | Рисование фигур мышью | [`guikit/canvas_draw.py`](guikit/canvas_draw.py) — интерактивный холст `tk.Canvas` с событиями `<Button-1>`, `<B1-Motion>`, `<ButtonRelease-1>` для рисования прямоугольников, овалов и линий |
| **Повышенная** | **6** | Программа «Конвертер валют» | [`guikit/converter.py`](guikit/converter.py) — движок курсов валют `CurrencyEngine` (USD, EUR, RUB, CNY, KZT) и графический интерфейс конвертации |

---

## Структура проекта

```text
mtp-lab5/
├── guikit/                     # Пакет графического интерфейса
│   ├── __init__.py             # Экспорт основных компонентов
│   ├── converter.py            # Повыш. №6 & Средн. №2: Конвертер валют (Entry, Button, Label)
│   ├── list_manager.py         # Средн. №4: Список Listbox с выбором и управлением элементами
│   ├── canvas_draw.py          # Повыш. №2: Холст Canvas для интерактивного рисования мышью
│   └── app.py                  # Средн. №7: Главное окно, вкладки Notebook и меню File -> Exit
├── tests/
│   └── test_guikit.py          # 10 unit-тестов (бизнес-логика, виджеты и события Tkinter)
├── .github/
│   └── workflows/
│       └── ci.yml              # CI workflow: flake8 (PEP 8) + xvfb-run unittest
├── .flake8                     # Конфигурация линтера (max-line-length = 120)
├── .gitignore                  # Игнорируемые файлы Python
├── main.py                     # Точка запуска GUI-приложения
└── README.md                   # Отчёт о выполнении лабораторной работы
```

---

## Описание работы интерфейса

### 1. Вкладка «Конвертер валют» (Повыш. №6 и Средн. №2)
Позволяет производить расчёт конвертации валют по кросс-курсам. Пользователь вводит сумму в текстовое поле `Entry` (по умолчанию 100), выбирает валюту отправления и назначения в выпадающих списках `Combobox`, нажимает кнопку `Button` «Конвертировать» и получает расчёт в текстовой метке `Label`. Предусмотрена валидация отрицательных значений и некорректного ввода.

### 2. Вкладка «Список (Listbox)» (Средн. №4)
Реализует компонент `Listbox` с возможностью выбора элемента кликом мыши или стрелками клавиатуры. При возникновении виртуального события `<<ListboxSelect>>` статусная строка мгновенно отображает значение выбранной строки и её индекс. Доступны функции добавления новых записей и удаления выбранных.

### 3. Вкладка «Рисование (Canvas)» (Повыш. №2)
Графический холст размером 500x280 пикселей. Поддерживает выбор типа фигуры (прямоугольник, овал, линия) и цвета контура. Рисование осуществляется зажатием левой кнопки мыши и перемещением курсора с динамическим масштабированием контура в реальном времени.

### 4. Строка меню (Средн. №7)
Содержит выпадающее меню `Файл (File)` с командой `Выход (Exit)`, которая вызывает завершение работы приложения (`destroy`), а также пункт очистки активного холста и окно «О программе».

---

## Запуск и тестирование

### Запуск GUI приложения:
```bash
python3 main.py
```

### Запуск модульных тестов:
```bash
python3 -m unittest -v tests/test_guikit.py
```
Результат прогона тестов:
```text
test_cross_conversion (tests.test_guikit.TestCurrencyEngine.test_cross_conversion) ... ok
test_direct_conversion (tests.test_guikit.TestCurrencyEngine.test_direct_conversion) ... ok
test_negative_amount_raises (tests.test_guikit.TestCurrencyEngine.test_negative_amount_raises) ... ok
test_unknown_currency_raises (tests.test_guikit.TestCurrencyEngine.test_unknown_currency_raises) ... ok
test_zero_amount (tests.test_guikit.TestCurrencyEngine.test_zero_amount) ... ok
test_canvas_drawing_events (tests.test_guikit.TestGUIWidgetsAndEvents.test_canvas_drawing_events) ... ok
test_converter_invalid_input (tests.test_guikit.TestGUIWidgetsAndEvents.test_converter_invalid_input) ... ok
test_converter_tab_logic_and_widgets (tests.test_guikit.TestGUIWidgetsAndEvents.test_converter_tab_logic_and_widgets) ... ok
test_listbox_tab_operations_and_selection (tests.test_guikit.TestGUIWidgetsAndEvents.test_listbox_tab_operations_and_selection) ... ok
test_menubar_has_exit_command (tests.test_guikit.TestGUIWidgetsAndEvents.test_menubar_has_exit_command) ... ok

----------------------------------------------------------------------
Ran 10 tests in 0.276s

OK
```
