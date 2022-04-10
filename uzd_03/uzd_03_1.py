# Apgriezt pozitīva skaitļa ciparu secību.
# Piemērs: 12345 => 54321


#  ????!!!!!!  end= ""   nākomo k.rindu pievelk klāt !!!!!! ??????
x=(input("Ievadiet pozitīvu skaitli: "))


#a=int(x)
#for a in range(len(x)-1, -1, -1):
#    print(x[a], end="")



#x=int(input("Ievadiet pozitīvu skaitli: "))
#for y in range(1, x+1):
#    print(y, end="")









x=input("Ievadi pozitīvu skaitli: ")
try:
    y=int(x)
    if y>0:
        for i in range(len(x)-1, -1, -1):
            print(x[i], end="") # end lai liek rindā ciparus vienu aiz otra
    else: print("Nav iev. poz. sk!!!")
except ValueError:
    print("Nav ievadīts skaitlis.")