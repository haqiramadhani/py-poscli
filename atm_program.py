import random
import datetime
from customer import Customer

atm = Customer(id)

while True:
    id = int(input("Masukan pin anda: "))
    trial = 0

    while (id != int(atm.cekPin()) and trial < 3):
        id = int(input("Pin anda salah. Silakan masukkan lagi: "))
        trial += 1

        if trial == 3:
            print("Error. Silakan ambil kartu dan coba lagi..")
            exit()
    
    while True:
        print("Selamat datang di ATM Progate..")
        print("\n1 - Cek Saldo \n2 - Debet \n3 - Simpan \n4 - Ganti Pin \n5 - Keluar ")

        selectmenu = int(input("\nSilakan pilih menu: "))

        if selectmenu == 1:
            print("\nSaldo anda sekarang: Rp. " + str(atm.cekBalance()) + "\n")

        elif selectmenu == 2:
            nominal = float(input("Masukkan nominal saldo: "))
            verify_withdrawal = input("Konfirmasi: Anda akan melakukan debet dengan nominal berikut ? y/n\n" + str(nominal) + "\n")
            
            if verify_withdrawal == "y":
                print("Saldo awal anda adalah: Rp. " + str(atm.cekBalance()) + "\n")
            else:
                break

            if nominal <= atm.cekBalance():
                atm.withdrawBalance(nominal)
                print("Transaksi debet berhasil!")
                print("Saldo sisa sekarang: Rp. " + str(atm.cekBalance()) + "\n")
            else:
                print("Maaf, saldo anda tidak mencukupi untuk melakukan debet!")
                print("Silakan lakukan penambahan nominal saldo!")

        elif selectmenu == 3:
            nominal = float(input("Masukkan nominal saldo: "))
            verify_deposit = input("Konfirmasi: Anda akan melakukan penyimpanan dengan nominal berikut ? y/n\n" + str(nominal) + "\n")
            
            if verify_withdrawal == "y":
                atm.depositBalance(nominal)
                print("Saldo anda sekarang adalah: Rp. " + str(atm.cekBalance()) + "\n")
            else:
                break

        elif selectmenu == 4:
            verify_pin = int(input("masukkan pin anda: "))
            while verify_pin != int(atm.cekPin()):
                print("pin anda salah, silakan masukkan pin: ")

            updated_pin = int(input("silakan masukkan pin baru: "))
            print("pin anda berhasil diganti!")

            verify_newpin = int(input("coba masukkan pin baru: "))

            if verify_newpin == updated_pin:
                print("pin baru anda sukses!")
            else:
                print("maaf, pin anda salah! ")

        elif selectmenu == 5:
            print("Resi tercetak otomatis saat anda keluar. \n Harap simpan tanda terima ini \n sebagai bukti transaksi anda.")
            print("No. Rekord: ", random.randint(100000, 1000000))
            print("Tanggal: ", datetime.datetime.now())
            print("Saldo akhir: ", str(atm.cekBalance()))
            print("Terima kasih telah menggunakan ATM Progate!")
            exit()

        else:
            print("Error. Maaf, menu tidak tersedia")

        print("\n==========================================================\n\n\n")
