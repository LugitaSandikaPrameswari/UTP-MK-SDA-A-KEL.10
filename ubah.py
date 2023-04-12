#Andria Laras Ramadhania (2217051016)

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

                #del list_nama[i-1]
                list_nama[j-1] = str(input("Masukan Nama Siswa     : "))
                #list_nama.insert(i-1, list_nama[i-1])

                #del list_kelas[i-1]
                list_kelas[j-1] = str(input("Masukan Kelas          : "))
                #list_kelas.insert(i-1, list_kelas[i-1])

                #del nilai_mtk[i-1]
                nilai_mtk[j-1] = float(input("Masukan Nilai Mtk      : "))
                #nilai_mtk.insert(i-1, nilai_mtk[i-1])

                #del nilai_bindo[i-1]
                nilai_bindo[j-1] = float(input("Masukan Nilai Bindo    : "))
                #nilai_bindo.insert(i-1, nilai_bindo[i-1])

                #del nilai_ipa[i-1]
                nilai_ipa[j-1] = float(input("Masukan Nilai Ipa      : "))
                #nilai_ipa.insert(i-1, nilai_ipa[i-1])

                #del nilai_bing[i-1]
                nilai_bing[j-1] = float(input("Masukan Nilai Bing     : "))
                #nilai_bing.insert(i-1, nilai_bing[i-1])

                print('=====================================')
                print ('Data Tersimpan'.center(40))
                print('=====================================\n')
                #dataSiswa1 = dataNilaiSiswa(list_nama[i-1],list_kelas[i-1],nilai_mtk[i-1],nilai_bindo[i-1], nilai_ipa[i-1], nilai_bing[i-1])
                lihat = input ('\nTekan [enter] untuk melihat data ')
                #dataSiswa1.InputData()
                tampil()
            else :
              kembali = input("\nData tidak ada / Input Data terlebih dahulu [enter] ") 
              menu()

        except (IndexError,ValueError):
            kembali = input("\nData tidak ada / Input Data terlebih dahulu [enter] ") 
            menu()
    rubah()