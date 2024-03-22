from PyQt5 import QtWidgets
import faulthandler

class NewGameDialog(QtWidgets.QDialog):
    """
    @brief La classe NewGameDialog représente une boîte de dialogue pour créer une nouvelle partie.

    @details
    Cette boîte de dialogue permet à l'utilisateur de saisir le nom du jeu et le nom du joueur, puis de sauvegarder
    la nouvelle partie.
    """

    def __init__(self):
        """
        @brief Initialise une nouvelle instance de la classe NewGameDialog.
        """
        super().__init__()
        self.setWindowTitle("Nouvelle Partie")
        self.setGeometry(100, 100, 400, 200)  # Ajustez les dimensions selon vos besoins

        layout = QtWidgets.QVBoxLayout()

        self.game_name_label = QtWidgets.QLabel("Nom du jeu :")
        self.game_name_input = QtWidgets.QLineEdit()
        layout.addWidget(self.game_name_label)
        layout.addWidget(self.game_name_input)

        self.player_name_label = QtWidgets.QLabel("Nom du joueur :")
        self.player_name_input = QtWidgets.QLineEdit()
        layout.addWidget(self.player_name_label)
        layout.addWidget(self.player_name_input)

        self.save_button = QtWidgets.QPushButton("Sauvegarder")
        self.save_button.clicked.connect(self.save_game)
        layout.addWidget(self.save_button)

        self.setLayout(layout)

    def save_game(self):
        """
        @brief Sauvegarde la nouvelle partie avec les informations fournies.

        @details
        Cette méthode est appelée lorsque l'utilisateur clique sur le bouton de sauvegarde. Elle récupère les noms
        du jeu et du joueur à partir des champs de saisie, vérifie s'ils sont non vides, puis accepte la boîte de dialogue.
        Si les champs sont vides, une boîte de message d'erreur est affichée.
        """
        game_name = self.game_name_input.text()
        player_name = self.player_name_input.text()

        if not game_name or not player_name:
            QtWidgets.QMessageBox.critical(self, "Erreur", "Veuillez remplir tous les champs.")
            return

        self.accept()
