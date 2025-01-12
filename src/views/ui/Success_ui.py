# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Success.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QPushButton, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)
import resources_rc

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        self.horizontalLayout_3 = QHBoxLayout(Form)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.frContent = QFrame(Form)
        self.frContent.setObjectName(u"frContent")
        self.frContent.setMaximumSize(QSize(600, 600))
        self.frContent.setFrameShape(QFrame.Shape.NoFrame)
        self.frContent.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frContent)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_2)

        self.frImage = QFrame(self.frContent)
        self.frImage.setObjectName(u"frImage")
        self.frImage.setFrameShape(QFrame.Shape.NoFrame)
        self.frImage.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frImage)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.lblImage = QLabel(self.frImage)
        self.lblImage.setObjectName(u"lblImage")
        self.lblImage.setMaximumSize(QSize(410, 300))
        self.lblImage.setFrameShape(QFrame.Shape.NoFrame)
        self.lblImage.setPixmap(QPixmap(u":/images/views/assets/undraw--success.svg"))
        self.lblImage.setScaledContents(True)
        self.lblImage.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lblImage.setMargin(20)

        self.horizontalLayout_2.addWidget(self.lblImage)


        self.verticalLayout_2.addWidget(self.frImage)

        self.label = QLabel(self.frContent)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label.setWordWrap(True)

        self.verticalLayout_2.addWidget(self.label)

        self.label_2 = QLabel(self.frContent)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_2.setWordWrap(True)

        self.verticalLayout_2.addWidget(self.label_2)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.frOptions = QFrame(self.frContent)
        self.frOptions.setObjectName(u"frOptions")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frOptions.sizePolicy().hasHeightForWidth())
        self.frOptions.setSizePolicy(sizePolicy1)
        self.frOptions.setFrameShape(QFrame.Shape.NoFrame)
        self.frOptions.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout = QHBoxLayout(self.frOptions)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.btnHome = QPushButton(self.frOptions)
        self.btnHome.setObjectName(u"btnHome")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.btnHome.sizePolicy().hasHeightForWidth())
        self.btnHome.setSizePolicy(sizePolicy2)
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


        self.horizontalLayout_3.addWidget(self.frContent)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"\u00c9xito", None))
        self.lblImage.setText("")
        self.label.setText(QCoreApplication.translate("Form", u"\u00a1Proyecto guardado con \u00e9xito!", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"Tu proyecto ha sido creado correctamente. Puedes descargar el PDF o volver a la p\u00e1gina de proyectos y guardarlo m\u00e1s tarde.", None))
        self.btnHome.setText(QCoreApplication.translate("Form", u"Volver al inicio", None))
        self.btnSavePDF.setText(QCoreApplication.translate("Form", u"Guardar PDF", None))
    # retranslateUi

