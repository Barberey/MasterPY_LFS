# -*- coding: utf-8 -*-

"""
@file menu_principal.py
@brief Fichier de définition de la classe Ui_menu_princ
"""


from PyQt5 import QtCore, QtGui, QtWidgets
from MAIN import main
from POPUP import BottomPopup
from PyQt5.QtMultimedia import QSoundEffect
import ressources

class Ui_menu_princ(object):
        """
        @class Ui_menu_princ
        @brief Classe définissant l'interface utilisateur du menu principale
        """


        def setupUi(self, menu_princ_widg):
                """
                @brief Configurer l'interface utilisateur du menu principal.

                @param menu_princ_widg Widget du menu principal
                @type menu_princ_widg QWidgets.QWidget()
                """
                menu_princ_widg.setObjectName("menu_princ")
                menu_princ_widg.resize(996, 892)
                ratioHeight = int(main.ratio_size(892,1))
                ratioWidth = int(main.ratio_size(996,0))
                menu_princ_widg.setStyleSheet("QWidget#menu_princ{\n"
                "    background-image: url(:/img/fond/fond.png);\n"
                "    background-repeat: no-repeat;\n"
                "    background-position: center;\n"
                "    background-attachment: fixed;\n"
                "    background-size: cover;\n"
                "}\n"
                "")
                self.gridLayout = QtWidgets.QGridLayout(menu_princ_widg)
                self.gridLayout.setObjectName("gridLayout")

                self.label_2 = QtWidgets.QLabel(menu_princ_widg)
                self.label_2.setText("")
                self.label_2.setPixmap(QtGui.QPixmap(":/img/logo_MasterPY.png"))
                self.label_2.setObjectName("label_2")
                self.gridLayout.addWidget(self.label_2, 0, 1, 1, 1)

                spacerItem = QtWidgets.QSpacerItem(201*ratioWidth, 20*ratioHeight, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
                self.gridLayout.addItem(spacerItem, 1, 0, 1, 1)
                spacerItem1 = QtWidgets.QSpacerItem(20*ratioWidth, 50*ratioHeight, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
                self.gridLayout.addItem(spacerItem1, 1, 1, 1, 1)
                spacerItem2 = QtWidgets.QSpacerItem(200*ratioWidth, 20*ratioHeight, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
                self.gridLayout.addItem(spacerItem2, 1, 2, 1, 1)


                fontButton = QtGui.QFont()
                fontButton.setPointSize(25)

                fontTitre = QtGui.QFont()
                fontTitre.setPointSize(53)
                fontTitre.setBold(True)
                fontTitre.setWeight(75)

                self.titre = QtWidgets.QLabel(menu_princ_widg)
                self.titre.setFont(fontTitre)
                self.titre.setLineWidth(1)
                self.titre.setAlignment(QtCore.Qt.AlignCenter)
                self.titre.setObjectName("titre")
                self.gridLayout.addWidget(self.titre, 2, 1, 1, 1)

                spacerItem3 = QtWidgets.QSpacerItem(20 * ratioWidth, 5*ratioHeight, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
                self.gridLayout.addItem(spacerItem3, 3, 1, 1, 1)

                self.new_part = QtWidgets.QPushButton(menu_princ_widg)
                self.new_part.setEnabled(True)
                self.new_part.setMinimumSize(QtCore.QSize(500*ratioWidth, 50*ratioHeight))
                self.new_part.setObjectName("new_part")
                self.new_part.setFont(fontButton)
                self.gridLayout.addWidget(self.new_part, 4, 1, 1, 1)

                spacerItem4 = QtWidgets.QSpacerItem(20*ratioWidth, 25*ratioHeight, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
                self.gridLayout.addItem(spacerItem4, 5, 1, 1, 1)

                self.charger_part = QtWidgets.QPushButton(menu_princ_widg)
                self.charger_part.setMinimumSize(QtCore.QSize(0*ratioWidth, 50*ratioHeight))
                self.charger_part.setObjectName("charger_part")
                self.charger_part.setFont(fontButton)
                self.gridLayout.addWidget(self.charger_part, 6, 1, 1, 1)

                spacerItem5 = QtWidgets.QSpacerItem(20*ratioWidth, 25*ratioHeight, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
                self.gridLayout.addItem(spacerItem5, 7, 1, 1, 1)
                self.quit = QtWidgets.QPushButton(menu_princ_widg)
                self.quit.setMinimumSize(QtCore.QSize(100*ratioWidth, 50*ratioHeight))
                self.quit.setObjectName("quit")
                self.quit.setFont(fontButton)
                self.gridLayout.addWidget(self.quit, 8, 1, 1, 1)

                spacerItem6 = QtWidgets.QSpacerItem(201*ratioWidth, 20*ratioHeight, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
                self.gridLayout.addItem(spacerItem6, 9, 0, 1, 1)
                spacerItem7 = QtWidgets.QSpacerItem(20*ratioWidth, 147*ratioHeight, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
                self.gridLayout.addItem(spacerItem7, 9, 1, 1, 1)

                self.label = QtWidgets.QLabel(menu_princ_widg)
                self.label.setText("")
                self.label.setPixmap(QtGui.QPixmap(":/img/perso/petit-helper.png"))
                self.label.setScaledContents(False)
                self.label.setObjectName("label")
                self.label.setToolTip("Helper")
                # Connecter le clic sur l'image à la fonction pour afficher la bulle de discussion
                self.label.mousePressEvent = self.showHintBubble
                self.gridLayout.addWidget(self.label, 9, 2, 1, 1)

                spacerItem8 = QtWidgets.QSpacerItem(50*ratioWidth, 20*ratioHeight, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
                self.gridLayout.addItem(spacerItem8, 9, 3, 1, 1)

                self.retranslateUi(menu_princ_widg)
                QtCore.QMetaObject.connectSlotsByName(menu_princ_widg)

                self.widget = menu_princ_widg

                # Création d'un effet sonore pour les boutons
                self.button_click_sound = QSoundEffect()
                self.button_click_sound.setSource(QtCore.QUrl.fromLocalFile("chemin/vers/ton/fichier/son.wav"))
                self.button_click_sound.setVolume(0.5)  # Ajuste le volume du son

                # Tu peux connecter le slot du bouton à une fonction qui jouera le son
                self.charger_part.clicked.connect(self.play_button_sound)

        def play_button_sound(self):
                """
                @brief Jouer un son lorsqu'un bouton est cliqué.

                """
                # Joue le son lorsque le bouton est cliqué
                self.button_click_sound.play()

        def retranslateUi(self, menu_princ):
                """
                @brief Retraduire les éléments de l'interface utilisateur du menu principal.

                @param menu_princ Fenêtre du menu principal
                @type menu_princ QWidgets.QWidget()
                """
                _translate = QtCore.QCoreApplication.translate
                menu_princ.setWindowTitle(_translate("menu_princ", "Form"))
                self.titre.setText(_translate("menu_princ", "Master PY"))
                self.new_part.setText(_translate("menu_princ", "Nouvelle Partie"))
                self.charger_part.setText(_translate("menu_princ", "Charger Partie"))
                self.quit.setText(_translate("menu_princ", "Quitter"))

        # Fonction pour afficher la bulle de discussion de Helper
        def showHintBubble(self, event):
                """
                @brief Afficher la bulle de discussion de l'assistant (Helper).

                @param event Événement de clic de la souris
                """
                # Création d'une fenêtre modale personnalisée avec QMessageBox
                self.popup = BottomPopup.BottomPopup(0, 5, 0, "gray", True)
                self.popup.show()
