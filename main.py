import sys
sys.path.append("models/")
from f_main import first_opt, second_opt, third_opt, checkInput


#================================================================================================
# Main mulai dari sini prgramnya!!!
if __name__ == "__main__":
    while True:
        print("=== Selamat Datang di Toko Elektronik ===")
        print("Anda ingin melakukan transaksi apa?\n1. Beli barang!\n2. Melihat transaksi anda!\n3. Exit!")

        user_input = int(checkInput("Masukkan pilihan anda: "))
        print()

        # User pilih beli barang (1)
        if user_input == 1:
            first_opt()
        # User pilih check transaksi (2)
        elif user_input == 2:
            second_opt()
        #  User pilih EXIT (3)
        else:
            third_opt()