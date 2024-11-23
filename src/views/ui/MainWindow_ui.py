# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainWindow.ui'
##
## Created by: Qt User Interface Compiler version 6.8.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (
    QCoreApplication,
    QDate,
    QDateTime,
    QLocale,
    QMetaObject,
    QObject,
    QPoint,
    QRect,
    QSize,
    QTime,
    QUrl,
    Qt,
)
from PySide6.QtGui import (
    QBrush,
    QColor,
    QConicalGradient,
    QCursor,
    QFont,
    QFontDatabase,
    QGradient,
    QIcon,
    QImage,
    QKeySequence,
    QLinearGradient,
    QPainter,
    QPalette,
    QPixmap,
    QRadialGradient,
    QTransform,
)
from PySide6.QtWidgets import (
    QApplication,
    QFrame,
    QHBoxLayout,
    QLabel,
    QLayout,
    QMainWindow,
    QPushButton,
    QSizePolicy,
    QSpacerItem,
    QVBoxLayout,
    QWidget,
)
import views.resources_rc as resources_rc


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName("MainWindow")
        MainWindow.resize(752, 296)
        MainWindow.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        MainWindow.setAutoFillBackground(False)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        sizePolicy = QSizePolicy(
            QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.centralwidget.sizePolicy().hasHeightForWidth()
        )
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setContextMenuPolicy(Qt.ContextMenuPolicy.DefaultContextMenu)
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.frNavbar = QFrame(self.centralwidget)
        self.frNavbar.setObjectName("frNavbar")
        self.frNavbar.setMaximumSize(QSize(42, 16777215))
        self.frNavbar.setFrameShape(QFrame.Shape.StyledPanel)
        self.frNavbar.setFrameShadow(QFrame.Shadow.Raised)
        self.frNavbar.setLineWidth(1)
        self.verticalLayout = QVBoxLayout(self.frNavbar)
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout.setSizeConstraint(
            QLayout.SizeConstraint.SetDefaultConstraint
        )
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.btnMenu = QPushButton(self.frNavbar)
        self.btnMenu.setObjectName("btnMenu")
        self.btnMenu.setStyleSheet("text-align: left;")
        icon = QIcon()
        icon.addFile(
            ":/icons/assets/ic--baseline-menu.svg",
            QSize(),
            QIcon.Mode.Normal,
            QIcon.State.Off,
        )
        self.btnMenu.setIcon(icon)
        self.btnMenu.setIconSize(QSize(32, 32))

        self.verticalLayout.addWidget(self.btnMenu)

        self.btnProjects = QPushButton(self.frNavbar)
        self.btnProjects.setObjectName("btnProjects")
        self.btnProjects.setStyleSheet("text-align: left;")
        icon1 = QIcon()
        icon1.addFile(
            ":/icons/assets/eos-icons--project-outlined.svg",
            QSize(),
            QIcon.Mode.Normal,
            QIcon.State.Off,
        )
        self.btnProjects.setIcon(icon1)
        self.btnProjects.setIconSize(QSize(32, 32))

        self.verticalLayout.addWidget(self.btnProjects)

        self.btnProducts = QPushButton(self.frNavbar)
        self.btnProducts.setObjectName("btnProducts")
        self.btnProducts.setStyleSheet("text-align: left;")
        icon2 = QIcon()
        icon2.addFile(
            ":/icons/assets/ic--baseline-lightbulb.svg",
            QSize(),
            QIcon.Mode.Normal,
            QIcon.State.Off,
        )
        self.btnProducts.setIcon(icon2)
        self.btnProducts.setIconSize(QSize(32, 32))

        self.verticalLayout.addWidget(self.btnProducts)

        self.verticalSpacer = QSpacerItem(
            20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding
        )

        self.verticalLayout.addItem(self.verticalSpacer)

        self.horizontalLayout.addWidget(self.frNavbar)

        self.frBody = QFrame(self.centralwidget)
        self.frBody.setObjectName("frBody")
        self.frBody.setFrameShape(QFrame.Shape.StyledPanel)
        self.frBody.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frBody)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frHeader = QFrame(self.frBody)
        self.frHeader.setObjectName("frHeader")
        self.frHeader.setMaximumSize(QSize(16777215, 80))
        self.frHeader.setFrameShape(QFrame.Shape.NoFrame)
        self.frHeader.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frHeader)
        self.verticalLayout_3.setSpacing(2)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.lblTitle = QLabel(self.frHeader)
        self.lblTitle.setObjectName("lblTitle")
        font = QFont()
        font.setFamilies(["Montserrat"])
        font.setPointSize(20)
        font.setBold(True)
        self.lblTitle.setFont(font)
        self.lblTitle.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_3.addWidget(self.lblTitle)

        self.lblDescription = QLabel(self.frHeader)
        self.lblDescription.setObjectName("lblDescription")
        font1 = QFont()
        font1.setFamilies(["Montserrat"])
        font1.setPointSize(12)
        self.lblDescription.setFont(font1)
        self.lblDescription.setAlignment(
            Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignTop
        )

        self.verticalLayout_3.addWidget(self.lblDescription)

        self.verticalLayout_2.addWidget(self.frHeader)

        self.frContent = QFrame(self.frBody)
        self.frContent.setObjectName("frContent")
        self.frContent.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.frContent.setFrameShape(QFrame.Shape.NoFrame)
        self.frContent.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frContent)
        self.verticalLayout_4.setObjectName("verticalLayout_4")

        self.verticalLayout_2.addWidget(self.frContent)

        self.horizontalLayout.addWidget(self.frBody)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)

    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(
            QCoreApplication.translate("MainWindow", "Budget Maker", None)
        )
        self.btnMenu.setText(
            QCoreApplication.translate("MainWindow", "Men\u00fa", None)
        )
        self.btnProjects.setText(
            QCoreApplication.translate("MainWindow", "Proyectos", None)
        )
        self.btnProducts.setText(
            QCoreApplication.translate("MainWindow", "Productos y Servicios", None)
        )
        self.lblTitle.setText(
            QCoreApplication.translate("MainWindow", "{Titulo}", None)
        )
        self.lblDescription.setText(
            QCoreApplication.translate("MainWindow", "{Descripci\u00f3n}", None)
        )

    # retranslateUi
