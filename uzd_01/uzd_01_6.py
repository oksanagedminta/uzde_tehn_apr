# K�da valsts nol�ma p�riet uz jaunu naudas sist�mu.
# Vecaj� sist�m� bija tr�s naudas vien�bas: d�lderis, grasis, sant�ms. 
# Naudas v�rt�bas nor�d�tas zem�k.
# 1 d�lderis = 37 gra�i
# 1 grasis = 162 sant�mi
# Jaunaj� naudas sist�m� paliek tikai sant�mi un d�lderi. 
# Sant�ms saglab� savu v�rt�bu, bet 1 d�lderis b�s vien�ds ar 100 sant�miem.
# Izveidot programmu, kas p�rveidotu vec�s sist�mas naudu uz jaunu.
# Lietot�jam prasa ievad�t vec�s sist�mas d�lderus, gra�us un sant�mus.
# Tiek apr��in�ts jaun�s sist�mas d�lderu un gra�u daudzums.
# Rezult�ts tiek par�d�ts konsol�.


# OK OK OK    ievadu 1d 2g 3s >>>63d un 21s
d=int(input("Ievadiet dalderu skaitu: "))
g=int(input("Ievadiet grasu skaitu: "))
s=int(input("Ievadiet santīmu skaitu: "))

d2=(((d*37)*162)+(g*162)+s)//100
s2=(((d*37)*162)+(g*162)+s)%100
print(d, "dalderis", g, "grasi un", s, "santīmi ir vienādi ar", d2, "dalderiem un", s2, "santīmiem." )

# nR.2      Ok ok ok        ievadu 1d 2g 3s >>>63d un 21s
d=int(input("Ievadiet dalderu skaitu: "))
g=int(input("Ievadiet grasu skaitu: "))
s=int(input("Ievadiet santīmu skaitu: "))

s=s+(g*162)+(d*162*37)
d2=s//100
s2=s-(d2*100)
print("Būs jaunās sistēmas", d2, "dalderi un", s2, "santīmi." )






dald=int(input("Dald.: "))
gras=int(input("Grs: "))
cents=int(input("Sant: "))

cents=cents+gras*162 + dald*37*162
dald2=cents//100
cents2=cents-dald2*100

print("Jaunie dald: ", dald2)
print("Jaunie sant: ", cents2)

