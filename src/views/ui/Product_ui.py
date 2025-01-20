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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLineEdit,
    QPushButton, QSizePolicy, QVBoxLayout, QWidget)
import resources_rc

class Ui_Element(object):
    def setupUi(self, Element):
        if not Element.objectName():
            Element.setObjectName(u"Element")
        Element.resize(627, 42)
        self.verticalLayout = QVBoxLayout(Element)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frBox = QFrame(Element)
        self.frBox.setObjectName(u"frBox")
        self.frBox.setFrameShape(QFrame.Shape.NoFrame)
        self.frBox.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout = QHBoxLayout(self.frBox)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.leName = QLineEdit(self.frBox)
        self.leName.setObjectName(u"leName")
        self.leName.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout.addWidget(self.leName)

        self.lePrice = QLineEdit(self.frBox)
        self.lePrice.setObjectName(u"lePrice")
        self.lePrice.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout.addWidget(self.lePrice)

        self.btnEdit = QPushButton(self.frBox)
        self.btnEdit.setObjectName(u"btnEdit")
        icon = QIcon()
        icon.addFile(u":/icons/views/assets/ic--outline-edit.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnEdit.setIcon(icon)

        self.horizontalLayout.addWidget(self.btnEdit)

        self.btnDelete = QPushButton(self.frBox)
        self.btnDelete.setObjectName(u"btnDelete")
        icon1 = QIcon()
        icon1.addFile(u":/icons/views/assets/ic--outline-delete.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnDelete.setIcon(icon1)

        self.horizontalLayout.addWidget(self.btnDelete)


        self.verticalLayout.addWidget(self.frBox)


        self.retranslateUi(Element)

        QMetaObject.connectSlotsByName(Element)
    # setupUi

    def retranslateUi(self, Element):
        Element.setWindowTitle(QCoreApplication.translate("Element", u"Producto", None))
        self.btnEdit.setText("")
        self.btnDelete.setText("")
    # retranslateUi

