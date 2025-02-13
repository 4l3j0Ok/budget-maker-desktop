# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Settings.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QFrame, QGridLayout,
    QGroupBox, QHBoxLayout, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(640, 480)
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.gbAppearance = QGroupBox(Form)
        self.gbAppearance.setObjectName(u"gbAppearance")
        self.verticalLayout_2 = QVBoxLayout(self.gbAppearance)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.cbDarkMode = QCheckBox(self.gbAppearance)
        self.cbDarkMode.setObjectName(u"cbDarkMode")

        self.verticalLayout_2.addWidget(self.cbDarkMode)


        self.verticalLayout.addWidget(self.gbAppearance)

        self.gbFunctions = QGroupBox(Form)
        self.gbFunctions.setObjectName(u"gbFunctions")
        self.horizontalLayout = QHBoxLayout(self.gbFunctions)
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(9, 9, 9, 9)
        self.frPDFExport = QFrame(self.gbFunctions)
        self.frPDFExport.setObjectName(u"frPDFExport")
        self.frPDFExport.setFrameShape(QFrame.Shape.NoFrame)
        self.frPDFExport.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout = QGridLayout(self.frPDFExport)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setHorizontalSpacing(6)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.lePDFExportPath = QLineEdit(self.frPDFExport)
        self.lePDFExportPath.setObjectName(u"lePDFExportPath")

        self.gridLayout.addWidget(self.lePDFExportPath, 1, 0, 1, 1)

        self.btnSearch = QPushButton(self.frPDFExport)
        self.btnSearch.setObjectName(u"btnSearch")

        self.gridLayout.addWidget(self.btnSearch, 1, 1, 1, 1)

        self.label = QLabel(self.frPDFExport)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.cbSaveWithoutAsk = QCheckBox(self.frPDFExport)
        self.cbSaveWithoutAsk.setObjectName(u"cbSaveWithoutAsk")

        self.gridLayout.addWidget(self.cbSaveWithoutAsk, 2, 0, 1, 2)


        self.horizontalLayout.addWidget(self.frPDFExport)


        self.verticalLayout.addWidget(self.gbFunctions)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Settings", None))
        self.gbAppearance.setTitle(QCoreApplication.translate("Form", u"Apariencia", None))
        self.cbDarkMode.setText(QCoreApplication.translate("Form", u"Modo oscuro", None))
        self.gbFunctions.setTitle(QCoreApplication.translate("Form", u"Funcionalidad", None))
#if QT_CONFIG(tooltip)
        self.btnSearch.setToolTip(QCoreApplication.translate("Form", u"Elegir una carpeta del PC.", None))
#endif // QT_CONFIG(tooltip)
        self.btnSearch.setText(QCoreApplication.translate("Form", u"Examinar...", None))
        self.label.setText(QCoreApplication.translate("Form", u"Ruta de exportaci\u00f3n por defecto para PDFs", None))
#if QT_CONFIG(tooltip)
        self.cbSaveWithoutAsk.setToolTip(QCoreApplication.translate("Form", u"Si est\u00e1 marcado, al guardar un PDF, se guardar\u00e1 en la ruta de exportaci\u00f3n por defecto sin preguntar si se desea guardar, estableciendo un nombre por defecto.", None))
#endif // QT_CONFIG(tooltip)
        self.cbSaveWithoutAsk.setText(QCoreApplication.translate("Form", u"Guardar en esta ruta sin preguntar", None))
    # retranslateUi

