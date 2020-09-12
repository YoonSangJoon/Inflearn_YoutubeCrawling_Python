import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5 import uic
from pyqt_basic_ui import Ui_MainWindow

form_class = uic.loadUiType('C:\\Pythonsource\\Workspace\\Crawling\\Class\\section6\\example\\pyqt_basic_3.ui')[0]

class TestForm(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = TestForm()
    window.show()
    app.exec_()

# ui 파일을 불러오는 것 보다는 cmd를 통해 py파일로 변경한 후 불러오는 것이 좋다.
# 다만 디자인이 확정됬을때 부르는 것이 좋다.
# ui상태에서 디자인을 최대한 수정후 py로 불러와 그 다음 작업을 시작하는 것이 좋다.