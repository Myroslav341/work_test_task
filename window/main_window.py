# -*- coding: utf-8 -*-
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QFileDialog
from odf.opendocument import OpenDocumentText
from odf.table import Table, TableColumn, TableRow, TableCell
from odf.text import P

from window.ui.main_window_ui import UiMainWindow
from .resize_window import ResizeWindow
from .confirm_window import ConfirmWindow


class MainWindow(QtWidgets.QMainWindow, UiMainWindow):
    """
    Main window of the application with data table
    """
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.actionSave.triggered.connect(self.file_save)
        self.resize_act.triggered.connect(self.open_resize_window)

    def file_save(self):
        data = []
        for i in range(self.table_widget.rowCount()):
            data.append(list())
            for j in range(self.table_widget.columnCount()):
                try:
                    data[-1].append(self.table_widget.item(i, j).text())
                except AttributeError:
                    data[-1].append('')
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getSaveFileName(self, "Save", "",
                                                  "OpenOfice (.odt)", options=options)
        if fileName:
            textdoc = OpenDocumentText()
            table = Table()
            for _ in range(len(data[0])):
                table.addElement(TableColumn())
            for row in data:
                tr = TableRow()
                for cell in row:
                    tc = TableCell()
                    p = P(text=cell)
                    tc.addElement(p)
                    tr.addElement(tc)
                table.addElement(tr)
            textdoc.text.addElement(table)
            textdoc.save(fileName, True)

    def open_resize_window(self):
        resize_window = ResizeWindow(self, self.table_widget.rowCount(), self.table_widget.columnCount())
        resize_window.setModal(True)
        if resize_window.exec_():  # if applied
            if self.row_check(resize_window) or self.column_check(resize_window):
                confirm_window = ConfirmWindow(self)  # if we will louse data in rows
                confirm_window.setModal(True)
                if confirm_window.exec_():  # if confirmed
                    self.table_widget.setRowCount(resize_window.spin_row.value())
                    self.table_widget.setColumnCount(resize_window.spin_col.value())
                    return
                else:  # if closed
                    return
            # if all is ok
            self.table_widget.setRowCount(resize_window.spin_row.value())
            self.table_widget.setColumnCount(resize_window.spin_col.value())

    def row_check(self, resize_window):
        """
        check data in rows that can be deleted
        return: True if have such a data, False if all is ok
        """
        for i in range(resize_window.spin_row.value(), self.table_widget.rowCount()):
            for j in range(self.table_widget.columnCount()):
                try:
                    self.table_widget.item(i, j).text()
                    return True
                except AttributeError:
                    pass
        return False

    def column_check(self, resize_window):
        """
        check data in columns that can be deleted
        return: True if have such a data, False if all is ok
        """
        for i in range(self.table_widget.rowCount()):
            for j in range(resize_window.spin_col.value(), self.table_widget.columnCount()):
                try:
                    self.table_widget.item(i, j).text()
                    return True
                except AttributeError:
                    pass
        return False
