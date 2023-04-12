def ubah():
    system('cls')
    def rubah():
        try:
            judul()
            j = int (input('Rubah Data Siswa ke-: '))
            
            if (j-1 <= len(list_nama)):
                system('cls')
                print('\n=====================================')
                print ('Ubah Data'.center(40))
                print('=====================================')

                list_nama[j-1] = str(input("Masukan Nama Siswa     : "))

                list_kelas[j-1] = str(input("Masukan Kelas          : "))
                
                nilai_mtk[j-1] = float(input("Masukan Nilai Mtk      : "))
                
                nilai_bindo[j-1] = float(input("Masukan Nilai Bindo    : "))
                
                nilai_ipa[j-1] = float(input("Masukan Nilai Ipa      : "))
                
                nilai_bing[j-1] = float(input("Masukan Nilai Bing     : "))
                
                print('=====================================')
                print ('Data Tersimpan'.center(40))
                print('=====================================\n')
                
                lihat = input ('\nTekan [enter] untuk melihat data ')
                tampil()
            else :
              kembali = input("\nData tidak ditemukan/Data tidak ada [enter] ") 
              menu()

        except (IndexError,ValueError):
            kembali = input("\nInputan Tidak Sesuai! [enter] ") 
            menu()
    rubah()
