import sys
sys.path.append("models/")
sys.path.append("repos/")
sys.path.append("util/")

from models.electronic_product import ElectronicProduct
from models.transaction import Transaction, getUserTransaction
from repos.product_repo import getAllProduct, getProductInfo, addProduct, changePrice
from repos.inventory_repo import repo_addStock
from util.exception_h import InsufficientStockErrorH, FailedAddingProduct, FailedChangingPrice, FailedAddingQuantity

def checkInput(prompt):
    data_input = input(prompt)
    while not data_input:
        print("Input tidak boleh kosong.")
        data_input = input(prompt)
    return data_input

def first_opt():
    print("Mohon masukkan nama user!")
    username = checkInput("Masukkan nama: ")

    # Init Transaksi disini!
    current_transaction = Transaction(username)

    while True:
        print("\n--- DAFTAR PRODUK ---")
        all_product_data = getAllProduct() 
        index = 1        

        for p in all_product_data:
            print(f"{index}. {p[1]}\nCategory: {p[2]}\nPrice: Rp.{p[4]}\nQuantity: {p[6]}\n")
            index += 1

            
        try:
            inp_id = int(checkInput("Pilih produk: "))
            inp_qty = int(checkInput("Berapa banyak: "))

            prod_info = getProductInfo(inp_id)
            # print(f"dari print prod_info: {prod_info}")

            if prod_info:
                product_obj = ElectronicProduct(
                    id=prod_info[0],
                    name=prod_info[1],
                    category=prod_info[2],
                    brand=prod_info[3],
                    price=prod_info[4],
                    warranty_months=prod_info[5] # Default atau ambil dari DB jika ada
                )

                # Masukkan Object ke Transaksi
                current_transaction.add_item(product_obj, inp_qty)
                print("Berhasil ditambahkan ke keranjang.")
            else:
                print("ID Produk tidak ditemukan.")

        except ValueError:
            print("Input harus berupa angka.")

        inp_buy_again = checkInput("Beli lagi? (yes/no): ")
        if inp_buy_again.lower() == "no":
            break
    
    try:
        current_transaction.final_transaction()
        print(f"\nTransaksi Berhasil! Total: Rp{current_transaction.total_price}")
    except InsufficientStockErrorH as e:
        print(f"\nGAGAL: {e}")
    except Exception as e:
        print(f"\nTerjadi kesalahan sistem: {e}")

def second_opt():
    print("Mohon masukkan nama user!")
    username = checkInput("Masukkan nama:")
    
    db_list = getUserTransaction(username)
    for transaction in db_list:
        print(f"\nTransaction ID: {transaction[0]}\nTransaction Date: {transaction[1]}\nTotal Amount: {transaction[3]}\n")

    pass

def third_opt():
    print("Masukkan Devleoper Account Name!")
    dev_name = checkInput("Name input: ")
    print()
    print("Masukkan Devleoper Account Password!")
    dev_pass = checkInput("Password input: ")
    print()

    if dev_name.lower() != "dev" or dev_pass.lower() != "dev":
        print("Kredensial Akun Developer Salah!!!\n")
        return None

    while True:
        print("---Welcome to Developer Mode---")
        print("Select what to do!")
        print("1. Add New Product\n2. Change Product Price\n3. Add Product Quantity\n4. Back")
        dev_select = int(checkInput("Input: "))


        # Feature "Add New Produce"
        if dev_select == 1:
            pname = checkInput("Input Product Name: ")
            pcategory = checkInput("Input Product Category: ") 
            pbrand = checkInput("Input Product Brand: ") 
            pprice = int(checkInput("Input Product Price: ")) 
            pwarranty = int(checkInput("Input Product Warranty Months: ")) 

            new_product = ElectronicProduct(
                id=100,
                name=pname,
                category=pcategory,
                brand=pbrand,
                price=pprice,
                warranty_months=pwarranty,
            )

            try:
                addProduct(new_product)
                print("Succesful adding new product")
            except FailedAddingProduct as e:
                print(f"\nGAGAL: {e}")
            except Exception as e:
                print(f"\nTerjadi kesalahan sistem: {e}")


        # Feature "Change Product Price" 
        elif dev_select == 2:
            print("\n--- DAFTAR PRODUK ---")
            all_product_data = getAllProduct() 
            index = 1        

            for p in all_product_data:
                print(f"{index}. {p[1]}\nCategory: {p[2]}\nPrice: Rp.{p[4]}\nQuantity: {p[6]}\n")
                index += 1

            pid = int(checkInput("Input Product ID: ")) 
            new_price = int(checkInput("Input New Price: "))
            
            try:
                changePrice(pid, new_price)
                print("Succesful changing price!")
            except FailedChangingPrice as e:
                print(f"\nGAGAL: {e}")
            except Exception as e:
                print(f"\nTerjadi kesalahan sistem: {e}")


        # Feature "Add Product Quantity" 
        elif dev_select == 3:
            print("\n--- DAFTAR PRODUK ---")
            all_product_data = getAllProduct() 
            index = 1        

            for p in all_product_data:
                print(f"{index}. {p[1]}\nCategory: {p[2]}\nPrice: Rp.{p[4]}\nQuantity: {p[6]}\n")
                index += 1
            
            pid = int(checkInput("Input Product ID: ")) 
            add_quantity = int(checkInput("Input How Much Quantity to Add: "))

            try:
                repo_addStock(pid, add_quantity)
                print("Succesful changing price!")
            except FailedChangingPrice as e:
                print(f"\nGAGAL: {e}")
            except Exception as e:
                print(f"\nTerjadi kesalahan sistem: {e}")

            
        # Feature "Back"
        else:
            return None


def fourth_opt():
    print("Terima kasih telah berbelanja!")
    print("GBU!")
    sys.exit(0)