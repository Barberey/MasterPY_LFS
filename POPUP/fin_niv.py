# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\ressource\fin_niv.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QVBoxLayout, QLabel, QHBoxLayout
import ressources


class Ui_fin_niv(object):
    """
    @brief La classe Ui_fin_niv représente l'interface utilisateur pour la fin d'un niveau.

    @details
    Cette classe générée par PyQt5 UI code generator est utilisée pour afficher l'écran de fin de niveau. Elle contient
    des éléments tels que le temps écoulé, le nombre d'étoiles, le pourcentage de réussite, etc.
    """

    def __init__(self, num_saison, num_niv, nb_etoile, temps, pourcentage, main_window):
        """
        @brief Initialise une nouvelle instance de la classe Ui_fin_niv.

        @param num_saison: Le numéro de la saison.
        @type num_saison: int
        @param num_niv: Le numéro du niveau.
        @type num_niv: int
        @param nb_etoile: Le nombre d'étoiles obtenues.
        @type nb_etoile: int
        @param temps: Le temps écoulé pour terminer le niveau.
        @type temps: int
        @param pourcentage: Le pourcentage de réussite.
        @type pourcentage: float
        @param main_window: La fenêtre principale de l'application.
        """
        self.main = main_window
        self.nb_etoile = nb_etoile
        self.temps = temps
        self.num_saison = num_saison
        self.pourcentage = pourcentage
        self.num_niveau = num_niv

    def setupUi(self, fin_niv):
        """
        @brief Configure l'interface utilisateur pour l'écran de fin de niveau.

        @param fin_niv: La fenêtre de fin de niveau à configurer.
        """
        fin_niv.setObjectName("fin_niv")
        fin_niv.resize(1920, 1080)

        layout = QVBoxLayout(fin_niv)
        layout.setSpacing(0)

        # Configuration du fond d'écran en fonction de la saison et du niveau
        match self.num_saison:
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

        styleFond = "QWidget#fin_niv{" + photoFond + "background-repeat: no-repeat;" + "background-position: center;" + "background-attachment: fixed;" + "background-size: cover;" + "}"
        styleFondWidg = "QLabel#Etoil {background-color: rgba(0, 0, 0, 0.5);} "
        styleQbutton = "QPushButton { color: white; background-color: gray; }"

        fin_niv.setStyleSheet(styleFond + styleQbutton + styleFondWidg)

        # Configuration des polices
        fontTitre = QFont()
        fontTitre.setPointSize(30)

        spacerItemAvTitre = QtWidgets.QSpacerItem(20, 50, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        layout.addItem(spacerItemAvTitre)

        titre = QLabel(fin_niv)
        titre.setFont(fontTitre)
        titre.setText(f"Niveau {self.num_niveau}")
        titre.setAlignment(QtCore.Qt.AlignCenter)
        layout.addWidget(titre)

        fontTmps = QFont()
        fontTmps.setPointSize(25)

        tmps = QLabel(fin_niv)
        tmps.setFont(fontTmps)
        tmps.setText(f"{self.affTmps(self.temps)}")
        tmps.setAlignment(QtCore.Qt.AlignCenter)
        layout.addWidget(tmps)

        spacerItemApTitre = QtWidgets.QSpacerItem(20, 150, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        layout.addItem(spacerItemApTitre)

        remarque = QLabel(fin_niv)
        remarque.setFont(fontTitre)
        remarque.setText(f"{self.remarque()}")
        remarque.setAlignment(QtCore.Qt.AlignCenter)
        layout.addWidget(remarque)

        # Configuration des étoiles obtenues
        horizonEtoi = QHBoxLayout()
        horizonEtoi.setSpacing(0)
        listeEtoile = []

        etoil1 = QtWidgets.QLabel(fin_niv)
        etoil1.setPixmap(QtGui.QPixmap(":/img/star.png"))
        etoil1.setEnabled(False)
        etoil1.setAlignment(QtCore.Qt.AlignCenter)
        etoil1.setObjectName("Etoil")
        listeEtoile.append(etoil1)

        etoil2 = QtWidgets.QLabel(fin_niv)
        etoil2.setPixmap(QtGui.QPixmap(":/img/star.png"))
        etoil2.setEnabled(False)
        etoil2.setAlignment(QtCore.Qt.AlignCenter)
        etoil2.setObjectName("Etoil")
        listeEtoile.append(etoil2)

        etoil3 = QtWidgets.QLabel(fin_niv)
        etoil3.setPixmap(QtGui.QPixmap(":/img/star.png"))
        etoil3.setEnabled(False)
        etoil3.setAlignment(QtCore.Qt.AlignCenter)
        etoil3.setObjectName("Etoil")
        listeEtoile.append(etoil3)

        etoil4 = QtWidgets.QLabel(fin_niv)
        etoil4.setPixmap(QtGui.QPixmap(":/img/star.png"))
        etoil4.setEnabled(False)
        etoil4.setAlignment(QtCore.Qt.AlignCenter)
        etoil4.setObjectName("Etoil")
        listeEtoile.append(etoil4)

        etoil5 = QtWidgets.QLabel(fin_niv)
        etoil5.setPixmap(QtGui.QPixmap(":/img/star.png"))
        etoil5.setEnabled(False)
        etoil5.setAlignment(QtCore.Qt.AlignCenter)
        etoil5.setObjectName("Etoil")
        listeEtoile.append(etoil5)

        for i in range(self.nb_etoile):
            listeEtoile[i].setEnabled(True)

        horizonEtoi.addWidget(etoil1)
        horizonEtoi.addWidget(etoil2)
        horizonEtoi.addWidget(etoil3)
        horizonEtoi.addWidget(etoil4)
        horizonEtoi.addWidget(etoil5)

        layout.addLayout(horizonEtoi)

        spacerItemApEt = QtWidgets.QSpacerItem(20, 100, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        layout.addItem(spacerItemApEt)

        fontPour = QtGui.QFont()
        fontPour.setPointSize(20)

        pourcent = QLabel(fin_niv)
        pourcent.setFont(fontPour)
        pourcent.setText(f"{self.pourcentage*100}% de réussite")
        pourcent.setAlignment(QtCore.Qt.AlignCenter)
        layout.addWidget(pourcent)

        # Configuration de la barre de progression
        progressBar = QtWidgets.QProgressBar(fin_niv)
        progressBar.setEnabled(True)
        font = QtGui.QFont()
        font.setKerning(True)
        progressBar.setFont(font)
        progressBar.setProperty("value", int(self.pourcentage*100))
        progressBar.setTextVisible(False)
        progressBar.setOrientation(QtCore.Qt.Horizontal)
        layout.addWidget(progressBar)

        spacerItemFin = QtWidgets.QSpacerItem(20, 200, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        layout.addItem(spacerItemFin)

        fontBout = QtGui.QFont()
        fontBout.setPointSize(15)

        # Configuration du bouton "Continuer"
        self.bouton = QtWidgets.QPushButton("Continuer", fin_niv)
        self.bouton.setFont(fontBout)
        layout.addWidget(self.bouton)

        self.widget = fin_niv
        fin_niv.setLayout(layout)
        self.retranslateUi(fin_niv)
        QtCore.QMetaObject.connectSlotsByName(fin_niv)

    def retranslateUi(self, fin_niv):
        """
        @brief Traduit les textes de l'interface utilisateur.

        @param fin_niv: La fenêtre de fin de niveau.
        """
        _translate = QtCore.QCoreApplication.translate
        fin_niv.setWindowTitle(_translate("fin_niv", "Form"))

    def affTmps(self, temps):
        """
        @brief Formate le temps en minutes et secondes.

        @param temps: Le temps à formater en secondes.

        @return Une chaîne de caractères représentant le temps au format mm:ss.
        """
        minute = temps // 60
        seconde = temps % 60

        return f"{minute:02}:{seconde:02}"

    def remarque(self):
        """
        @brief Donne une remarque en fonction du nombre d'étoiles obtenues.

        @return Une chaîne de caractères représentant la remarque.
        """
        match self.nb_etoile:
            case 0:
                return "Ressaye encore !"
            case 1:
                return "Persevere !"
            case 2:
                return "Encore un effort !"
            case 3:
                return "Pas mal !"
            case 4:
                return "Bravo !"
            case 5:
                return "Excellent !"