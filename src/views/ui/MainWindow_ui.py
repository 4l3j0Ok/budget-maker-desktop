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
        MainWindow.resize(752, 310)
        icon = QIcon()
        icon.addFile(u":/icons/views/assets/icon.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        MainWindow.setWindowIcon(icon)
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
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frNavbar.sizePolicy().hasHeightForWidth())
        self.frNavbar.setSizePolicy(sizePolicy1)
        self.frNavbar.setFrameShape(QFrame.Shape.StyledPanel)
        self.verticalLayout = QVBoxLayout(self.frNavbar)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.btnMenu = QPushButton(self.frNavbar)
        self.btnMenu.setObjectName(u"btnMenu")
        self.btnMenu.setStyleSheet(u"text-align: left;")
        icon1 = QIcon()
        icon1.addFile(u":/icons/views/assets/ic--baseline-menu.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnMenu.setIcon(icon1)
        self.btnMenu.setIconSize(QSize(32, 32))

        self.verticalLayout.addWidget(self.btnMenu)

        self.btnHome = QPushButton(self.frNavbar)
        self.btnHome.setObjectName(u"btnHome")
        self.btnHome.setStyleSheet(u"text-align: left;")
        icon2 = QIcon()
        icon2.addFile(u":/icons/views/assets/eva--home-outline.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnHome.setIcon(icon2)
        self.btnHome.setIconSize(QSize(32, 32))

        self.verticalLayout.addWidget(self.btnHome)

        self.btnProjects = QPushButton(self.frNavbar)
        self.btnProjects.setObjectName(u"btnProjects")
        self.btnProjects.setStyleSheet(u"text-align: left;")
        icon3 = QIcon()
        icon3.addFile(u":/icons/views/assets/eos-icons--project-outlined.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnProjects.setIcon(icon3)
        self.btnProjects.setIconSize(QSize(32, 32))

        self.verticalLayout.addWidget(self.btnProjects)

        self.btnProducts = QPushButton(self.frNavbar)
        self.btnProducts.setObjectName(u"btnProducts")
        self.btnProducts.setStyleSheet(u"text-align: left;")
        icon4 = QIcon()
        icon4.addFile(u":/icons/views/assets/ant-design--product-outlined.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnProducts.setIcon(icon4)
        self.btnProducts.setIconSize(QSize(32, 32))

        self.verticalLayout.addWidget(self.btnProducts)

        self.btnSettings = QPushButton(self.frNavbar)
        self.btnSettings.setObjectName(u"btnSettings")
        self.btnSettings.setStyleSheet(u"text-align: left;")
        icon5 = QIcon()
        icon5.addFile(u":/icons/views/assets/eva--settings-outline.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnSettings.setIcon(icon5)
        self.btnSettings.setIconSize(QSize(32, 32))

        self.verticalLayout.addWidget(self.btnSettings)

        self.btnAbout = QPushButton(self.frNavbar)
        self.btnAbout.setObjectName(u"btnAbout")
        self.btnAbout.setStyleSheet(u"text-align: left;")
        icon6 = QIcon()
        icon6.addFile(u":/icons/views/assets/ix--about.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnAbout.setIcon(icon6)
        self.btnAbout.setIconSize(QSize(32, 32))

        self.verticalLayout.addWidget(self.btnAbout)

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
        self.frHeader.setFrameShape(QFrame.Shape.NoFrame)
        self.frHeader.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frHeader)
        self.verticalLayout_3.setSpacing(2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.lblTitle = QLabel(self.frHeader)
        self.lblTitle.setObjectName(u"lblTitle")
        font = QFont()
        font.setFamilies([u"Segoe UI"])
        font.setPointSize(20)
        font.setBold(True)
        self.lblTitle.setFont(font)
        self.lblTitle.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_3.addWidget(self.lblTitle)

        self.lblDescription = QLabel(self.frHeader)
        self.lblDescription.setObjectName(u"lblDescription")
        font1 = QFont()
        font1.setFamilies([u"Segoe UI"])
        font1.setPointSize(12)
        self.lblDescription.setFont(font1)
        self.lblDescription.setAlignment(Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignTop)

        self.verticalLayout_3.addWidget(self.lblDescription)


        self.verticalLayout_2.addWidget(self.frHeader)

        self.frContent = QFrame(self.frBody)
        self.frContent.setObjectName(u"frContent")
        self.frContent.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.frContent.setFrameShape(QFrame.Shape.NoFrame)
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
#if QT_CONFIG(tooltip)
        self.btnMenu.setToolTip(QCoreApplication.translate("MainWindow", u"Expandir men\u00fa", None))
#endif // QT_CONFIG(tooltip)
        self.btnMenu.setText(QCoreApplication.translate("MainWindow", u"Men\u00fa", None))
#if QT_CONFIG(tooltip)
        self.btnHome.setToolTip(QCoreApplication.translate("MainWindow", u"P\u00e1gina de inicio", None))
#endif // QT_CONFIG(tooltip)
        self.btnHome.setText(QCoreApplication.translate("MainWindow", u"Inicio", None))
#if QT_CONFIG(tooltip)
        self.btnProjects.setToolTip(QCoreApplication.translate("MainWindow", u"Proyectos", None))
#endif // QT_CONFIG(tooltip)
        self.btnProjects.setText(QCoreApplication.translate("MainWindow", u"Proyectos", None))
#if QT_CONFIG(tooltip)
        self.btnProducts.setToolTip(QCoreApplication.translate("MainWindow", u"Productos", None))
#endif // QT_CONFIG(tooltip)
        self.btnProducts.setText(QCoreApplication.translate("MainWindow", u"Productos y Servicios", None))
#if QT_CONFIG(tooltip)
        self.btnSettings.setToolTip(QCoreApplication.translate("MainWindow", u"Configuraci\u00f3n", None))
#endif // QT_CONFIG(tooltip)
        self.btnSettings.setText(QCoreApplication.translate("MainWindow", u"Configuraci\u00f3n", None))
#if QT_CONFIG(tooltip)
        self.btnAbout.setToolTip(QCoreApplication.translate("MainWindow", u"Acerca de", None))
#endif // QT_CONFIG(tooltip)
        self.btnAbout.setText(QCoreApplication.translate("MainWindow", u"Acerca de", None))
        self.lblTitle.setText(QCoreApplication.translate("MainWindow", u"{Titulo}", None))
        self.lblDescription.setText(QCoreApplication.translate("MainWindow", u"{Descripci\u00f3n}", None))
    # retranslateUi

