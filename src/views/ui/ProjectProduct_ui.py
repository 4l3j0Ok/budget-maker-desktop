# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ProjectProduct.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLineEdit, QPushButton,
    QSizePolicy, QWidget)
import resources_rc

class Ui_Element(object):
    def setupUi(self, Element):
        if not Element.objectName():
            Element.setObjectName(u"Element")
        Element.resize(804, 42)
        self.horizontalLayout = QHBoxLayout(Element)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.leProduct = QLineEdit(Element)
        self.leProduct.setObjectName(u"leProduct")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.leProduct.sizePolicy().hasHeightForWidth())
        self.leProduct.setSizePolicy(sizePolicy)
        self.leProduct.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout.addWidget(self.leProduct)

        self.leAmount = QLineEdit(Element)
        self.leAmount.setObjectName(u"leAmount")
        sizePolicy.setHeightForWidth(self.leAmount.sizePolicy().hasHeightForWidth())
        self.leAmount.setSizePolicy(sizePolicy)
        self.leAmount.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout.addWidget(self.leAmount)

        self.leTotal = QLineEdit(Element)
        self.leTotal.setObjectName(u"leTotal")
        sizePolicy.setHeightForWidth(self.leTotal.sizePolicy().hasHeightForWidth())
        self.leTotal.setSizePolicy(sizePolicy)
        self.leTotal.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout.addWidget(self.leTotal)

        self.btnLock = QPushButton(Element)
        self.btnLock.setObjectName(u"btnLock")
        icon = QIcon()
        icon.addFile(u":/icons/views/assets/ic--outline-lock.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnLock.setIcon(icon)

        self.horizontalLayout.addWidget(self.btnLock)

        self.btnDelete = QPushButton(Element)
        self.btnDelete.setObjectName(u"btnDelete")
        icon1 = QIcon()
        icon1.addFile(u":/icons/views/assets/ic--outline-delete.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnDelete.setIcon(icon1)

        self.horizontalLayout.addWidget(self.btnDelete)


        self.retranslateUi(Element)

        QMetaObject.connectSlotsByName(Element)
    # setupUi

    def retranslateUi(self, Element):
        Element.setWindowTitle(QCoreApplication.translate("Element", u"Proyecto - Producto", None))
        self.leProduct.setPlaceholderText(QCoreApplication.translate("Element", u"Ingrese el nombre del producto", None))
        self.leAmount.setPlaceholderText(QCoreApplication.translate("Element", u"Ingrese la cantidad", None))
        self.leTotal.setPlaceholderText(QCoreApplication.translate("Element", u"Ingrese el precio total", None))
        self.btnLock.setText("")
        self.btnDelete.setText("")
    # retranslateUi

