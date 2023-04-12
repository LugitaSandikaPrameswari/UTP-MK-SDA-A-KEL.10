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
