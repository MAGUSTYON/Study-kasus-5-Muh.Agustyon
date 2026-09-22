def pemesanan_hotel ( jenis_kamar, check_in, check_out ) :
    if jenis_kamar == "Standard":
        tarif = 200000
    elif jenis_kamar == "Deluxe":
        tarif = 350000
    else:
        print ( "kamar tidak tersedia")
        return

    lama_menginap = check_out - check_in
    biaya = tarif * lama_menginap

    print ( "==== DATA PEMESANAN HOTEL ====")
    print ( "Jenis kamar       :", jenis_kamar)
    print ( "Tanggal check-in  :", check_in)
    print ( "Tanggal check-out :", check_out)
    print ( "Lama menginap     :", lama_menginap, "malam")
    print ( "Total biaya       : Rp", biaya)

    return biaya


jenis_kamar = input( "Masukkan jenis kamar (Standard/Deluxe) : ")
check_in = int ( input( "Masukkan tanggal check-in: " ) )
check_out = int ( input( "Masukkan tanggal check-out :" ) )

pemesanan_hotel ( jenis_kamar, checkin, checkout )
