# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Product.ui'
##
## Created by: Qt User Interface Compiler version 6.8.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QLineEdit, QPushButton,
    QSizePolicy, QWidget)
import resources_rc

class Ui_Element(object):
    def setupUi(self, Element):
        if not Element.objectName():
            Element.setObjectName(u"Element")
        Element.resize(816, 42)
        self.gridLayout = QGridLayout(Element)
        self.gridLayout.setObjectName(u"gridLayout")
        self.lePrice = QLineEdit(Element)
        self.lePrice.setObjectName(u"lePrice")
        self.lePrice.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.lePrice, 0, 1, 1, 1)

        self.btnDelete = QPushButton(Element)
        self.btnDelete.setObjectName(u"btnDelete")
        icon = QIcon()
        icon.addFile(u":/icons/views/assets/ic--outline-delete.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnDelete.setIcon(icon)

        self.gridLayout.addWidget(self.btnDelete, 0, 2, 1, 1)

        self.leName = QLineEdit(Element)
        self.leName.setObjectName(u"leName")
        self.leName.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.leName, 0, 0, 1, 1)


        self.retranslateUi(Element)

        QMetaObject.connectSlotsByName(Element)
    # setupUi

    def retranslateUi(self, Element):
        Element.setWindowTitle(QCoreApplication.translate("Element", u"Producto", None))
        self.btnDelete.setText("")
    # retranslateUi

