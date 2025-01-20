# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Project.ui'
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

class Ui_Element(object):
    def setupUi(self, Element):
        if not Element.objectName():
            Element.setObjectName(u"Element")
        Element.resize(626, 44)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Element.sizePolicy().hasHeightForWidth())
        Element.setSizePolicy(sizePolicy)
        self.verticalLayout = QVBoxLayout(Element)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frBox = QFrame(Element)
        self.frBox.setObjectName(u"frBox")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frBox.sizePolicy().hasHeightForWidth())
        self.frBox.setSizePolicy(sizePolicy1)
        self.frBox.setLineWidth(1)
        self.horizontalLayout_2 = QHBoxLayout(self.frBox)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(9, -1, -1, -1)
        self.lblProjectName = QLabel(self.frBox)
        self.lblProjectName.setObjectName(u"lblProjectName")
        sizePolicy1.setHeightForWidth(self.lblProjectName.sizePolicy().hasHeightForWidth())
        self.lblProjectName.setSizePolicy(sizePolicy1)

        self.horizontalLayout_2.addWidget(self.lblProjectName)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.btnEdit = QPushButton(self.frBox)
        self.btnEdit.setObjectName(u"btnEdit")
        self.btnEdit.setStyleSheet(u"")
        icon = QIcon()
        icon.addFile(u":/icons/views/assets/ic--outline-edit.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnEdit.setIcon(icon)

        self.horizontalLayout_2.addWidget(self.btnEdit)

        self.btnPreview = QPushButton(self.frBox)
        self.btnPreview.setObjectName(u"btnPreview")
        icon1 = QIcon()
        icon1.addFile(u":/icons/views/assets/eva--eye-outline.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnPreview.setIcon(icon1)

        self.horizontalLayout_2.addWidget(self.btnPreview)

        self.btnDelete = QPushButton(self.frBox)
        self.btnDelete.setObjectName(u"btnDelete")
        icon2 = QIcon()
        icon2.addFile(u":/icons/views/assets/ic--outline-delete.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnDelete.setIcon(icon2)

        self.horizontalLayout_2.addWidget(self.btnDelete)


        self.verticalLayout.addWidget(self.frBox)


        self.retranslateUi(Element)

        QMetaObject.connectSlotsByName(Element)
    # setupUi

    def retranslateUi(self, Element):
        Element.setWindowTitle(QCoreApplication.translate("Element", u"Proyecto", None))
        self.lblProjectName.setText(QCoreApplication.translate("Element", u"Nombre de proyecto", None))
        self.btnEdit.setText("")
        self.btnPreview.setText("")
        self.btnDelete.setText("")
    # retranslateUi

