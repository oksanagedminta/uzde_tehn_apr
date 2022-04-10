#           OK
# Izveidot programmu, kura prasa lietot�jam ievad�t cilindra r�diusu
# un t� augstumu, tiek apr��in�ts cilindra laukums un tilpums.
# Rezult�ts tiek par�d�ts konsol�.
# tilpums = 3.14 * r�diuss * r�diuss * augstums
# laukums = 2 * (3.14 * r�diuss * r�diuss) + augstums * (2 * 3.14 * r�diuss)

#PI- ... 3.14  šīvietā lieto matemātiskās konstances
#ok
import math
r=int(input("Cilindra rādius= "))
h=int(input("Cilindra augstums= "))
tilpums=math.pi*r*r*h
laukums=2*(math.pi*r*r)+h*(2*math.pi*r)
print(f"Cilindra laukums ir {laukums}.")
print(f"Cilindra tilpums ir {tilpums}.")





import math
h=int(input("Ievadi augstumu: "))
r=int(input("Ievadi rādiusu: "))

tilpums=math.pi*r*r*h
laukums=2*(math.pi*r*r)+h*(2*math.pi*r)
print(f"Tilpums ir {tilpums}.")
print(f"Laukus ir {laukums}.")