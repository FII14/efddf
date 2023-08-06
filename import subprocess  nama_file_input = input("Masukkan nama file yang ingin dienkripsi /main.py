import subprocess

print("""
Menu:

[1] Enkripsi file
[2] Deskripsi file
[3] Keluar dari program
""")

tindakan = input("Pilih tindakan:\n1. Enkripsi\n2. Dedekripsi\nPilih 1 atau 2: ")

if tindakan == "1":
    nama_file_input = input("Masukkan nama file yang ingin dienkripsi / didedekripsi: ")
    nama_file_output = input("Masukkan nama file output: ")
    passphrase = input("Masukkan kata sandi: ")
    perintah = f'openssl enc -aes-256-cbc -salt -in "{nama_file_input}" -out "{nama_file_output}"'
    subprocess.run(perintah, shell=True, text=True, input=passphrase, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    print("File telah dienkripsi.")
    exit(0)

elif tindakan == "2":
    nama_file_input = input("Masukkan nama file yang ingin dienkripsi / didedekripsi: ")
    nama_file_output = input("Masukkan nama file output: ")
    passphrase = input("Masukkan kata sandi: ")
    perintah = f'openssl enc -d -aes-256-cbc -in "{nama_file_input}" -out "{nama_file_output}"'
    subprocess.run(perintah, shell=True, text=True, input=passphrase, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    print("File telah didedekripsi.")
    exit(0)

elif tindakan == "3":
  exit(0)

else:
    print("Pilihan tidak valid.")
    exit(1)
