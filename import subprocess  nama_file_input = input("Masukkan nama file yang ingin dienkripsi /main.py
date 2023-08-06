import subprocess

print("""
Menu:

[1] Enkripsi file
[2] Deskripsi file
[3] Keluar dari program
""")

tindakan = input("Pilih 1 atau 2: ")

if tindakan == "1":
    nama_file_masukkan = input("Masukkan nama file yang ingin dienkripsi: ")
    nama_file_keluaran = input("Masukkan nama file keluaran: ")
    perintah = f'openssl enc -aes-256-cbc -salt -in "{nama_file_masukkan}" -out "{nama_file_keluaran}"'
    subprocess.run(perintah, shell=True, text=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    print("File telah dienkripsi.")
    exit(0)

elif tindakan == "2":
    nama_file_masukkan = input("Masukkan nama file yang ingin didedekripsi: ")
    nama_file_keluaran = input("Masukkan nama file keluaran: ")
    perintah = f'openssl enc -d -aes-256-cbc -in "{nama_file_masukkan}" -out "{nama_file_keluaran}"'
    subprocess.run(perintah, shell=True, text=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    print("File telah didedekripsi.")
    exit(0)

elif tindakan == "3":
  exit(0)

else:
    print("Pilihan tidak valid.")
    exit(1)
