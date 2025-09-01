# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'camera_md_data_widgetqcUHOx.ui'
##
## Created by: Qt User Interface Compiler version 6.8.1
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
from PySide6.QtWidgets import (QApplication, QFormLayout, QLabel, QLineEdit,
    QSizePolicy, QSpacerItem, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(312, 715)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        Form.setMaximumSize(QSize(312, 715))
        self.formLayout = QFormLayout(Form)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout_2 = QFormLayout()
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.label_md_location = QLabel(Form)
        self.label_md_location.setObjectName(u"label_md_location")
        font = QFont()
        font.setFamilies([u"\ud734\uba3c\ub465\uadfc\ud5e4\ub4dc\ub77c\uc778"])
        font.setPointSize(22)
        self.label_md_location.setFont(font)

        self.formLayout_2.setWidget(0, QFormLayout.LabelRole, self.label_md_location)

        self.verticalSpacer_6 = QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.formLayout_2.setItem(1, QFormLayout.LabelRole, self.verticalSpacer_6)

        self.label_title_camera = QLabel(Form)
        self.label_title_camera.setObjectName(u"label_title_camera")
        font1 = QFont()
        font1.setPointSize(15)
        font1.setBold(True)
        font1.setItalic(False)
        font1.setUnderline(True)
        font1.setStrikeOut(False)
        self.label_title_camera.setFont(font1)

        self.formLayout_2.setWidget(2, QFormLayout.LabelRole, self.label_title_camera)

        self.label_cam_lat = QLabel(Form)
        self.label_cam_lat.setObjectName(u"label_cam_lat")

        self.formLayout_2.setWidget(3, QFormLayout.LabelRole, self.label_cam_lat)

        self.line_edit_cam_lat = QLineEdit(Form)
        self.line_edit_cam_lat.setObjectName(u"line_edit_cam_lat")

        self.formLayout_2.setWidget(3, QFormLayout.FieldRole, self.line_edit_cam_lat)

        self.label_cam_lng = QLabel(Form)
        self.label_cam_lng.setObjectName(u"label_cam_lng")

        self.formLayout_2.setWidget(4, QFormLayout.LabelRole, self.label_cam_lng)

        self.line_edit_cam_lng = QLineEdit(Form)
        self.line_edit_cam_lng.setObjectName(u"line_edit_cam_lng")

        self.formLayout_2.setWidget(4, QFormLayout.FieldRole, self.line_edit_cam_lng)

        self.verticalSpacer = QSpacerItem(20, 10, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.formLayout_2.setItem(5, QFormLayout.FieldRole, self.verticalSpacer)

        self.label_cam_zoom = QLabel(Form)
        self.label_cam_zoom.setObjectName(u"label_cam_zoom")

        self.formLayout_2.setWidget(6, QFormLayout.LabelRole, self.label_cam_zoom)

        self.line_edit_cam_zoom = QLineEdit(Form)
        self.line_edit_cam_zoom.setObjectName(u"line_edit_cam_zoom")

        self.formLayout_2.setWidget(6, QFormLayout.FieldRole, self.line_edit_cam_zoom)

        self.verticalSpacer_3 = QSpacerItem(20, 10, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.formLayout_2.setItem(7, QFormLayout.FieldRole, self.verticalSpacer_3)

        self.label_cam_roll = QLabel(Form)
        self.label_cam_roll.setObjectName(u"label_cam_roll")

        self.formLayout_2.setWidget(8, QFormLayout.LabelRole, self.label_cam_roll)

        self.line_edit_cam_roll = QLineEdit(Form)
        self.line_edit_cam_roll.setObjectName(u"line_edit_cam_roll")

        self.formLayout_2.setWidget(8, QFormLayout.FieldRole, self.line_edit_cam_roll)

        self.label_cam_pitch = QLabel(Form)
        self.label_cam_pitch.setObjectName(u"label_cam_pitch")

        self.formLayout_2.setWidget(9, QFormLayout.LabelRole, self.label_cam_pitch)

        self.line_edit_cam_pitch = QLineEdit(Form)
        self.line_edit_cam_pitch.setObjectName(u"line_edit_cam_pitch")

        self.formLayout_2.setWidget(9, QFormLayout.FieldRole, self.line_edit_cam_pitch)

        self.label_cam_yaw = QLabel(Form)
        self.label_cam_yaw.setObjectName(u"label_cam_yaw")

        self.formLayout_2.setWidget(10, QFormLayout.LabelRole, self.label_cam_yaw)

        self.line_edit_cam_yaw = QLineEdit(Form)
        self.line_edit_cam_yaw.setObjectName(u"line_edit_cam_yaw")

        self.formLayout_2.setWidget(10, QFormLayout.FieldRole, self.line_edit_cam_yaw)

        self.verticalSpacer_2 = QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.formLayout_2.setItem(11, QFormLayout.LabelRole, self.verticalSpacer_2)

        self.label_title_md = QLabel(Form)
        self.label_title_md.setObjectName(u"label_title_md")
        font2 = QFont()
        font2.setPointSize(15)
        font2.setBold(True)
        font2.setUnderline(True)
        self.label_title_md.setFont(font2)

        self.formLayout_2.setWidget(12, QFormLayout.LabelRole, self.label_title_md)

        self.label_md_lat = QLabel(Form)
        self.label_md_lat.setObjectName(u"label_md_lat")

        self.formLayout_2.setWidget(13, QFormLayout.LabelRole, self.label_md_lat)

        self.line_edit_md_lat = QLineEdit(Form)
        self.line_edit_md_lat.setObjectName(u"line_edit_md_lat")

        self.formLayout_2.setWidget(13, QFormLayout.FieldRole, self.line_edit_md_lat)

        self.label_md_lng = QLabel(Form)
        self.label_md_lng.setObjectName(u"label_md_lng")

        self.formLayout_2.setWidget(14, QFormLayout.LabelRole, self.label_md_lng)

        self.line_edit_md_lng = QLineEdit(Form)
        self.line_edit_md_lng.setObjectName(u"line_edit_md_lng")

        self.formLayout_2.setWidget(14, QFormLayout.FieldRole, self.line_edit_md_lng)

        self.label_md_alt = QLabel(Form)
        self.label_md_alt.setObjectName(u"label_md_alt")

        self.formLayout_2.setWidget(15, QFormLayout.LabelRole, self.label_md_alt)

        self.line_edit_md_alt = QLineEdit(Form)
        self.line_edit_md_alt.setObjectName(u"line_edit_md_alt")

        self.formLayout_2.setWidget(15, QFormLayout.FieldRole, self.line_edit_md_alt)

        self.verticalSpacer_4 = QSpacerItem(20, 10, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.formLayout_2.setItem(16, QFormLayout.LabelRole, self.verticalSpacer_4)

        self.label_md_volt = QLabel(Form)
        self.label_md_volt.setObjectName(u"label_md_volt")

        self.formLayout_2.setWidget(17, QFormLayout.LabelRole, self.label_md_volt)

        self.line_edit_md_volt = QLineEdit(Form)
        self.line_edit_md_volt.setObjectName(u"line_edit_md_volt")

        self.formLayout_2.setWidget(17, QFormLayout.FieldRole, self.line_edit_md_volt)

        self.label_md_air_pressure = QLabel(Form)
        self.label_md_air_pressure.setObjectName(u"label_md_air_pressure")

        self.formLayout_2.setWidget(18, QFormLayout.LabelRole, self.label_md_air_pressure)

        self.line_edit_md_air_pressure = QLineEdit(Form)
        self.line_edit_md_air_pressure.setObjectName(u"line_edit_md_air_pressure")

        self.formLayout_2.setWidget(18, QFormLayout.FieldRole, self.line_edit_md_air_pressure)

        self.label_md_temperature = QLabel(Form)
        self.label_md_temperature.setObjectName(u"label_md_temperature")

        self.formLayout_2.setWidget(19, QFormLayout.LabelRole, self.label_md_temperature)

        self.line_edit_md_temperature = QLineEdit(Form)
        self.line_edit_md_temperature.setObjectName(u"line_edit_md_temperature")

        self.formLayout_2.setWidget(19, QFormLayout.FieldRole, self.line_edit_md_temperature)

        self.verticalSpacer_5 = QSpacerItem(20, 10, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.formLayout_2.setItem(20, QFormLayout.LabelRole, self.verticalSpacer_5)

        self.label_md_roll = QLabel(Form)
        self.label_md_roll.setObjectName(u"label_md_roll")

        self.formLayout_2.setWidget(21, QFormLayout.LabelRole, self.label_md_roll)

        self.line_edit_md_roll = QLineEdit(Form)
        self.line_edit_md_roll.setObjectName(u"line_edit_md_roll")

        self.formLayout_2.setWidget(21, QFormLayout.FieldRole, self.line_edit_md_roll)

        self.label_md_pitch = QLabel(Form)
        self.label_md_pitch.setObjectName(u"label_md_pitch")

        self.formLayout_2.setWidget(22, QFormLayout.LabelRole, self.label_md_pitch)

        self.line_edit_md_pitch = QLineEdit(Form)
        self.line_edit_md_pitch.setObjectName(u"line_edit_md_pitch")

        self.formLayout_2.setWidget(22, QFormLayout.FieldRole, self.line_edit_md_pitch)

        self.label_md_yaw = QLabel(Form)
        self.label_md_yaw.setObjectName(u"label_md_yaw")

        self.formLayout_2.setWidget(23, QFormLayout.LabelRole, self.label_md_yaw)

        self.line_edit_md_yaw = QLineEdit(Form)
        self.line_edit_md_yaw.setObjectName(u"line_edit_md_yaw")

        self.formLayout_2.setWidget(23, QFormLayout.FieldRole, self.line_edit_md_yaw)


        self.formLayout.setLayout(0, QFormLayout.LabelRole, self.formLayout_2)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"\uce74\uba54\ub77c/\uc784\ubb34\uc7a5\ube44 \ub370\uc774\ud130", None))
        self.label_md_location.setText(QCoreApplication.translate("Form", u"\uc911\uad6c", None))
        self.label_title_camera.setText(QCoreApplication.translate("Form", u"\uce74\uba54\ub77c \ub370\uc774\ud130", None))
        self.label_cam_lat.setText(QCoreApplication.translate("Form", u"\uc704\ub3c4", None))
        self.label_cam_lng.setText(QCoreApplication.translate("Form", u"\uacbd\ub3c4", None))
        self.label_cam_zoom.setText(QCoreApplication.translate("Form", u"\uc90c", None))
        self.label_cam_roll.setText(QCoreApplication.translate("Form", u"X\ucd95 \uae30\uc900 \ud68c\uc804 \ubc18\uacbd(Roll)", None))
        self.label_cam_pitch.setText(QCoreApplication.translate("Form", u"Y\ucd95 \uae30\uc900 \ud68c\uc804 \ubc18\uacbd(Pitch)", None))
        self.label_cam_yaw.setText(QCoreApplication.translate("Form", u"Z\ucd95 \uae30\uc900 \ud68c\uc804 \ubc18\uacbd(Yaw)", None))
        self.label_title_md.setText(QCoreApplication.translate("Form", u"\uc784\ubb34\uc7a5\ube44 \ub370\uc774\ud130", None))
        self.label_md_lat.setText(QCoreApplication.translate("Form", u"\uc704\ub3c4", None))
        self.label_md_lng.setText(QCoreApplication.translate("Form", u"\uacbd\ub3c4", None))
        self.label_md_alt.setText(QCoreApplication.translate("Form", u"\uace0\ub3c4", None))
        self.label_md_volt.setText(QCoreApplication.translate("Form", u"\uc804\uc555", None))
        self.label_md_air_pressure.setText(QCoreApplication.translate("Form", u"\uae30\uc555", None))
        self.label_md_temperature.setText(QCoreApplication.translate("Form", u"\uc628\ub3c4", None))
        self.label_md_roll.setText(QCoreApplication.translate("Form", u"X\ucd95 \uae30\uc900 \ud68c\uc804 \ubc18\uacbd(Roll)", None))
        self.label_md_pitch.setText(QCoreApplication.translate("Form", u"Y\ucd95 \uae30\uc900 \ud68c\uc804 \ubc18\uacbd(Pitch)", None))
        self.label_md_yaw.setText(QCoreApplication.translate("Form", u"Z\ucd95 \uae30\uc900 \ud68c\uc804 \ubc18\uacbd(Yaw)", None))
    # retranslateUi

