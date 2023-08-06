import subprocess

print("""
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@ Program : Enkripsi dan deskripsi file   @
@ Pembuat : Rofi [FII14]                  @
@ GitHub  : https://github.com/FII14/eddf @
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@""")

print("""
Menu:

[1] Enkripsi file
[2] Deskripsi file
[3] Keluar dari program
""")

tindakan = input("Pilih 1 atau 2: ")

if tindakan == "1":
    nama_file_masukkan = input("Masukkan nama file yang ingin dienkripsi: ")

    if not os.path.exists(nama_file_masukkan):
        print(f"Kesalahan: File '{nama_file_masukkan}' tidak ditemukan.")
        sys.exit(1)
    
    nama_file_keluaran = input("Masukkan nama file keluaran: ")

    if os.path.exists(nama_file_keluaran):
        pilihan = input(f"File '{nama_file_keluaran}' sudah ada. Apakah Anda ingin menimpa file yang ada? (iya/tidak): ")
    
        if pilihan.lower() != 'iya':
            print("Enkripsi dibatalkan.")
            sys.exit(1)
    
    perintah = f'openssl enc -aes-256-cbc -salt -in "{nama_file_masukkan}" -out "{nama_file_keluaran}"'
    subprocess.run(perintah, shell=True, text=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    print("\n[*] Sedang melakukan enkripsi...")
    print("\nFile telah dienkripsi.")
    exit(0)

elif tindakan == "2":
    nama_file_masukkan = input("Masukkan nama file yang ingin didedekripsi: ")

    if not os.path.exists(nama_file_masukkan):
        print(f"Kesalahan: File '{nama_file_masukkan}' tidak ditemukan.")
        sys.exit(1)
    
    nama_file_keluaran = input("Masukkan nama file keluaran: ")

    if os.path.exists(nama_file_keluaran):
        pilihan = input(f"File '{nama_file_keluaran}' sudah ada. Apakah Anda ingin menimpa file yang ada? (iya/tidak): ")
    
        if pilihan.lower() != 'iya':
            print("Deskripsi dibatalkan.")
            sys.exit(1)
    
    perintah = f'openssl enc -d -aes-256-cbc -in "{nama_file_masukkan}" -out "{nama_file_keluaran}"'
    subprocess.run(perintah, shell=True, text=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    print("\n[*] Sedang melakukan dekripsi...")
    print("\nFile telah didedekripsi.")
    exit(0)

elif tindakan == "3":
  exit(0)

else:
    print("Pilihan tidak valid.")
    exit(1)
