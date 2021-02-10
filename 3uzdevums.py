def materialuAprekins(garums, platums, augstums, skaits):
  print(garums*garums)
  materialaUzskaite("STURIS", garums, augstums, skaits)

def materialaUzskaite(tips, izmers1, izmers2, skaits):
    print(tips)
    if (tips == "FINIERIS"):
        print("Skaits -",skaits)
        print("izmers1-",izmers1)
        print("izmers2-",izmers2)
#tad parametri izmers1 un izmers2 apraksta taisnstūrveida finiera plāksnes izmērus, secība nav svarīga. 
    

    elif (tips == "LISTE"):
        print("Skaits -",skaits)
        print("izmers1-",izmers1)
#tad parametrs izmers1 apraksta līstes detaļas garumu, savukārt parametra izmers2 vērtība nav svarīga. 

    elif (tips == "STURIS"):
        print("Skaits -",skaits)
        #tad parametru izmers1 un izmers2 vērtības nav svarīgas.

    
   

materialuAprekins (2,3,4,5)