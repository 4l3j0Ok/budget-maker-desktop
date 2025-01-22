# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Preview.ui'
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
from PySide6.QtWebEngineWidgets import QWebEngineView
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QPushButton,
    QSizePolicy, QVBoxLayout, QWidget)
import resources_rc

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(791, 337)
        self.verticalLayout_2 = QVBoxLayout(Form)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.webview = QWebEngineView(Form)
        self.webview.setObjectName(u"webview")
        self.webview.setUrl(QUrl(u"about:blank"))

        self.verticalLayout_2.addWidget(self.webview)

        self.frOptions = QFrame(Form)
        self.frOptions.setObjectName(u"frOptions")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frOptions.sizePolicy().hasHeightForWidth())
        self.frOptions.setSizePolicy(sizePolicy)
        self.frOptions.setFrameShape(QFrame.Shape.NoFrame)
        self.frOptions.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout = QHBoxLayout(self.frOptions)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.btnHome = QPushButton(self.frOptions)
        self.btnHome.setObjectName(u"btnHome")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.btnHome.sizePolicy().hasHeightForWidth())
        self.btnHome.setSizePolicy(sizePolicy1)
        icon = QIcon()
        icon.addFile(u":/icons/views/assets/eva--home-outline.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnHome.setIcon(icon)

        self.horizontalLayout.addWidget(self.btnHome)

        self.btnSavePDF = QPushButton(self.frOptions)
        self.btnSavePDF.setObjectName(u"btnSavePDF")
        icon1 = QIcon()
        icon1.addFile(u":/icons/views/assets/eva--save-outline.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnSavePDF.setIcon(icon1)

        self.horizontalLayout.addWidget(self.btnSavePDF)


        self.verticalLayout_2.addWidget(self.frOptions)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Preview", None))
        self.btnHome.setText(QCoreApplication.translate("Form", u"Volver al inicio", None))
        self.btnSavePDF.setText(QCoreApplication.translate("Form", u"Guardar PDF", None))
    # retranslateUi

