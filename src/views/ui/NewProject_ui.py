# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'NewProject.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QScrollArea,
    QSizePolicy, QSpacerItem, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(708, 347)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        self.gridLayout = QGridLayout(Form)
        self.gridLayout.setObjectName(u"gridLayout")
        self.scrollArea = QScrollArea(Form)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 688, 162))
        self.layout = QGridLayout(self.scrollAreaWidgetContents)
        self.layout.setObjectName(u"layout")
        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.layout.addItem(self.verticalSpacer_3, 3, 4, 1, 1)

        self.label_3 = QLabel(self.scrollAreaWidgetContents)
        self.label_3.setObjectName(u"label_3")
        font = QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.label_3.setFont(font)
        self.label_3.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.layout.addWidget(self.label_3, 0, 1, 1, 1)

        self.leTotal = QLineEdit(self.scrollAreaWidgetContents)
        self.leTotal.setObjectName(u"leTotal")
        font1 = QFont()
        font1.setPointSize(12)
        self.leTotal.setFont(font1)
        self.leTotal.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.layout.addWidget(self.leTotal, 1, 4, 1, 1)

        self.label_5 = QLabel(self.scrollAreaWidgetContents)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font)
        self.label_5.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.layout.addWidget(self.label_5, 0, 4, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.layout.addItem(self.verticalSpacer_2, 3, 2, 1, 1)

        self.btnAdd = QPushButton(self.scrollAreaWidgetContents)
        self.btnAdd.setObjectName(u"btnAdd")
        self.btnAdd.setFont(font)

        self.layout.addWidget(self.btnAdd, 2, 1, 1, 4)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.layout.addItem(self.verticalSpacer, 3, 1, 1, 1)

        self.leAmount = QLineEdit(self.scrollAreaWidgetContents)
        self.leAmount.setObjectName(u"leAmount")
        self.leAmount.setFont(font1)
        self.leAmount.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.layout.addWidget(self.leAmount, 1, 2, 1, 1)

        self.leProduct = QLineEdit(self.scrollAreaWidgetContents)
        self.leProduct.setObjectName(u"leProduct")
        self.leProduct.setBaseSize(QSize(0, 0))
        self.leProduct.setFont(font1)
        self.leProduct.setStyleSheet(u"")
        self.leProduct.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.layout.addWidget(self.leProduct, 1, 1, 1, 1)

        self.label_4 = QLabel(self.scrollAreaWidgetContents)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font)
        self.label_4.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.layout.addWidget(self.label_4, 0, 2, 1, 1)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.gridLayout.addWidget(self.scrollArea, 4, 0, 1, 3)

        self.leProjectName = QLineEdit(Form)
        self.leProjectName.setObjectName(u"leProjectName")
        font2 = QFont()
        font2.setPointSize(14)
        self.leProjectName.setFont(font2)
        self.leProjectName.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.leProjectName, 2, 0, 1, 3)

        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setFont(font1)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.label, 0, 0, 1, 3)

        self.frButtons = QFrame(Form)
        self.frButtons.setObjectName(u"frButtons")
        self.frButtons.setFrameShape(QFrame.Shape.StyledPanel)
        self.frButtons.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout = QHBoxLayout(self.frButtons)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.btnClear = QPushButton(self.frButtons)
        self.btnClear.setObjectName(u"btnClear")
        self.btnClear.setFont(font1)

        self.horizontalLayout.addWidget(self.btnClear)

        self.btnNext = QPushButton(self.frButtons)
        self.btnNext.setObjectName(u"btnNext")
        self.btnNext.setFont(font1)

        self.horizontalLayout.addWidget(self.btnNext)


        self.gridLayout.addWidget(self.frButtons, 10, 0, 1, 3)

        self.frame = QFrame(Form)
        self.frame.setObjectName(u"frame")
        self.frame.setFont(font1)
        self.frame.setFrameShape(QFrame.Shape.NoFrame)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.frame.setLineWidth(3)
        self.horizontalLayout_2 = QHBoxLayout(self.frame)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.lblTotalInfo = QLabel(self.frame)
        self.lblTotalInfo.setObjectName(u"lblTotalInfo")
        self.lblTotalInfo.setFont(font1)

        self.horizontalLayout_2.addWidget(self.lblTotalInfo)

        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy1)
        self.label_2.setFont(font)

        self.horizontalLayout_2.addWidget(self.label_2)

        self.lblTotal = QLabel(self.frame)
        self.lblTotal.setObjectName(u"lblTotal")
        self.lblTotal.setFont(font)

        self.horizontalLayout_2.addWidget(self.lblTotal)


        self.gridLayout.addWidget(self.frame, 6, 2, 1, 1)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Nuevo Proyecto", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"Producto", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"Total", None))
        self.btnAdd.setText(QCoreApplication.translate("Form", u"+", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"Cantidad", None))
        self.label.setText(QCoreApplication.translate("Form", u"Proyecto", None))
        self.btnClear.setText(QCoreApplication.translate("Form", u"Limpiar", None))
        self.btnNext.setText(QCoreApplication.translate("Form", u"Siguiente", None))
        self.lblTotalInfo.setText(QCoreApplication.translate("Form", u"Total General:", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"$", None))
        self.lblTotal.setText(QCoreApplication.translate("Form", u"0", None))
    # retranslateUi

