from PyQt5 import QtCore, QtGui, QtWidgets
from PIL import Image
from crypto_functions import encrypt, decrypt, add_header, read_header
import random
import os
import numpy as np


class Ui_main_window(object):
    def setupUi(self, main_window):
        main_window.setObjectName("main_window")
        main_window.setEnabled(True)
        main_window.resize(500, 420)

        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(main_window.sizePolicy().hasHeightForWidth())

        main_window.setSizePolicy(sizePolicy)
        main_window.setMinimumSize(QtCore.QSize(500, 400))
        main_window.setMaximumSize(QtCore.QSize(500, 420))

        font = QtGui.QFont()
        font.setFamily("Roboto Mono")
        font.setPointSize(9)
        main_window.setFont(font)
        main_window.setAutoFillBackground(False)

        self.centralwidget = QtWidgets.QWidget(main_window)
        self.centralwidget.setMinimumSize(QtCore.QSize(0, 0))
        self.centralwidget.setObjectName("centralwidget")

        self.title = QtWidgets.QLabel(self.centralwidget)
        self.title.setGeometry(QtCore.QRect(10, 10, 481, 41))
        font = QtGui.QFont()
        font.setFamily("Roboto Mono")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.title.setFont(font)
        self.title.setAlignment(QtCore.Qt.AlignJustify | QtCore.Qt.AlignVCenter)
        self.title.setWordWrap(True)
        self.title.setObjectName("title")

        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(10, 40, 481, 16))
        font = QtGui.QFont()
        font.setFamily("Roboto Mono")
        font.setPointSize(9)
        self.line.setFont(font)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")

        self.encrypt_button = QtWidgets.QPushButton(self.centralwidget)
        self.encrypt_button.setGeometry(QtCore.QRect(19, 190, 461, 41))
        font = QtGui.QFont()
        font.setFamily("Roboto Mono")
        font.setPointSize(9)
        self.encrypt_button.setFont(font)
        self.encrypt_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.encrypt_button.setObjectName("encrypt_button")
        self.encrypt_button.clicked.connect(self.encrypt)

        self.file_localization_line_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.file_localization_line_edit.setGeometry(QtCore.QRect(20, 60, 351, 23))
        font = QtGui.QFont()
        font.setFamily("Roboto Mono")
        font.setPointSize(9)
        self.file_localization_line_edit.setFont(font)
        self.file_localization_line_edit.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.file_localization_line_edit.setAcceptDrops(False)
        self.file_localization_line_edit.setReadOnly(True)
        self.file_localization_line_edit.setObjectName("file_localization_line_edit")

        self.file_selector_button = QtWidgets.QPushButton(self.centralwidget)
        self.file_selector_button.setGeometry(QtCore.QRect(390, 60, 91, 23))
        font = QtGui.QFont()
        font.setFamily("Roboto Mono")
        font.setPointSize(8)
        self.file_selector_button.setFont(font)
        self.file_selector_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.file_selector_button.setObjectName("file_selector_button")
        self.file_selector_button.clicked.connect(self.get_file_to_encrypt)

        self.encryption_type_combobox = QtWidgets.QComboBox(self.centralwidget)
        self.encryption_type_combobox.setGeometry(QtCore.QRect(180, 120, 101, 23))
        font = QtGui.QFont()
        font.setFamily("Roboto Mono")
        font.setPointSize(9)
        self.encryption_type_combobox.setFont(font)
        self.encryption_type_combobox.setMaxVisibleItems(3)
        self.encryption_type_combobox.setObjectName("encryption_type_combobox")
        self.encryption_type_combobox.addItem("")
        self.encryption_type_combobox.addItem("")
        self.encryption_type_combobox.addItem("")

        self.encryption_type_label = QtWidgets.QLabel(self.centralwidget)
        self.encryption_type_label.setGeometry(QtCore.QRect(20, 120, 151, 20))
        font = QtGui.QFont()
        font.setFamily("Roboto Mono")
        font.setPointSize(9)
        self.encryption_type_label.setFont(font)
        self.encryption_type_label.setObjectName("encryption_type_label")

        self.key_len_label = QtWidgets.QLabel(self.centralwidget)
        self.key_len_label.setGeometry(QtCore.QRect(20, 150, 151, 21))
        font = QtGui.QFont()
        font.setFamily("Roboto Mono")
        font.setPointSize(9)
        self.key_len_label.setFont(font)
        self.key_len_label.setObjectName("key_len_label")

        self.key_len_combobox = QtWidgets.QComboBox(self.centralwidget)
        self.key_len_combobox.setGeometry(QtCore.QRect(180, 150, 101, 23))
        font = QtGui.QFont()
        font.setFamily("Roboto Mono")
        font.setPointSize(9)
        self.key_len_combobox.setFont(font)
        self.key_len_combobox.setObjectName("key_len_combobox")
        self.key_len_combobox.addItem("")
        self.key_len_combobox.addItem("")
        self.key_len_combobox.addItem("")

        self.algorithm_type_label = QtWidgets.QLabel(self.centralwidget)
        self.algorithm_type_label.setGeometry(QtCore.QRect(20, 90, 151, 21))
        font = QtGui.QFont()
        font.setFamily("Roboto Mono")
        font.setPointSize(9)
        self.algorithm_type_label.setFont(font)
        self.algorithm_type_label.setObjectName("algorithm_type_label")

        self.algorithm_type_combobox = QtWidgets.QComboBox(self.centralwidget)
        self.algorithm_type_combobox.setGeometry(QtCore.QRect(180, 90, 101, 23))
        font = QtGui.QFont()
        font.setFamily("Roboto Mono")
        font.setPointSize(9)
        self.algorithm_type_combobox.setFont(font)
        self.algorithm_type_combobox.setObjectName("algorithm_type_combobox")
        self.algorithm_type_combobox.addItem("")
        # self.algorithm_type_combobox.addItem("")
        # self.algorithm_type_combobox.addItem("")
        # self.algorithm_type_combobox.addItem("")

        self.file_localization_line_edit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.file_localization_line_edit_2.setGeometry(QtCore.QRect(20, 260, 351, 23))
        self.file_localization_line_edit_2.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.file_localization_line_edit_2.setAcceptDrops(False)
        self.file_localization_line_edit_2.setReadOnly(True)
        self.file_localization_line_edit_2.setObjectName("file_localization_line_edit_2")

        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(10, 240, 481, 16))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")

        self.file_selector_button_2 = QtWidgets.QPushButton(self.centralwidget)
        self.file_selector_button_2.setGeometry(QtCore.QRect(390, 260, 91, 23))
        font = QtGui.QFont()
        font.setFamily("Roboto Mono")
        font.setPointSize(8)
        self.file_selector_button_2.setFont(font)
        self.file_selector_button_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.file_selector_button_2.setObjectName("file_selector_button_2")
        self.file_selector_button_2.clicked.connect(self.get_file_to_decrypt)

        self.key_localization_line_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.key_localization_line_edit.setGeometry(QtCore.QRect(20, 290, 351, 23))
        self.key_localization_line_edit.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.key_localization_line_edit.setAcceptDrops(False)
        self.key_localization_line_edit.setReadOnly(True)
        self.key_localization_line_edit.setObjectName("key_localization_line_edit")

        self.key_selector_button = QtWidgets.QPushButton(self.centralwidget)
        self.key_selector_button.setGeometry(QtCore.QRect(390, 290, 91, 23))
        font = QtGui.QFont()
        font.setFamily("Roboto Mono")
        font.setPointSize(8)
        self.key_selector_button.setFont(font)
        self.key_selector_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.key_selector_button.setObjectName("key_selector_button")
        self.key_selector_button.clicked.connect(self.get_key_to_decrypt)

        self.decrypt_button = QtWidgets.QPushButton(self.centralwidget)
        self.decrypt_button.setGeometry(QtCore.QRect(20, 370, 461, 41))
        self.decrypt_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.decrypt_button.setObjectName("decrypt_button")
        self.decrypt_button.clicked.connect(self.decrypt)

        self.modify_ct_button = QtWidgets.QPushButton(self.centralwidget)
        self.modify_ct_button.setGeometry(QtCore.QRect(20, 320, 461, 41))
        self.modify_ct_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.modify_ct_button.setObjectName("modify_ct_button")
        self.modify_ct_button.clicked.connect(self.modify_ct)

        main_window.setCentralWidget(self.centralwidget)

        self.retranslateUi(main_window)
        self.encryption_type_combobox.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(main_window)

    def retranslateUi(self, main_window):
        _translate = QtCore.QCoreApplication.translate
        main_window.setWindowTitle(_translate("main_window", "Aplikacja projektowa"))
        self.title.setText(_translate("main_window", "Aplikacja projektowa."))
        self.encrypt_button.setText(_translate("main_window", "Szyfruj"))
        self.file_localization_line_edit.setPlaceholderText(_translate("main_window", "Lokalizacja pliku"))
        self.file_selector_button.setText(_translate("main_window", "Wybierz plik"))
        self.encryption_type_combobox.setCurrentText(_translate("main_window", "ECB"))
        self.encryption_type_combobox.setPlaceholderText(_translate("main_window", "Wybierz tryb szyfrowania"))
        self.encryption_type_combobox.setItemText(0, _translate("main_window", "ECB"))
        self.encryption_type_combobox.setItemText(1, _translate("main_window", "CBC"))
        self.encryption_type_combobox.setItemText(2, _translate("main_window", "CTR"))
        self.encryption_type_label.setText(_translate("main_window", "Tryb szyfrowania"))
        self.key_len_label.setText(_translate("main_window", "Długość klucza"))
        self.key_len_combobox.setItemText(0, _translate("main_window", "128"))
        self.key_len_combobox.setItemText(1, _translate("main_window", "192"))
        self.key_len_combobox.setItemText(2, _translate("main_window", "256"))
        self.algorithm_type_label.setText(_translate("main_window", "Algorytm szyfrowania"))
        self.algorithm_type_combobox.setItemText(0, _translate("main_window", "AES"))
        # self.algorithm_type_combobox.setItemText(1, _translate("main_window", "Camellia"))
        # self.algorithm_type_combobox.setItemText(2, _translate("main_window", "ChaCha20"))
        # self.algorithm_type_combobox.setItemText(3, _translate("main_window", "TripleDES"))
        self.file_localization_line_edit_2.setPlaceholderText(_translate("main_window", "Lokalizacja pliku"))
        self.file_selector_button_2.setText(_translate("main_window", "Wybierz plik"))
        self.key_localization_line_edit.setPlaceholderText(_translate("main_window", "Lokalizacja klucza"))
        self.key_selector_button.setText(_translate("main_window", "Wybierz klucz"))
        self.decrypt_button.setText(_translate("main_window", "Deszyfruj"))
        self.modify_ct_button.setText(_translate("main_window", "Modyfikuj szyfrogram"))

    def get_file_to_encrypt(self):
        """
        Function associated with the self.file_selector_button. Opens a dialog to select the input file to encrypt.
        """
        file_localization, _ = QtWidgets.QFileDialog.getOpenFileName(self.centralwidget, "Select file to encrypt",
                                                                     os.getenv("HOME"),
                                                                     "Text Files (*.txt);;"
                                                                     "Image Files (*.png *.jpg *.bmp);;"
                                                                     "PDF Files (*.pdf)")
        self.file_localization_line_edit.setText(file_localization)

    def get_file_to_decrypt(self):
        """
        Function associated with the self.file_selector_button_2.
        Opens a dialog to select the input file to be decrypted.
        """
        file_localization, _ = QtWidgets.QFileDialog.getOpenFileName(self.centralwidget, "Select file to decrypt",
                                                                     os.getenv("HOME"),
                                                                     "Text Files (*.txt);;"
                                                                     "Image Files (*.png *.jpg *.bmp);;"
                                                                     "PDF Files (*.pdf)")
        self.file_localization_line_edit_2.setText(file_localization)

    def encrypt(self):
        """
        Function associated with self.encrypt_button. Takes input from self.file_localization_line_edit,
        self.algorithm_type_combobox and self.key_len_combobox. Encrypts the file and adds a header with the information
        needed for decryption. If the file is an image, an encrypted preview of the file is created.
        The created optional preview with the key and ciphertext is stored in the same directory as the input file.
        """
        file_localization = self.file_localization_line_edit.text()
        if len(file_localization) == 0:
            QtWidgets.QMessageBox.about(self.centralwidget, "Fail", f"Failed to encrypt a file. "
                                                                    f"No file selected!")
            return

        algorithm = self.algorithm_type_combobox.currentText()
        mode = self.encryption_type_combobox.currentText()
        key_len = self.key_len_combobox.currentText()

        output_extension = os.path.splitext(file_localization)[1]
        shape = None
        data_preview = None
        if output_extension in ('.png', '.jpg'):
            pixels = np.asarray(Image.open(file_localization))
            shape = (pixels.shape[0], pixels.shape[1])
            data_preview = pixels.tobytes()

        input_file = open(file_localization, 'r+b')
        data = bytearray(input_file.read())
        input_file.close()

        output_dir = os.path.dirname(file_localization)
        output_name = os.path.basename(file_localization).split('.')[0]
        output_file_loc = output_dir + f'/cipher_{output_name}' + output_extension
        output = encrypt(algorithm, mode, int(key_len), data)

        if data_preview is not None:
            output_preview_loc = output_dir + f'/cipher_{output_name}_preview' + output_extension
            output_preview = encrypt(algorithm, mode, int(key_len), data_preview)
            Image.frombuffer('RGB', shape, output_preview['ciphertext'], 'raw', 'RGB', 0, 1).save(output_preview_loc)

        output_file = open(output_file_loc, 'w+b')
        output_file.write(output['ciphertext'])
        output_file.close()

        key_file = open(output_dir + f'/key_{output_name}.bin', 'w+b')
        key_file.write(output['key'])
        key_file.close()

        add_header(output_file_loc, algorithm, mode, output['additional'], shape)
        QtWidgets.QMessageBox.about(self.centralwidget, "Success", f"File successfully encrypted. "
                                                                   f"The output is in {output_dir} directory!")

    def get_key_to_decrypt(self):
        """
        Function associated with self.key_selector_button. Opens a dialog box to select the input key to decrypt.
        """
        key_localization, _ = QtWidgets.QFileDialog.getOpenFileName(self.centralwidget, "Select key",
                                                                    os.getenv("HOME"),
                                                                    "Binary files (*.bin)")
        self.key_localization_line_edit.setText(key_localization)

    def decrypt(self):
        """
        Function associated with self.decrypt_button. Takes input from self.file_localization_line_edit_2,
        self.key_localization_line_edit. Reads headers from the file and decrypts it. The created output file
        is stored in the same directory as the ciphertext file.
        """
        ciphertext_localization = self.file_localization_line_edit_2.text()
        key_localization = self.key_localization_line_edit.text()
        output_extension = os.path.splitext(ciphertext_localization)[1]
        output_dir = os.path.dirname(ciphertext_localization)
        output_name = os.path.basename(ciphertext_localization).split('.')[0]
        output_localization = output_dir + f'/decrypted_{output_name}' + output_extension

        if len(ciphertext_localization) == 0 or len(key_localization) == 0:
            QtWidgets.QMessageBox.about(self.centralwidget, "Fail", f"Failed to decrypt a file. "
                                                                    f"No file or key selected!")
            return

        options = read_header(ciphertext_localization)
        with open(key_localization, 'r+b') as key_file, \
                open(ciphertext_localization, 'r+b') as ciphertext, \
                open(output_localization, 'w+b') as out:
            key = bytearray(key_file.read())
            data = bytearray(ciphertext.read())

            output = decrypt(options['algorithm'],
                             options['mode'],
                             key,
                             options['additional'],
                             data)
            out.write(output)

        QtWidgets.QMessageBox.about(self.centralwidget, "Success", f"File successfully decrypted. "
                                                                   f"The output is in {output_dir} directory!")

    def modify_ct(self):
        """
        The function to modify a ciphertext. The ciphertext localization is obtained via
        self.file_localization_line_edit_2. For every single byte of the ciphertext there is a 33% chance
        that it will be modified. The modification is performed as the XOR product of a given byte and a randomly
        generated byte.
        """
        path = self.file_localization_line_edit_2.text()
        if len(path) == 0:
            QtWidgets.QMessageBox.about(self.centralwidget, "Fail", f"Failed to modify a ciphertext. "
                                                                    f"No file selected!")
            return

        output_extension = os.path.splitext(path)[1]
        options = read_header(path)
        output_name = os.path.basename(path).split('.')[0]
        output_localization = os.path.dirname(path) + f"/new_{output_name}" + output_extension
        with open(path, 'rb') as ciphertext, \
             open(output_localization, 'wb') as new_ciphertext:

            ciphertext = ciphertext.read()
            print('Old ciphertext:', ciphertext, len(ciphertext))
            new_ciphertext_bytes = []
            for byte in ciphertext:
                if random.random() < 0.3:
                    byte = byte ^ int.from_bytes(os.urandom(1), 'big')
                new_ciphertext_bytes.append(byte)
            new_ciphertext_bytes = bytes(new_ciphertext_bytes)
            print('New ciphertext', new_ciphertext_bytes, len(ciphertext))
            new_ciphertext.write(new_ciphertext_bytes)
            add_header(output_localization, options['algorithm'], options['mode'], options['additional'])


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    main_window = QtWidgets.QMainWindow()
    ui = Ui_main_window()
    ui.setupUi(main_window)
    main_window.show()
    sys.exit(app.exec_())
