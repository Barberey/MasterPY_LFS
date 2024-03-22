import traceback
import ast
import json

class Verifier:
    """
    @brief La classe Verifier permet de vérifier le code utilisateur avec des tests.

    @details
    La classe Verifier prend en charge la vérification du code utilisateur en utilisant des tests spécifiés.
    Elle compile le code, exécute les tests et compare les résultats pour attribuer un score basé sur la réussite des tests.
    """

    def __init__(self, fichier_utilisateur, test_cases, niveau):
        """
        @brief Initialise une nouvelle instance de la classe Verifier.

        @param fichier_utilisateur: Chemin vers le fichier contenant le code utilisateur.
        @type fichier_utilisateur: str

        @param test_cases: Chemin vers le fichier contenant les cas de test.
        @type test_cases: str

        @param niveau: Numéro du niveau.
        @type niveau int
        """
        self.user_code_path = fichier_utilisateur
        self.test_cases = self.load_tests_from_file(test_cases)
        self.niveau = niveau

        # Exécuter le code utilisateur pour définir self.user_function
        self.user_function = self.compile_user_code()

    def load_tests_from_file(self, file_path):
        """
        @brief Charge les cas de test à partir d'un fichier.

        @param file_path: Chemin vers le fichier contenant les cas de test.
        @type file_path: str

        @return Liste de tuples (input_data, expected_output).
        @rtype list
        """
        try:
            test_cases = []

            with open(file_path, 'r') as file:
                lines = file.readlines()

            for line in lines:
                line = line.strip()

                if not line or line.startswith("--"):
                    # Ignorer les lignes vides et les commentaires de question
                    continue

                data = line.split(":")
                input_data = data[0].strip()
                expected_output = data[1].strip()
                test_cases.append((input_data, eval(expected_output)))

            return test_cases
        except Exception as e:
            print(e)

    def load_code_from_file(self, file_path):
        """
        @brief Charge le code utilisateur à partir d'un fichier.

        @param file_path: Chemin vers le fichier contenant le code utilisateur.
        @type file_path str

        @return Contenu du fichier.
        """
        with open(file_path, 'r') as file:
            return file.read()

    def extract_first_function_name(self, code):
        """
        @brief Extrait le nom de la première fonction du code.

        @param code: Code source.

        @return Nom de la première fonction.
        """
        try:
            tree = ast.parse(code)
            for node in ast.walk(tree):
                if isinstance(node, ast.FunctionDef):
                    return node.name
            raise ValueError("Aucune fonction n'a été trouvée dans le code utilisateur.")
        except Exception as e:
            print(e)

    def compile_user_code(self):
        """
        @brief Compile le code utilisateur et retourne la fonction.

        @return Fonction extraite du code utilisateur.
        """
        try:
            user_code = self.load_code_from_file(self.user_code_path)
            function_name = self.extract_first_function_name(user_code)
            compiled_code = compile(user_code, '<string>', 'exec')
            global_namespace = {}
            exec(compiled_code, global_namespace)
            user_function = global_namespace.get(function_name)
            if not user_function or not callable(user_function):
                raise ValueError(f"La fonction '{function_name}' n'a pas été trouvée dans le code utilisateur.")
            return user_function
        except Exception as e:
            print(f"Erreur lors de la compilation : {e}")
            return None

    def run_test(self, input_data, expected_output):
        """
        @brief Exécute un test avec les données d'entrée fournies.

        @param input_data: Données d'entrée du test.
        @param expected_output: Résultat attendu du test.

        @return True si le test réussit, False sinon.
        """
        try:
            if self.niveau == 2 or self.niveau == 3 or self.niveau == 4:
                parametre = input_data
                input_data = json.loads(parametre)
                result = self.user_function(input_data)
            elif self.niveau == 5:
                # Traitement spécifique pour le niveau 5
                tab = input_data.strip("()")
                tab = tab.split(",")
                input_data = tab[0]
                input_data2 = tab[1]
                result = self.user_function(input_data, input_data2)
            else:
                result = self.user_function(input_data)

            print(f"sortie voulue: {expected_output}")
            print(f"sortie : {result}")
            return result == expected_output
        except Exception as e:
            # Gérer les exceptions (peut être affiné selon les besoins)
            print(f"Erreur lors de l'exécution du code de l'utilisateur : {e}")
            traceback.print_exc()
            return False

    def compare_programs(self):
        """
        @brief Compare le programme utilisateur avec les cas de test.

        @return Tuple (score, pourcentage de tests réussis).
        """
        if self.user_function is None:
            print(self.user_function)
            return 0, 0
        passed_tests = 0
        total_tests = len(self.test_cases)
        print(self.test_cases)
        for test_case in self.test_cases:
            input_data, expected_output = test_case
            if self.run_test(input_data, expected_output):
                passed_tests += 1
                print(f"test réussi : {passed_tests}")
        # Calculer le pourcentage de tests réussis
        success_percentage = (passed_tests / total_tests)

        score = 0

        if success_percentage > 0.9:
            score = 3
        elif success_percentage > 0.7:
            score = 2
        elif success_percentage > 0.5:
            score = 1

        print(f"Pourcentage de tests réussis : {success_percentage * 100:.2f}%")
        return score, success_percentage
