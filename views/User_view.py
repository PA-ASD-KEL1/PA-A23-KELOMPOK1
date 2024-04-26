from controllers.User_Controller import ProjectController, ProfileController
from views import Login_views
from colorama import Fore, Style
import random

class User:
    def __init__(self):
        self.app = Login_views.App()
        self.colors = [
            Fore.RED, Fore.GREEN, Fore.YELLOW,
            Fore.BLUE, Fore.MAGENTA, Fore.CYAN
        ]
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
        while True:
            try:
                print("\n\033[1;36m╭───────────────────────╮\033[0m")
                print("\033[1;36m│\033[0;94m       Menu User       \033[1;36m│\033[0m")
                print("\033[1;36m├───────────────────────┤\033[0m")
                print("\033[92m│ 1. Profil             │\033[0m")
                print("\033[92m│ 2. Lihat Project      │\033[0m")
                print("\033[92m│ 3. Daftar Project     │\033[0m")
                print("\033[92m│ 4. Keluar             │\033[0m")
                print("\033[1;36m╰───────────────────────╯\033[0m")

                choice = input("\033[3;32mEnter your choice: \033[0m")

                if choice == '1':
                    # Opsi Profil
                    print("Anda memilih opsi Profil")
                    self.app.loading_animation()
                    ProfileController().display_data()
                elif choice == '2':
                    # Opsi Daftar Project
                    print("Anda memilih opsi Lihat Project")
                    self.app.loading_animation()
                    ProjectController().display_data()
                elif choice == '3':
                    # Opsi Registrasi Project
                    print("Anda memilih opsi Registrasi Project")
                    # Tambahkan implementasi untuk registrasi project di sini
                elif choice == '4':
                    self.app.loading_animation()
                    print(f"{random.choice(self.colors)}")
                    print(f"{random.choice(self.colors)} Thank you for using our app! {random.choice(self.goodbyes)}")
                    print(Style.RESET_ALL)
                    raise SystemExit
                else:
                    raise ValueError("\033[91mInvalid choice! Please enter a valid option.\033[0m")
            except ValueError as ve:
                print("\033[91mError:", ve, "\033[0m")

