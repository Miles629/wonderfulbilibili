# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 5.15.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QDate, QDateTime, QMetaObject,
    QObject, QPoint, QRect, QSize, QTime, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter,
    QPixmap, QRadialGradient)
from PySide2.QtWidgets import *


class Ui_mainform(object):
    def setupUi(self, mainform):
        if not mainform.objectName():
            mainform.setObjectName(u"mainform")
        mainform.resize(813, 553)
        self.verticalLayoutWidget = QWidget(mainform)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(20, 40, 131, 481))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.getbilibili = QPushButton(self.verticalLayoutWidget)
        self.getbilibili.setObjectName(u"getbilibili")

        self.verticalLayout.addWidget(self.getbilibili)

        self.showarea = QLabel(mainform)
        self.showarea.setObjectName(u"showarea")
        self.showarea.setGeometry(QRect(210, 45, 571, 461))

        self.retranslateUi(mainform)

        QMetaObject.connectSlotsByName(mainform)
    # setupUi

    def retranslateUi(self, mainform):
        mainform.setWindowTitle(QCoreApplication.translate("mainform", u"mainform", None))
        self.getbilibili.setText(QCoreApplication.translate("mainform", u"\u63a5\u6536\u7535\u6ce2", None))
        self.showarea.setText("")
    # retranslateUi

