# Atrast cik skaitļi norādītajā intervālā dalās ar lietotāja norādīto dalītāju.

# OK
x=int(input("Ievadiet pirmo intervāla skaitli: "))
y=int(input("Ievadiet pēdējo intervāla skaitli: "))
z=int(input("Ievadiet dalītāju: "))



cikskaitli=0                #Obligāti jānorāda sākuma punkts, lai zin no cik +=1
for a in range(x, y+1):
    if a%z==0:
        cikskaitli+=1
print(f"Robežās starp {x} un {y} ar {cikskaitli} skaitļiem dalās ar dalītāju {z}")








x=int(input("Sākuma skaitlis: "))
y=int(input("Beigu skaitlis: "))
z=int(input("Dalītājs: "))

cik=0           #jānorāda sākuma skaitlis
for i in range(x, y+1):
    if i%z==0:
        cik+=1  # cik=cik+1
print(f"Robežās starp {x} un {y} - {cik} skaitļi dalās ar {z}")