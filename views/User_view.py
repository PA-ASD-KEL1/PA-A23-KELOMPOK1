from controllers.User_Controller import ProjectController
from views import Login_views
from colorama import Fore, Style
import random

class User:
    def __init__(self):
        self.app = Login_views.App()
        self.colors = [Fore.RED, Fore.GREEN, Fore.YELLOW, Fore.BLUE, Fore.MAGENTA, Fore.CYAN]
        self.goodbyes = [
            "See you later, alligator!",
            "Catch you on the flip side!",
            "Adios, amigos!",
            "Until we meet again!",
            "Stay classy!",
            "Farewell, traveler!",
            "Take care, mate!",
            "May the Force be with you!",
            "Auf Wiedersehen!",
            "Arrivederci!",
            "Goodbye, for now!",
            "Keep on coding!",
        ]
    def user_menu(self):
        from controllers.auth_controller import LoginPengguna
        while True:
            try:
                print("\n\033[1;36m╭───────────────────────╮\033[0m")
                print("\033[1;36m│\033[0;94m       Menu User       \033[1;36m│\033[0m")
                print("\033[1;36m├───────────────────────┤\033[0m")
                print("\033[92m│ 1. Profil             │\033[0m")
                print("\033[92m│ 2. Lihat Project      │\033[0m")
                print("\033[92m│ 3. Daftar Project     │\033[0m")
                print("\033[92m│ 4. Cari Project       │\033[0m")
                print("\033[92m│ 5. Keluar             │\033[0m")
                print("\033[1;36m╰───────────────────────╯\033[0m")

                choice = input("Enter your choice: ")

                if choice == '1':
                    # Memanggil method profil dari objek LoginPengguna
                    LoginPengguna().profil()
                elif choice == '2':
                    print("Anda memilih opsi Lihat Project")
                    self.app.loading_animation()
                    ProjectController().display_data()
                elif choice == '3':
                    print("Anda memilih opsi Daftar Project")
                    self.app.loading_animation()
                    ProjectController().daftar_project()
                elif choice == '4':
                    print("Anda memilih opsi Cari Project")
                    self.app.loading_animation()
                    ProjectController().search_data()
                elif choice == '5':
                    self.app.loading_animation()
                    print(f"{random.choice(self.colors)}")
                    print(f"{random.choice(self.colors)} Thank you for using our app! {random.choice(self.goodbyes)}")
                    print(Style.RESET_ALL)
                    break
                else:
                    raise ValueError("Invalid choice! Please enter a valid option.")
            except ValueError as ve:
                print(f"Error: {ve}")