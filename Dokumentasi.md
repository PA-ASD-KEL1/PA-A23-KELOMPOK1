# Platfrom Pekerjaan Fleksibel untuk Pertumbuhan Ekonomi (EcoFusion)
--------------------------------------------------------------------------------------------
### Deskripsi Program
> Ecofusion adalah platfrom freelance yang menghubungkan para freelance dengan 
project-project yang relevan dengan keahlian mereka. Freelance akan memilih project 
dan berkesempatan untuk direktur oleh mitra dari proyek tersebut. Dengan ini dapat membantu 
pertumbuhan ekonomi berkelanjutan. Program ini membantu admin project untuk mengelola pendaftaran project dan memudahkan freelancer untuk memilih project, melakukan project, serta membantu melakukan monitoring terhadap freelancer untuk mendapatkan kontrak dari para recruiter. Memudahkan para freelancer untuk mendapatkan gaji sebagai freelancer dan mendapatkan pekerjaan disebuah perusahaan jika project yang mereka kerjakan diminati oleh perusahaan terkait. Dengan begitu, program ini diharapkan dapat mengurangi para pengangguran yang ada agar mendapatkan pekerjaan yang lebih layak dan membantu perekonomian di zaman sekarang.

> Program ini dibuat dengan menggunakan bahasa pemrograman Python dan mengimplementasikan struktur data Linked List, menggunakan CRUD, dan melakukan sorting serta searching dari data yang ada. Platform Pekerjaan Fleksibel ini hanya menggunakan sebuah database, yaitu database mysql  yang digunakan untuk menyimpan data dari admin projeect, project, perusahaan, freelancer, recruiter, dan kontrak.
-----------------------------------------------------------------------------------------------

### Struktur Project

> 1. Folder Controller, berisi file-file controller yang akan mengatur alur program serta mengambil data dari model dan menampilkan ke view.                           
> - File Controller Account, sebagai file controller yang berisi logika untuk manajemen akun admin, user (freelancer), dan recruiter untuk mengatur registrasi, login, dan menampilkan profil.
> - File Controller Linked List, sebagai file controller yang berisi logika untuk manajemen data ruang kelas dalam bentuk linked list, dimana data dalam linked list diambil dari database.
> - File Controller User, sebagai file controller yang berisi logika untuk manajemen data user (freelancer) mulai dari menampilkan data profil user (freelancer), menampilkan project, melakukan sorting project, dan searching project.

> 2. Folder Model, berisi file-file model yang berisi fungsi-fungsi untuk mengakses database dan memproses data.
> - File Database, sebagai file yang berisi class untuk menghubungkan python dan database.
> - File model, sebagai file yang berisi definisi class abstractmodel yang digunakan untuk merepresentasikan sebuah node pada struktur data Linked List dan melakukan CRUD.

> 3. Folder View, berisi file-file view yang berisi tampilan antarmuka aplikasi yang akan dilihat oleh pengguna.
> - File admin, sebagai halaman untuk menampilkan informasi, melakukan pemdaftaran dari setiap entitas yang ada, dan melakukan CRUD dari setiap entitas yang bisa diatur oleh admin
> - File login, sebagai halaman untuk menampilkan informasi dan melakukan login untuk pengguna, admin, dan recruiter.
> - File Recruiter, sebagai halaman untuk menampilkan informasi dan melakukan CRUD untuk entitas kontrak yang hanya dapat diatur oleh recruiter.
> - File User, sebagai halaman untuk menampilkan informasi profil user(freelancer), lihat project, dan melakukan pendaftaran project.

> 4. File main, sebagai file utama yang berfungsi untuk menjalankan program.
---------------------------------------------------------------------------------

### Fitur
Pada program ini terdapat library yang digunakan, diantaranya adalah PrettyTable, Datetime, time, PyMongo, os dan random. 
>  1. Modul os dapat digunakan untuk berinteraksi dengan sistem operasi dan melakukan operasi pada file dan folder.
>  2. Modul random pada adalah modul yang menyediakan fungsi-fungsi untuk menghasilkan bilangan acak.
>  3. Modul time adalah modul yang menyediakan fungsi-fungsi untuk mengelola waktu dan tanggal.
>  4. Modul sys adalah modul untuk memberi akses ke berbagai variabel dan fungsi yang terkait dengan interpretasi Python itu sendiri.
>  5. Modul colorama adalah modul untuk mempermudah penulisan teks berwarna pada konsol atau terminal Python. Fore digunakan untuk mengubah warna teks, sementara Style digunakan untuk mengatur gaya teks seperti cetak tebal, miring, atau normal.
>  6. Modul mysql.connector adalah modul untuk menyediakan fungsi-fungsi untuk menjalankan kueri SQL, memanipulasi data, dan mengelola koneksi ke server MySQL.
>  7. Modul pwinput adalah modul untuk menerima input password tanpa menampilkan karakter yang dimasukkan ke layar, sehingga meningkatkan keamanan saat memasukkan kata sandi.
 
Beberapa fitur yang terdapat pada program ini, yaitu :
- User (Freelancer)
> 1. Melihat profil : User dapat melihat profil yang berisi data diri seperti ID Freelancer, nama, no hp, jenis kelamin, email, alamt
> 2. Melihat Bidang Project : User dapat melihat bidang project yang sesuai dengan yang diminati oleh para freelancer dan akan ditampilkan project-project yang sesuai dengan bidang tersebut.
> 3. Melakukan searching project : User dapat melakukan pencarian dari project dengan beberapa kata kunci.
> 4. Melakukan sorting project: User dapat melakukan pemilahan dari project berdasarkan
> 5. Pendaftaran project: Setelah user mendapatkan project yang sesuai, use dapat melakukan pendaftaran project dan melakukan project tersebut.

- Admin Project
> 1. Membuat dan mengupdate peminjaman : Staff dapat menambahkan daftar kelas dan mengupdate status kelas yang digunakan.
> 2. Konfirmasi Peminjaman : Staff dapat melakukan konfirmasi peminjaman yang telah dilakukan oleh mahasiswa. 
> 3. Mencetak bukti peminjaman : Setelah Staff menambahkan daftar kelas yang akan digunakan maka dapat mencetak bukti peminjaman sebagai bukti tanda kelas digunakan sudah terkonfirmasi oleh staff.
> 4. Mencari NIM : Staff juga dapat mencari NIM Mahasiswa yang mengkonfirmasi peminjaman ruang kelas.
> 5. Menghapus daftar peminjaman : Staff dapat menghapus daftar peminjaman.
> 6. Melihat profil : Staff dapat  melihat profil yang berisi data diri seperti  NIP, Nama, Jenis Kelamin, dan Jabatan.

- Recruiter
> 1. Create kontrak: Recruiter dapat membuat data kontrak kerja terbaru untuk freelancer.
> 2. Read Kontrak: Recruiter dapaat melihat daftar kontrak yang sudah recruiter buat.
> 3. Update Kontrak: Recruiter dapat memperbarui informasi kontrak yang sudah recruiter buat sebelumnya.
> 4. Delete Kontrak: Recruiter dapat menghapus kontrak yang sudah recruiter buat.
--------------------------------------------------------------------------------------------

### Fungsionalitas
>  1. Registrasi User dan recruiter. Mahasiswa dapat melakukan pendaftaran untuk dapat masuk ke dalam sistem peminjaman ruang kelas dengan mengisi formulir pendaftaran. Mahsiswa harus memberikan informasi pribadi seperti nim, nama, program studi, dan jenis kelamin.
>  2. Login dan Logout (Exit). User dapat melakukan login ke dalam sistem dengan menggunakan nim/nip dan password mereka. User juga dapat keluar dari program dengan melalui pilihan Exit.
>  3. CRUD. User dapat meminjam ruang kelas dengan mengisi formulir peminjaman. User harus memberikan informasi seperti tanggal dan waktu peminjaman, mata kuliah, dan keperluan peminjaman.
-------------------------------------------------------------------------------------------------

### Cara Penggunaan
> 1. Login dan Registrasi User
Login bisa dilakukan oleh user atau admin. User harus melakukan login terlebih dahulu sebelum dapat melakukan pelatihan atau untuk menyelesaikan project.  Jika user belum terdaftar, maka user dapat melakukan registrasi terlebih dahulu.



--------------------------------------


