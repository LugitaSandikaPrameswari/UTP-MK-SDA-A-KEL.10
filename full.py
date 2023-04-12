# PROGRAM PENGOLAHAN DATA NILAI UN SISWA 

from os import stat, system

list_nama = []
list_kelas = []
nilai_mtk = []
nilai_bindo = []
nilai_ipa = []
nilai_bing = []

class dataNilaiSiswa :
    def __init__(self,nama,kelas,mtk,bindo,ipa,bing):
        self.nama = nama
        list_nama.append(self.nama)

        self.kelas = kelas
        list_kelas.append(self.kelas)

        self.mtk = mtk
        nilai_mtk.append(self.mtk)

        self.bindo = bindo
        nilai_bindo.append(self.bindo)

        self.ipa = ipa
        nilai_ipa.append(self.ipa)

        self.bing = bing
        nilai_bing.append(self.bing)

    def InputData(self):
        header()
        print("\nJumlah Siswa Terinput : ", len(list_nama))
        header2()
        for i in range(len(list_nama)) :
            if ((nilai_mtk[i] + nilai_bindo[i] + nilai_ipa[i]+ nilai_bing[i]) / 4) >= 76 :
                rerata = (nilai_mtk[i] + nilai_bindo[i] + nilai_ipa[i]+ nilai_bing[i]) / 4
                print("|", i+1,".  |  ", list_kelas[i], "    |  ", list_nama[i] ,"\t\t|", nilai_mtk[i], "\t|", nilai_bindo[i],"\t|", nilai_ipa[i], "\t|", nilai_bing [i], "\t|",rerata,"   ", " | Lulus          |")
            else : 
                rerata = (nilai_mtk[i] + nilai_bindo[i] + nilai_ipa[i]+ nilai_bing[i]) / 4
                print("|", i+1,".  |  ", list_kelas[i], "    |  ", list_nama[i] ,"\t\t|", nilai_mtk[i], "\t|", nilai_bindo[i],"\t|", nilai_ipa[i], "\t|", nilai_bing [i], "\t|",rerata,"    ", "| Tidak Lulus    |")
        print("|______|__________|_____________________|_______|_______|_______|_______|___________|________________|")
        tahan = input('\nTekan [enter] untuk kembali ke menu ')
        system('cls')
        menu()

def judul():
    print('=====================================')
    print('|                                   |')
    print('| Program Pengisian Nilai UN Siswa  |')
    print('|                ...                |')
    print('=====================================')

def header ():
        print("======================================================================================================")
        print("|                                      DAFTAR NILAI UN SISWA                                         |")
        print("|                                        SMP N 1 BOJONGGEDE                                          |")
        print("======================================================================================================")

def header2 ():
        print("_____________________________________________________________________________________________________")
        print("| No   |   Kelas  |   Nama              |  MTK  | BINDO | IPA   | BING  | Rata-rata |  Keterangan    |")
        print("|______|__________|_____________________|_______|_______|_______|_______|___________|________________|")

def tampil():
        system('cls')
        header()
        print("\nJumlah Siswa Terinput : ", len(list_nama))
        header2()
        for i in range(len(list_nama)) :   
          if ((nilai_mtk[i] + nilai_bindo[i] + nilai_ipa[i]+ nilai_bing[i]) / 4) >= 76 :
            rerata = (nilai_mtk[i] + nilai_bindo[i] + nilai_ipa[i]+ nilai_bing[i]) / 4
            print("|", i+1,".  |  ", list_kelas[i], "    |  ", list_nama[i] ,"\t\t|", nilai_mtk[i], "\t|", nilai_bindo[i],"\t|", nilai_ipa[i], "\t|", nilai_bing [i], "\t|",rerata,"   ", " | Lulus          |")
            
          else :
            rerata = (nilai_mtk[i] + nilai_bindo[i] + nilai_ipa[i]+ nilai_bing[i]) / 4
            print("|", i+1,".  |  ", list_kelas[i], "    |  ", list_nama[i] ,"\t\t|", nilai_mtk[i], "\t|", nilai_bindo[i],"\t|", nilai_ipa[i], "\t|", nilai_bing [i], "\t|",rerata,"    ", "| Tidak Lulus    |")

        print("|______|__________|_____________________|_______|_______|_______|_______|___________|________________|")
        i+=1
        tahan = input('\nTekan [enter] untuk kembali ke menu ')
        menu()

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
            kembali = input("\nInputan Tidak Sesuai / Belum Input Data! [enter] ") 
            menu()
    rubah()

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
