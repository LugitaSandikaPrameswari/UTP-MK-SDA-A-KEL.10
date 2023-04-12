def menu():
    try :
        system('cls')
        judul()
        print('| 1. Tambah & Lihat Nilai           |')
        print('| 2. Ubah Nilai                     |')
        print('| 3. Hapus Nilai                    |')
        print('| 4. Keluar                         |')
        print('=====================================')
        pilihan = input('\nPilih Menu : ')
        
        if pilihan == "1":
            Stop = False
            b = 0
            while (not Stop):
                print("\n")
                system('cls')
                judul()
                
                print()
                inputNama = str(input("Masukan Nama Siswa     : "))
                inputKelas = str(input("Masukan Kelas          : "))
                inputMtk = float(input("Masukan Nilai Mtk      : "))
                inputBindo = float(input("Masukan Nilai Bindo    : "))
                inputIpa = float(input("Masukan Nilai Ipa      : "))
                inputBing = float(input("Masukan Nilai Bing     : "))

                dataSiswa = dataNilaiSiswa(inputNama,inputKelas,inputMtk,inputBindo,inputIpa,inputBing)
                b+=1
                print('=====================================')
                print ('Data Tersimpan'.center(40))
                print('=====================================\n')
                ulang = input("Ingin menginput nilai lagi? (y/t) : ")
                print()
                if ulang == 't':
                    Stop = True
                    lihat = input ('Tekan [enter] Untuk melihat data')
            system('cls')        
            dataSiswa.InputData()

        elif pilihan == "2" :
            ubah()
                
        elif pilihan == "3" :
            hapus()
            menu()

        elif pilihan == "4" :
            print("\nAnda Berhasil Keluar!")
            exit()

        else:
            tidak = input('Menu Tidak Ada ')
            system('cls')
            menu()

    except (IndexError,ValueError):
            system('cls')
            kembali = input("\nInputan Tidak Sesuai ! \nTekan [enter] untuk kembali ke Menu ") 
            menu()
menu()
