# -------------YT video and audio downloader------------------
# --------------Developed by: Sayed Reda----------------------


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog
from pytube import *
import os
import sys


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(566, 542)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("img.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form.setWindowIcon(icon)
        self.main_label = QtWidgets.QLabel(Form)
        self.main_label.setGeometry(QtCore.QRect(160, 10, 231, 41))
        self.main_label.setStyleSheet("QLabel {\n"
                                      "font-size: 18px;\n"
                                      "}")
        self.main_label.setTextFormat(QtCore.Qt.AutoText)
        self.main_label.setObjectName("main_label")
        self.url_label = QtWidgets.QLabel(Form)
        self.url_label.setGeometry(QtCore.QRect(40, 80, 51, 16))
        self.url_label.setStyleSheet("QLabel {\n"
                                     "font-size: 16px\n"
                                     "}")
        self.url_label.setObjectName("url_label")
        self.link_field = QtWidgets.QLineEdit(Form)
        self.link_field.setGeometry(QtCore.QRect(90, 80, 411, 20))
        self.link_field.setObjectName("link_field")
        self.quallity_combo = QtWidgets.QComboBox(Form)
        self.quallity_combo.setGeometry(QtCore.QRect(90, 160, 91, 22))
        self.quallity_combo.setObjectName("quallity_combo")
        self.quallity_combo.addItem("")
        self.quallity_combo.addItem("")
        self.quallity_combo.addItem("")
        self.quallity_combo.addItem("")
        self.quallity_combo.addItem("")
        self.quallity_combo.addItem("")
        self.quality_label = QtWidgets.QLabel(Form)
        self.quality_label.setGeometry(QtCore.QRect(30, 160, 51, 20))
        self.quality_label.setStyleSheet("QLabel {\n"
                                         "font-size: 15px;\n"
                                         "}")
        self.quality_label.setObjectName("quality_label")
        self.type_label = QtWidgets.QLabel(Form)
        self.type_label.setGeometry(QtCore.QRect(350, 160, 47, 21))
        self.type_label.setStyleSheet("QLabel {\n"
                                      "font-size: 15px;\n"
                                      "}")
        self.type_label.setObjectName("type_label")
        self.type_comobo = QtWidgets.QComboBox(Form)
        self.type_comobo.setGeometry(QtCore.QRect(400, 160, 101, 22))
        self.type_comobo.setObjectName("type_comobo")
        self.type_comobo.addItem("")
        self.type_comobo.addItem("")
        self.type_comobo.addItem("")
        self.location_field = QtWidgets.QLineEdit(Form)
        self.location_field.setGeometry(QtCore.QRect(90, 230, 331, 20))
        self.location_field.setObjectName("location_field")
        self.location_label = QtWidgets.QLabel(Form)
        self.location_label.setGeometry(QtCore.QRect(20, 230, 61, 16))
        self.location_label.setStyleSheet("QLabel {\n"
                                          "font-size: 15px;\n"
                                          "}")
        self.location_label.setObjectName("location_label")
        self.browse_button = QtWidgets.QPushButton(Form)
        self.browse_button.setGeometry(QtCore.QRect(430, 230, 81, 21))
        self.browse_button.setObjectName("browse_button")
        self.start_button = QtWidgets.QPushButton(Form)
        self.start_button.setGeometry(QtCore.QRect(190, 310, 171, 31))
        self.start_button.setStyleSheet("QPushButton {\n"
                                        "font-size: 18px;\n"
                                        "}")
        self.start_button.setObjectName("start_button")
        self.message_box = QtWidgets.QTextEdit(Form)
        self.message_box.setGeometry(QtCore.QRect(120, 400, 331, 91))
        self.message_box.setObjectName("message_box")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

        self.browse_button.clicked.connect(self.show_browse_window)
        self.start_button.clicked.connect(self.downloadVideo)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "YT Video Downloader"))
        self.main_label.setText(_translate("Form", "Youtube Video Downloader"))
        self.url_label.setText(_translate("Form", "URL:"))
        self.quallity_combo.setItemText(0, _translate("Form", "Select quality"))
        self.quallity_combo.setItemText(1, _translate("Form", "1080p"))
        self.quallity_combo.setItemText(2, _translate("Form", "720p"))
        self.quallity_combo.setItemText(3, _translate("Form", "480p"))
        self.quallity_combo.setItemText(4, _translate("Form", "360p"))
        self.quallity_combo.setItemText(5, _translate("Form", "240p"))
        self.quallity_combo.setItemText(6, _translate("Form", "144p"))
        self.quality_label.setText(_translate("Form", "Quality"))
        self.type_label.setText(_translate("Form", "Type"))
        self.type_comobo.setItemText(0, _translate("Form", "Select type"))
        self.type_comobo.setItemText(1, _translate("Form", "Video(mp4)"))
        self.type_comobo.setItemText(2, _translate("Form", "Audio"))
        self.location_label.setText(_translate("Form", "Location:"))
        self.browse_button.setText(_translate("Form", "Browse"))
        self.start_button.setText(_translate("Form", "Start"))

    def show_browse_window(self):

        file_path = QFileDialog.getExistingDirectory()
        self.location_field.setText(file_path)
        self.abs_path = os.path.abspath(file_path)

    def downloadVideo(self):
        vid = YouTube(self.link_field.text())
        self.message_box.append("------------ Download Info ---------------")
        self.message_box.append(f"Title: {vid.title}")
        self.message_box.append(f"Channel: {vid.author}")

        self.message_box.append("------------ Download Status -------------")

        try:
            # execute the itag for the selected resolution for the audio or video
            itag = []
            if self.type_comobo.currentText() == "Video(mp4)":
                for stream in vid.streams.filter(res=self.quallity_combo.currentText(), subtype="mp4", progressive=True):
                    itag.append(stream.itag)

            elif self.type_comobo.currentText() == "Audio":
                for stream in vid.streams.filter(type="audio"):
                    itag.append(stream.itag)
            else:
                print("Unknown type")

            # downloading the vid
            stream = vid.streams.get_by_itag(itag[0])
            stream.download(output_path=self.abs_path)

            # print a message notifies that the download is complete
            def finish():
                self.message_box.append("Download Complete")

            vid.register_on_complete_callback(finish())
        except:
            self.message_box.append("Wrong input or the type not supported, please try again")


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
