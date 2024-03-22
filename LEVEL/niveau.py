# -*- coding: utf-8 -*-

"""
@file niveau.py
@brief Fichier de définition de la classe Niveau
"""
import random

# Form implementation generated from reading ui file '.\ressource\niveau.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtWidgets, QtGui
from OTHER import verifier
from LEVEL.chronometre import Chronometre
from PyQt5.QtWidgets import QScrollArea, QLineEdit
import ressources


class Ui_Form(object):
    """
    @class Ui_Form
    @brief Classe générée automatiquement pour l'interface utilisateur du niveau.
    """

    def __init__(self, numSaison, numNiv):
        """
        @brief Constructeur de la classe Ui_Form.

        @param numSaison: Numéro de la saison.
        @type numSaison int

        @param numNiv: Numéro du niveau.
        @type numNiv: int
        """
        self.num_saison = numSaison
        self.num_niveau = numNiv

    def setupUi(self, Form, player):
        """
        @brief Configure l'interface utilisateur du niveau.

        @param Form: Widget du niveau.
        @type Form: QtWidgets.QWidget

        @param player: Objet joueur.
        @type player: Player (ou le type approprié)
        """

        self.widget = Form

        self.player = player

        Form.setObjectName("Niv")
        Form.resize(1135, 870)

        match self.num_saison:
            case 1:
                if(self.num_niveau==5):
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

        styleFond = "QWidget#Niv{"+photoFond+"background-repeat: no-repeat;"+"background-position: center;"+"background-attachment: fixed;"+"background-size: cover;"+"}"
        stylePseudo = "QWidget#Pseudo{background-color: rgba(255, 255, 255, 0.5);}"
        styleTextEdit = "QPlainTextEdit#plainTextEdit{background-color: rgba(255, 255, 255, 0.5);}"

        Form.setStyleSheet(styleFond+stylePseudo+styleTextEdit)

        self.fontQuest = QtGui.QFont()
        self.fontQuest.setPointSize(15)



        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")


        if(self.num_saison==4):
            self.plainTextEdit = QtWidgets.QPlainTextEdit(Form)
            self.plainTextEdit.setEnabled(True)
            self.plainTextEdit.setMaximumSize(QtCore.QSize(1064, 868))
            self.plainTextEdit.setObjectName("plainTextEdit")
            self.plainTextEdit.setFont(self.fontQuest)
            self.gridLayout.addWidget(self.plainTextEdit, 0, 0, 1, 1)
            self.fini = QtWidgets.QPushButton(Form)
            self.fini.setObjectName("fini")
            self.fini.setFont(self.fontQuest)
            self.gridLayout.addWidget(self.fini, 1, 0, 1, 1)
            consigne = self.recupConsig(self.num_niveau)
        else:
            lignes, options, self.reponse, consigne = self.recupTxt()
            grid = QtWidgets.QVBoxLayout()
            self.listBox = self.creaTxtIndent(grid,lignes,options)


        spacerItem = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(0, 0, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 0, 2, 1, 1)

        photoBoss = ""

        if(self.num_niveau == 5):
            if(self.num_saison == 1):
                photoBoss = "bossete.png"
            elif(self.num_saison == 2):
                photoBoss = "bossautomne.png"
            elif(self.num_saison == 3):
                photoBoss = "bosshiver.png"
            elif(self.num_saison == 4):
                photoBoss = "bossprintemps.png"

        self.chronometre = Chronometre(Form, self.num_saison, self.num_niveau, photoBoss)
        self.chronometre.initUI(consigne)
        self.chronometre.setEnabled(True)
        self.chronometre.setMinimumSize(QtCore.QSize(500, 0))
        self.chronometre.setObjectName("widget")
        self.gridLayout.addWidget(self.chronometre, 0, 3, 1, 1)


        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        """
        @brief Traduit l'interface utilisateur.

        @param Form Widget du niveau.
        @type Form QtWidgets.QWidget
        """
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.fini.setText(_translate("Form", "Terminer"))

    def terminer(self):
        """
        @brief Termine le niveau et retourne le temps, le nombre d'étoiles et la réponse correcte.

        @return Temps écoulé, nombre d'étoiles, réponse correcte.
        @rtype tuple
        """
        temps = self.chronometre.terminerChronometre()
        print(f"Le temps est égal à :{temps}")

        if self.num_saison == 4:
            with open('../texte/texte_des_niveaux/niveau.txt', 'a') as fichier:
                fichier.write(self.plainTextEdit.toPlainText())

            verification = verifier.Verifier("../texte/texte_des_niveaux/niveau.txt",
                                          f"../texte/texte_des_niveaux/saison{self.num_saison}/{self.num_niveau}",
                                             self.num_niveau)
            nb_etoile, bonneReponse = verification.compare_programs()

            print(nb_etoile)
            print(type(nb_etoile))

        else : # L'autre méthode
            nb_etoile = 0
            correct = 0
            for i in range(len(self.listBox)):
                if(type(self.listBox[i]) == type(QLineEdit()) ):
                    res = self.listBox[i].text()
                    res = res.replace(" ","")
                    print(res)
                    print(self.reponse[i])
                    if(res == self.reponse[i]):
                        correct += 1
                else:
                    if(self.listBox[i].currentText() == self.reponse[i]):
                        correct +=1

            bonneReponse = correct/len(self.listBox)

            if(bonneReponse==1):
                nb_etoile = 3
            elif(bonneReponse>=0.75):
                nb_etoile = 2
            elif(bonneReponse>=0.50):
                nb_etoile = 1

        if nb_etoile > 0:
            if nb_etoile >= 2:
                if temps // 300 == 0:
                    nb_etoile += 2
                elif temps // 300 == 1:
                    nb_etoile += 1
                self.player.valide(self.num_saison, self.num_niveau)
            elif nb_etoile == 1:
                if temps // 300 <= 1:
                    nb_etoile += 1

        self.player.updateStars(self.num_saison, self.num_niveau, nb_etoile)

        return temps, nb_etoile, bonneReponse

    def recupTxt(self):
        """
        @brief Récupère le texte du niveau.

        @return Lignes, options, réponses, consigne.
        @rtype tuple
        """
        with open(f"../texte/texte_des_niveaux/saison{self.num_saison}/{self.num_niveau}", 'r', encoding="utf-8") as fichier:
            lignes_pre = fichier.readlines()
            lignes = []
            reponse = []
            options = []
            consigne =""
            for i in range(len(lignes_pre)):
                if (len(lignes_pre[i].strip().split("!!")) != 1):
                    options.append(lignes_pre[i][2:].strip().split("+++"))
                elif(len(lignes_pre[i].strip().split("&&")) != 1):
                    reponse.append(lignes_pre[i][2:].strip())
                elif (len(lignes_pre[i].strip().split("--")) != 1):
                    consigne += lignes_pre[i][2:].strip()+"\n"
                else:
                    lignes.append(lignes_pre[i].strip().split("##"))

        return lignes,options, reponse, consigne

    def creaTxtIndent(self, grid, lignes, reponse):
        """
        @brief Crée le texte indenté dans le niveau.

        @param grid: La grille pour disposer les éléments.
        @type grid: QtWidgets.QVBoxLayout
        @param lignes: Lignes de texte.
        @type lignes: list
        @param reponse: Réponses du niveau.
        @type reponse: list
        @return Liste des boîtes de texte.
        @rtype list
        """
        
        listeBox = []
        nbr_rep = 0
        for i in range(len(lignes)):
            colonne = len(lignes[i]) - 1
            indent = "\t"*colonne
            box = lignes[i][colonne].split("{::}")
            if (len(box) == 1):
                txt = QtWidgets.QLabel(self.widget)
                txt.setText(indent+lignes[i][colonne])
                txt.setFont(self.fontQuest)
                grid.addWidget(txt)
            else:
                horizon = QtWidgets.QHBoxLayout()
                indentLabel = QtWidgets.QLabel(self.widget)
                indentLabel.setText(indent)
                indentLabel.setFont(self.fontQuest)
                horizon.addWidget(indentLabel)
                for i in box:
                    if (i == "B"):
                        comboBox = QtWidgets.QComboBox(self.widget)
                        comboBox.addItem("----")
                        rand = reponse[nbr_rep]
                        random.shuffle(rand)
                        for rep in rand:
                            comboBox.addItem(rep)

                        comboBox.setFont(self.fontQuest)
                        horizon.addWidget(comboBox)
                        listeBox.append(comboBox)
                        nbr_rep += 1
                    elif(i == "V"):
                        lineEdit = QLineEdit(self.widget)
                        lineEdit.setFont(self.fontQuest)
                        horizon.addWidget(lineEdit)
                        listeBox.append(lineEdit)
                    elif (i != ""):
                        txt = QtWidgets.QLabel(self.widget)
                        txt.setText(i)
                        txt.setFont(self.fontQuest)
                        horizon.addWidget(txt)

                spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding,
                                                   QtWidgets.QSizePolicy.Minimum)
                horizon.addItem(spacerItem)
                grid.addLayout(horizon)

        widg = QtWidgets.QWidget()
        widg.setLayout(grid)
        widg.setObjectName("widg")
        widg.setStyleSheet("QWidget#widg{background-color: rgba(255, 255, 255, 0);}")


        self.fini = QtWidgets.QPushButton(self.widget)
        self.fini.setObjectName("fini")
        self.fini.setFont(self.fontQuest)
        grid.addWidget(self.fini)

        scroll_area = QScrollArea()
        scroll_area.setObjectName("Pseudo")
        scroll_area.setSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        scroll_area.setWidget(widg)
        self.gridLayout.addWidget(scroll_area, 0, 0, 1, 1)

        return listeBox

    def recupConsig(self, num_niveau):
        """
        @brief Récupère la consigne du niveau.

        @param num_niveau: Numéro du niveau.
        @type num_niveau: int
        @return La consigne du niveau.
        @rtype str
        """
        consigne = ""
        with open(f"../texte/texte_des_niveaux/saison4/{num_niveau}", 'r', encoding="utf-8") as fichier:
            for i in fichier.readlines():
                ligne = i.split("--")
                if(len(ligne) == 1):
                    break
                consigne+=ligne[1]

        return consigne
