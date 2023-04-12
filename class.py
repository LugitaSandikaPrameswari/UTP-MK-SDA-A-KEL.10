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
