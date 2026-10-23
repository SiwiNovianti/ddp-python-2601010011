nama_barang = input("Masukkan nama barang: ")
harga_satuan = float(input("Masukkan harga satuan barang:"))
jumlah_barang = int(input("Masukkan jumlah barang: "))

Subtotal = harga_satuan * jumlah_barang
print(f"Subtotal belanja {nama_barang} adalah: Rp. {Subtotal}")

PPN = 0.11 * Subtotal
print(f"PPN 11% dari subtotal belanja {nama_barang} adalah: Rp. {PPN}")

Total_bayar = Subtotal + PPN
print(f"Total bayar belanja {nama_barang} adalah: Rp. {Total_bayar}")