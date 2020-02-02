# -*- coding: utf-8 -*-
from window.ui.resize_window_ui import NewDialogResize


class ResizeWindow(NewDialogResize):
    """
    window for resize data table
    """
    def __init__(self, parent, row_count, column_count):
        super().__init__(parent)
        self.setupUi(self)
        self.spin_col.setValue(column_count)
        self.spin_row.setValue(row_count)
        self.apply_button.clicked.connect(self.reject)
        self.close_button.clicked.connect(self.accept)
