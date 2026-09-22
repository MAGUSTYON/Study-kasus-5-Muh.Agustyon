def pemesanan_hotel(jenis_kamar, lama_menginap):
    if jenis_kamar == "Standard":
        tarif = 200000
    elif jenis_kamar == "Deluxe":
        tarif = 350000
    else:
        return 0
      
    total_biaya = tarif * lama_menginap
  

    print("\n=== DATA PEMESANAN HOTEL ===")
    print("Jenis kamar       :", jenis_kamar)
    print("Lama menginap     :", lama_menginap, "malam")
    print("Total biaya       : Rp", total_biaya)

    return total_biaya


jenis_kamar = input("Masukkan jenis kamar (Standard/Deluxe): ")
lama_menginap = int(input("Masukkan lama menginap (malam): "))

pemesanan_hotel(jenis_kamar, lama_menginap)
