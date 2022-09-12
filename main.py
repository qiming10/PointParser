import re
from typing import List, Any

from PySide2.QtWidgets import *
from PySide2.QtCore import *
from ui_PointParser import Ui_MainWindow
from PySide2.QtGui import QClipboard


class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.table_init()
        self.point_list = []

        # Add slot
        self.ui.ptext_input.textChanged.connect(self.point_parser)
        self.ui.chkbox_auto_clear.clicked.connect(self.auto_clear)
        self.ui.btn_save_output.clicked.connect(self.save_to_table)
        self.ui.tbl_save.cellDoubleClicked.connect(self.copy_select_row)

    def point_parser(self) -> list:
        self.point_list.clear()
        input_text = self.ui.ptext_input.toPlainText()
        if not input_text:
            return
        try:
            x_pattern = re.compile(r'[x][ ]*=[ ]*(-?\d+)(\.\d+)?')
            y_pattern = re.compile(r'[y][ ]*=[ ]*(\d+)(\.\d+)?')
            z_pattern = re.compile(r'[z][ ]*=[ ]*(\d+)(\.\d+)?')
            x_all: List[Any] = x_pattern.findall(input_text)
            y_all: List[Any] = y_pattern.findall(input_text)
            z_all: List[Any] = z_pattern.findall(input_text)

            # Check
            if (not x_all) or (not y_all) or (not z_all):
                return
            elif len(x_all) != len(y_all) or len(x_all) != len(z_all):
                return

            self.ui.ptext_output.setPlainText('')
            last_point = ''
            for i in range(len(x_all)):
                point = [x_all[i][0]+x_all[i][1], y_all[i][0] + y_all[i][1], z_all[i][0] + z_all[i][1]]
                self.point_list.append(point)
                self.ui.ptext_output.appendPlainText(point[0] + ',' + point[1] + ',' + point[2])
                if i == len(x_all) - 1:
                    last_point = point[0] + ',' + point[1] + ',' + point[2]

            # Save to clipboard
            if self.ui.chkbox_auto_copy.isChecked():
                clip_board = QClipboard()
                clip_board.setText(last_point)

            # Auto clear
            if self.ui.chkbox_auto_clear.isChecked():
                self.ui.ptext_input.clear()
        except:
            return

    def auto_clear(self, value: bool):
        if value:
            self.ui.ptext_input.clear()

    def table_init(self):
        table = self.ui.tbl_save
        table.setColumnCount(4)
        table.setRowCount(0)
        table.setShowGrid(True)

        table.setHorizontalHeaderLabels(['x', 'y', 'z', '备注'])

    def save_to_table(self):
        if not self.point_list:
            return
        table = self.ui.tbl_save
        for point in self.point_list:
            row_count = table.rowCount()
            table.insertRow(row_count)
            for i in range(len(point)):
                table.setItem(row_count, i, QTableWidgetItem(str(point[i])))

        # Table resize
        table.resizeColumnsToContents()
        table.resizeRowsToContents()

    def copy_select_row(self):
        table = self.ui.tbl_save
        row_idx = table.currentRow()
        point = list()
        for col_idx in range(3):
            item = table.item(row_idx, col_idx)
            point.append(item.text())

        # Save to clipboard
        clip_board = QClipboard()
        clip_board.setText(point[0] + ',' + point[1] + ',' + point[2])


# Boot the program
if __name__ == '__main__':
    QCoreApplication.setAttribute(Qt.AA_EnableHighDpiScaling)
    app = QApplication([])
    main_window = MainWindow()
    main_window.show()
    app.exec_()
