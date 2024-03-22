# -*- coding: utf-8 -*-

"""
@file main_window.py
@brief Fichier de définition de la classe Ui_MainWindow
"""

import sys
import time

# Form implementation generated from reading ui file '.\ressource\main_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets

from POPUP import dial
from POPUP import fin_niv
from IHM import menu_principal
from LEVEL import niveau
from OTHER import player
import ressources
from IHM import saison_1
from IHM import saison_2
from IHM import saison_3
from IHM import saison_4
from OTHER import save_handler
from POPUP import dialogue
from OTHER import sauvegarde
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent


class Ui_MainWindow(object):
    """
    @class Ui_MainWindow
    @brief Classe définissant l'interface utilisateur de tout le jeu
    """

    def __init__(self):
        self.dial = None
        self.menu_music = QMediaPlayer()
        self.level_music = QMediaPlayer()
        self.num_sais = 0
        self.num_sais_prec = 1

    def setupUi(self, MainWindow):
        """
        @brief Configurer l'interface utilisateur principale.

        @param MainWindow Fenêtre principale de l'application
        @type MainWindow QWidgets.QMainWindow()
        """
        self.mainWindow = MainWindow
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/img/logo_MasterPY.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName("stackedWidget")
        self.gridLayout.addWidget(self.stackedWidget, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)


        self.ui_menu_princ = menu_principal.Ui_menu_princ()
        self.ui_menu_princ.setupUi(QtWidgets.QWidget(MainWindow))

        self.ui_menu_princ.quit.clicked.connect(self.quitter)
        self.ui_menu_princ.new_part.clicked.connect(self.pop_up)
        self.ui_menu_princ.charger_part.clicked.connect(self.show_saves)

        self.stackedWidget.addWidget(self.ui_menu_princ.widget)

        self.creatWidegts(MainWindow)

        self.save_handler = save_handler.SaveHandler()

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.menu_music.setMedia(QMediaContent(QtCore.QUrl.fromLocalFile("../ressource/music/menu.MP3")))
        self.menu_music.play()

        self.menu_music.mediaStatusChanged.connect(self.loop_menu_music)

        self.level_music.setMedia(QMediaContent(QtCore.QUrl.fromLocalFile("../ressource/music/niveau.MP3")))

    def loop_menu_music(self, status):
        """
        @brief Gérer la boucle de lecture pour la musique du menu.

        @param status Statut de la lecture audio
        """
        if status == QMediaPlayer.EndOfMedia:
            # Lorsque la musique se termine, revenir au début et jouer à nouveau
            self.menu_music.setPosition(0)
            self.menu_music.play()

    def creatWidegts(self, MainWindow):
        """
        @brief Créer les widgets pour chaque saison.

        @param MainWindow Fenêtre principale de l'application
        @type MainWindow QWidgets.QMainWindow()
        """
        self.listWidgetsSais = []
        for i in range(4):
            match i:
                case 0:
                    obj = saison_1.Ui_saison_1()
                    obj.setupUi(QtWidgets.QWidget(MainWindow))
                    obj.sais_suiv.clicked.connect(self.sais_suiv)
                case 1:
                    obj = saison_2.Ui_saison_2()
                    obj.setupUi(QtWidgets.QWidget(MainWindow))
                    obj.sais_suiv.clicked.connect(self.sais_suiv)
                    obj.sais_prec.clicked.connect(self.sais_prec)
                case 2:
                    obj = saison_3.Ui_saison_3()
                    obj.setupUi(QtWidgets.QWidget(MainWindow))
                    obj.sais_suiv.clicked.connect(self.sais_suiv)
                    obj.sais_prec.clicked.connect(self.sais_prec)
                case 3:
                    obj = saison_4.Ui_saison_4()
                    obj.setupUi(QtWidgets.QWidget(MainWindow))
                    obj.sais_prec.clicked.connect(self.sais_prec)

            self.stackedWidget.addWidget(obj.widget)

            obj.save.clicked.connect(self.save)
            obj.quit.clicked.connect(self.quitter)
            obj.niv_1.clicked.connect(self.niv_1)
            obj.niv_2.clicked.connect(self.niv_2)
            obj.niv_3.clicked.connect(self.niv_3)
            obj.niv_4.clicked.connect(self.niv_4)
            obj.niv_5.clicked.connect(self.niv_5)


            self.listWidgetsSais.append(obj)

    def retranslateUi(self, MainWindow):
        """
        @brief Retraduire les éléments de l'interface utilisateur.

        @param MainWindow Fenêtre principale de l'application
        @type MainWindow QWidgets.QMainWindow()
        """
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MasterPY"))


    def save(self):
        """
        @brief Sauvegarder la partie en cours.

        """
        self.save_handler.sauvegarde(self.player)

    def quitter(self):
        """
        @brief Quitter l'application.

        """
        sys.exit(0)

    def pop_up(self):
        """
        @brief Afficher la fenêtre de nouvelle partie.

        """
        if not hasattr(self, 'new_game_dialog') or not self.new_game_dialog.isVisible():
            self.new_game_dialog = dialogue.NewGameDialog()
            result = self.new_game_dialog.exec_()
            if result == QtWidgets.QDialog.Accepted:
                try:
                    self.save_handler.new_save(self.new_game_dialog.game_name_input.text(),
                                               self.new_game_dialog.player_name_input.text())
                    self.player = player.Player("../save/"+self.new_game_dialog.game_name_input.text())
                    self.continuer_game()
                except ValueError:
                    QtWidgets.QMessageBox.information(self.mainWindow, "Erreur de creation de sauvegarde",
                                                      "Nom de sauvegarde deja existant")

        else:
            QtWidgets.QMessageBox.information(self.mainWindow, "Nouvelle Partie déjà ouverte",
                                              "La pop-up de nouvelle partie est déjà ouverte.")

    def continuer_game(self):
        """
        @brief Continuer la partie en cours.

        """
        for i in range(len(self.listWidgetsSais)):
            self.listWidgetsSais[i].nom_joueur.setText(self.player.name)
            self.listWidgetsSais[i].nbr_etoile.setText(str(self.player.nb_etoile))
            self.listWidgetsSais[i].updateStars(self.player.etoiles[i])
            self.listWidgetsSais[i].changeColor(self.player.niv_complet[i])

        if(self.player.cine[0]):
            self.stackedWidget.setCurrentIndex(1)
        else:
            self.player.modifCine(0)
            self.creaDialHist(0)

    def show_saves(self):
        """
        @brief Afficher les parties sauvegardées.

        """
        saved_games = self.save_handler.get_saves()
        if not saved_games:
            QtWidgets.QMessageBox.information(self.mainWindow, "Aucune sauvegarde",
                                              "Aucune partie sauvegardée.")
        else:
            self.load_game_dialog = sauvegarde.LoadGameDialog(saved_games)
            result = self.load_game_dialog.exec_()
            if result == QtWidgets.QDialog.Accepted:
                selected_game = self.load_game_dialog.selected_game
                self.player = player.Player(f"../save/{selected_game}")
                self.continuer_game()

    def niv_1(self):
        """
         @brief Charger le niveau 1.

         """
        self.num_sais = self.stackedWidget.indexOf(self.stackedWidget.currentWidget())
        self.constr_niv(1,"rgb(70, 7, 49)",self.num_sais)

    def niv_2(self):
        """
        @brief Charger le niveau 2.

        """
        self.num_sais = self.stackedWidget.indexOf(self.stackedWidget.currentWidget())
        if(self.player.nb_etoile >= (3*1+ 21*(self.num_sais-1))):
            self.constr_niv(2,"rgb(70, 7, 49)",self.num_sais)

    def niv_3(self):
        """
        @brief Charger le niveau 3.

        """
        self.num_sais = self.stackedWidget.indexOf(self.stackedWidget.currentWidget())
        if (self.player.nb_etoile >= (3*2 + 21 * (self.num_sais - 1))):
            self.constr_niv(3,"rgb(70, 7, 49)",self.num_sais)
    def niv_4(self):
        """
        @brief Charger le niveau 4.

        """
        self.num_sais = self.stackedWidget.indexOf(self.stackedWidget.currentWidget())
        if (self.player.nb_etoile >= (3*3 + 21 * (self.num_sais - 1))):
            self.constr_niv(4,"rgb(70, 7, 49)",self.num_sais)

    def niv_5(self):
        """
        @brief Charger le niveau 5.

        """
        self.num_sais = self.stackedWidget.indexOf(self.stackedWidget.currentWidget())
        if (self.player.nb_etoile >= (3*4 + 21 * (self.num_sais - 1))):
            self.constr_niv(5,"rgb(38, 68, 70)",self.num_sais)

    def constr_niv(self, num_niv, couleur, num_sais):
        open('../texte/texte_des_niveaux/niveau.txt', 'w').close()
        if(self.stackedWidget.count() == 6):
            self.stackedWidget.removeWidget(self.stackedWidget.widget(5))

        self.niv = niveau.Ui_Form(num_sais,num_niv)
        self.creaDialNiv(couleur)

    def loop_level_music(self, status):
        """
        @brief Gérer la boucle de lecture pour la musique du niveau.

        @param status Statut de la lecture audio
        """
        if status == QMediaPlayer.EndOfMedia:
            # Lorsque la musique se termine, revenir au début et jouer à nouveau
            self.level_music.setPosition(0)
            self.level_music.play()

    def term_niv(self):
        """
        @brief Gérer la fin du niveau et le changement d'affichage.

        """
        temps, nb_etoiles, pourcentage = self.niv.terminer()
        self.listWidgetsSais[self.niv.num_saison-1].updateStars(self.player.etoiles[self.niv.num_saison-1])
        self.listWidgetsSais[self.niv.num_saison-1].nbr_etoile.setText(str(self.player.nb_etoile))
        self.listWidgetsSais[self.niv.num_saison-1].changeColor(self.player.niv_complet[self.niv.num_saison-1])

        self.ui_fin = fin_niv.Ui_fin_niv(self.niv.num_saison, self.niv.num_niveau, nb_etoiles, temps, pourcentage, self)
        self.ui_fin.setupUi(QtWidgets.QWidget(self.mainWindow))
        self.ui_fin.bouton.clicked.connect(self.fin_niveau)
        self.stackedWidget.setCurrentIndex(self.niv.num_saison)
        self.stackedWidget.removeWidget(self.niv.widget)
        self.stackedWidget.addWidget(self.ui_fin.widget)
        self.stackedWidget.setCurrentIndex(5)

    def sais_suiv(self):
        """
        @brief Passer à la saison suivante.

        """
        num_sais = self.stackedWidget.indexOf(self.stackedWidget.currentWidget())
        if(self.player.nb_etoile >= (21*num_sais) and self.player.is_valide(num_sais)):
            if(self.player.cine[num_sais]):
                self.stackedWidget.setCurrentIndex(num_sais+1)
            else:
                self.num_sais_prec = num_sais+1
                self.num_sais = 0
                self.player.modifCine(num_sais)
                self.creaDialHist(num_sais)

    def sais_prec(self):
        """
        @brief Revenir à la saison précédente.

        """
        num_sais = self.stackedWidget.indexOf(self.stackedWidget.currentWidget())
        self.stackedWidget.setCurrentIndex(num_sais-1)

    def creaDialNiv(self,couleur):
        """
        @brief Créer une boîte de dialogue.

        @param couleur Couleur de la boîte de dialogue
        @type couleur str
        """
        self.dial = dial.Ui_dial(self.num_sais, self.niv.num_niveau,couleur,self)
        self.dial.setupUi(QtWidgets.QWidget(self.mainWindow))
        self.stackedWidget.addWidget(self.dial.widget)
        self.stackedWidget.setCurrentIndex(5)


        self.menu_music.pause()
        self.level_music.play()

        self.level_music.mediaStatusChanged.connect(self.loop_level_music)
        if(self.dial.vide):
            self.finDial()

    def creaDialHist(self,num_dial):
        """
        @brief Créer une boîte de dialogue pour le lore du jeu.

        @param num_dial Numero du dialogue
        @type num_dial int
        """
        couleur = "rgb(38, 68, 70)"

        if(self.num_sais!= 0):
            self.num_sais_prec = self.num_sais
            self.num_sais = 0

        self.dial = dial.Ui_dial(self.num_sais, num_dial,couleur,self,hist=True)
        self.dial.setupUi(QtWidgets.QWidget(self.mainWindow))
        self.stackedWidget.addWidget(self.dial.widget)
        self.stackedWidget.setCurrentIndex(5)


    def finDial(self):
        if(self.dial.hist):
            print("Hello")
            self.finDialHist()
        else:
            self.finDialNiv()

    def finDialNiv(self):
        """
        @brief Gérer la fin du dialogue.

        """
        self.stackedWidget.setCurrentIndex(self.num_sais)
        self.stackedWidget.removeWidget(self.dial.widget)
        self.niv.setupUi(QtWidgets.QWidget(self.mainWindow), self.player)
        self.niv.fini.clicked.connect(self.term_niv)
        self.stackedWidget.addWidget(self.niv.widget)
        self.stackedWidget.setCurrentIndex(5)

    def finDialHist(self):
        """
        @brief Gérer la fin du dialogue.

        """
        self.stackedWidget.setCurrentIndex(self.num_sais_prec)
        self.stackedWidget.removeWidget(self.dial.widget)

    def fin_niveau(self):
        """
        @brief Gérer la fin du niveau.

        """

        couleur = "rgb(38, 68, 70)"

        self.stackedWidget.setCurrentIndex(self.niv.num_saison)
        self.stackedWidget.removeWidget(self.ui_fin.widget)

        self.num_sais_prec = self.niv.num_saison
        self.dial = dial.Ui_dial(self.niv.num_saison, self.niv.num_niveau, couleur, self, hist=True, bis=True)
        self.dial.setupUi(QtWidgets.QWidget(self.mainWindow))
        self.stackedWidget.addWidget(self.dial.widget)
        self.stackedWidget.setCurrentIndex(5)
        if (self.dial.vide):
            self.finDial()

        self.level_music.stop()
        self.menu_music.play()