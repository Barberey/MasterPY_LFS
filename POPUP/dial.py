# -*- coding: utf-8 -*-

# Implémentation de formulaire générée à partir du fichier d'interface utilisateur '.\ressource\dial.ui'
#
# Créé par : Générateur de code d'interface utilisateur PyQt5 5.15.9
#
# AVERTISSEMENT : Toute modification manuelle apportée à ce fichier sera perdue lors de l'exécution de pyuic5.
# N'éditez pas ce fichier à moins de savoir ce que vous faites.

from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import QVBoxLayout

from POPUP import BottomPopup
import ressources

class Ui_dial(object):
    """
    @brief La classe Ui_dial gère l'interface utilisateur pour les dialogues dans le jeu.

    @details
    Cette classe est générée à partir d'un fichier d'interface utilisateur (.ui) et configure l'interface pour afficher
    des dialogues avec des images de fond en fonction de la saison et du niveau du jeu.
    """

    def __init__(self, numSaison, numNiv, couleur, main_window, bis=False, hist=False):
        """
        @brief Initialise une nouvelle instance de la classe Ui_dial.

        @param numSaison: Numéro de la saison.
        @type numSaison: bool
        @param numNiv: Niveau du jeu.
        @type numNiv: bool
        @param couleur: Couleur du fond de l'interface.
        @type couleur: str
        @param main_window: Fenêtre principale du jeu.
        @param bis: Indique si c'est une version bis du niveau.
        @type bis: bool
        @param hist: Indique si le dialogue est historique.
        @type hist: bool
        """
        self.num_saison = numSaison
        self.num_niveau = numNiv
        self.bis = bis
        self.hist = hist
        self.couleur = couleur
        self.main = main_window
        self.vide = False

    def setupUi(self, dial):
        """
        @brief Configure l'interface utilisateur.

        @param dial: Fenêtre de dialogue.
        """
        dial.setObjectName("dial")
        dial.resize(1920, 1080)

        layout = QVBoxLayout(dial)

        # Détermine l'image de fond en fonction de la saison et du niveau
        match self.num_saison:
            case 0:
                match self.num_niveau:
                    case 0:
                        photoFond = "background-image:url(:/img/fond/ete-niv.png);"
                    case 1:
                        photoFond = "background-image:url(:/img/fond/automne-niv.png);"
                    case 2:
                        photoFond = "background-image:url(:/img/fond/hiver-niv.png);"
                    case 3:
                        photoFond = "background-image:url(:/img/fond/printemps-niv.png);"
            case 1:
                if (self.num_niveau == 5):
                    photoFond = "background-image:url(:/img/fond/ete-boss.png);"
                else:
                    photoFond = "background-image:url(:/img/fond/ete-niv.png);"
            case 2:
                if (self.num_niveau == 5):
                    photoFond = "background-image:url(:/img/fond/automne-boss.png);"
                else:
                    photoFond = "background-image:url(:/img/fond/automne-niv.png);"
            case 3:
                if (self.num_niveau == 5):
                    photoFond = "background-image:url(:/img/fond/hiver-boss.png);"
                else:
                    photoFond = "background-image:url(:/img/fond/hiver-niv.png);"
            case 4:
                if (self.num_niveau == 5):
                    photoFond = "background-image:url(:/img/fond/printemps-boss.png);"
                else:
                    photoFond = "background-image:url(:/img/fond/printemps-niv.png);"

        styleFond = "QWidget#dial{" + photoFond + "background-repeat: no-repeat;" + "background-position: center;" + "background-attachment: fixed;" + "background-size: cover;" + "}"
        styleFondWidg = "QLabel {background-color: rgba(255, 255, 255, 0.5);} "
        styleQbutton = "QPushButton { color: white; background-color: gray; }"

        dial.setStyleSheet(styleFond + styleQbutton + styleFondWidg)

        self.widget = dial

        # Crée une instance de BottomPopup pour gérer les dialogues
        self.popup = BottomPopup.BottomPopup(self.num_saison, self.num_niveau, 0, self.couleur, parent=dial, parent_obj=self, bis=self.bis)

        # Vérifie si le dialogue n'est pas vide et configure l'interface en conséquence
        if not self.popup.vide:
            fontDial = QtGui.QFont()
            fontDial.setPointSize(25)
            self.popup.label.setFont(fontDial)
            layout.addWidget(self.popup)
            dial.setLayout(layout)

            self.retranslateUi(dial)
            QtCore.QMetaObject.connectSlotsByName(dial)

        else:
            self.vide = True

    def retranslateUi(self, dial):
        """
        @brief Traduit les éléments de l'interface.

        @param dial: Fenêtre de dialogue.
        """
        _translate = QtCore.QCoreApplication.translate
        dial.setWindowTitle(_translate("dial", "Form"))

    def fin(self):
        """
        @brief Gère la fin du dialogue.
        """
        self.main.finDial()
