# Izveidot kalkulatoru. 
# Programma prasa lietotājam ievadīt divus skaitļus. 
# Ar šiem skaitļiem tiek veiktas operācijas (saskaitīšana, atņemšana, 
# reizināšana, dalīšana). Rezultāts tiek parādīts konsolē.

# MANS     OK OK OK 
x=int(input("Ievadi skaitli 1: "))
y=int(input("Ievadi skaitli 2: "))
print(f"{x} + {y} =", x+y )
print(f"{x} - {y} =", x-y )
print(f"{x} * {y} =", x*y )
if y==0:
    print("Uz 0 dalīt ndrīkst.")
else: print(f"{x} / {y} =", x/y )








num1=int(input("Ievadi pirmo skaitli: "))
num2=int(input("Ievadi otro skaitli: "))
print(num1, "+", num2, "+", num1+num2)  # 5 + 6 =11

print(num1, "+", num2, "=", num1+num2)
print(num1, "-", num2, "=", num1-num2)
print(num1, "*", num2, "=", num1*num2)
# print(num1, "/", num2, "=", num1/num2)  # uz 0 nevar dalīt tāpēc šī rinda neder domājām kā savādāk
if num2==0:
    print(num1, "/", num2, "=", "Neeksistē")         # vai šitā >>print("Uz 0 dalīt nedrīkst")
else: print(num1, "/", num2, "=", "num1/num2")