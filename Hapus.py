def hapus():
    system('cls')
    def hapuss():
        try:
            print('=====================================')
            print('Hapus Data'.center(40))
            print('=====================================')
            j = int(input('\nHapus Data Siswa ke-: '))
            
            if (j-1 <= len(list_nama)):
                list_nama.remove(list_nama[j-1])
                list_kelas.remove(list_kelas[j-1])
                nilai_mtk.remove(nilai_mtk[j-1])
                nilai_bindo.remove(nilai_bindo[j-1])
                nilai_ipa.remove(nilai_ipa[j-1])
                nilai_bing.remove(nilai_bing[j-1])

                system('cls')
                print('-------------------------------------')
                print ('Data Berhasil Dihapus'.center(40))
                print('-------------------------------------')
                lihat = input ('\nTekan [enter] Untuk melihat data ')
                tampil()
                menu()

            else:
              kembali = input("\nData tidak ditemukan/Data tidak ada [enter] ") 
              menu()

        except (IndexError,ValueError,UnboundLocalError):
            kembali = input("\nInputan Tidak Sesuai / Belum Input Data! [enter] ") 
            hapus()

    hapuss()
    tampil()
