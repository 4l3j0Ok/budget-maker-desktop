# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'About.ui'
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
    QSizePolicy, QVBoxLayout, QWidget)
import resources_rc

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(640, 480)
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frIcon = QFrame(Form)
        self.frIcon.setObjectName(u"frIcon")
        self.frIcon.setFrameShape(QFrame.Shape.NoFrame)
        self.frIcon.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout = QHBoxLayout(self.frIcon)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.lblBMIcon = QLabel(self.frIcon)
        self.lblBMIcon.setObjectName(u"lblBMIcon")
        self.lblBMIcon.setMaximumSize(QSize(250, 250))
        self.lblBMIcon.setPixmap(QPixmap(u":/icons/views/assets/icon.png"))
        self.lblBMIcon.setScaledContents(True)
        self.lblBMIcon.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout.addWidget(self.lblBMIcon)


        self.verticalLayout.addWidget(self.frIcon)

        self.lblTitle = QLabel(Form)
        self.lblTitle.setObjectName(u"lblTitle")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblTitle.sizePolicy().hasHeightForWidth())
        self.lblTitle.setSizePolicy(sizePolicy)
        font = QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.lblTitle.setFont(font)
        self.lblTitle.setAlignment(Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignTop)

        self.verticalLayout.addWidget(self.lblTitle)

        self.lbAbout = QLabel(Form)
        self.lbAbout.setObjectName(u"lbAbout")
        self.lbAbout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.lbAbout)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Acerca de", None))
        self.lblBMIcon.setText("")
        self.lblTitle.setText(QCoreApplication.translate("Form", u"Budget Maker Desktop {version}", None))
        self.lbAbout.setText(QCoreApplication.translate("Form", u"<b>Desarrollado por</b>: \n"
"<p>\n"
"Alejo Sarmiento (<a href=\"https://alejoide.com\">Alejoide</span></a>)\n"
"</p>\n"
"\n"
"<p>\n"
"<b>Licencia</b>:\n"
"</p>\n"
"<p>\n"
"Este software es de c\u00f3digo abierto, pero su uso comercial est\u00e1 restringido.\n"
"<br>\n"
"Para m\u00e1s informaci\u00f3n y contribuciones, visita el repositorio oficial.\n"
"</p>\n"
"", None))
    # retranslateUi

