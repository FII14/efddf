import os
import sys
import base64

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
    
    nama_file_enkripsi = base64.b32encode(nama_file_masukkan.encode()).decode() + ".b32"
    
    if os.path.exists(nama_file_enkripsi):
        pilihan = input(f"File '{nama_file_enkripsi}' sudah ada. Apakah Anda ingin menimpa file yang ada? (iya/tidak): ")
    
        if pilihan.lower() != 'iya':
            print("Enkripsi dibatalkan.")
            sys.exit(1)
    
    with open(nama_file_masukkan, 'rb') as infile:
        data = infile.read()
        encoded_data = base64.b32encode(data)
        with open(nama_file_enkripsi, 'wb') as outfile:
            outfile.write(encoded_data)
    print("\n[*] Sedang melakukan enkripsi...")
    print(f"\nFile telah dienkripsi dan disimpan sebagai '{nama_file_enkripsi}'.")
    exit(0)

elif tindakan == "2":
    nama_file_masukkan = input("Masukkan nama file yang ingin didedekripsi: ")

    if not os.path.exists(nama_file_masukkan):
        print(f"Kesalahan: File '{nama_file_masukkan}' tidak ditemukan.")
        sys.exit(1)
    
    if not nama_file_masukkan.endswith(".b32"):
        print("Kesalahan: File yang ingin didedekripsi harus memiliki ekstensi .b32")
        sys.exit(1)
    
    nama_file_deskripsi = base64.b32decode(nama_file_masukkan[:-4]).decode()
    
    if os.path.exists(nama_file_deskripsi):
        pilihan = input(f"File '{nama_file_deskripsi}' sudah ada. Apakah Anda ingin menimpa file yang ada? (iya/tidak): ")
    
        if pilihan.lower() != 'iya':
            print("Deskripsi dibatalkan.")
            sys.exit(1)
    
    with open(nama_file_masukkan, 'rb') as infile:
        encoded_data = infile.read()
        decoded_data = base64.b32decode(encoded_data)
        with open(nama_file_deskripsi, 'wb') as outfile:
            outfile.write(decoded_data)
    print("\n[*] Sedang melakukan dekripsi...")
    print(f"\nFile telah didedekripsi dan disimpan sebagai '{nama_file_deskripsi}'.")
    exit(0)

elif tindakan == "3":
    exit(0)

else:
    print("Pilihan tidak valid.")
    exit(1)
