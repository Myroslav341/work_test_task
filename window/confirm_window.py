# -*- coding: utf-8 -*-
from window.ui.confirm_window_ui import NewDialogConfirm


class ConfirmWindow(NewDialogConfirm):
    """
    window for confirm table size changes if data can be lost
    """
    def __init__(self, parent):
        super().__init__(parent)
        self.setupUi(self)
        self.close_button.clicked.connect(self.reject)
        self.confirm_button.clicked.connect(self.accept)
