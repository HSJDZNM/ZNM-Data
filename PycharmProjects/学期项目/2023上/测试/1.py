from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QVBoxLayout
from PyQt5.QtCore import Qt


class MyWidget(QWidget):
    def __init__(self):
        super().__init__()

        # 创建 QLineEdit
        self.line_edit = QLineEdit()
        self.line_edit.returnPressed.connect(self.clear_line_edit)

        # 创建布局，并将 QLineEdit 添加到布局中
        layout = QVBoxLayout()
        layout.addWidget(self.line_edit)

        self.setLayout(layout)

    def clear_line_edit(self):
        self.line_edit.clear()


if __name__ == '__main__':
    app = QApplication([])
    widget = MyWidget()
    widget.show()
    app.exec_()
