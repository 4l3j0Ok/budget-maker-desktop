# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainWindow.ui'
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
    QLayout, QMainWindow, QPushButton, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)
import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(709, 432)
        MainWindow.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        MainWindow.setAutoFillBackground(False)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setContextMenuPolicy(Qt.ContextMenuPolicy.DefaultContextMenu)
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.frNavbar = QFrame(self.centralwidget)
        self.frNavbar.setObjectName(u"frNavbar")
        self.frNavbar.setMaximumSize(QSize(42, 16777215))
        self.frNavbar.setFrameShape(QFrame.Shape.StyledPanel)
        self.frNavbar.setFrameShadow(QFrame.Shadow.Raised)
        self.frNavbar.setLineWidth(1)
        self.verticalLayout = QVBoxLayout(self.frNavbar)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.btnMenu = QPushButton(self.frNavbar)
        self.btnMenu.setObjectName(u"btnMenu")
        self.btnMenu.setStyleSheet(u"text-align: left;\n"
"hover {\n"
"background-color: red;\n"
"}")
        icon = QIcon()
        icon.addFile(u":/icons/assets/ic--baseline-menu.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnMenu.setIcon(icon)
        self.btnMenu.setIconSize(QSize(32, 32))
        self.btnMenu.setFlat(True)

        self.verticalLayout.addWidget(self.btnMenu)

        self.btnProjects = QPushButton(self.frNavbar)
        self.btnProjects.setObjectName(u"btnProjects")
        self.btnProjects.setStyleSheet(u"text-align: left;")
        icon1 = QIcon()
        icon1.addFile(u":/icons/assets/eos-icons--project-outlined.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnProjects.setIcon(icon1)
        self.btnProjects.setIconSize(QSize(32, 32))
        self.btnProjects.setFlat(True)

        self.verticalLayout.addWidget(self.btnProjects)

        self.btnProducts = QPushButton(self.frNavbar)
        self.btnProducts.setObjectName(u"btnProducts")
        self.btnProducts.setStyleSheet(u"text-align: left;")
        icon2 = QIcon()
        icon2.addFile(u":/icons/assets/ic--baseline-lightbulb.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnProducts.setIcon(icon2)
        self.btnProducts.setIconSize(QSize(32, 32))
        self.btnProducts.setAutoDefault(False)
        self.btnProducts.setFlat(True)

        self.verticalLayout.addWidget(self.btnProducts)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.horizontalLayout.addWidget(self.frNavbar)

        self.frBody = QFrame(self.centralwidget)
        self.frBody.setObjectName(u"frBody")
        self.frBody.setFrameShape(QFrame.Shape.StyledPanel)
        self.frBody.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frBody)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frHeader = QFrame(self.frBody)
        self.frHeader.setObjectName(u"frHeader")
        self.frHeader.setMaximumSize(QSize(16777215, 80))
        self.frHeader.setFrameShape(QFrame.Shape.StyledPanel)
        self.frHeader.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frHeader)
        self.verticalLayout_3.setSpacing(2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.verticalLayout_3.setContentsMargins(9, 9, 9, 9)
        self.lblTitle = QLabel(self.frHeader)
        self.lblTitle.setObjectName(u"lblTitle")
        font = QFont()
        font.setFamilies([u"Montserrat"])
        font.setPointSize(20)
        self.lblTitle.setFont(font)
        self.lblTitle.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_3.addWidget(self.lblTitle)

        self.lblDescription = QLabel(self.frHeader)
        self.lblDescription.setObjectName(u"lblDescription")
        font1 = QFont()
        font1.setFamilies([u"Montserrat"])
        font1.setPointSize(9)
        self.lblDescription.setFont(font1)
        self.lblDescription.setAlignment(Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignTop)

        self.verticalLayout_3.addWidget(self.lblDescription)


        self.verticalLayout_2.addWidget(self.frHeader)

        self.frContent = QFrame(self.frBody)
        self.frContent.setObjectName(u"frContent")
        self.frContent.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.frContent.setFrameShape(QFrame.Shape.StyledPanel)
        self.frContent.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frContent)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")

        self.verticalLayout_2.addWidget(self.frContent)


        self.horizontalLayout.addWidget(self.frBody)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Budget Maker", None))
        self.btnMenu.setText(QCoreApplication.translate("MainWindow", u"Men\u00fa", None))
        self.btnProjects.setText(QCoreApplication.translate("MainWindow", u"Proyectos", None))
        self.btnProducts.setText(QCoreApplication.translate("MainWindow", u"Productos y Servicios", None))
        self.lblTitle.setText(QCoreApplication.translate("MainWindow", u"{Titulo}", None))
        self.lblDescription.setText(QCoreApplication.translate("MainWindow", u"{Descripci\u00f3n}", None))
    # retranslateUi

