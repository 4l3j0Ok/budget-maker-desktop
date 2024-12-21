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
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)
import resources_rc

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
        self.frTotal = QFrame(Form)
        self.frTotal.setObjectName(u"frTotal")
        font = QFont()
        font.setPointSize(12)
        self.frTotal.setFont(font)
        self.frTotal.setFrameShape(QFrame.Shape.NoFrame)
        self.frTotal.setFrameShadow(QFrame.Shadow.Raised)
        self.frTotal.setLineWidth(3)
        self.horizontalLayout_2 = QHBoxLayout(self.frTotal)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.lblTotalInfo = QLabel(self.frTotal)
        self.lblTotalInfo.setObjectName(u"lblTotalInfo")
        font1 = QFont()
        font1.setPointSize(9)
        self.lblTotalInfo.setFont(font1)

        self.horizontalLayout_2.addWidget(self.lblTotalInfo)

        self.lblPrice = QLabel(self.frTotal)
        self.lblPrice.setObjectName(u"lblPrice")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.lblPrice.sizePolicy().hasHeightForWidth())
        self.lblPrice.setSizePolicy(sizePolicy1)
        font2 = QFont()
        font2.setPointSize(9)
        font2.setBold(True)
        self.lblPrice.setFont(font2)

        self.horizontalLayout_2.addWidget(self.lblPrice)

        self.lblTotal = QLabel(self.frTotal)
        self.lblTotal.setObjectName(u"lblTotal")
        self.lblTotal.setFont(font2)

        self.horizontalLayout_2.addWidget(self.lblTotal)


        self.gridLayout.addWidget(self.frTotal, 6, 1, 1, 1)

        self.scrollArea = QScrollArea(Form)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setFrameShape(QFrame.Shape.NoFrame)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 690, 119))
        self.verticalLayout = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.gridLayout.addWidget(self.scrollArea, 4, 0, 1, 2)

        self.frColumns = QFrame(Form)
        self.frColumns.setObjectName(u"frColumns")
        self.frColumns.setFrameShape(QFrame.Shape.NoFrame)
        self.frColumns.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frColumns)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label = QLabel(self.frColumns)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_3.addWidget(self.label)

        self.label_2 = QLabel(self.frColumns)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_3.addWidget(self.label_2)

        self.label_3 = QLabel(self.frColumns)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_3.addWidget(self.label_3)

        self.label_4 = QLabel(self.frColumns)
        self.label_4.setObjectName(u"label_4")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy2)
        self.label_4.setMinimumSize(QSize(80, 0))
        self.label_4.setBaseSize(QSize(70, 0))
        self.label_4.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_3.addWidget(self.label_4)


        self.gridLayout.addWidget(self.frColumns, 3, 0, 1, 2)

        self.leProjectName = QLineEdit(Form)
        self.leProjectName.setObjectName(u"leProjectName")
        self.leProjectName.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.leProjectName, 2, 0, 1, 2)

        self.frButtons = QFrame(Form)
        self.frButtons.setObjectName(u"frButtons")
        self.frButtons.setFrameShape(QFrame.Shape.StyledPanel)
        self.frButtons.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout = QHBoxLayout(self.frButtons)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.btnClear = QPushButton(self.frButtons)
        self.btnClear.setObjectName(u"btnClear")

        self.horizontalLayout.addWidget(self.btnClear)

        self.btnNext = QPushButton(self.frButtons)
        self.btnNext.setObjectName(u"btnNext")

        self.horizontalLayout.addWidget(self.btnNext)


        self.gridLayout.addWidget(self.frButtons, 10, 0, 1, 2)

        self.btnAdd = QPushButton(Form)
        self.btnAdd.setObjectName(u"btnAdd")
        font3 = QFont()
        font3.setBold(True)
        self.btnAdd.setFont(font3)

        self.gridLayout.addWidget(self.btnAdd, 5, 0, 1, 2)

        self.lblProject = QLabel(Form)
        self.lblProject.setObjectName(u"lblProject")
        self.lblProject.setFont(font3)
        self.lblProject.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.lblProject, 0, 0, 1, 2)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Nuevo Proyecto", None))
        self.lblTotalInfo.setText(QCoreApplication.translate("Form", u"Total General:", None))
        self.lblPrice.setText(QCoreApplication.translate("Form", u"$", None))
        self.lblTotal.setText(QCoreApplication.translate("Form", u"0", None))
        self.label.setText(QCoreApplication.translate("Form", u"Producto", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"Cantidad", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"Total", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"Acci\u00f3n", None))
        self.leProjectName.setPlaceholderText(QCoreApplication.translate("Form", u"Ingresa el nombre del proyecto", None))
        self.btnClear.setText(QCoreApplication.translate("Form", u"Limpiar", None))
        self.btnNext.setText(QCoreApplication.translate("Form", u"Siguiente", None))
        self.btnAdd.setText(QCoreApplication.translate("Form", u"+", None))
        self.lblProject.setText(QCoreApplication.translate("Form", u"Proyecto", None))
    # retranslateUi

