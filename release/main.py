import sys
import json
from PySide2.QtWidgets import QApplication
from PySide2.QtWidgets import QMainWindow
import requests
from ui_form import Ui_mainform


class LoginForm(QMainWindow):
    def __init__(self, parent=None):
        QMainWindow.__init__(self, parent)

        self.ui = Ui_mainform()
        self.ui.setupUi(self)
        self.ui.getbilibili.clicked.connect(self.getbili)
    def getbili(self):
        r=requests.get("https://v1.hitokoto.cn/")
        msg=json.loads(r.text)

        self.ui.showarea.setText(msg["hitokoto"])
if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = LoginForm()
    form.show()
    sys.exit(app.exec_())