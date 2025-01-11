# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'NewProjectTemplate.ui'
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
        self.verticalLayout_2 = QVBoxLayout(Form)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.lblProject = QLabel(Form)
        self.lblProject.setObjectName(u"lblProject")
        font = QFont()
        font.setBold(True)
        self.lblProject.setFont(font)
        self.lblProject.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_2.addWidget(self.lblProject)

        self.leProjectName = QLineEdit(Form)
        self.leProjectName.setObjectName(u"leProjectName")
        self.leProjectName.setEnabled(False)
        self.leProjectName.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_2.addWidget(self.leProjectName)

        self.scrollArea = QScrollArea(Form)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setFrameShape(QFrame.Shape.NoFrame)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 690, 229))
        self.verticalLayout = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")

        self.verticalLayout.addLayout(self.gridLayout)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_2.addWidget(self.scrollArea)

        self.frButtons = QFrame(Form)
        self.frButtons.setObjectName(u"frButtons")
        self.frButtons.setFrameShape(QFrame.Shape.StyledPanel)
        self.frButtons.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout = QHBoxLayout(self.frButtons)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.btnBack = QPushButton(self.frButtons)
        self.btnBack.setObjectName(u"btnBack")

        self.horizontalLayout.addWidget(self.btnBack)

        self.btnNext = QPushButton(self.frButtons)
        self.btnNext.setObjectName(u"btnNext")

        self.horizontalLayout.addWidget(self.btnNext)


        self.verticalLayout_2.addWidget(self.frButtons)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Nuevo Proyecto", None))
        self.lblProject.setText(QCoreApplication.translate("Form", u"Proyecto", None))
        self.leProjectName.setPlaceholderText(QCoreApplication.translate("Form", u"Nombre no establecido", None))
        self.btnBack.setText(QCoreApplication.translate("Form", u"Atr\u00e1s", None))
        self.btnNext.setText(QCoreApplication.translate("Form", u"Siguiente", None))
    # retranslateUi

