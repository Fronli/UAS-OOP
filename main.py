import sys
sys.path.append("models/")
from f_main import first_opt, second_opt, third_opt, fourth_opt, checkInput


#===============================================================================

# Main mulai dari sini prgramnya!!!
if __name__ == "__main__":
    while True:
        print("=== Selamat Datang di Toko Elektronik ===")
        print("Anda ingin melakukan transaksi apa?\n1. Beli barang!\n2. Melihat transaksi anda!\n3. Developer Mode\n4. Exit!")

        user_input = int(checkInput("Masukkan pilihan anda: "))
        print()

        # user pilih beli barang (1)
        if user_input == 1:
            first_opt()
        # user pilih check transaksi (2)
        elif user_input == 2:
            second_opt()
        elif user_input == 3:
            third_opt()
        #  user pilih EXIT (4)
        else:
            fourth_opt()