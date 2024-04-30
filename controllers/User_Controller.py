from tabulate import tabulate
from models.model import ProjectModel

class AbstractController:
    def __init__(self):
        self.model = None

    def display_data(self):
        raise NotImplementedError("Subclasses must implement display_data method.")

    def search_data(self):
        raise NotImplementedError("Subclasses must implement search_data method.")


class ProjectController(AbstractController):
    def __init__(self):
        super().__init__()
        self.model = ProjectModel()

    def display_data(self):
        fields = ["Desain Grafis", "Event", "Fashion", "Marketing", "Teknologi", "Kesehatan", "Media"]

        print("\n\033[1;36m╭──────────────────────────╮\033[0m")
        print("\033[1;36m│\033[0;94m    Pilih Bidang Project   \033[1;36m│\033[0m")
        print("\033[1;36m├──────────────────────────┤\033[0m")
        for index, field in enumerate(fields, start=1):
            print(f"\033[92m│ {index}. {field:<24} │\033[0m")
        print("\033[1;36m│ 0. Kembali                │\033[0m")
        print("\033[1;36m╰──────────────────────────╯\033[0m")

        choice = input("\033[3;32mPilih bidang (0 untuk kembali): \033[0m")
        try:
            choice = int(choice)
            if choice == 0:
                return
            elif 1 <= choice <= len(fields):
                chosen_field = fields[choice - 1]
                projects = self.model.read_records('project')  # Menggunakan metode read_records dari ProjectModel
                filtered_projects = [proj for proj in projects if proj["Bidang"] == chosen_field]
                if filtered_projects:
                    self.display_projects_table(filtered_projects)
                else:
                    print("Tidak ada project dalam bidang ini.")
            else:
                print("\033[91mPilihan tidak valid!\033[0m")
        except ValueError:
            print("\033[91mMasukkan angka sebagai pilihan!\033[0m")

    def display_projects_table(self, projects):
        headers = ["ID Project", "Judul", "Status", "Deskripsi", "Bidang", "Gaji", "ID Admin", "Rentang Waktu"]
        project_data = [[proj["ID_Project"], proj["Judul"], proj["Status"], proj["Deskripsi"], proj["Bidang"], proj["Gaji"], proj["ID_adminproject"], proj["rentang_waktu"]] for proj in projects]
        print(tabulate(project_data, headers=headers, tablefmt="fancy_grid"))

    def search_data(self):
        print("\n\033[1;36m╭──────────────────────────╮\033[0m")
        print("\033[1;36m│\033[0;94m   Pilih Kriteria Pencarian  \033[1;36m│\033[0m")
        print("\033[1;36m├──────────────────────────┤\033[0m")
        print("\033[92m│ 1. Berdasarkan Gaji          │\033[0m")
        print("\033[92m│ 2. Berdasarkan Rentang Waktu │\033[0m")
        print("\033[1;36m│ 0. Kembali                │\033[0m")
        print("\033[1;36m╰──────────────────────────╯\033[0m")

        choice = input("\033[3;32mPilih kriteria (0 untuk kembali): \033[0m")
        try:
            choice = int(choice)
            if choice == 0:
                return
            elif choice == 1:
                gaji = int(input("\033[3;36mMasukkan gaji proyek yang ingin dicari: "))
                self.model.Search_by_salary(gaji)
            elif choice == 2:
                allowed_time_ranges = ["1 bulan", "2 bulan", "3 bulan"]
                while True:
                    time_range = input("\033[3;32mMasukkan rentang waktu (1 bulan/2 bulan/3 bulan): \033[0m").strip().lower()
                    if time_range in allowed_time_ranges:
                        self.model.search_by_time_range(time_range)
                        break
                    else:
                        print("\033[91mRentang waktu yang dimasukkan tidak valid. Silakan masukkan 1 bulan, 2 bulan, atau 3 bulan.")
            else:
                print("\033[91mPilihan tidak valid!\033[0m")
        except ValueError:
            print("\033[91mMasukkan angka sebagai pilihan!\033[0m")

    def daftar_project(self):
        try:
            # Membuat instance dari ProjectModel
            project_model = ProjectModel()

            # Meminta input ID project dari pengguna
            project_id = input("Masukkan ID Project yang Anda inginkan: ")

            # Mencari proyek berdasarkan ID
            project = project_model.find_project_by_id(project_id)

            if project:
                print(f"\nProject ditemukan: {project['Judul']}")
                print(f"Deskripsi: {project['Deskripsi']}")

                # Meminta konfirmasi dari pengguna untuk mendaftar proyek
                confirm = input("Apakah Anda ingin mendaftar untuk proyek ini? (ya/tidak): ")

                if confirm.lower() == 'ya':
                    # Meminta nama freelancer
                    nama_freelancer = input("Masukkan nama Anda: ")
                    # Memperbarui status proyek menjadi "Menunggu Persetujuan"
                    project_model.register_for_project(project_id, nama_freelancer)
                    print("Pendaftaran berhasil!")
                elif confirm.lower() == 'tidak':
                    print("Pendaftaran dibatalkan.")
                else:
                    print("Masukkan tidak valid. Pendaftaran dibatalkan.")

            else:
                print("Project tidak ditemukan.")
        except Exception as e:
            print(f"Error: {e}")
