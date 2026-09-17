#!/usr/bin/env python3
"""Launch script for Lab 5 GUI Application."""

import sys
from guikit import MainWindow


def main() -> None:
    """Initialize and run main event loop."""
    app = MainWindow()
    app.mainloop()


if __name__ == "__main__":
    main()
