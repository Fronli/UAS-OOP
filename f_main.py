import sys
sys.path.append("models/")
sys.path.append("repos/")
from product import Product
from product_repo import getAllProduct
from transaction import Transaction, getUserTransaction

#Input checker agar input tidak kosong!
def checkInput(prompt):
    data_input = input(prompt)
    if not data_input:
        while not data_input:
            print("Input tidak boleh kosong. Silakan coba lagi.")
            data_input = input(prompt)
    return data_input


def first_opt():
    print("Mohon masukkan nama user!")
    username = checkInput("Masukkan nama:")

    product_list = []

    while True:
        print("Silahkan pilih barang!")
        all_product_list = getAllProduct()
        index = 1
        # print(product_list)
        for product in all_product_list:
            print(f"{index}. {product[1]}\nCategory: {product[2]}\nPrice: Rp.{product[4]}\nQuantity: {product[6]}\n")
            index += 1
            
        print("Pilih produk yang mana?")
        inp_product = int(checkInput("Masukkan pilihan: "))
        inp_total = int(checkInput("Berapa banyak: "))

        product_dict = {
            "product": inp_product,
            "qty": inp_total 
        }
        product_list.append(product_dict)
        
        print("Apakah ingin membeli produk lain lagi?")
        inp_buy_again = checkInput("Masukkan jawaban (yes / no): ")
        if inp_buy_again == "no":
            break
    
    transaction = Transaction(
        product_list,
        username
    )
    transaction.final_transaction()
    print(f"Total pembelian anda adalah Rp{transaction.total_price}\n")


def second_opt():
    print("Mohon masukkan nama user!")
    username = checkInput("Masukkan nama:")
    
    db_list = getUserTransaction(username)
    for transaction in db_list:
        print(f"\nTransaction ID: {transaction[0]}\nTransaction Date: {transaction[1]}\nTotal Amount: {transaction[3]}\n")

def third_opt():
    print("Terima kasih telah berbelanja!")
    print("GBU!")
    sys.exit(0)