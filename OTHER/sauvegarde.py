from POPUP.dialogue import *

"""
@file sauvegarde.py
@brief Fichier decrivant la classe qui gere toutes les actions qui affecte le chargement de sauvegarde
"""

class LoadGameDialog(QtWidgets.QDialog):
    """
    @brief Constructeur de la classe LoadGameDialog.

    @param saved_games: Liste des parties sauvegardées.
    @type saved_games: list[str]
    """

    def __init__(self, saved_games):
        super().__init__()
        self.setWindowTitle("Charger Partie")
        self.setGeometry(100, 100, 400, 200)  # Ajustez les dimensions selon vos besoins

        layout = QtWidgets.QVBoxLayout()

        self.game_list = QtWidgets.QListWidget()
        for game in saved_games:
            self.game_list.addItem(f"{game}")
        layout.addWidget(self.game_list)

        self.load_button = QtWidgets.QPushButton("Charger")
        self.load_button.clicked.connect(self.load_game)
        layout.addWidget(self.load_button)

        self.setLayout(layout)

        self.selected_game = None

    def load_game(self):
        """
         @brief Charge la partie sélectionnée.

        """
        selected_item = self.game_list.currentItem()
        if selected_item:
            selected_text = selected_item.text()
            self.selected_game = selected_text
            self.accept()
