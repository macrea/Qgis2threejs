# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\Documents\minorua\QGIS\plugins\Qgis2threejs\ui\pcproperties.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_PCPropertiesWidget(object):
    def setupUi(self, PCPropertiesWidget):
        PCPropertiesWidget.setObjectName("PCPropertiesWidget")
        PCPropertiesWidget.resize(335, 366)
        self.verticalLayout = QtWidgets.QVBoxLayout(PCPropertiesWidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBox = QtWidgets.QGroupBox(PCPropertiesWidget)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.lineEdit_Name = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_Name.setObjectName("lineEdit_Name")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEdit_Name)
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.url = QtWidgets.QLineEdit(self.groupBox)
        self.url.setStyleSheet("background-color: #F0F0F0;")
        self.url.setReadOnly(True)
        self.url.setObjectName("url")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.url)
        self.verticalLayout_2.addLayout(self.formLayout)
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.textBrowser = QtWidgets.QTextBrowser(self.groupBox)
        self.textBrowser.setMinimumSize(QtCore.QSize(0, 100))
        self.textBrowser.setObjectName("textBrowser")
        self.verticalLayout_2.addWidget(self.textBrowser)
        self.verticalLayout.addWidget(self.groupBox)
        self.groupBox_2 = QtWidgets.QGroupBox(PCPropertiesWidget)
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label_17 = QtWidgets.QLabel(self.groupBox_2)
        self.label_17.setObjectName("label_17")
        self.gridLayout.addWidget(self.label_17, 0, 0, 1, 1)
        self.horizontalSlider_Opacity = QtWidgets.QSlider(self.groupBox_2)
        self.horizontalSlider_Opacity.setMaximum(100)
        self.horizontalSlider_Opacity.setProperty("value", 100)
        self.horizontalSlider_Opacity.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_Opacity.setObjectName("horizontalSlider_Opacity")
        self.gridLayout.addWidget(self.horizontalSlider_Opacity, 0, 1, 1, 1)
        self.spinBox_Opacity = QtWidgets.QSpinBox(self.groupBox_2)
        self.spinBox_Opacity.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.spinBox_Opacity.sizePolicy().hasHeightForWidth())
        self.spinBox_Opacity.setSizePolicy(sizePolicy)
        self.spinBox_Opacity.setPrefix("")
        self.spinBox_Opacity.setMinimum(0)
        self.spinBox_Opacity.setMaximum(100)
        self.spinBox_Opacity.setSingleStep(1)
        self.spinBox_Opacity.setProperty("value", 100)
        self.spinBox_Opacity.setObjectName("spinBox_Opacity")
        self.gridLayout.addWidget(self.spinBox_Opacity, 0, 2, 1, 1)
        self.verticalLayout_4.addLayout(self.gridLayout)
        self.verticalLayout.addWidget(self.groupBox_2)
        self.groupBox_3 = QtWidgets.QGroupBox(PCPropertiesWidget)
        self.groupBox_3.setObjectName("groupBox_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.groupBox_3)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.checkBox_Visible = QtWidgets.QCheckBox(self.groupBox_3)
        self.checkBox_Visible.setChecked(True)
        self.checkBox_Visible.setObjectName("checkBox_Visible")
        self.verticalLayout_3.addWidget(self.checkBox_Visible)
        self.verticalLayout.addWidget(self.groupBox_3)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)

        self.retranslateUi(PCPropertiesWidget)
        self.spinBox_Opacity.valueChanged['int'].connect(self.horizontalSlider_Opacity.setValue)
        self.horizontalSlider_Opacity.valueChanged['int'].connect(self.spinBox_Opacity.setValue)
        QtCore.QMetaObject.connectSlotsByName(PCPropertiesWidget)
        PCPropertiesWidget.setTabOrder(self.lineEdit_Name, self.url)
        PCPropertiesWidget.setTabOrder(self.url, self.textBrowser)
        PCPropertiesWidget.setTabOrder(self.textBrowser, self.horizontalSlider_Opacity)
        PCPropertiesWidget.setTabOrder(self.horizontalSlider_Opacity, self.spinBox_Opacity)
        PCPropertiesWidget.setTabOrder(self.spinBox_Opacity, self.checkBox_Visible)

    def retranslateUi(self, PCPropertiesWidget):
        _translate = QtCore.QCoreApplication.translate
        PCPropertiesWidget.setWindowTitle(_translate("PCPropertiesWidget", "Form"))
        self.groupBox.setTitle(_translate("PCPropertiesWidget", "General"))
        self.label.setText(_translate("PCPropertiesWidget", "Name"))
        self.label_3.setText(_translate("PCPropertiesWidget", "URL"))
        self.label_2.setText(_translate("PCPropertiesWidget", "Information"))
        self.groupBox_2.setTitle(_translate("PCPropertiesWidget", "Material"))
        self.label_17.setText(_translate("PCPropertiesWidget", "Opacity (%)"))
        self.groupBox_3.setTitle(_translate("PCPropertiesWidget", "Other Options"))
        self.checkBox_Visible.setText(_translate("PCPropertiesWidget", "Visible on load"))