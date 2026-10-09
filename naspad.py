print("=" * 30)
print("Menu warung naspad nabil: ")
print("1. Ayam goreng = Rp. 5.000\n2. Ikan goreng = Rp. 4.000\n3. Ayam Bakar = Rp. 6.000")
print("=" * 30)

ayamgoreng = 5000
ikangoreng = 4000
ayambakar = 6000

Tanya1 = int(input("kamu mau pesan apa? masukkan nomer menu. (1, 2, 3): "))

if Tanya1 == 1:
    sub_tanya1 = int(input("kamu mau pesan ayam goreng berapa?: "))
    print("oke kamu mau beli ayam goreng sebanyak: ", sub_tanya1)
    subsub_tanya1 = int(input("ini doang? jika ingin nambah piih menu (1, 2, 3). Jika tidak ketik angka (0): "))
    if subsub_tanya1 == 1:
        subsubsub_tanya1 = int(input("lu mau nambah ayam goreng berapa?: "))
        print(f"kamu nambah ayam goreng sebanyak {subsubsub_tanya1} yah, jadi kamu beli Lauk sebanyak:", sub_tanya1 + subsubsub_tanya1)
        print("dengan total harga sebanyak:", (ayamgoreng * sub_tanya1) + (ayamgoreng * subsubsub_tanya1))

    elif subsub_tanya1 == 2:
        subsubsub_tanya2 = int(input("lu mau nambah ikan goreng berapa?: "))
        print(f"kamu nambah ikan goreng sebanyak {subsubsub_tanya2} yah, jadi kamu beli Lauk sebanyak:", sub_tanya1 + subsubsub_tanya2)
        print("dengan total harga sebanyak:", (ayamgoreng * sub_tanya1) + (ikangoreng * subsubsub_tanya2))

    elif subsub_tanya1 == 3:
        subsubsub_tanya3 = int(input("lu mau nambah ayam bakar berapa?: "))
        print(f"kamu nambah ayam bakar sebanyak {subsubsub_tanya3} yah, jadi kamu beli Lauk sebanyak:", sub_tanya1 + subsubsub_tanya3)
        print("dengan total harga sebanyak:", (ayamgoreng * sub_tanya1) + (ayambakar * subsubsub_tanya3))

    else:
        print("oke, kalo memang itu saja, sekarang kamu perlu bayar totalnya sebanyak:", ayamgoreng * sub_tanya1)

if Tanya1 == 2:
    sub_tanya2 = int(input("kamu mau pesan ikan goreng berapa?: "))
    print("oke kamu mau beli ikan goreng sebanyak:", sub_tanya2)
    subsub_tanya2 = int(input("ini doang? jika ingin nambah piih menu (1, 2, 3). Jika tidak ketik angka (0): "))
    if subsub_tanya2 == 1:
        print("kamu nambah ayam goreng yah, jadi kamu beli Lauk sebanyak:", sub_tanya2 + subsub_tanya2)
        print("dengan total harga sebanyak:", (ikangoreng * sub_tanya2) + (ayamgoreng * subsub_tanya2))
    elif subsub_tanya2 == 2:
        print("kamu nambah ikan goreng yah, jadi kamu beli Lauk sebanyak:", sub_tanya2 + subsub_tanya2)
        print("dengan total harga sebanyak:", (ikangoreng * sub_tanya2) + (ikangoreng * subsub_tanya2))
    elif subsub_tanya2 == 3:
        print("kamu nambah ayam bakar yah, jadi kamu beli Lauk sebanyak:", sub_tanya2 + subsub_tanya2)
        print("dengan total harga sebanyak:", (ikangoreng * sub_tanya2) + (ayambakar * subsub_tanya2))
    else:
        print("oke, kalo memang itu saja, sekarang kamu perlu bayar totalnya sebanyak:", ikangoreng * sub_tanya2)

# if Tanya1 == 3:
    # sub_tanya1 = int(input("kamu mau pesan ayam goreng berapa?: "))
    # print("oke kamu mau beli ayam goreng sebanyak:", sub_tanya1)
    # subsub_tanya1 = int(input("ini doang? jika ingin nambah piih menu (1, 2, 3). Jika tidak ketik angka (0): "))
    # if subsub_tanya1 == 1:
    #     print("kamu nambah ayam goreng yah, jadi kamu beli Lauk sebanyak:", sub_tanya1 + subsub_tanya1)
    #     print("dengan total harga sebanyak:", (ayamgoreng * sub_tanya1) + (ayamgoreng * subsub_tanya1))
    # elif subsub_tanya1 == 2:
    #     print("kamu nambah ikan goreng yah, jadi kamu beli Lauk sebanyak:", sub_tanya1 + subsub_tanya1)
    #     print("dengan total harga sebanyak:", (ayamgoreng * sub_tanya1) + (ikangoreng * subsub_tanya1))
    # elif subsub_tanya1 == 3:
    #     print("kamu nambah ayam bakar yah, jadi kamu beli Lauk sebanyak:", sub_tanya1 + subsub_tanya1)
    #     print("dengan total harga sebanyak:", (ayamgoreng * sub_tanya1) + (ayambakar * subsub_tanya1))
    # else:
    #     print("oke, kalo memang itu saja, sekarang kamu perlu bayar totalnya sebanyak:", ayamgoreng * sub_tanya1)
