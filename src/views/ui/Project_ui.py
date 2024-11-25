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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QPushButton,
    QSizePolicy, QWidget)
import resources_rc

class Ui_Element(object):
    def setupUi(self, Element):
        if not Element.objectName():
            Element.setObjectName(u"Element")
        Element.resize(812, 42)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Element.sizePolicy().hasHeightForWidth())
        Element.setSizePolicy(sizePolicy)
        self.horizontalLayout = QHBoxLayout(Element)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.lblProjectName = QLabel(Element)
        self.lblProjectName.setObjectName(u"lblProjectName")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.lblProjectName.sizePolicy().hasHeightForWidth())
        self.lblProjectName.setSizePolicy(sizePolicy1)

        self.horizontalLayout.addWidget(self.lblProjectName)

        self.btnEdit = QPushButton(Element)
        self.btnEdit.setObjectName(u"btnEdit")
        self.btnEdit.setStyleSheet(u"")
        icon = QIcon()
        icon.addFile(u":/icons/views/assets/ic--outline-edit.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnEdit.setIcon(icon)

        self.horizontalLayout.addWidget(self.btnEdit)

        self.btnPreview = QPushButton(Element)
        self.btnPreview.setObjectName(u"btnPreview")
        icon1 = QIcon()
        icon1.addFile(u":/icons/views/assets/ic--outline-remove-red-eye.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnPreview.setIcon(icon1)

        self.horizontalLayout.addWidget(self.btnPreview)

        self.btnDelete = QPushButton(Element)
        self.btnDelete.setObjectName(u"btnDelete")
        icon2 = QIcon()
        icon2.addFile(u":/icons/views/assets/ic--outline-delete.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnDelete.setIcon(icon2)

        self.horizontalLayout.addWidget(self.btnDelete)


        self.retranslateUi(Element)

        QMetaObject.connectSlotsByName(Element)
    # setupUi

    def retranslateUi(self, Element):
        Element.setWindowTitle(QCoreApplication.translate("Element", u"Proyectos", None))
        self.lblProjectName.setText(QCoreApplication.translate("Element", u"Nombre de proyecto", None))
        self.btnEdit.setText("")
        self.btnPreview.setText("")
        self.btnDelete.setText("")
    # retranslateUi

