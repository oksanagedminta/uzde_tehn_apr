# izveidot programmu, kas prasa lietot�jam ievad�t skaitli n, 
# tad programma apr��ina n+nn+nnn. 
# Rezult�ts tiek par�d�ts konsol�.

# 3+ 33 + 333  ....12 + 1212 + 121212

# OK  OK  OK
# nR. 1
x= int(input ("Ievadi skaitli: "))  # var izm.input
print(f"{x} + {x}*2 + {x}*3")       # x=2 >>> 2 + 2*2 + 2*3
sum=int(x)+int(x*2)+int(x*3)
print(sum)                           #x=2  >>>=246

#Nr.2
y=int(input("Ievadiet skaitli: "))
print(y, "+", y*2, "+", y*3, "=", sum)

#Nr.3  Kā es sākumā sapratu uzdevumu!!!!!!!
z=(input("Ievadi skaitli: "))
zz=(z+z)
zzz=(z+z+z)
print(z, "+", zz, "+", zzz, "=", z+zz+zzz)  #ne polu4aetsa pos4itatj = a tak ok: 2+22+222
print((z)+zz+zzz)
#sumz=(z+zz+zzz)
#print(z, "+", z+z, "+", z+z+z, "=", sumz)

#git?